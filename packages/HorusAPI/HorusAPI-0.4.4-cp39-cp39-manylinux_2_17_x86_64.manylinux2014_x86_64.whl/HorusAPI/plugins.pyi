import typing
from .utils import ResetRemoteException as ResetRemoteException
from Server.FlowManager import Flow
from _typeshed import Incomplete
from enum import Enum
from pydantic import BaseModel
from typing import Any, List

class UniqueVariableIDException(Exception):
    """
    Exception that is raised when a variable ID is not unique inside a block.
    """
    variableId: Incomplete
    def __init__(self, message: str, variableId: str = 'Unknown') -> None: ...

class PluginRemote:
    """
    Remote interface for blocks
    """
    def __init__(self, remote) -> None: ...
    def remoteCommand(self, command: str):
        """
        Executes a command on the remote.
        The output of the command will be returned.

        :param command: The command to execute.
        """
    def sendData(self, source: str, destination: str) -> str:
        """
        Sends a file to the remote.
        :param file: The path to the file to send.

        :return: The final absolute path to the uploaded file.
        """
    def getData(self, source: str, destination: str) -> str:
        """
        Gets a file from the remote.
        :param file: The path to the file to get.

        :return: The final absolute path to the downloaded file.
        """
    def submitJob(self, script: str, changeDir: bool = True) -> int:
        """
        Submit a slurm job to the queue system of the cluster (SLURM)

        :param script: The  absolute path to the script to submit.
        :param: changeDir: automatically cd to the container folder of the script.         Disable this if using the cd context manager or for specific cases.

        :return: The job ID.
        """
    def cd(self, path: str):
        """
        Context manager to change directory on the remote.

        Works with the remoteCommand, submitJob and send/get data functions.
        """
    @property
    def userHome(self) -> str:
        """
        Returns the expanded user home directory.
        """
    @property
    def workDir(self) -> str:
        """
        Returns the Horus directory on the remote.
        If on local, returns the flow directory.
        """
    @property
    def name(self) -> str:
        """
        Returns the name of the remote.
        """
    @property
    def host(self) -> str:
        """
        Returns the host adress of the remote.
        """
    @property
    def isLocal(self) -> bool:
        """
        Returns whether the remote is local or not
        """

class PluginEndpoint:
    """
    Endpoints for plugin pages.
    """
    url: Incomplete
    methods: Incomplete
    function: Incomplete
    def __init__(self, url: str, methods: typing.List[str], function: typing.Callable) -> None:
        """
        Create a new PluginEndpoint.

        :param url: The URL of the endpoint.
        :param method: The method of the endpoint.
        :param function: The function that will be called when the endpoint is accessed.
        """

class PluginPage:
    """
    Class that defines a page that can be accessed from the extension menu.
    """
    endpoints: typing.List[PluginEndpoint]
    id: Incomplete
    name: Incomplete
    description: Incomplete
    html: Incomplete
    hidden: Incomplete
    def __init__(self, id: str, name: str, description: str, html: str, hidden: bool = False) -> None:
        '''
        Create a new PluginPage.

        :param id: The ID of the page.
        :param name: The name of the page.
        :param description: A description of the page.
        :param html: The name of the HTML file (i.e. "my_page.html").         The html file must be located in the "Pages" folder of the plugin.
        :param hidden: Whether the page should be hidden from the extension menu (default: False).
        '''
    def addEndpoint(self, endpoint: PluginEndpoint):
        '''
        Add an endpoint to the page.

        Define endpoints that the plugin can access from the defined pages.         The endpoint URL should be defined as a string, for example: "/my_endpoint".         Later, Horus will add the endpoint in the following format:         "/plugins/pages/<pluginID>.<pageID>/my_endpoint".         Therefore, remember to perform any GET or POST request to that endpoint.         You can use \'window.location\' in JS to get the current URL.

        Note: pluginID and pageID are always lowercase.

        :param endpoint: The endpoint to add.
        '''

class VariableTypes(str, Enum):
    """
    The types of variables.
    """
    ANY: str
    STRING: str
    TEXT_AREA: str
    NUMBER: str
    INTEGER: str
    FLOAT: str
    BOOLEAN: str
    STRING_LIST: str
    NUMBER_LIST: str
    NUMBER_RANGE: str
    CONSTRAINED_NUMBER_RANGE: str
    FILE: str
    FOLDER: str
    MULTIPLE_STRUCTURE: str
    STRUCTURE: str
    HETERORES: str
    STDRES: str
    RESIDUE: str
    ATOM: str
    CHAIN: str
    BOX: str
    SPHERE: str
    SMILES: str
    LIST: str
    OBJECT: str
    CODE: str
    CUSTOM: str
    RADIO: str
    CHECKBOX: str
    @staticmethod
    def getTypes():
        """
        Returns a list of all the available types.
        """
    def __eq__(self, other): ...
    def __hash__(self): ...

