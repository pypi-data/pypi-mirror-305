# ################################################################## 
# 
# Copyright 2023 Teradata. All rights reserved.
# TERADATA CONFIDENTIAL AND TRADE SECRET
# 
# Primary Owner: Adithya Avvaru (adithya.avvaru@teradata.com)
# Secondary Owner: Pankaj Purandare (pankajvinod.purandare@teradata.com)
# 
# Version: 1.0
# Function Version: 1.0
#
# This file contains object wrapper class for opensource packages and child object
# wrapper classes for each opensource package. Currently, we have child object
# wrapper class for scikit-learn.
# 
# ################################################################## 

from collections import OrderedDict, defaultdict
from importlib import import_module

import base64
import json
import numpy
import os
import pickle
import time
import inspect
import warnings
import json
import math
import pandas as pd
from teradatasqlalchemy import BLOB, CLOB, FLOAT, TIMESTAMP, VARCHAR, INTEGER
import pandas.api.types as pt

from teradataml import _TDML_DIRECTORY, Script, TeradataMlException, Apply
from teradataml.dataframe.copy_to import _get_sqlalchemy_mapping
from teradataml.common import pylogger
from teradataml.common.utils import UtilFuncs
from teradataml.context.context import _get_current_databasename, get_connection
from teradataml.dbutils.filemgr import install_file, remove_file
from teradataml.utils.utils import execute_sql
from teradataml.options.configure import configure
from teradataml.opensource._wrapper_utils import _validate_fit_run, _generate_new_name,\
    _validate_opensource_func_args, _derive_df_and_required_columns, _validate_df_query_type
from teradataml.opensource.constants import OpenSourcePackage, _OSML_MODELS_PRIMARY_INDEX,\
    _OSML_MODELS_TABLE_NAME, _OSML_MODELS_TABLE_COLUMNS_TYPE_DICT, OpensourceModels,\
    _OSML_ADDITIONAL_COLUMN_TYPES
from teradataml.common.messagecodes import MessageCodes
from teradataml.common.messages import Messages
from teradataml.catalog.byom import save_byom, retrieve_byom, delete_byom
from teradataml.dbutils.dbutils import _create_table, set_session_param
from teradataml.utils.validators import _Validators
from teradataml.dataframe.dataframe import DataFrame
from teradataml.dataframe.dataframe_utils import DataFrameUtils
from teradataml.common.garbagecollector import GarbageCollector
from teradataml.common.constants import TeradataConstants


logger = pylogger.getLogger()

validator = _Validators()

installed_model_files = defaultdict(int)

## Flag to ensure the sklearn script
## installation occurs only once.
_file_installed = False

