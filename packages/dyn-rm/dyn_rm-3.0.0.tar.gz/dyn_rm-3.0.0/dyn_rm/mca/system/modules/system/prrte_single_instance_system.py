from dyn_rm.mca.base.logger.component import MCALoggerComponent
from dyn_rm.mca.base.system.module.logging import *
from dyn_rm.mca.base.system.module import MCASystemModule
from dyn_rm.mca.base.callback.component import MCACallbackComponent
from dyn_rm.mca.callback.modules.pmix import PmixCallbackModule
from dyn_rm.mca.base.event_loop.component import MCAEventLoopComponent
from dyn_rm.mca.base.event_loop.module import MCAEventLoopModule
from dyn_rm.mca.base.system.component import MCAProcessManagerComponent
from dyn_rm.mca.base.system.module import *
from dyn_rm.mca.system.modules.psets.psetop_models import *
from dyn_rm.mca.system.modules.psets.pset_models import *
from dyn_rm.mca.system.modules.process_manager.prrte_process_manager_module import PrrteProcessManagerModule
from dyn_rm.util.constants import *
from dyn_rm.util.functions import v_print
from pmix import *
import os
import time
from functools import partial


### TODO: This class does not yet implement the system module interface ###

class PrrteSingleInstanceSystem(MCASystemModule):

    def __init__(self, parent = None, parent_dir = ".", verbosity = 0, enable_output = False):
        super().__init__(parent = parent, parent_dir = parent_dir, verbosity = verbosity, enable_output = enable_output)

    
    # Just use the default callbacks of the MCASystemModule
    def register_callbacks_func(self, conn_name):
        return super().register_callbacks_func(conn_name)

    # Creates global Prrte DVM and connects to it as PMIx Tool
    def set_topology_graph_epilog(self, topo_graph, params):

        # Add a Global Prrte PM Module 
        rc = self.run_component_service(MCAProcessManagerComponent, "ADD", "PM", "GLOBAL_PM", PrrteProcessManagerModule(verbosity = self.verbosity))
        if rc != DYNRM_MCA_SUCCESS:
            return rc
        
        # Launch Global Prrte instance
        rc = self.run_component_service(MCAProcessManagerComponent, "LAUNCH", "PM", "GLOBAL_PM", topo_graph, {})
        if rc != DYNRM_MCA_SUCCESS:
            # Remove module if launch fails
            self.run_component_service(MCAProcessManagerComponent, "REMOVE", "PM", "GLOBAL_PM")
            return rc
        
        # Get the connection info
        conn_info = self.run_component_service(MCAProcessManagerComponent, "GET", "INFO", "GLOBAL_PM", [DYNRM_PARAM_CONN_INFO])
        if None == conn_info or 0 == len(conn_info):
            return DYNRM_MCA_ERR_CONNECTION
        
        # Try to establish a connection
        for info in conn_info[DYNRM_PARAM_CONN_INFO]:
            module = info[DYNRM_PARAM_CONN_MODULE]
            params = info[DYNRM_PARAM_CONN_PARAMS]
            params[DYNRM_PARAM_CONN_SCHEDULER] = True

            rc = self.run_component_service(MCACallbackComponent, "REQUEST", "CONNECTION", module, "GLOBAL_PM", self, None, params)
            if rc == DYNRM_MCA_SUCCESS:
                break
            else:
                return rc
        
        rc = self.register_callbacks_func("GLOBAL_PM")
                
        return rc


    def apply_psetops_epilog(self, psetops):

        if 0 == len(psetops):
            return DYNRM_MCA_SUCCESS
        
        for psetop in psetops:
            if "GLOBAL_PM" not in self.run_component_service(MCACallbackComponent, "GET", "CONNECTION_NAMES"):
                return DYNRM_MCA_ERR_NOT_FOUND
            
            # Send the command to the global PRRTE instance
            rc = self.run_component_service(MCACallbackComponent, "SEND", "EVENT", "GLOBAL_PM", DYNRM_CMD_PSETOP_APPLY, psetop)
            if rc != DYNRM_MCA_SUCCESS:
                return rc
            
        return DYNRM_MCA_SUCCESS