class PluginVariable:
    """
    Class that defines a variable that can be used in a PluginBlock.
    """
    id: str
    name: Incomplete
    description: Incomplete
    type: Incomplete
    disabled: Incomplete
    required: Incomplete
    placeholder: Incomplete
    category: Incomplete
    defaultValue: Incomplete
    value: Incomplete
    allowedValues: Incomplete
    def __init__(self, id: str, name: str, description: str, type: typing.Union[VariableTypes, str], defaultValue: typing.Optional[typing.Any] = None, allowedValues: typing.Optional[typing.List[typing.Any]] = None, category: typing.Optional[str] = None, disabled: bool = False, required: bool = False, placeholder: typing.Optional[str] = None) -> None:
        """
        :param name: The name of the variable.
        :param description: A description of the variable.
        :param type: The type of the variable. Assign it using the VariableTypes class.
        :param defaultValue: The default value of the variable.
        :param id: The ID of the variable.
        :param allowedValues: A list of allowed values for the variable.
        :param disabled: Whether the variable is disabled or not
        :param required: Whether the variable is required or not.
        This will show the variable in orange when not connected.
        :param placeholder: The placeholder of the input field.
        """
    def toDict(self, minimal: bool = False):
        """
        Convert the variable to a dictionary.
        """

class CustomVariable(PluginVariable):
    """
    Custom varialbe which supports custom view
    """
    customPage: PluginPage
    def __init__(self, id: str, name: str, description: str, type: VariableTypes, customPage: PluginPage, defaultValue: Any | None = None, allowedValues: List[Any] | None = None, category: str | None = None, disabled: bool = False, required: bool = False) -> None:
        """
        The custom variable works like a regular variable, but it can use an extension         page to render a custom and complex configuration view to define the variable value.         The variableType attribute will work just as the regular variables counterpart.

        Inside the extension page, the variable value can be set using the following function:
        ```
        parent.horus.setVariableValue(variableID, value)
        ```
        Where variableID is the ID of the variable and value is the value to set.         The values must be JSON serializable.
        

        :param customPage: The page instance where the variable will be rendered.
        """
    def toDict(self, minimal: bool = False):
        """
        Converts the variable to a dictionary and adds the pageID.
        """

class VariableGroup(PluginVariable):
    """
    A group of varaibles to be used together as input.
    """
    variables: typing.List[PluginVariable]
    def __init__(self, id: str, name: str, description: str, variables: typing.List[PluginVariable], allowedValues: typing.Optional[typing.List[typing.Any]] = None, category: typing.Optional[str] = None, disabled: bool = False, required: bool = False) -> None:
        """
        Initialize a VariableGroup

        :param id: The ID of the variable group (must be unique).
        :param name: The name of the variable group.
        :param description: A description of the variable group.
        :param variables: The list of variables in the group.
        :param allowedValues: In this case, the allowed values will indicate in
        the GUI which groups can be connected (with the same allowedValues)
        :param disabled: This will set all the variables under the group as disabled
        """
    def toDict(self, minimal: bool = False):
        """
        Converts the variable group to a dictionary.
        """

class VariableList(PluginVariable):
    """
    A list of the designed input variables.
    """
    prototypes: Incomplete
    def __init__(self, id: str, name: str, description: str, prototypes: typing.List[PluginVariable], allowedValues: typing.Optional[typing.List[typing.Any]] = None, category: typing.Optional[str] = None, disabled: bool = False, required: bool = False) -> None:
        """
        :param id: The ID of the variable.
        :param name: The name of the variable.
        :param description: A description of the variable.
        :param prototypes: The list of variables in each row of the list.
        :param allowedValues: Matching allowedValues in other variables will         indicate in the GUI which variables can be connected.
        :param disabled: Will set all variables under the list as disabled.
        :param required: Will set all variables under the list as required.
        """
    def toDict(self, minimal: bool = False):
        """
        Converts the variable list to a dictionary.
        """

class PluginBlockTypes(str, Enum):
    """
    The different types of blocks.
    """
    BASE: str
    INPUT: str
    ACTION: str
    SLURM: str
    CONFIG: str
    GHOST: str

class BlockVarPair:
    """
    A connection of a block for a given variable of that block.
    """
    blockPlacedID: Incomplete
    blockID: Incomplete
    variableID: Incomplete
    variableType: Incomplete
    variableAllowedValues: Incomplete
    def __init__(self, blockPlacedID: int, blockID: str, variableID: str, variableType: typing.Optional[str] = None, variableAllowedValues: typing.Optional[typing.List[typing.Any]] = None) -> None: ...