class _GenericObjectWrapper:
    def __init__(self) -> None:
        if not get_connection():
            raise TeradataMlException(Messages.get_message(MessageCodes.INVALID_CONTEXT_CONNECTION),
                                      MessageCodes.INVALID_CONTEXT_CONNECTION)
        self._db_name = _get_current_databasename()

        self._scripts_path = os.path.join(_TDML_DIRECTORY, "data", "scripts", "sklearn")

        # Some random number to be used as partition value if partition_columns is None for fit().
        self._default_data_partition_value = -1001

        self.modelObj = None
        self._model_data = None

        self._tdml_tmp_dir = GarbageCollector._get_temp_dir_name()

        self._env = None

        self._is_lake_system = UtilFuncs._is_lake()

        if self._is_lake_system:
            if configure.openml_user_env is not None:
                self._env = configure.openml_user_env
            else:
                self._env = UtilFuncs._create_or_get_env("open_source_ml.json")
        else:
            set_session_param("searchuifdbpath",self._db_name)

        global _file_installed
        ## Flag to check whether trained model is installed or not.
        self._is_trained_model_installed = False

        ## Install all sklearn script files on Vantage.
        if not _file_installed:
            sklearn_script_files = ["sklearn_fit.py", "sklearn_score.py",
                                    "sklearn_transform.py", "sklearn_fit_predict.py",
                                    "sklearn_neighbors.py", "sklearn_model_selection_split.py"]
            for script_file in sklearn_script_files:
                self._install_script_file(file_identifier=script_file.split(".")[0],
                                          file_name=script_file)

            _file_installed = True

    def _get_columns_as_list(self, cols):
        """
        Internal function to get columns as list of strings.
        Empty list is returned if cols is None.
        """
        if cols is None:
            return []
        if not isinstance(cols, list) and not isinstance(cols, tuple):
            return [cols]
        return cols

    def _get_data_and_data_partition_columns(self, data, feature_columns, label_columns,
                                             partition_columns=None, group_columns=[]):
        """
        Internal function to generate one new partition column (if not provided) and return
        data and partition columns (either generated or passed one).
        """
        new_partition_columns = self._get_columns_as_list(partition_columns)

        if not partition_columns:
            # If partition column is not specified, create a partition column and run Script.
            # This runs the Script in one AMP as we are partitioning data using this column
            # which contains only one value.
            new_partition_columns = [_generate_new_name(type="column")]
            data = data.assign(**{new_partition_columns[0]: self._default_data_partition_value})

        # Filter out partition columns from feature columns and label columns.
        new_partition_columns_filtered = [col for col in new_partition_columns
                                          if col not in (feature_columns + label_columns + group_columns)]

        all_columns = feature_columns + label_columns + group_columns + new_partition_columns_filtered
        return data.select(all_columns), new_partition_columns

    def _run_script(self, data, command, partition_columns, return_types):
        """
        Internal function to run Script(), given the argument needed by STO's or
        Apply's Script.
        """
        if isinstance(partition_columns, list) and len(partition_columns) == 0:
            partition_columns = None

        if self._is_lake_system:
            obj = Apply(data=data,
                        returns=OrderedDict(return_types),
                        apply_command=command,
                        data_partition_column=partition_columns,
                        env_name=self._env,
                        delimiter="\t")
        else:
            obj = Script(data=data,
                         returns=OrderedDict(return_types),
                         script_command=command,
                         data_partition_column=partition_columns)
            obj.check_reserved_keyword = False

        obj.skip_argument_validation = True
        return obj.execute_script(output_style="TABLE")

    def _install_script_file(self, 
                             file_identifier=None, 
                             file_name=None, 
                             is_binary=False, 
                             file_location=None):
        """
        Internal function to install script file in Vantage.
        """
        if file_location is None:
            file_location = self._scripts_path
        new_script = os.path.join(file_location, file_name)

        # _env is set while object creation
        # If not set, it is Vantage Enterprise. Otherwise, it is Vantage Lake.

        if not self._is_lake_system:
            status = install_file(file_identifier=file_identifier,
                                  file_path=new_script,
                                  replace=True,
                                  suppress_output=True,
                                  is_binary=is_binary)
        else:
            status = self._env.install_file(file_path=new_script,
                                            replace=True,
                                            suppress_output=True)
        if not status:
            raise TeradataMlException(
                f"Script file '{file_name}' failed to get installed/replaced in Vantage."
            )

    def _remove_script_file(self, file_name):
        """
        Internal function to remove script file in Vantage.
        """
        # _env is set while object creation
        # If not set, it is Vantage Enterprise. Otherwise, it is Vantage Lake.

        if not self._is_lake_system:
            status = remove_file(file_identifier=file_name.split(".")[0],
                                 force_remove=True,
                                 suppress_output=True)
        else:
            status = self._env.remove_file(file_name=file_name,
                                           suppress_output=True)
        if not status:
            raise TeradataMlException(
                f"Script file '{file_name}' failed to remove in Vantage."
            )

    def _get_data_col_types_and_partition_col_indices_and_types(self, data, partition_columns,
                                                                idx_delim=",",
                                                                types_delim="--"):
        """
        Internal function to get the data column types and partition column names, indices and types.
        Function returns delimiter separated string of types and indices if idx_delim and
        types_delim are provided. Otherwise, it returns list of types and indices. Partition names
        are returned as list always.
        """
        data_column_types = "" if types_delim else []
        partition_indices = "" if idx_delim else []
        partition_types = "" if types_delim else []
        new_partition_columns = []
        j = 0
        for i, col in enumerate(data.columns):
            _type = data._td_column_names_and_sqlalchemy_types[col.lower()].python_type.__name__
            if types_delim:
                data_column_types += (_type if i == 0 else f"{types_delim}{_type}")
            else:
                data_column_types.append(_type)
            if col in partition_columns:
                new_partition_columns.append(col)
                if idx_delim:
                    partition_indices += (str(i) if j == 0 else f"{idx_delim}{str(i)}")
                else:
                    partition_indices.append(i)
                if types_delim:
                    partition_types += (_type if j == 0 else f"{types_delim}{_type}")
                else:
                    partition_types.append(_type)
                j += 1
        # Return types of all columns (as list or str), partition column indices (as list or str)
        # and partition column types (as list or str).
        return data_column_types, partition_indices, partition_types, new_partition_columns

    def _get_kwargs_str(self, kwargs):
        """
        Returns string of kwargs in the format:
            key1 val1-type1 key2 val2-type2 ...
        """
        args_str = ""
        for key, val in kwargs.items():
            strr = f"{key} {str(val)}-{type(val).__name__}"
            if args_str == "":
                args_str += strr
            else:
                args_str += f" {strr}"
        return args_str

    def _extract_model_objs(self, n_unique_partitions=1, n_partition_cols=1):
        """
        Internal function to extract sklearn object from the model(s) depending on the number of
        partitions. When it is only one model, it is directly used as sklearn object (modelObj).
        When it is multiple models, it is converted to pandas DataFrame and stored in sklearn
        object.
        """
        vals = execute_sql("select * from {}".format(self._model_data._table_name)).fetchall()

        # pickle will issue a caution warning, if model pickling was done with
        # different library version than used here. The following disables any warnings
        # that might otherwise show in the scriptlog files on the Advanced SQL Engine
        # nodes in this case. Yet, do keep an eye for incompatible pickle versions.
        warnings.filterwarnings("ignore")

        model_obj = None
        # Extract and unpickle last column which is the model object.
        for i, row in enumerate(vals):
            if self._is_lake_system:
                model_obj = pickle.loads(row[n_partition_cols])
            else:
                model_obj = pickle.loads(base64.b64decode(row[n_partition_cols].partition("'")[2]))
            row[n_partition_cols] = model_obj
            vals[i] = row
        if n_unique_partitions == 1:
            self.modelObj = model_obj
        elif n_unique_partitions > 1:
            self.modelObj = pd.DataFrame(vals, columns=self._model_data.columns)
        else:
            ValueError("Number of partitions should be greater than 0.")

        warnings.filterwarnings("default")

    def _validate_existence_of_partition_columns(self, partition_columns, all_columns, arg_names_for_dfs):
        """
        Validate if columns in "partition_columns" argument are present in any of the given
        dataframes.
        """
        invalid_part_cols = [c for c in partition_columns if c not in all_columns]

        if invalid_part_cols:
            raise ValueError(Messages.get_message(MessageCodes.INVALID_PARTITIONING_COLS,
                                                  ", ".join(invalid_part_cols),
                                                  "', '".join(arg_names_for_dfs))
                                                  )

    def _prepare_data_args_string(self, kwargs):
        """
        Get column indices and types of each data related arguments in the format:
        "{<arg_name>-<comma separated indices>-<comma separated types>}--
         {<arg_name>-<comma separated indices>-<comma separated types>}"
        """
        data_args_str = []
        for arg_name in list(self._data_args.keys()):
            # Remove DataFrame arguments from kwargs, which will be passed to Script.
            kwargs.pop(arg_name)

            # Get column indices and their types for each dataframe from parent dataframe.
            _, partition_indices_str, partition_types_str, _ = \
                self._get_data_col_types_and_partition_col_indices_and_types(self._tdml_df,
                                                                   self._data_args[arg_name].columns,
                                                                   idx_delim=",",
                                                                   types_delim=",")
        
            # Format "<arg_name>-<comma separated indices>-<comma separated types>"            
            data_args_str.append(f"{arg_name}-{partition_indices_str}-{partition_types_str}")
        
        # Format "{<arg_name>-<comma separated indices>-<comma separated types>}--
        #    {<arg_name>-<comma separated indices>-<comma separated types>}"
        return "--".join(data_args_str)

    def _prepare_and_install_file(self, replace_dict):
        """
        Prepare function script file from template file and install it in Vantage.
        Takes the dictionary with keys as strings to be replaced in script and values as
        strings which should be added in place of keys.
        """

        with open(os.path.join(self._scripts_path, self._template_file)) as fp:
            script_data = fp.read()
        
        for old, new in replace_dict.items():
            script_data = script_data.replace(old, new)

        self._script_file_local = os.path.join(self._tdml_tmp_dir, self._script_file_name)

        with open(self._script_file_local, "w") as fp:
            fp.write(script_data)
        
        self._install_script_file(file_identifier=self._script_file_name.split(".")[0],
                                  file_name=self._script_file_name,
                                  file_location=self._tdml_tmp_dir)

    def _get_dataframe_related_args_and_their_columns(self, kwargs):
        """
        Get dataframe related arguments and return all their column names from kwargs.
        """
        __data_columns = []
        __data_args_dict = OrderedDict()

        # Separate dataframe related arguments and their column names from actual kwargs.
        for k, v in kwargs.items():
            if isinstance(v, DataFrame):
                # All dataframes should be select of parent dataframe.
                _validate_df_query_type(v, "select", k)

                # Save all columns in dataframe related arguments.
                __data_columns.extend(v.columns)

                __data_args_dict[k] = v
        
        return __data_args_dict, __data_columns

    def _process_data_for_funcs_returning_objects(self, kwargs):
        """
        Internal function to process all arguments and assign self._data_args, self._tdml_df
        and return 
        1. dictionary of elements (needed to replace in the script template file)
        2. partition columns list.
        """
        partition_cols = self._get_columns_as_list(kwargs.get("partition_columns", None))
        if partition_cols:
            kwargs.pop("partition_columns")

        self._data_args, __data_columns = self._get_dataframe_related_args_and_their_columns(kwargs)

        arg_names_for_dfs = list(self._data_args.keys())

        # Get common parent dataframe from all dataframes.
        self._tdml_df =  DataFrameUtils()._get_common_parent_df_from_dataframes(list(self._data_args.values()))

        self._tdml_df = self._tdml_df.select(__data_columns + partition_cols)

        self._validate_existence_of_partition_columns(partition_cols, self._tdml_df.columns, arg_names_for_dfs)

        self._tdml_df, partition_cols = self._get_data_and_data_partition_columns(self._tdml_df,
                                                                                   __data_columns,
                                                                                   [],
                                                                                   partition_cols
                                                                                   )

        # Prepare string of data arguments with name, indices where columns of that argument resides
        # and types of each of the column.
        data_args_str = self._prepare_data_args_string(kwargs)

        # Get indices of partition_columns and types of all columns.
        data_column_types_str, partition_indices_str, _, partition_cols = \
            self._get_data_col_types_and_partition_col_indices_and_types(self._tdml_df,
                                                                         partition_cols,
                                                                         types_delim=None,
                                                                         idx_delim=None)

        replace_dict = {"<partition_cols_indices>": str(partition_indices_str),
                        "<types_of_data_cols>": str(data_column_types_str),
                        "<data_args_info_str>": f"'{data_args_str}'"}

        return replace_dict, partition_cols

    def _validate_equality_of_partition_values(self, fit_values, trans_values):
        """
        Internal function to compare the partition values in fit() and predict() are same.
        """
        if len(fit_values) != len(trans_values):
            return False

        for val in fit_values:
            if not all([val in trans_values]):
                return False

        return True

    def _get_non_data_related_args_from_kwargs(self, kwargs):
        """
        Get all non-data related arguments from kwargs.
        """
        non_data_related_args = {}
        for k, v in kwargs.items():
            if not isinstance(v, DataFrame):
                non_data_related_args[k] = v
        non_data_related_args.pop("partition_columns", None)
        return non_data_related_args

    def _read_from_template_and_write_dict_to_file(self, template_file, replace_dict,
                                                   output_script_file_name=None):
        """
        Read template file, replace the keys with values and write to new file.
        """
        with open(os.path.join(self._scripts_path, template_file)) as fp:
            script_data = fp.read()
        
        for old, new in replace_dict.items():
            script_data = script_data.replace(old, new)

        if output_script_file_name is None:
            output_script_file_name = self._script_file_name
        file_path = os.path.join(self._tdml_tmp_dir, output_script_file_name)
        with open(file_path, "w") as fp:
            fp.write(script_data)

    def _generate_script_file_from_template_file(self, kwargs, template_file, func_name,
                                                 output_script_file_name=None):
        """
        Internal function to generate script file from template file. It just adds the non-data
        related arguments to the template file and writes the contents to new file, so that these
        arguments are available in the script file for running this function "func_name".
        """
        # Take out all non-data related arguments to write to template file.
        non_data_related_args = self._get_non_data_related_args_from_kwargs(kwargs)

        # Read template file and write the contents to new file with non-data related arguments.
        template_f = os.path.join(self._scripts_path, template_file)
        with open(template_f, "r") as f:
            template = f.read()

        if output_script_file_name is None:
            output_script_file_name = self._script_file_name
        file_path = os.path.join(self._tdml_tmp_dir, output_script_file_name)
        with open(file_path, "w") as f:
            f.write("import json\n")
            f.write(f"params = json.loads('{json.dumps(non_data_related_args)}')\n")
            f.write(template)

        kwargs["file_name"] = output_script_file_name
        kwargs["name"] = func_name

    def _remove_data_related_args_from_kwargs(self, kwargs):
        """
        Internal function to remove data related arguments from kwargs.
        """
        kwargs.pop("data", None)
        kwargs.pop("feature_columns", None)
        kwargs.pop("group_columns", None)
        kwargs.pop("partition_columns", None)
        kwargs.pop("label_columns", None)

    def _convert_pos_args_to_kwargs_for_function(self, pos_args, kwargs, func_name):
        """
        Internal function to convert positional arguments to keyword arguments.
        """
        fn = getattr(getattr(import_module(self.module_name), self.class_name), func_name)
        kwargs.update(zip(fn.__code__.co_varnames[1:], pos_args))

    def _install_model_and_script_files(self, file_name, file_location):
        """
        Internal function to install model and script files to Vantage.
        """
        self._install_initial_model_file()
        self._install_script_file(file_identifier=file_name.split(".")[0],
                                  file_name=file_name,
                                  is_binary=False,
                                  file_location=file_location)

    def _assign_fit_variables_after_execution(self, data, partition_columns, label_columns):
        """
        Internal function to assign fit related variables.
        """
        # Extract sklearn object(s) from the depending on the number of unique partitioning values.
        self._extract_model_objs(n_unique_partitions=len(self._fit_partition_unique_values),
                                 n_partition_cols=len(partition_columns))

        # Need this label columns types in prediction.
        self._fit_label_columns_types = []
        self._fit_label_columns_python_types = []

        for l_c in label_columns:
            column_data = data._td_column_names_and_sqlalchemy_types[l_c.lower()]
            self._fit_label_columns_types.append(column_data)
            self._fit_label_columns_python_types.append(column_data.python_type.__name__)

        # If the model is trained a second time after the object creation,
        # or if set_params() is called after the first model training,
        # this flag will reset to False. So that for subsequent predict/score
        # operations, the newly trained model will be installed.
        if self._is_trained_model_installed:
            self._is_trained_model_installed = False


