from teradataml.common.deprecations import argument_deprecation
from teradataml.common.exceptions import TeradataMlException
from teradataml.common.messagecodes import MessageCodes
from teradataml.common.messages import Messages
from teradataml.options.configure import configure
from teradataml.utils.internal_buffer import _InternalBuffer
from teradataml.telemetry_utils.queryband import collect_queryband


@collect_queryband(queryband="StCnfgPrms")
def set_config_params(**kwargs):
    """
    DESCRIPTION:
        Function to set the configurations in Vantage. Alternatively, user can set the
        configuration parameters independently using 'teradataml.configure' module.

    PARAMETERS:
        kwargs:
            Optional Argument.
            Specifies keyword arguments. Accepts following keyword arguments:

            certificate_file:
                Optional Parameter.
                Specifies the path of the certificate file, which is used in
                encrypted REST service calls.
                Types: str

            default_varchar_size:
                Optional Parameter.
                Specifies the size of varchar datatype in Vantage, the default
                size is 1024.
                Types: int

            vantage_version:
                Specifies the Vantage version teradataml is connected to.
                Types: str

            val_install_location:
                Specifies the database name where Vantage Analytic Library functions
                are installed.
                Types: str

            byom_install_location:
                Specifies the database name where Bring Your Own Model functions
                are installed.
                Types: str

            database_version:
                Specifies the database version of the system teradataml is connected to.
                Types: str

            read_nos_function_mapping:
                Specifies the mapping function name for the read_nos table operator function.
                Types: str

            write_nos_function_mapping:
                Specifies the mapping function name for the write_nos table operator function.
                Types: str

            indb_install_location:
                Specifies the installation location of In-DB Python package.
                Types: str
                Default Value: "/var/opt/teradata/languages/sles12sp3/Python/"
                Note:
                    The default value is the installation location of In-DB 2.0.0 packages.
                    Older versions of In-DB packages are installed at
                    "/opt/teradata/languages/Python/".

            local_storage:
                Specifies the location on client where garbage collector folder will be created.
                Types: str

    RETURNS:
        bool

    RAISES:
        None

    EXAMPLES:
        # Example 1: Set configuration params using set_config_params() function.
        >>> from teradataml import set_config_params
        >>> set_config_params(certificate_file="cert.crt",
        ...                   default_varchar_size=512,
        ...                   val_install_location="VAL_USER",
        ...                   read_nos_function_mapping="read_nos_fm",
        ...                   write_nos_function_mapping="write_nos_fm",
        ...                   indb_install_location="/opt/teradata/languages/Python",
        ...                   local_storage="/Users/gc")
        True

        # Example 2: Alternatively, set configuration parameters without using set_config_params() function.
        #            To do so, we will use configure module.
        >>> from teradataml import configure
        >>> configure.certificate_file="cert.crt"
        >>> configure.default_varchar_size=512
        >>> configure.val_install_location="VAL_USER"
        >>> configure.read_nos_function_mapping="read_nos_fm"
        >>> configure.write_nos_function_mapping="write_nos_fm"
        >>> configure.indb_install_location="/opt/teradata/languages/Python"
        >>> configure.local_storage = "/Users/gc/"
    """
    for option in kwargs:
        try:
            if option == "auth_token" or option == 'ues_url':
                raise TeradataMlException(Messages.get_message(
                    MessageCodes.FUNC_EXECUTION_FAILED, 'set_config_params',
                    'Setting of parameter \'{}\' is prohibited from set_config_params(). '
                    'Use set_auth_token() to set parameter.'.format(option)),
                    MessageCodes.FUNC_EXECUTION_FAILED)
            else:
                setattr(configure, option, kwargs[option])
        except AttributeError as e:
            raise TeradataMlException(Messages.get_message(
                MessageCodes.FUNC_EXECUTION_FAILED, 'set_config_params', 'Invalid parameter \'{}\'.'.format(option)),
                                      MessageCodes.FUNC_EXECUTION_FAILED)
    return True