class BlockConnection:
    """
    A connection between blocks and variables.
    """
    origin: Incomplete
    destination: Incomplete
    isCyclic: Incomplete
    cycles: Incomplete
    currentCycle: Incomplete
    def __init__(self, origin: BlockVarPair, destination: BlockVarPair, isCyclic: bool, cycles: int = 1, currentCycle: int = 0) -> None: ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...

class BlockNotFoundError(Exception):
    """
    Exception raised when a block is not found.
    """
    def __init__(self, blockID: str) -> None: ...

class PluginBlock:
    """
    The base block class for Horus blocks. Not to be used directly.
    """
    error: bool
    blockLogs: str
    selectedInputGroup: str
    selectedRemote: str
    time: float
    extraData: typing.Dict[str, typing.Any]
    flow: Flow
    pluginDir: str
    dirty: bool
    id: Incomplete
    name: Incomplete
    description: Incomplete
    action: Incomplete
    externalURL: Incomplete
    TYPE: Incomplete
    def __init__(self, name: str, description: str, action: typing.Optional[typing.Callable] = None, variables: typing.List[PluginVariable] = [], inputs: typing.List[PluginVariable] = [], inputGroups: typing.List[VariableGroup] = [], outputs: typing.List[PluginVariable] = [], blockType: PluginBlockTypes = ..., id: typing.Optional[str] = None, externalURL: typing.Optional[str] = None) -> None:
        """
        Initialize a PluginBlock.
        """
    def __call__(self, *args, **kwargs): ...
    def __eq__(self, other): ...
    @property
    def variables(self) -> dict:
        """
        The variables assigned to the block.

        :return: A dictionary with the variables of the block with key
        the variable ID and value the variable value.
        """
    @property
    def inputs(self) -> dict:
        """
        The inputs assigned to the block.

        :return: A dictionary with the inputs of the block with key
        the input ID and value the input value.
        """
    @property
    def outputs(self) -> dict:
        """
        The outputs assigned to the block.

        :return: A dictionary with the outputs of the block with key
        the output ID and value the output value.
        """
    def setOutput(self, id: str, value: typing.Any):
        """
        Sets the value of an output variable.

        :param id: The id of the output variable.
        :param value: The value to set.
        """
    remote: PluginRemote
    def copy(self):
        """
        Returns a deep copy of the block in order to not
        modify the original reference.
        """
    config: dict

class GhostBlock(PluginBlock):
    """
    A block used to represent missing or unavailable blocks in a flow.
    """
    error: bool
    blockLogs: str
    def __init__(self, id: str) -> None: ...
    def __call__(self, *args, **kwargs) -> None: ...

class PluginConfig(PluginBlock):
    '''
    The PluginConfig class is a special type of block that is used to configure
    the plugin. It is not meant to be used in the pipeline. It works as a regular
    PluginBlock but it is shown only in the configuration page of the plugin.
    Its variables will be stored once set, and can be accessed by the Block actions
    using the block.config["variable_id"] syntax.
    '''
    def __init__(self, name: str, description: str, action: typing.Optional[typing.Callable] = None, variables: typing.List[PluginVariable] = [], id: typing.Optional[str] = None) -> None:
        """
        :param name: The name of the block.
        :param description: The description of the block.
        :param action: The action of the block. Will be run when storing the config.
        :param variables: The variables of the block.
        """

class InputBlock(PluginBlock):
    """
    The InputBlock class is a special type of block that is used to get input from
    the user. It works as a regular PluginBlock but only shows its PluginVariable.
    Its output will be automatically set to the value the variable has if it does
    not have a defined action.

    When only the variable parameter is defined, the block will output directly the value
    of the variable.

    If parsing of the variable is needed, the action parameter can be used to define
    a function that will parse the value of the variable and return the parsed value. In that
    case, use the output parameter to define the output variable of the block.
    """
    def __init__(self, name, description, variable: PluginVariable, output: typing.Optional[PluginVariable] = None, action: typing.Optional[typing.Callable] = None, id: typing.Optional[str] = None, externalURL: typing.Optional[str] = None) -> None:
        """
        :param name: The name of the block.
        :param description: The description of the block.
        :param variable: The variable of the block.
        :param output: The output of the block.
        :param action: The action of the block. Will be run when storing the config.
        :param id: The id of the block.
        :param externalURL: The external URL of the block for documentation purposes.
        """
    def __call__(self, *args, **kwargs): ...