class _OpenSourceObjectWrapper(_GenericObjectWrapper):
    # This has to be set for every package which subclasses this class.
    OPENSOURCE_PACKAGE_NAME = None

    def __init__(self, model=None, module_name=None, class_name=None, pos_args=None, kwargs=None):
        if model is None and not module_name and not class_name:
            raise TeradataMlException(Messages.get_message(MessageCodes.EITHER_THIS_OR_THAT_ARGUMENT, "model",
                                                           "module_name and class_name"),
                                      MessageCodes.EITHER_THIS_OR_THAT_ARGUMENT)

        validator._validate_mutually_inclusive_arguments(module_name, "module_name",
                                                         class_name, "class_name")

        super().__init__()

        self.module_name = module_name
        self.class_name = class_name
        self.kwargs = kwargs if kwargs is not None else {}
        self.pos_args = pos_args if pos_args is not None else tuple()

        self._fit_label_columns_types = None
        self._fit_label_columns_python_types = None
        self._table_name_prefix = None

        self._is_default_partition_value_fit = True # False when the user provides partition columns.
        self._fit_partition_colums_non_default = None
        self._is_default_partition_value_predict = True # False when the user provides partition columns.

    def __repr__(self):
        if self._is_default_partition_value_fit:
            # Single model use case.
            return self.modelObj.__repr__()

        pd.set_option("display.expand_frame_repr", None)
        pd.set_option("display.max_colwidth", None)
        opt = self.modelObj.__repr__()
        pd.reset_option("display.expand_frame_repr")
        pd.reset_option("display.max_colwidth")
        return opt

    def _initialize_object(self):
        """
        Internal function to initialize sklearn object from module name and class name.
        """
        # Needed when writing imported modules to generated file. TODO: Remove later.
        imported_args = {} 
        # If there are any objects of class `_SkLearnObjectWrapper`, it is modified to
        # corresponding sklearn object.
        _partition_column_names = None
        if "partition_columns" in self.kwargs:
            self._fit_partition_colums_non_default = self.kwargs["partition_columns"]
            self._is_default_partition_value_fit = False
            _partition_column_names = self._fit_partition_colums_non_default


        new_sklearn_pos_args = self.modify_args(None, self.pos_args, imported_args)
        new_sklearn_kwargs = self.modify_args(None, self.kwargs, imported_args)

        # Create model object from new positional and keyword arguments.
        class_obj = getattr(import_module(self.module_name), self.class_name)
        if new_sklearn_pos_args:
            self.modelObj = class_obj(*new_sklearn_pos_args, **new_sklearn_kwargs)
        else:
            self.modelObj = class_obj(**new_sklearn_kwargs)

        # All arguments are moved to kwargs and kept pos_args empty.
        # Might help in set_params() bug fix.
        self.pos_args = tuple()
        _arguments = self.modelObj.__dict__

        if hasattr(self.modelObj, "get_params"):
            # Update kwargs that are both in modelObj and get_params() as there are
            # some classes which return other internals variables also. 
            # Hence, filtering them using get_params().
            for k, v in _arguments.items():
                if type(v).__name__ in ["function", "generator"]:
                    # TODO: ELE-6351: Skipping adding functions and generators to kwargs as these
                    #       are not supported yet due to pickling issue.
                    continue
                if self.get_params():
                    if k in self.get_params():
                        self.kwargs[k] = v
                else:
                    _model_init_arguments = None
                    try:
                        _model_init_arguments = self.modelObj.__init__.__code__.co_varnames
                    except AttributeError:
                        pass
                    if _model_init_arguments:
                        self.kwargs = dict((k, v) for k, v in _arguments.items() if k in _model_init_arguments)
                    else:
                        self.kwargs = _arguments
        else:
            # Model selection classes will not have `get_params`, in which case modelObj's __dict__
            # is saved as kwargs.
            self.kwargs = _arguments

        if _partition_column_names:
            self.kwargs["partition_columns"] = _partition_column_names

    def _initialize_variables(self, table_name_prefix):
        """
        Internal function to initialize variables used in this class.
        """
        self.feature_names_in_ = None
        self._table_name_prefix = table_name_prefix
        self._model_file_name_prefix = _generate_new_name(type="file")
        self.model_file_paths_local = set()

        self._fit_execution_time = None
        self._fit_predict_execution_time = None
        self._partial_fit_execution_time = None
        self._predict_execution_time = None
        self._transform_execution_time = None
        self._score_execution_time = None

        # Set to partition columns when training is done with partition columns.
        self._fit_partition_colums_non_default = None

        self._is_model_installed = False
        self._fit_partition_unique_values = [[self._default_data_partition_value]]

    def _get_returning_df(self, script_df, partition_column, returns):
        """
        Internal function to return the teradataml Dataframe except
        partition_column.
        """
        if self._is_default_partition_value_fit:
            # For single model case, partition column is internally generated
            # and no point in returning it to the user.

            # Extract columns from return types.
            returning_cols = [col[0] for col in returns[len(partition_column):]]
            return script_df.select(returning_cols)
        return script_df

    def modify_args(self, fp1, arg, imported_args):
        """
        Internal function to recursively (if "arg" is list/tuple/dict) check if any sklearn object
        of opensourceML is present in the argument "arg" and modify it to corresponding sklearn
        object.
        This function can also be used to write import statements to file (if "fp1" is not
        None). Update "imported_args" dictionary with imported module and class name to avoid
        importing same module and class again when writing to file. This is useful when we want to
        generate script from template file.
        Pass None to "fp1" if we don't want to write to file and just modify opensourceML sklearn
        object to corresponding sklearn object.
        """
        if isinstance(arg, type(self)):
            imported_tuple = (arg.module_name, arg.class_name)
            already_imported = imported_args.get(imported_tuple, False)
            if not already_imported:
                imported_args[imported_tuple] = True
                if fp1:
                    fp1.write(f"from {arg.module_name} import {arg.class_name}\n")
                self.modify_args(fp1, arg.pos_args, imported_args)
                self.modify_args(fp1, arg.kwargs, imported_args)
            return arg.modelObj
        elif isinstance(arg, list):
            return [self.modify_args(fp1, val, imported_args) for val in arg]
        elif isinstance(arg, tuple):
            return tuple([self.modify_args(fp1, val, imported_args) for val in arg])
        elif type(arg).__name__ == "generator":
            # Raising exception as generator object can't be pickled.
            # TODO: ELE-6351 - Find ways to pickle generator object later.
            raise ValueError("Generator type/iterator is not supported for any argument. "\
                             "Support will be added later.")
        elif type(arg).__name__ == "function":
            # Raising exception as functions/lambda functions can't be pickled.
            # TODO: ELE-6351 - Find ways to pickle functions later.
            raise ValueError("Functions are not supported for any argument. "\
                             "Support will be added later.")
        elif isinstance(arg, dict):
            return dict(
                (
                    self.modify_args(fp1, k, imported_args),
                    self.modify_args(fp1, v, imported_args),
                )
                for k, v in arg.items() if k != "partition_columns"
            )
        # elif arg == "partition_columns":

        else:
            return arg

    def _install_initial_model_file(self, use_dummy_initial_file=False):
        """
        If model file(s) is/are not installed in Vantage, then install it/them.
        """
        if isinstance(self.modelObj, pd.DataFrame):
            # Get list of unique partition values and corresponding model object as dict.
            partition_values_model_dict = {}
            obj_list = self.modelObj.values.tolist()
            for lst in obj_list:
                partition_values_model_dict[tuple(lst[:len(self._fit_partition_colums_non_default)])] = \
                    lst[len(self._fit_partition_colums_non_default)]

        for partition in self._fit_partition_unique_values:
            # Create a new file with file name with partition values and
            # dump sklearn object into it. Finally install the file to Vantage.
            partition_join = "_".join([str(x) for x in partition])
            file_name = f"{self._model_file_name_prefix}_{partition_join}"
            # Replace '-' with '_' as '-' can't be present in file identifier.
            # Needed this replace because partition_columns can be negative.
            file_name = file_name.replace("-", "_")
            full_file_name = os.path.join(self._tdml_tmp_dir, file_name)
            with open(full_file_name, "wb+") as fp:
                # Write sklearn object to file.
                if isinstance(self.modelObj, pd.DataFrame):
                    # If multiple models, then write the model corresponding to the partition value.
                    fp.write(pickle.dumps(partition_values_model_dict[tuple(partition)]))
                else:
                    if use_dummy_initial_file:
                        fp.write(pickle.dumps("abc"))
                    else:
                        fp.write(pickle.dumps(self.modelObj))
            self.model_file_paths_local.add(file_name)

            self._install_script_file(file_identifier=file_name,
                                      file_name=file_name,
                                      is_binary=True,
                                      file_location=self._tdml_tmp_dir)

            if self._is_lake_system:
                # Need to pass env_name along with file_name for cleaning up the files in env.
                obj = f"{self._env.env_name}::{file_name}"
                if installed_model_files[obj] == 0:
                    # Add to GC for the first time the model file (along with env name) is encountered.
                    installed_model_files[obj] = 1
                    GarbageCollector._add_to_garbagecollector(object_name=obj,
                                                object_type=TeradataConstants.TERADATA_APPLY)
            else:
                if installed_model_files[file_name] == 0:
                    # Add to GC for the first time the model file is encountered.
                    installed_model_files[file_name] = 1
                    GarbageCollector._add_to_garbagecollector(object_name=file_name,
                                                object_type=TeradataConstants.TERADATA_SCRIPT)

            self._is_model_installed = True

    def _validate_unique_partition_values(self, data, partition_columns):
        """
        Internal function to validate if the partition values in partition_columns used in fit()
        and predict() are same.
        """
        data._index_label = None
        unique_values = data.drop_duplicate(partition_columns).get_values()

        trans_unique_values = sorted(unique_values.tolist(), key=lambda x: tuple(x))
        fit_unique_values = sorted(self._fit_partition_unique_values.tolist() \
                                    if not isinstance(self._fit_partition_unique_values, list) \
                                    else self._fit_partition_unique_values, key=lambda x: tuple(x))
        default_unique_values = [[self._default_data_partition_value]]

        if fit_unique_values == default_unique_values and \
            trans_unique_values != default_unique_values:
            error_msg = Messages.get_message(MessageCodes.PARTITION_IN_BOTH_FIT_AND_PREDICT,
                                             "without", "with")
            msg_code = MessageCodes.PARTITION_IN_BOTH_FIT_AND_PREDICT
            raise TeradataMlException(error_msg, msg_code)

        if not self._validate_equality_of_partition_values(fit_unique_values, trans_unique_values):
            raise TeradataMlException(
                Messages.get_message(MessageCodes.PARTITION_VALUES_NOT_MATCHING, "training", "test"),
                MessageCodes.PARTITION_VALUES_NOT_MATCHING
            )

    def fit(self, **kwargs):
        pass

    def _convert_arguments_to_modelObj(self, args, idx_multi_model=None):
        """
        Internal function to convert all OpensourceML related objects in arguments to
        underlying model objects.
        """
        if isinstance(args, dict):
            new_args = args.copy() # To avoid updating 
            for k, v in new_args.items():
                if isinstance(v, type(self)):
                    if idx_multi_model is not None:
                        # single model. This argument is set only when modelObj is single model.
                        new_args[k] = v.modelObj
                    else:
                        # multi-model. Get appropriate model from modelObj.
                        new_args[k] = v.modelObj.iloc[idx_multi_model]["model"]
                else:
                    new_args[k] = v
            return new_args
        
        # If args is tuple, convert all elements to underlying model object.
        elif isinstance(args, tuple):
            new_args = tuple()
            for arg in args:
                if isinstance(arg, type(self)):
                    if idx_multi_model is None:
                        # single model. This argument is set only when modelObj is single model.
                        new_args += (arg.modelObj,)
                    else:
                        # multi-model. Get appropriate model from modelObj.
                        new_args += (arg.modelObj.iloc[idx_multi_model]["model"],)
                else:
                    new_args += (arg,)
            return new_args
        return args

    def __get_obj_attributes_multi_model(self, name):
        """
        Internal function to get attributes of all sklearn model objects when multiple models are
        generated by fit.
        """

        def __generate_model_object(model_obj_value, init_model_obj):
            """
            Internal function to generate _SkLearnWrapperObject model object from model_obj_value.
            """
            # Create _SkLearnObjectWrapper object from opensource model object.
            model_obj = self.__class__(model=init_model_obj)

            model_obj.modelObj = model_obj_value
            model_obj._is_model_installed = True

            # Setting other model attributes.
            model_obj._is_default_partition_value_fit = self._is_default_partition_value_fit
            model_obj._is_default_partition_value_predict = self._is_default_partition_value_predict
            model_obj._fit_partition_colums_non_default = self._fit_partition_colums_non_default
            model_obj._fit_partition_unique_values = self._fit_partition_unique_values
            return model_obj

        # Wrapper function to invoke dynamic method, using arguments
        # passed by user, on model in each row.
        def __sklearn_method_invoker_for_multimodel(*c, **kwargs):
            multi_models = self.modelObj.copy()
            for i in range(multi_models.shape[0]):
                curr_model = multi_models.iloc[i]["model"]
                partition_values = multi_models.iloc[i][0:len(self._fit_partition_colums_non_default)].to_list()
                partition_values = "_".join([str(x) for x in partition_values])
                if self.module_name == "lightgbm.basic" and self.class_name == "Booster" and name == "save_model":
                    # filename is first argument.
                    kwargs1 = kwargs.copy()
                    c1 = c

                    if len(c) > 0:
                        c1 = list(c1)
                        c1[0] = f"{c1[0]}_{partition_values}"
                        c1 = tuple(c1)
                    if len(kwargs) > 0 and kwargs.get("filename", None):
                        kwargs1["filename"] = f"{kwargs1['filename']}_{partition_values}"
                    
                    multi_models.at[i, "model"] = getattr(curr_model, name)(*self._convert_arguments_to_modelObj(c1, i),
                                                                            **self._convert_arguments_to_modelObj(kwargs1, i))
                else:
                    multi_models.at[i, "model"] = getattr(curr_model, name)(*self._convert_arguments_to_modelObj(c, i),
                                                                            **self._convert_arguments_to_modelObj(kwargs, i))
            
            first_function_value = multi_models.at[0, "model"]
            if self.__class__._validate_model_supportability(first_function_value):
                return __generate_model_object(multi_models, init_model_obj=first_function_value)

            multi_models = multi_models.rename(columns={"model": name})

            # Select only partition columns and the attribute column.
            return multi_models[self._fit_partition_colums_non_default + [name]]

        # Assuming that self.modelObj will have at least 1 row.

        # Get attribute instance from first model object.
        first_atrribute_instance = getattr(self.modelObj.iloc[0]["model"], name)

        # If first_atrribute_instance is callable, it should be applied on model in each row
        # using passed arguments.
        if callable(first_atrribute_instance):
            return __sklearn_method_invoker_for_multimodel

        output_attributes = self.modelObj.copy()
        for i in range(output_attributes.shape[0]):
            model = output_attributes.iloc[i]["model"]
            output_attributes.at[i, "model"] = getattr(model, name)

        if self.__class__._validate_model_supportability(first_atrribute_instance):
            return __generate_model_object(output_attributes, init_model_obj=first_atrribute_instance)

        return output_attributes.rename(columns={"model": name})

    def __getattr__(self, name):
        # This just run attributes (functions and properties) from opensource (sklearn/lightgbm) objects.
        def __sklearn_method_invoker(*c, **kwargs):
            # Opensource model is returned from the function call. Create _OpensourceObjectWrapper object.
            model_obj = attribute_instance(*self._convert_arguments_to_modelObj(c), **self._convert_arguments_to_modelObj(kwargs))
            if self.__class__._validate_model_supportability(model_obj):
                model_obj = self.__class__(model=model_obj)
                model_obj._is_model_installed = True # Trained model is returned by function call.
            return model_obj

        if isinstance(self.modelObj, pd.DataFrame):
            return self.__get_obj_attributes_multi_model(name)

        attribute_instance = getattr(self.modelObj, name)

        if callable(attribute_instance):
            return __sklearn_method_invoker

        if self.__class__._validate_model_supportability(attribute_instance):
            # sklearn model is returned from the attribute. Create _SkLearnObjectWrapper object.
            model_obj = self.__class__(model=attribute_instance)
            model_obj._is_model_installed = True # Trained model is returned as attribute.
            return model_obj

        return attribute_instance

    @classmethod
    def _validate_model_supportability(cls, model):
        """
        Internal function to validate if the model provided for deployment is supported by
        teradataml's opensourceML.
        """
        error_msg = Messages.get_message(MessageCodes.MODEL_CATALOGING_OPERATION_FAILED, "validate",
                                         "The given model is not a supported opensource model.")
        msg_code = MessageCodes.MODEL_CATALOGING_OPERATION_FAILED
        package_name = None
        class_name = None
        try:
            # For scikit-learn, model.__module__ is similar to 'sklearn.linear_model._base'.
            # TODO: check for other supported packages.
            if hasattr(model, "__module__"):
                package_name = model.__module__.split(".")[0]
                if package_name not in OpenSourcePackage.values():
                    return False
            if hasattr(model, "__class__"):
                class_name = model.__class__.__name__
        except Exception as ex:
            # If in case, model.__module__ fails.
            raise TeradataMlException(error_msg, msg_code) from ex

        # True only if package name is opensource package name and class name is not internal class.
        return True if package_name and class_name and \
            package_name == cls.OPENSOURCE_PACKAGE_NAME.value and not class_name.startswith("_") else False

    def _save_model(self, model_name, replace_if_exists=False):
        """
        Internal function to save the model stored in file at location mentioned by class variable
        "model_file_path_local" to Vantage using BYOM methods save_byom() and delete_byom() based
        on the value of "replace_if_exists" argument.
        """
        # Creating a table, if doesn't exist, in Vantage to store the model info.
        conn = get_connection()
        osml_models_table_exists = conn.dialect.has_table(conn,
                                                          table_name=_OSML_MODELS_TABLE_NAME,
                                                          schema=self._db_name,
                                                          table_only=True)
        if not osml_models_table_exists:
            all_columns = _OSML_MODELS_TABLE_COLUMNS_TYPE_DICT.copy()
            all_columns.update(_OSML_ADDITIONAL_COLUMN_TYPES)
            _create_table(table_name=_OSML_MODELS_TABLE_NAME, columns=all_columns,
                          primary_index=_OSML_MODELS_PRIMARY_INDEX, schema_name=self._db_name)

        model_obj = OpensourceModels(is_default_partition_value=self._is_default_partition_value_fit, 
                                     partition_file_prefix=self._model_file_name_prefix,
                                     fit_partition_columns_non_default=self._fit_partition_colums_non_default,
                                     model=self.modelObj,
                                     pos_args=self.pos_args,
                                     key_args=self.kwargs)

        # Saved the model object to a file to be used in save_byom() for writing to Vantage table.
        file_name = os.path.join(self._tdml_tmp_dir, "deployed_file.pickle")
        with open(file_name, "wb+") as fp:
            fp.write(pickle.dumps(model_obj))

        try:
            save_byom(model_id=model_name,
                    model_file=file_name,
                    table_name=_OSML_MODELS_TABLE_NAME,
                    additional_columns_types=_OSML_ADDITIONAL_COLUMN_TYPES,
                    additional_columns={"package": self.OPENSOURCE_PACKAGE_NAME.value})
        except TeradataMlException as ex:
            model_exists_msg = Messages.get_message(MessageCodes.MODEL_ALREADY_EXISTS, model_name)
            if not replace_if_exists and model_exists_msg == str(ex):
                raise
            elif replace_if_exists and model_exists_msg == str(ex):
                # Delete the model from Model table and save again.
                delete_byom(model_id=model_name, table_name=_OSML_MODELS_TABLE_NAME)
                save_byom(model_id=model_name,
                          model_file=file_name,
                          table_name=_OSML_MODELS_TABLE_NAME,
                          additional_columns_types=_OSML_ADDITIONAL_COLUMN_TYPES,
                          additional_columns={"package": self.OPENSOURCE_PACKAGE_NAME.value})
            else:
                raise
        finally:
            os.remove(file_name)

    @classmethod
    def _deploy(cls, model_name, model, replace_if_exists=False):
        """
        Internal function to create an instance of the class using the model and deploy
        the model to Vantage.
        """
        is_model_supportable = cls._validate_model_supportability(model=model)
        if not is_model_supportable:
            raise TeradataMlException(Messages.get_message(MessageCodes.MODEL_CATALOGING_OPERATION_FAILED,
                                                           "deploy", "The given model is not a supported opensource model."),
                                      MessageCodes.MODEL_CATALOGING_OPERATION_FAILED)

        cls = cls(model=model)
        # Load the model file into Vantage node as file can be used in
        # predict or other operations.
        cls._install_initial_model_file()

        cls._save_model(model_name, replace_if_exists)
        
        return cls

    @classmethod
    def _load(cls, model_name):
        """
        Internal function to load model corresponding to the package (like sklearn etc)
        from Vantage to client using retrieve_byom() and create an instance of the class if
        the model is from the same package.
        """
        try:
            model = retrieve_byom(model_id=model_name, table_name=_OSML_MODELS_TABLE_NAME,
                                  return_addition_columns=True)
        except TeradataMlException as ex:
            # Not showing table name in error message as it is an internal table.
            part_msg = f"Model '{model_name}' not found in the table "
            if part_msg in str(ex):
                raise TeradataMlException(Messages.get_message(MessageCodes.MODEL_NOT_FOUND, model_name, ""),
                                          MessageCodes.MODEL_NOT_FOUND)
            raise

        model_vals_list = model.get_values()[0]
        # List of 3 elements -
        #   - model name as index column,
        #   - 1st contains model object with fields: is_default_partition_value, partition_file_prefix, model. etc
        #   - 2nd contains package name.
        model_obj = pickle.loads(model_vals_list[0])
        model = model_obj.model
        package = model_vals_list[1]

        if package != cls.OPENSOURCE_PACKAGE_NAME.value:
            # Raise error if trying to access model of different package.
            raise TeradataMlException(Messages.get_message(MessageCodes.MODEL_NOT_FOUND, model_name, 
                                        f". Requested model is from '{package}' package"),
                                      MessageCodes.MODEL_NOT_FOUND)

        if isinstance(model, pd.DataFrame):
            # Create a new instance of the class and set the model object to the instance.
            # Instantiation can take only model, not model object. Hence, passing one of the model
            # from pandas df. Updating modelObj and other fields later
            cls = cls(model=model.iloc[1,2])
            cls.modelObj = model
            cls._fit_partition_unique_values = [lst[:len(lst)-1] for lst in model.values.tolist()]
        else:
            cls = cls(model=model)
        
        cls._model_file_name_prefix = model_obj.partition_file_prefix
        cls._is_default_partition_value_fit = model_obj.is_default_partition_value
        cls._fit_partition_colums_non_default = model_obj.fit_partition_columns_non_default
        cls.pos_args = model_obj.pos_args
        cls.kwargs = model_obj.key_args

        # Load the model file into Vantage node as file can be used in
        # predict or other operations.
        cls._install_initial_model_file()

        return cls

    def deploy(self, model_name, replace_if_exists=False):
        """
        DESCRIPTION:
            Deploys the model held by interface object to Vantage.

        PARAMETERS:
            model_name:
                Required Argument.
                Specifies the unique name of the model to be deployed.
                Types: str

            replace_if_exists:
                Optional Argument.
                Specifies whether to replace the model if a model with the same name already
                exists in Vantage. If this argument is set to False and a model with the same
                name already exists, then the function raises an exception.
                Default Value: False
                Types: bool

        RETURNS:
            The opensource object wrapper.

        RAISES:
            TeradataMLException if model with "model_name" already exists and the argument
            "replace_if_exists" is set to False.

        EXAMPLES:
            >>> from teradataml import td_sklearn
            >>> model = td_sklearn.LinearRegression(normalize=True)
            >>> model
            LinearRegression(normalize=True)

            # Example 1: Deploy the model held by interface object to Vantage.
            >>> lin_reg = model.deploy("linreg_model_ver_2")
            Model is saved.
            >>> lin_reg
            LinearRegression(normalize=True)

            # Example 2: Deploy the model held by interface object to Vantage with the name same
            #            as that of model that already existed in Vantage.
            >>> lin_reg = model.deploy("linreg_model_ver_2", replace_if_exists=True)
            Model is deleted.
            Model is saved.
            >>> lin_reg
            LinearRegression(normalize=True)
        """

        # Install model file into Vantage, if not installed.
        self._install_initial_model_file()

        self._save_model(model_name, replace_if_exists)
        return self


