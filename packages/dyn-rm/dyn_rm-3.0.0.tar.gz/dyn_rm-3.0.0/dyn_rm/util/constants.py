# DYNRM ERRORS
DYNRM_SUCCESS = 0
DYNRM_ERR_NOT_FOUND = 1
DYNRM_ERR_BAD_PARAM = 2
DYNRM_ERR_NO_PERM = 3
DYNRM_ERR_EXISTS = 4
DYNRM_ERR_NOT_IMPLEMENTED = 5

DYNRM_ERR_MCA = 1000
# MCA ERRORS
DYNRM_MCA_SUCCESS = DYNRM_SUCCESS
DYNRM_MCA_ERR_NOT_FOUND = DYNRM_ERR_NOT_FOUND
DYNRM_MCA_ERR_BAD_PARAM = DYNRM_ERR_BAD_PARAM
DYNRM_MCA_ERR_NO_PERM = DYNRM_ERR_NO_PERM
DYNRM_MCA_ERR_EXISTS = DYNRM_ERR_EXISTS
DYNRM_MCA_ERR_NOT_IMPLEMENTED = DYNRM_ERR_NOT_IMPLEMENTED

DYNRM_MCA_ERR_CONNECTION = DYNRM_ERR_MCA + 1

# DYNRM EVENTS
DYNRM_EVENT_PSETOP_DEFINED      =       "dyn_rm.system_event.psetop_defined"
DYNRM_EVENT_PSETOP_CANCELED     =       "dyn_rm.system_event.psetop_canceled"
DYNRM_EVENT_PSETOP_FINALIZED    =       "dyn_rm.system_event.psetop_finalized"

DYNRM_EVENT_TASK_TERMINATED     =       "dyn_rm.system_event.task_terminated"

# DYNRM COMMANDS    
DYNRM_CMD_PSETOP_APPLY          =       "dyn_rm.cmd.psetop.apply"
DYNRM_CMD_PM_LAUNCH             =       "dyn_rm.cmd.pm.launch"
DYNRM_CMD_PM_EXPAND             =       "dyn_rm.cmd.pm.expand"
DYNRM_CMD_CONN_REQ              =       "dyn_rm.cmd.connection.request"

# DYNRM PARAMETERS
DYNRM_PARAM_PM_MODULE           =       "dyn_rm.param.pm.module"
DYNRM_PARAM_PM_MODULE_DEFAULT   =       "dyn_rm.param.pm.module.default"
DYNRM_PARAM_PM_PARAMS           =       "dyn_rm.param.pm.params"
DYNRM_PARAM_PM_PARAMS_DEFAULT   =       "dyn_rm.param.pm.params.default"
DYNRM_PARAM_PM_TOPOLOGY         =       "dyn_rm.param.pm.topology"
DYNRM_PARAM_PM_NAME             =       "dyn_rm.param.pm.name"

DYNRM_PARAM_CONN_INFO           =       "dyn_rm.param.connection.params"        # List of dicts with conn_module and conn_params 
DYNRM_PARAM_CONN_MODULE         =       "dyn_rm.param.connection.module"
DYNRM_PARAM_CONN_PARAMS         =       "dyn_rm.param.connection.params"
DYNRM_PARAM_CONN_PID            =       "dyn_rm.param.connection.pid"
DYNRM_PARAM_CONN_TCP            =       "dyn_rm.param.connection.tcp"
DYNRM_PARAM_CONN_NAME           =       "dyn_rm.param.connection.name"
DYNRM_PARAM_CONN_SCHEDULER      =       "dyn_rm.param.connection.scheduler"

DYNRM_PARAM_PSETOP_APPLY_PARAMS =       "dyn_rm.param.connection.tcp"
DYNRM_PARAM_PSETOP_APPLY_CONN   =       "dyn_rm.param.connection.tcp"

# DYNRM PSET OPERATIONS
DYNRM_PSETOP_NULL               =       0        # Invalid pset operation
DYNRM_PSETOP_ADD                =       1        # Resources are added
DYNRM_PSETOP_SUB                =       2        # Resources are removed
DYNRM_PSETOP_GROW               =       3        # ADD + UNION
DYNRM_PSETOP_SHRINK             =       4        # SUB + DIFFERENCE
DYNRM_PSETOP_REPLACE            =       5        # Resources are replaced
DYNRM_PSETOP_UNION              =       6        # The union of two psets is requested
DYNRM_PSETOP_DIFFERENCE         =       7        # The difference of two psets is requested
DYNRM_PSETOP_INTERSECTION       =       8        # The intersection of two psets is requested
DYNRM_PSETOP_MULTI              =       9        # Multiple operations specified in the info object
DYNRM_PSETOP_SPLIT              =       10       # Splt operation
DYNRM_PSETOP_CANCEL             =       11       # Cancel PSet Operations