class SlurmBlock(PluginBlock):
    """
    The SlurmBlock class is a special type of block that is used to run an action
    in a remote server. It works as a regular PluginBlock but it has two actions,
    one before the job is submitted and one after the job is completed.
    """
    jobID: typing.Optional[int]
    class Status(Enum):
        """
        The status of the block.
        """
        BOOT_FAIL: str
        CANCELLED: str
        CANCELLING: str
        COMPLETED: str
        CONFIGURING: str
        COMPLETING: str
        DEADLINE: str
        FAILED: str
        NODE_FAIL: str
        OUT_OF_ME: str
        PENDING: str
        PREEMPTED: str
        RUNNING: str
        RESV_DEL_HOLD: str
        REQUEUE_FED: str
        REQUEUE_HOLD: str
        REQUEUED: str
        RESIZING: str
        REVOKED: str
        SIGNALING: str
        SPECIAL_EXIT: str
        STAGE_OUT: str
        STOPPED: str
        SUSPENDED: str
        TIMEOUT: str
        UNKNOWN: str
        IDLE: str
    status: Status
    stdOut: typing.Optional[str]
    stdErr: typing.Optional[str]
    detailedStatus: typing.Optional[str]
    failOnSlurmError: bool
    initalAction: Incomplete
    finalAction: Incomplete
    def __init__(self, name: str, description: str, initialAction: typing.Callable, finalAction: typing.Callable, variables: typing.List[PluginVariable] = [], inputs: typing.List[PluginVariable] = [], inputGroups: typing.List[VariableGroup] = [], outputs: typing.List[PluginVariable] = [], id: typing.Optional[str] = None, failOnSlurmError: bool = True, extenrnalURL: typing.Optional[str] = None) -> None:
        """
        :param name: The name of the block.
        :param description: The description of the block.
        :param initialAction: The action of the block before the job is submitted.
        :param finalAction: The action of the block after the job is completed.
        :param variables: The variables of the block.
        :param inputs: The inputs of the block.
        :param inputGroups: The input groups of the block.
        :param outputs: The outputs of the block.
        :param id: The id of the block.
        :param failOnSlurmError: Whether to fail the block if the slurm job fails.
        :param extenrnalURL: The external URL of the block for documentation purposes.
        """
    action: Incomplete
    def __call__(self, *args, **kwargs): ...
    def parseStatus(self):
        """
        The status of the block as a parsed string.
        """
    @property
    def isWaitingForJob(self):
        """
        Whether the block is waiting for the job to finish or not.
        """
    def waitTillJobFinished(self, interval: int = 10):
        """
        Waits until the job is finished.

        :param interval: The interval in seconds to check if the job is finished.
        """

PlatformType: Incomplete

class PluginMetaModel(BaseModel):
    """
    The metadata of a plugin
    """
    id: str
    name: str
    description: str
    author: str
    version: str
    pluginFile: str
    minHorusVersion: typing.Optional[str]
    maxHorusVersion: typing.Optional[str]
    platforms: typing.Optional[PlatformType]
    externalURL: typing.Optional[str]
    dependencies: typing.Optional[typing.List[str]]

class Plugin:
    """
    Base class for all plugins.
    """
    pluginMeta: PluginMetaModel
    logo: typing.Optional[str]
    default: bool
    id: str
    actions: Incomplete
    views: Incomplete
    def __init__(self, id: typing.Optional[str] = None, noMetaLoad: bool = False) -> None:
        """
        Initializes the plugin.

        :param id: The id of the plugin.
        """
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def loadPluginMeta(self) -> None:
        """
        Loads the information about the plugin from the plugin.meta file.

        - name: The name of the plugin
        - version: The version of the plugin
        - author: The author of the plugin
        - description: A description of the plugin
        - dependencies: A list of dependencies of the plugin
        """
    def getBlock(self, id):
        """
        Returns a block by its ID.

        :param id: The ID of the block.
        """
    def getBlocks(self):
        """
        Returns a list of all the blocks in the plugin.
        """
    @property
    def blocks(self):
        """
        Returns a list of all the blocks in the plugin.
        """
    def addBlock(self, block: PluginBlock):
        """
        Adds a PluginBlock to the plugin.
        """
    def getPage(self, id):
        """
        Returns a page by its ID.

        :param id: The ID of the page.
        """
    def getPages(self):
        """
        Returns a list of all the pages in the plugin.
        """
    @property
    def pages(self):
        """
        Returns a list of all the pages in the plugin.
        """
    def addPage(self, page: PluginPage):
        """
        Adds a PluginPage to the plugin.
        """
    @property
    def config(self) -> dict:
        """
        A dictionary with the configs of the block
        """
    def addConfig(self, config: PluginConfig):
        """
        Adds a PluginConfig to the plugin.
        """