class _SkLearnObjectWrapper(_OpenSourceObjectWrapper):

    OPENSOURCE_PACKAGE_NAME = OpenSourcePackage.SKLEARN

    def __init__(self, model=None, module_name=None, class_name=None, pos_args=None, kwargs=None):
        super().__init__(model=model, module_name=module_name, class_name=class_name,
                         pos_args=pos_args, kwargs=kwargs)

        self._initialize_variables(table_name_prefix="td_sklearn_")
        if model is not None:
            self.modelObj = model
            self.module_name = model.__module__.split("._")[0]
            self.class_name = model.__class__.__name__
            # __dict__ gets all the arguments as dictionary including default ones and positional
            # args.
            self.kwargs = model.__dict__
            self.pos_args = tuple() # Kept empty as all are moved to kwargs.
        else:
            self._initialize_object()

    def _validate_args_and_get_data(self, X=None, y=None, groups=None, kwargs={},
                                    skip_either_or_that=False):
        """
        Internal function to validate arguments passed to exposed opensource APIs and return
        parent DataFrame, feature columns, label columns, group columns, data partition columns.
        """
        _validate_opensource_func_args(X=X, y=y, groups=groups,
                                       fit_partition_cols=self._fit_partition_colums_non_default,
                                       kwargs=kwargs,
                                       skip_either_or_that=skip_either_or_that)
        return _derive_df_and_required_columns(X=X, y=y, groups=groups, kwargs=kwargs,
                                        fit_partition_cols=self._fit_partition_colums_non_default)

    def _run_fit_related_functions(self,
                                   data,
                                   feature_columns,
                                   label_columns,
                                   partition_columns,
                                   func,
                                   classes=None,
                                   file_name="sklearn_fit.py"):
        """
        Internal function to run fit() and partial_fit() functions.
        """
        label_columns = self._get_columns_as_list(label_columns)

        data, new_partition_columns = self._get_data_and_data_partition_columns(data,
                                                                                feature_columns,
                                                                                label_columns,
                                                                                partition_columns)

        model_type = BLOB() if self._is_lake_system else CLOB()
        return_types = [(col, data._td_column_names_and_sqlalchemy_types[col.lower()]) 
                        for col in new_partition_columns] + [("model", model_type)]

        if classes:
            class_type = type(classes[0]).__name__
            classes = "--".join([str(x) for x in classes])
        else:
            classes = str(None)
            class_type = str(None)
        
        data_column_types_str, partition_indices_str, _, new_partition_columns = \
            self._get_data_col_types_and_partition_col_indices_and_types(data, new_partition_columns)

        # db_name is applicable for enterprise system.
        db_file_name = file_name if self._is_lake_system else f"./{self._db_name}/{file_name}"
        py_exc = UtilFuncs._get_python_execution_path()
        script_command = f"{py_exc} {db_file_name} {func} {len(feature_columns)} "\
            f"{len(label_columns)} {partition_indices_str} {data_column_types_str} "\
            f"{self._model_file_name_prefix} {classes} {class_type} {self._is_lake_system}"

        # Get unique values in partitioning columns.
        self._fit_partition_unique_values = data.drop_duplicate(new_partition_columns).get_values()

        self._install_initial_model_file()

        self._model_data = self._run_script(data, script_command, new_partition_columns,
                                            return_types)

        self._assign_fit_variables_after_execution(data, new_partition_columns, label_columns)

    def partial_fit(self, X=None, y=None, classes=None, **kwargs):
        """
        Please check the description in Docs/OpensourceML/sklearn.py.
        """
        st_time = time.time()

        # "classes" argument validation.
        arg_info_matrix = []
        arg_info_matrix.append(["classes", classes, True, (list)])
        _Validators._validate_function_arguments(arg_info_matrix)

        self._is_default_partition_value_fit = True # False when the user provides partition columns.

        data, feature_columns, label_columns, _, partition_columns = \
            self._validate_args_and_get_data(X=X, y=y, groups=None, kwargs=kwargs)

        if partition_columns:
            self._is_default_partition_value_fit = False
            self._fit_partition_colums_non_default = partition_columns

        self._run_fit_related_functions(data,
                                        feature_columns,
                                        label_columns,
                                        partition_columns,
                                        inspect.stack()[0][3],
                                        classes)

        self._partial_fit_execution_time = time.time() - st_time

        return self

    def fit(self, X=None, y=None, **kwargs):
        """
        Please check the description in Docs/OpensourceML/sklearn.py.
        """
        st_time = time.time()

        self._is_default_partition_value_fit = True # False when the user provides partition columns.

        data, feature_columns, label_columns, _, partition_columns = \
            self._validate_args_and_get_data(X=X, y=y, groups=None, kwargs=kwargs)

        if partition_columns:
            self._is_default_partition_value_fit = False
            self._fit_partition_colums_non_default = partition_columns

        file_name = kwargs.pop("file_name", None)
        func_name = kwargs.pop("name", "fit")

        args = {"data": data,
                "feature_columns": feature_columns,
                "label_columns": label_columns,
                "partition_columns": partition_columns,
                "func": func_name}
        
        if file_name is not None:
            args["file_name"] = file_name

        self._run_fit_related_functions(**args)

        self._fit_execution_time = time.time() - st_time

        return self

    def set_params(self, **params):
        """
        Please check the description in Docs/OpensourceML/sklearn.py.
        """
        for key, val in params.items():
            self.kwargs[key] = val

        # Initialize with new arguments and return the class/model object.
        # set_params takes all keyword arguments and no positional arguments.
        self.__init__(None, self.module_name, self.class_name, tuple(), self.kwargs)
        return self

    # get_params() will be executed through __getattr__().

    # @_validate_fit_run
    def __getattr__(self, name):
        def __run_transform(*c, **kwargs):
            kwargs["name"] = name
            return self._transform(*c, **kwargs)

        def __run_function_needing_all_rows(*c, **kwargs):
            kwargs["name"] = name
            return self._run_function_needing_all_rows(*c, **kwargs)

        def __run_kneighbors(*c, **kwargs):
            kwargs["name"] = name
            return self._run_neighbors(*c, **kwargs)

        if name in ["score", "aic", "bic", "perplexity"]:
            # TODO: ELE-6352 - Implement error_norm() function later.
            return __run_function_needing_all_rows

        if name in ["kneighbors",
                    "radius_neighbors",
                    "kneighbors_graph",
                    "radius_neighbors_graph"]:
            return __run_kneighbors

        if name in ["predict",
                    "transform",
                    "inverse_transform",
                    "predict_proba",
                    "predict_log_proba",
                    "decision_function",
                    "score_samples",
                    "decision_path",
                    "apply",
                    "cost_complexity_pruning_path",
                    "gibbs",
                    "kneighbors_graph",
                    "radius_neighbors_graph",
                    "mahalanobis",
                    "correct_covariance",
                    "reweight_covariance",
                    "path"]:
            return __run_transform

        return super().__getattr__(name)

    def _special_handling_multimodel_(self, data, feature_columns, label_columns, partition_columns,
                                      func_name, **kwargs):
        """
        Internal function to handle multi model case for transform function for functions 
        ["SelectFpr", "SelectFdr", "SelectFwe", "SelectFromModel", "RFECV"] of feature_selection module
        and "Birch" of cluster module.
        These functions generate multiple models and when transform is applied to each model, it generates
        output with different number of columns.
        """
        skl_objs_dict = {}
        no_of_unique_partitions = len(self._fit_partition_unique_values)
        no_of_partitioning_cols = len(self._fit_partition_unique_values[0])

        # Run on 10 rows of data individually using corresponding scikit-learn objects based on paritition value
        # and get the maximum number of columns and their types.
        for i in range(no_of_unique_partitions):
            skl_objs_dict[tuple(self.modelObj.iloc[i, :no_of_partitioning_cols])] = self.modelObj.iloc[i]["model"]
        

        data = data.select(feature_columns + label_columns + partition_columns)
        ten_row_data = data.head(10).get_values()
        X = numpy.array(ten_row_data)

        # For multi-model case, model in one AMP can give more number of columns than other AMPs.
        # Returns clause can't contain different number of columns in different AMPs. Hence, taking
        # maximum number of columns and their types from all models.
        max_no_of_columns = 0
        max_col_names = []
        max_col_types = []

        def _get_input_row_without_nans(row):
            """
            `inverse_transform` should not contain NaNs. Hence, removing NaNs from the row.
            """
            X1 = []
            for _, v in enumerate(row):
                if isinstance(v, type(None)) or isinstance(v, str) or not math.isnan(v) or self.module_name == "sklearn.impute":
                    # Add to list when:
                    #  - v is None or
                    #   - v is string or
                    #   - v is not nan or
                    #   - if module is impute (which transforms nan values) even though v is nan.
                    X1.append(v)
                else:
                    # skip nan values.
                    pass
            return X1

        for i in range(X.shape[0]):
            # Run `transform` or `inverse_transform` on each row with corresponding scikit-learn model object.
            partition_values = tuple(X[i, -no_of_partitioning_cols:])
            skl_obj = skl_objs_dict[partition_values]

            X1 = X[i, :-no_of_partitioning_cols]
            # Since Nans/NULLs are added in transform for last columns where some models generated
            # less number of columns, removing Nans/NULLs from the input row for inverse_transform
            # using function _get_input_row_without_nans().
            X1 = numpy.array([_get_input_row_without_nans(X1)])

            trans_opt = getattr(skl_obj, func_name)(X1, **kwargs)

            no_of_columns = 1

            if trans_opt.shape == (X1.shape[0],):
                trans_opt = trans_opt.reshape(X1.shape[0], 1)
            
            if isinstance(trans_opt[0], numpy.ndarray) \
                    or isinstance(trans_opt[0], list) \
                    or isinstance(trans_opt[0], tuple):
                no_of_columns = len(trans_opt[0])
            
            col_names = [f"{self.class_name.lower()}_{func_name}_{(i + 1)}" for i in range(no_of_columns)]

            # Get new column sqlalchemy types for pandas df columns of transform output.
            opt_pd = pd.DataFrame(trans_opt)

            # Get output column types for each column in pandas df from the output of transform
            # type functions.
            types = {}
            for idx in range(no_of_columns):
                col = list(opt_pd.columns)[idx]

                # Only one row in trans_opt.
                if isinstance(trans_opt[0], numpy.ndarray) or isinstance(trans_opt[0], tuple) or isinstance(trans_opt[0], list):
                    type_ = type(trans_opt[0][idx])
                else:
                    # only one value in the output.
                    type_ = type(trans_opt[0])

                # If type of the output value (trans_opt) is None, then use `str` as type since
                # pandas astype() does not accept None type.
                if type_ is type(None):
                    type_ = str

                # numpy integer columns with nan values can't be typecasted using pd.astype() to int64.
                # It raises error like "Cannot convert non-finite values (NA or inf) to integer: 
                #                       Error while type casting for column '2'"
                # Hence, using pd.Int64Dtype() for integer columns with nan values.
                types[col] = type_ if type_ not in [int, numpy.int64] else pd.Int64Dtype()

            # Without this, all columns will be of object type and gets converted to VARCHAR in Vantage.
            opt_pd = opt_pd.astype(types)

            # If the datatype is not specified then check if the datatype is datetime64 and timezone is present then map it to
            # TIMESTAMP(timezone=True) else map it according to default value.
            col_types = [TIMESTAMP(timezone=True)
                        if pt.is_datetime64_ns_dtype(opt_pd.dtypes[key]) and (opt_pd[col_name].dt.tz is not None)
                        else _get_sqlalchemy_mapping(str(opt_pd.dtypes[key]))
                        for key, col_name in enumerate(list(opt_pd.columns))]

            # Different models in multi model case can generate different number of output columns for example in
            # SelectFpr. Hence, taking the model which generates maximum number of columns.
            if no_of_columns > max_no_of_columns:
                max_no_of_columns = no_of_columns
                max_col_names = col_names
                max_col_types = col_types

        return [(c_name, c_type) for c_name, c_type in zip(max_col_names, max_col_types)]

    def _get_return_columns_for_function_(self,
                                          data,
                                          feature_columns,
                                          label_columns,
                                          partition_columns,
                                          func_name,
                                          kwargs):
        """
        Internal function to return list of column names and their sqlalchemy types
        which should be used in return_types of Script.
        """
        if func_name == "fit_predict":
            """
            Get return columns using label_columns.
            """
            return [(f"{self.class_name.lower()}_{func_name}_{(i + 1)}",
                     data._td_column_names_and_sqlalchemy_types[col.lower()])
                    for i, col in enumerate(label_columns)]

        if func_name == "predict" and self.OPENSOURCE_PACKAGE_NAME == OpenSourcePackage.SKLEARN:
            """
            Return predict columns using either label_columns (if provided) or 
            self._fit_label_columns_types (if the function is trained using label columns).
            Otherwise run predict on ten rows of data to get the number of columns and their types
            after this if condition.
            """
            if label_columns:
                return [(f"{self.class_name.lower()}_{func_name}_{(i + 1)}",
                         data._td_column_names_and_sqlalchemy_types[col.lower()])
                             for i, col in enumerate(label_columns)]
            if self._fit_label_columns_types:
                return [(f"{self.class_name.lower()}_{func_name}_{(i + 1)}", col_type)
                        for i, col_type in enumerate(self._fit_label_columns_types)]

        ## If function is not `fit_predict`:
        #   then take one row of transform/other functions to execute in client
        #   to get number of columns in return clause and their Vantage types.
        n_f = len(feature_columns)
        n_c = len(label_columns)

        # For paritioning columns, it will be a dataframe and getattr(modelObj, func_name) fails.
        # Just for getting the number of columns and their types, using only one model of all.
        if len(self._fit_partition_unique_values) == 1:
            # Single model case.
            skl_obj = self.modelObj
        else:
            # Multi model case.
            if (func_name in ["transform", "inverse_transform"] and \
                self.class_name in ["SelectFpr", "SelectFdr", "SelectFwe", "SelectFromModel", "RFECV", "Birch"]) or \
                (self.module_name == "lightgbm.sklearn" and self.class_name == "LGBMClassifier"):
                # Special handling for multi model case for transform function as these classes
                # generate transform output with different number of columns for each model.
                # Hence, need to add Nulls/Nans to columns which are not present in the transform output of
                # some models.
                return self._special_handling_multimodel_(data, feature_columns, label_columns,
                                                          partition_columns, func_name, **kwargs)

            skl_obj = self.modelObj.iloc[0]["model"]

        data = data.select(feature_columns + label_columns)

        ten_row_data = data.head(10).get_values()
        X = numpy.array(ten_row_data)
        if label_columns:
            y = X[:,n_f : n_f + n_c]
            X = X[:,:n_f]
            # predict() now takes 'y' also for it to return the labels from script. Skipping 'y'
            # in local run if passed. Generally, 'y' is passed to return y along with actual output.
            try:
                trans_opt = getattr(skl_obj, func_name)(X, y, **kwargs)
            except TypeError as ex:
                # Function which does not accept 'y' like predict_proba() raises error like
                # "predict_proba() takes 2 positional arguments but 3 were given".
                trans_opt = getattr(skl_obj, func_name)(X, **kwargs)
        else:
            trans_opt = getattr(skl_obj, func_name)(X, **kwargs)

        if func_name == "path":
            raise NotImplementedError(
                "path() returns tuple of ndarrays of different shapes. Not Implemented yet."
            )

        if isinstance(trans_opt, numpy.ndarray) and trans_opt.shape == (X.shape[0],):
            trans_opt = trans_opt.reshape(X.shape[0], 1)
        
        if type(trans_opt).__name__ in ["csr_matrix", "csc_matrix"]:
            no_of_columns = trans_opt.get_shape()[1]
            trans_opt = trans_opt.toarray()
        elif isinstance(trans_opt, dict):
            raise NotImplementedError(f"Output returns dictionary {trans_opt}. NOT implemented yet.")
        elif isinstance(trans_opt[0], numpy.ndarray) \
                or isinstance(trans_opt[0], list) \
                or isinstance(trans_opt[0], tuple):
            no_of_columns = len(trans_opt[0])
        else:
            no_of_columns = 1

        # Special handling when inverse_transform of no_of_columns returns no of rows 
        # less than the no of classes. Such columns are filled with NaN values.
        # Updating number of columns here (new columns with NaN values will be added).
        if func_name == "inverse_transform" and self.class_name == "MultiLabelBinarizer":
            no_of_columns = len(self.classes_)
            for i in range(len(ten_row_data)):
                trans_opt[i] += tuple([numpy.nan] * (no_of_columns - len(trans_opt[i])))

        # Special handling required for cross_decomposition classes's transform function, which
        # takes label columns also. In this case, output is a tuple of numpy arrays - x_scores and
        # y_scores. If label columns are not provided, only x_scores are returned.
        if self.module_name == "sklearn.cross_decomposition" and func_name == "transform":
            # For cross_decomposition, output is a tuple of arrays when label columns are provided
            # along with feature columns for transform function. In this case, concatenate the
            # arrays and return the column names accordingly.
            if isinstance(trans_opt, tuple): # tuple when label_columns is provided.
                assert trans_opt[0].shape == trans_opt[1].shape,\
                    "Output arrays should be of same shape when transform/fit_transform is run "\
                    "with label columns for cross_decomposition classes.."
                first_cols = [f"x_scores_{(i + 1)}" for i in range(trans_opt[0].shape[1])]
                second_cols = [f"y_scores_{(i + 1)}" for i in range(trans_opt[1].shape[1])]
                no_of_columns = trans_opt[0].shape[1] + trans_opt[1].shape[1]
                col_names = first_cols + second_cols

                trans_opt = numpy.concatenate(trans_opt, axis=1)
            else:
                assert isinstance(trans_opt, numpy.ndarray), "When transform/fit_transform is run "\
                    "without label columns for cross_decomposition classes, "\
                    "output should be a numpy array."
                no_of_columns = trans_opt.shape[1]
                col_names =[f"x_scores_{(i + 1)}" for i in range(trans_opt.shape[1])]
        else:
            # Generate list of new column names.
            col_names = [f"{self.class_name.lower()}_{func_name}_{(i + 1)}" for i in range(no_of_columns)]

        # Get new column sqlalchemy types for pandas df columns of transform output.
        opt_pd = pd.DataFrame(trans_opt)

        # Get output column types for each column in pandas df from the output of transform
        # type functions.
        types = {}
        for idx, col in enumerate(list(opt_pd.columns)):
            # Get type of column using data from all rows, in case if the column has None values.
            # 'and' of types of all values in the column with type(None) gives the type of the column.
            type_ = type(None)
            for i in range(len(trans_opt)):
                type_ = type_ and type(trans_opt[i][idx])
            
            # If all the values of the output (trans_opt) is None, thelen use `str` as type since
            # pandas astype() does not accept None type.
            if type_ is type(None):
                type_ = str

            # numpy integer columns with nan values can't be typecasted using pd.astype() to int64.
            # It raises error like "Cannot convert non-finite values (NA or inf) to integer: 
            #                       Error while type casting for column '2'"
            # Hence, using pd.Int64Dtype() for integer columns with nan values.
            types[col] = type_ if type_ not in [int, numpy.int64] else pd.Int64Dtype()

        # Without this, all columns will be of object type and gets converted to VARCHAR in Vantage.
        opt_pd = opt_pd.astype(types)

        # If the datatype is not specified then check if the datatype is datetime64 and timezone is present then map it to
        # TIMESTAMP(timezone=True) else map it according to default value.
        col_types = [TIMESTAMP(timezone=True)
                     if pt.is_datetime64_ns_dtype(opt_pd.dtypes[key]) and (opt_pd[col_name].dt.tz is not None)
                     else _get_sqlalchemy_mapping(str(opt_pd.dtypes[key]))
                     for key, col_name in enumerate(list(opt_pd.columns))]

        return [(c_name, c_type) for c_name, c_type in zip(col_names, col_types)]

    @_validate_fit_run
    def _run_function_needing_all_rows(self, X=None, y=None, file_name="sklearn_score.py", **kwargs):
        """
        Internal function to run functions like score, aic, bic which needs all rows and return
        one floating number as result.
        """
        st_time = time.time()

        assert kwargs["name"], "function name should be passed."
        func_name = kwargs["name"]

        # Remove 'name' to pass other kwargs to script. TODO: Not passing it now.
        kwargs.pop("name")

        data, feature_columns, label_columns, _, partition_columns = \
            self._validate_args_and_get_data(X=X, y=y, groups=None, kwargs=kwargs)

        label_columns = self._get_columns_as_list(label_columns)

        data, new_partition_columns = self._get_data_and_data_partition_columns(data,
                                                                                feature_columns,
                                                                                label_columns,
                                                                                partition_columns)

        script_file_path = f"{file_name}" if self._is_lake_system \
            else f"./{self._db_name}/{file_name}"

        data_column_types_str, partition_indices_str, _, new_partition_columns = \
            self._get_data_col_types_and_partition_col_indices_and_types(data, new_partition_columns)

        self._validate_unique_partition_values(data, new_partition_columns)

        py_exc = UtilFuncs._get_python_execution_path()
        script_command = f"{py_exc} {script_file_path} {func_name} {len(feature_columns)} "\
            f"{len(label_columns)} {partition_indices_str} {data_column_types_str} "\
            f"{self._model_file_name_prefix} {self._is_lake_system}"

        # score, aic, bic returns float values.
        return_types = [(col, data._td_column_names_and_sqlalchemy_types[col.lower()])
                        for col in new_partition_columns] + [(func_name, FLOAT())]

        # Checking the trained model installation. If not installed,
        # install it and set flag to True.
        if not self._is_trained_model_installed:
            self._install_initial_model_file()
            self._is_trained_model_installed = True

        opt = self._run_script(data, script_command, new_partition_columns, return_types)

        self._score_execution_time = time.time() - st_time

        if self._is_default_partition_value_fit:
            # For single model case, partition column is internally generated and
            # no point in returning it to the user.
            return opt.select(func_name)

        return opt

    @_validate_fit_run
    def _transform(self, X=None, y=None, file_name="sklearn_transform.py", **kwargs):
        """
        Internal function to run predict/transform and similar functions, which returns
        multiple columns. This function will return data row along with the generated
        columns' row data, unlike sklearn's functions which returns just output data.
        """
        st_time = time.time()

        assert kwargs["name"], "function name should be passed."
        func_name = kwargs["name"]

        # Remove 'name' to pass other kwargs to script. TODO: Not passing it now.
        kwargs.pop("name")

        data, feature_columns, label_columns, _, partition_columns = \
            self._validate_args_and_get_data(X=X, y=y, groups=None, kwargs=kwargs)

        data, new_partition_columns = self._get_data_and_data_partition_columns(data,
                                                                                feature_columns,
                                                                                label_columns,
                                                                                partition_columns)

        # Since kwargs are passed to transform, removing additional unrelated arguments from kwargs.
        self._remove_data_related_args_from_kwargs(kwargs)

        script_file_path = f"{file_name}" if self._is_lake_system \
            else f"./{self._db_name}/{file_name}"

        data_column_types_str, partition_indices_str, _, new_partition_columns = \
            self._get_data_col_types_and_partition_col_indices_and_types(data, new_partition_columns)

        self._validate_unique_partition_values(data, new_partition_columns)

        return_columns_python_types = None
        if self._fit_label_columns_python_types:
            return_columns_python_types = '--'.join(self._fit_label_columns_python_types)

        # Returning feature columns also along with transformed columns because we don't know the
        # mapping of feature columns to the transformed columns.
        ## 'correct_covariance()' returns the (n_features, n_features)
        if func_name == "correct_covariance":
            return_types = [(col, data._td_column_names_and_sqlalchemy_types[col.lower()])
                            for col in new_partition_columns]
        else:
            return_types = [(col, data._td_column_names_and_sqlalchemy_types[col.lower()])
                            for col in (new_partition_columns + feature_columns)]
        if func_name in ["predict", "decision_function"] and label_columns:
            return_types += [(col, data._td_column_names_and_sqlalchemy_types[col.lower()])
                             for col in label_columns]

        output_cols_types = self._get_return_columns_for_function_(data,
                                                                   feature_columns,
                                                                   label_columns,
                                                                   new_partition_columns,
                                                                   func_name,
                                                                   kwargs)
        return_types += output_cols_types

        py_exc = UtilFuncs._get_python_execution_path()
        script_command = f"{py_exc} {script_file_path} {func_name} {len(feature_columns)} "\
            f"{len(label_columns)} {partition_indices_str} {data_column_types_str} "\
            f"{self._model_file_name_prefix} {len(output_cols_types)} {self._is_lake_system} " \
            f"{return_columns_python_types}"

        # Checking the trained model installation. If not installed,
        # install it and set flag to True.
        if not self._is_trained_model_installed:
            self._install_initial_model_file()
            self._is_trained_model_installed = True

        opt = self._run_script(data, script_command, new_partition_columns, return_types)

        self._transform_execution_time = time.time() - st_time

        return self._get_returning_df(opt, new_partition_columns, return_types)

    def fit_predict(self, X=None, y=None, **kwargs):
        """
        Please check the description in Docs/OpensourceML/sklearn.py.
        """
        st_time = time.time()

        self._is_default_partition_value_fit = True # False when the user provides partition columns.

        data, feature_columns, label_columns, _, partition_columns = \
            self._validate_args_and_get_data(X=X, y=y, groups=None, kwargs=kwargs)

        if partition_columns:
            self._is_default_partition_value_fit = False

        data, new_partition_columns = self._get_data_and_data_partition_columns(data,
                                                                                feature_columns,
                                                                                label_columns,
                                                                                partition_columns)

        # Return label_columns also if user provides in the function call.
        return_types = [(col, data._td_column_names_and_sqlalchemy_types[col.lower()])
                        for col in (new_partition_columns + feature_columns + label_columns)]

        func_name = inspect.stack()[0][3]
        if label_columns:
            return_types += self._get_return_columns_for_function_(data,
                                                                   feature_columns,
                                                                   label_columns,
                                                                   new_partition_columns,
                                                                   func_name,
                                                                   {})
        else:
            # If there are no label_columns, we will have only one
            # predicted column.
            return_types += [(f"{self.class_name.lower()}_{func_name}_1", FLOAT())]

        file_name = "sklearn_fit_predict.py"

        data_column_types_str, partition_indices_str, _, new_partition_columns = \
            self._get_data_col_types_and_partition_col_indices_and_types(data, new_partition_columns)

        script_file_name = f"{file_name}" if self._is_lake_system \
            else f"./{self._db_name}/{file_name}"
        py_exc = UtilFuncs._get_python_execution_path()
        script_command = f"{py_exc} {script_file_name} {len(feature_columns)} "\
            f"{len(label_columns)} {partition_indices_str} {data_column_types_str} "\
            f"{self._model_file_name_prefix} {self._is_lake_system}"

        # Get unique values in partitioning columns.
        self._fit_partition_unique_values = data.drop_duplicate(new_partition_columns).get_values()

        # Checking the trained model installation. If not installed,
        # install it and flag to True.
        if not self._is_trained_model_installed:
            self._install_initial_model_file()
            self._is_trained_model_installed = True

        opt = self._run_script(data, script_command, new_partition_columns, return_types)

        self._fit_predict_execution_time = time.time() - st_time

        if self._is_default_partition_value_fit:
            # For single model case, partition column is internally generated and no point in
            # returning it to the user.

            # Extract columns from return types.
            returning_cols = [col[0] for col in return_types[len(new_partition_columns):]]
            return opt.select(returning_cols)

        return opt

    def fit_transform(self, X=None, y=None, **kwargs):
        """
        Please check the description in Docs/OpensourceML/sklearn.py.
        """
        # 'y' is not needed for transform().
        fit_obj = self.fit(X, y, **kwargs)
        kwargs["label_columns"] = None
        return fit_obj.transform(X, None, **kwargs)

    @_validate_fit_run
    def _run_neighbors(self, X=None, **kwargs):
        """
        Internal function to run functions like kneighbors, radius_neighbors, kneighbors_graph,
        radius_neighbors_graph which returns multiple columns. This function will return data row
        along with the generated columns' row data, unlike sklearn's functions which returns just
        output data.
        """
        assert kwargs["name"], "function name should be passed."
        func_name = kwargs["name"]
        kwargs.pop("name")

        if self.module_name != "sklearn.neighbors":
            raise AttributeError(f"{self.module_name+'.'+self.class_name} does not have {func_name}() method.")

        data = kwargs.get("data", None)
        partition_columns = kwargs.get("partition_columns", None)

        if not X and not partition_columns and not data:
            # If data is not passed, then run from client only.
            # TODO: decide whether to run from client or from Vantage.
            opt = super().__getattr__(func_name)(**kwargs)
            from scipy.sparse.csr import csr_matrix
            if isinstance(opt, csr_matrix):
                return opt.toarray()
            return opt

        self._is_default_partition_value_fit = True # False when the user provides partition columns.

        data, feature_columns, _, _, new_partition_columns = \
            self._validate_args_and_get_data(X=X, y=None, groups=None, kwargs=kwargs,
                                             skip_either_or_that=True)

        # Remove the kwargs data.
        self._remove_data_related_args_from_kwargs(kwargs)

        if partition_columns:
            # kwargs are passed to kneighbors function. So, removing them from kwargs.
            self._is_default_partition_value_fit = False

        # Generating new partition column name.
        data, new_partition_columns = self._get_data_and_data_partition_columns(data,
                                                                                feature_columns,
                                                                                [],
                                                                                partition_columns)

        args_str = self._get_kwargs_str(kwargs)

        file_name = "sklearn_neighbors.py"

        script_file_path = f"{file_name}" if self._is_lake_system \
            else f"./{self._db_name}/{file_name}"

        # Returning feature columns also along with new columns.
        return_types = [(col, data._td_column_names_and_sqlalchemy_types[col.lower()])
                        for col in (new_partition_columns + feature_columns)]

        # `return_distance` is needed as the result is a tuple of two arrays when it is True.
        return_distance = kwargs.get("return_distance", True) # Default value is True.

        # Though new columns return numpy arrays, we are returning them as strings.
        # TODO: Will update to columns later, if requested later.
        if func_name in ['kneighbors', 'radius_neighbors']:
            if return_distance:
                return_types += [("neigh_dist", VARCHAR())]
            return_types += [("neigh_ind", VARCHAR())]
        elif func_name in ['kneighbors_graph', 'radius_neighbors_graph']:
            return_types += [("A", VARCHAR())]
        else:
            return_types += [("output", VARCHAR())]

        data_column_types_str, partition_indices_str, _, new_partition_columns = \
            self._get_data_col_types_and_partition_col_indices_and_types(data, new_partition_columns)

        py_exc = UtilFuncs._get_python_execution_path()
        script_command = f"{py_exc} {script_file_path} {func_name} {len(feature_columns)} "\
            f"{partition_indices_str} {data_column_types_str} {self._model_file_name_prefix} {self._is_lake_system} "\
            f"{args_str}"

        # Get unique values in partitioning columns.
        self._fit_partition_unique_values = data.drop_duplicate(new_partition_columns).get_values()

        # Checking the trained model installation. If not installed,
        # install it and set flag to True.
        if not self._is_trained_model_installed:
            self._install_initial_model_file()
            self._is_trained_model_installed = True

        opt = self._run_script(data, script_command, new_partition_columns, return_types)

        return self._get_returning_df(opt, new_partition_columns, return_types)

    def split(self, X=None, y=None, groups=None, **kwargs):
        """
        Please check the description in Docs/OpensourceML/sklearn.py.
        """
        opt = self._run_model_selection("split", X=X, y=y, groups=groups,
                                        skip_either_or_that=True, kwargs=kwargs)

        # Get number of splits in the result DataFrame.
        n_splits = opt.drop_duplicate("split_id").shape[0]

        data = kwargs.get("data", None)
        feature_columns = kwargs.get("feature_columns", [])
        label_columns = self._get_columns_as_list(kwargs.get("label_columns", []))

        # If there is not X and y, get feature_columns and label_columns for "data".
        partition_columns = kwargs.get("partition_columns", [])
        feature_columns = [col for col in X.columns if col not in partition_columns] \
            if X and not data and not feature_columns else feature_columns
        label_columns = y.columns if y and not data and not label_columns else label_columns

        # Return iterator of the train and test dataframes for each split.
        for i in range(1, n_splits+1):
            train_df = opt[(opt.split_id == i) & (opt.data_type == "train")]\
                .select(partition_columns + feature_columns + label_columns)
            train_df._index_label = None
            test_df = opt[(opt.split_id == i) & (opt.data_type == "test")]\
                .select(partition_columns + feature_columns + label_columns)
            test_df._index_label = None

            yield train_df, test_df

    def get_n_splits(self, X=None, y=None, groups=None, **kwargs):
        """
        Please check the description in Docs/OpensourceML/sklearn.py.
        """
        return self._run_model_selection("get_n_splits", X=X, y=y, groups=groups,
                                         skip_either_or_that=True, kwargs=kwargs)

    def _run_model_selection(self,
                             func_name,
                             X=None,
                             y=None,
                             groups=None,
                             skip_either_or_that=False,
                             kwargs={}):
        """
        Internal function to run functions like split, get_n_splits of model selection module.
        - get_n_splits() returns number of splits as value, not as teradataml DataFrame.
        - split() returns teradataml DataFrame containing train and test data for each split
          (add partition information if the argument "partition_cols" is provided).
        """
        if self.module_name != "sklearn.model_selection":
            raise AttributeError(f"{self.module_name+'.'+self.class_name} does not "
                                 f"have {func_name}() method.")

        data = kwargs.get("data", None)

        if not X and not y and not groups and not data:
            # If data is not passed, then run from client only.
            # TODO: decide whether to run from client or from Vantage.
            return super().__getattr__(func_name)()

        self._is_default_partition_value_fit = True # False when the user provides partition columns.

        data, feature_columns, label_columns, group_columns, partition_columns = \
            self._validate_args_and_get_data(X=X, y=y, groups=groups, kwargs=kwargs,
                                             skip_either_or_that=skip_either_or_that)

        if partition_columns:
            self._is_default_partition_value_fit = False

        data, new_partition_columns = self._get_data_and_data_partition_columns(data,
                                                                                feature_columns,
                                                                                label_columns,
                                                                                partition_columns,
                                                                                group_columns)

        file_name = "sklearn_model_selection_split.py"

        script_file_path = f"{file_name}" if self._is_lake_system \
            else f"./{self._db_name}/{file_name}"

        if func_name == "split":
            # Need to generate data into splits of train and test.
            #   split_id - the column which will be used to identify the split.
            #   data_type - the column which will be used to identify whether the row is
            #               train or test row.
            return_types = [("split_id", INTEGER()), ("data_type", VARCHAR())]
            # Returning feature columns and label columns as well.
            return_types += [(col, data._td_column_names_and_sqlalchemy_types[col.lower()])
                            for col in (feature_columns + label_columns)]
        else:
            # Return Varchar by default.
            # Returns Varchar even for functions like `get_n_splits` which returns large integer
            # numbers like `4998813702034726525205100` for `LeavePOut` class (when the argument
            # `p` is 28 and no of data rows is 100) as Vantage cannot scope it to INTEGER.
            return_types = [(func_name, VARCHAR())]

        return_types = [(col, data._td_column_names_and_sqlalchemy_types[col.lower()])
                        for col in new_partition_columns] + return_types

        data_column_types_str, partition_indices_str, _, new_partition_columns = \
            self._get_data_col_types_and_partition_col_indices_and_types(data, new_partition_columns)

        py_exc = UtilFuncs._get_python_execution_path()
        script_command = f"{py_exc} {script_file_path} {func_name} {len(feature_columns)} "\
            f"{len(label_columns)} {len(group_columns)} {partition_indices_str} {data_column_types_str} "\
            f"{self._model_file_name_prefix} {self._is_lake_system}"

        # Get unique values in partitioning columns.
        self._fit_partition_unique_values = data.drop_duplicate(new_partition_columns).get_values()

        # Checking the trained model installation. If not installed,
        # install it and set flag to True.
        if not self._is_trained_model_installed:
            self._install_initial_model_file()
            self._is_trained_model_installed = True

        opt = self._run_script(data, script_command, new_partition_columns, return_types)

        if func_name == "get_n_splits" and not partition_columns:
                # Return number of splits as value, not as dataframe.
                vals = execute_sql("select {} from {}".format(func_name, opt._table_name))
                opt = vals.fetchall()[0][0]

                # Varchar is returned by the script. Convert it to int.
                return int(opt)

        return opt


class _FunctionWrapper(_GenericObjectWrapper):
    def __init__(self, module_name, func_name, file_type, template_file):
        super().__init__()
        self._module_name = module_name
        self._func_name = func_name
        self._params = None
        self._data_args = OrderedDict()
        self._template_file = template_file
        self._script_file_name = _generate_new_name(type=file_type, extension="py")

    def __call__(self, **kwargs):
        """
        Run the function with all the arguments passed from `td_sklearn.<function_name>` function.
        """
        replace_dict, partition_cols = self._process_data_for_funcs_returning_objects(kwargs)

        script_file_path = f"{self._script_file_name}" if self._is_lake_system \
            else f"./{self._db_name}/{self._script_file_name}"

        model_file_prefix = None
        if self._is_lake_system:
            model_file_prefix = self._script_file_name.replace(".py", "")

        py_exc = UtilFuncs._get_python_execution_path()
        script_command = f"{py_exc} {script_file_path} {model_file_prefix} {self._is_lake_system}"

        model_type = BLOB() if self._is_lake_system else CLOB()

        return_types = [(col, self._tdml_df._td_column_names_and_sqlalchemy_types[col.lower()]) 
                        for col in partition_cols] + [(self._func_name, model_type)]

        replace_dict.update({"<module_name>": self._module_name,
                             "<func_name>": self._func_name,
                             "<params>": json.dumps(kwargs)})

        # Generate new file in .teradataml directory and install it to Vantage.
        self._prepare_and_install_file(replace_dict=replace_dict)

        try:
            self._model_data = self._run_script(self._tdml_df, script_command, partition_cols, return_types)
            self._model_data._index_label = None

            fit_partition_unique_values = self._tdml_df.drop_duplicate(partition_cols).get_values()

            self._extract_model_objs(n_unique_partitions=len(fit_partition_unique_values),
                                     n_partition_cols=len(partition_cols))

        except Exception as ex:
            # File cleanup if script execution fails or unable to fetch modelObj.
            os.remove(self._script_file_local)
            self._remove_script_file(self._script_file_name)
            raise

        # File cleanup after processing.
        os.remove(self._script_file_local)
        self._remove_script_file(self._script_file_name)

        return self.modelObj


class _SKLearnFunctionWrapper(_FunctionWrapper):
    def __init__(self, module_name, func_name):
        file_type = "file_fn_sklearn"
        template_file = "sklearn_function.template"
        super().__init__(module_name, func_name, file_type=file_type, template_file=template_file)
