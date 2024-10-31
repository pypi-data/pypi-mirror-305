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
from dyn_rm.util.constants import *
from dyn_rm.util.functions import v_print
from pmix import *
import os
import time
from functools import partial


### TODO: This class does not yet implement the system module interface ###

class FlexibleSystem(MCASystemModule):

    def __init__(self, parent = None, parent_dir = ".", verbosity = 0, enable_output = False):
        super().__init__(parent = parent, parent_dir = parent_dir, verbosity = verbosity, enable_output = enable_output)

    
    # We register the same callbacks for all connections
    def register_callbacks_func(self, conn_name):
        
        # PSETOP DEFINED
        cbfunc = partial(self.run_component_service, MCAEventLoopComponent, "RUN", "FUNC_NB", "MAIN_LOOP", self.null_cbfunc, None, self.define_new_psetop)        
        rc = self.run_component_service(
            MCACallbackComponent, "REGISTER", "CONNECTION_CALLBACK", conn_name, 
            DYNRM_EVENT_PSETOP_DEFINED, cbfunc)
        if rc != DYNRM_MCA_SUCCESS:
            return rc

        # PSETOP FINALIZED
        cbfunc = partial(self.run_component_service, MCAEventLoopComponent, "RUN", "FUNC_NB", "MAIN_LOOP", self.null_cbfunc, None, self._finalize_psetop)
        rc = self.run_component_service(
            MCACallbackComponent, "REGISTER", "CONNECTION_CALLBACK", conn_name, 
            DYNRM_EVENT_PSETOP_FINALIZED, cbfunc)
        if rc != DYNRM_MCA_SUCCESS:
            return rc

        # TASK TERMINATED
        cbfunc = partial(self.run_component_service, MCAEventLoopComponent, "RUN", "FUNC_NB", "MAIN_LOOP", self.null_cbfunc, None, self.finalize_task)
        rc = self.run_component_service(
            MCACallbackComponent, "REGISTER", "CONNECTION_CALLBACK", conn_name, 
            DYNRM_EVENT_TASK_TERMINATED, cbfunc)
        if rc != DYNRM_MCA_SUCCESS:
            return rc

        return DYNRM_MCA_SUCCESS   

    # creates Prrte DVM and connects to it as PMIx Tool
    def set_topology_graph_epilog(self, topo_graph, params):

        # They command us to launch a Process Manager 
        if DYNRM_CMD_PM_LAUNCH in params.keys():
            launch_cmd = params[DYNRM_CMD_PM_LAUNCH]
            if DYNRM_PARAM_PM_MODULE in launch_cmd.keys():
                pm_module = launch_cmd[DYNRM_PARAM_PM_MODULE]
            else:
                v_print("Launch requested but no module provided. Defaulting to error")
                return DYNRM_MCA_ERR_BAD_PARAM
            pm_params = {}
            if DYNRM_PARAM_PM_PARAMS in launch_cmd.keys():
                pm_params = launch_cmd[DYNRM_PARAM_PM_PARAMS]
            rc = self.run_component_service(MCAProcessManagerComponent, "ADD", "PM", "GLOBAL_PM", pm_module(verbosity = self.verbosity))
            if rc != DYNRM_MCA_SUCCESS:
                return 
            
            rc = self.run_component_service(MCAProcessManagerComponent, "LAUNCH", "PM", "GLOBAL_PM", topo_graph, pm_params)
            if rc != DYNRM_MCA_SUCCESS:
                self.run_component_service(MCAProcessManagerComponent, "REMOVE", "PM", "GLOBAL_PM")
                return 
            
            if DYNRM_CMD_CONN_REQ in launch_cmd.keys:
                pm_info = self.run_component_service(MCAProcessManagerComponent, "GET", "INFO", "GLOBAL_PM")
                conn_info = pm_info.get(None, DYNRM_PARAM_CONN_INFO)
                if None == conn_info or 0 == len(conn_info):
                    return DYNRM_MCA_ERR_CONNECTION
                for info in conn_info:
                    module = info[DYNRM_PARAM_CONN_MODULE]
                    params = info[DYNRM_PARAM_CONN_PARAMS]
                    rc = self.run_component_service(MCACallbackComponent, "REQUEST", "CONNECTION", module, "GLOBAL_PM", self, None, params)
                    if rc == DYNRM_MCA_SUCCESS:
                        break
                if rc != DYNRM_MCA_SUCCESS:
                    return rc


        # If they request that we connect to the daemons network do it
        if DYNRM_CMD_CONN_REQ in params.keys():
            if DYNRM_PARAM_CONN_INFO in params.keys():
                conn_info = params.get(None, DYNRM_PARAM_CONN_INFO)
                if None == conn_info or 0 == len(conn_info):
                    return DYNRM_MCA_ERR_CONNECTION
                for info in conn_info:
                    module = info[DYNRM_PARAM_CONN_MODULE]
                    params = info[DYNRM_PARAM_CONN_PARAMS]
                    rc = self.run_component_service(MCACallbackComponent, "REQUEST", "CONNECTION", module, "GLOBAL_PM", self, None, params)
                    if rc == DYNRM_MCA_SUCCESS:
                        break
                if rc != DYNRM_MCA_SUCCESS:
                    return rc
            else:
                return DYNRM_MCA_ERR_BAD_PARAM
                
        return DYNRM_MCA_SUCCESS

    def default_psetop_finalized_cbfunc(self, conn_name, event_name, psetop_id):
        return self.finalize_psetop(psetop_id)
 
    def default_task_finalized_cbfunc(self, conn_name, event_name, task_id):
        return self.finalize_task(task_id)
        
    def default_psetop_defined_cbfunc(self, conn_name, event_name, psetop):
        return self.add_psetop(psetop)

    def null_cbfunc(*args, **kwargs):
        pass


    def apply_psetops_epilog(self, psetops):

        if 0 == len(psetops):
            return DYNRM_MCA_SUCCESS
        
        for psetop in psetops:
            launched_pm_name = None
            connected_pm_name = None
            task_name = psetop.run_service("GET", "TASK").run_service("GET", "GID")

            params = psetop.run_service("GET", "PARAM", DYNRM_PARAM_PSETOP_APPLY_PARAMS)
            # They command us to launch a Process Manager for this set operation 
            if DYNRM_CMD_PM_LAUNCH in params.keys():
                task = psetop.run_service("GET", "INPUT")[0].run_service("")
                # Choose a process manager module
                launch_cmd = params[DYNRM_CMD_PM_LAUNCH]
                if DYNRM_PARAM_PM_MODULE in launch_cmd.keys():
                    pm_module = launch_cmd[DYNRM_PARAM_PM_MODULE]
                elif DYNRM_PARAM_PM_MODULE_DEFAULT in self.params:
                    pm_module = self.params[DYNRM_PARAM_PM_MODULE_DEFAULT]
                else:
                    v_print("Launch requested but no module found. Defaulting to error")
                    return DYNRM_MCA_ERR_BAD_PARAM
                
                # Choose launch params
                pm_params = {}
                if DYNRM_PARAM_PM_PARAMS in launch_cmd.keys():
                    pm_params = launch_cmd[DYNRM_PARAM_PM_PARAMS]
                elif DYNRM_PARAM_PM_PARAMS_DEFAULT in self.params:
                    pm_params = launch_cmd[DYNRM_PARAM_PM_PARAMS_DEFAULT]
                
                # Get Topology where pm should be launched on
                if DYNRM_PARAM_PM_TOPOLOGY in launch_cmd.keys():
                    topology = launch_cmd[DYNRM_PARAM_PM_TOPOLOGY]
                else:
                    nodes = set()
                    for pset in psetop.run_service("GET", "OUTPUT"):
                        for node in pset.run_service("GET", "ACCESSED_NODES"):
                            nodes.add(node)
                    topology = MCATopologyGraphModule()
                    topology.run_service("ADD", "TOPOLOGY_OBJECTS", nodes, assign_graph = False)
                    for node in nodes:
                        topology.run_service("ADD", "TOPOLOGY_OBJECTS", node.run_service("GET", "CORES"), assign_graph = False)
                    v_print("Launch requested but no topology provided. Defaulting to error")
                    return DYNRM_MCA_ERR_BAD_PARAM
                
                # Choose a name for the PM
                if DYNRM_PARAM_PM_NAME in launch_cmd.keys():
                    launched_pm_name = launch_cmd[DYNRM_PARAM_PM_NAME]
                else:
                    launched_pm_name = task_name
                rc = self.run_component_service(MCAProcessManagerComponent, "ADD", "PM", launched_pm_name, pm_module(verbosity = self.verbosity))
                if rc != DYNRM_MCA_SUCCESS:
                    return 
                rc = self.run_component_service(MCAProcessManagerComponent, "LAUNCH", "PM", launched_pm_name, topology, pm_params)
                if rc != DYNRM_MCA_SUCCESS:
                    self.run_component_service(MCAProcessManagerComponent, "REMOVE", "PM", "name")
                    return 
                
                # Now connect to it 
                pm_info = self.run_component_service(MCAProcessManagerComponent, "GET", "INFO", launched_pm_name)
                conn_info = pm_info.get(None, DYNRM_PARAM_CONN_INFO)
                if None == conn_info or 0 == len(conn_info):
                    return DYNRM_MCA_ERR_CONNECTION
                # loop over provide modules and try to establish a connection
                for info in conn_info:
                    module = info[DYNRM_PARAM_CONN_MODULE]
                    params = info[DYNRM_PARAM_CONN_PARAMS]
                    if DYNRM_PARAM_CONN_NAME in info:
                        connected_pm_name = info[DYNRM_PARAM_CONN_NAME]
                    else:
                        connected_pm_name = launched_pm_name
                    rc = self.run_component_service(MCACallbackComponent, "REQUEST", "CONNECTION", module, connected_pm_name, self, None, params)
                    if rc == DYNRM_MCA_SUCCESS:
                        rc = self.register_callbacks_func(connected_pm_name)
                        if rc != DYNRM_MCA_SUCCESS:
                            return rc
                        break
                if rc != DYNRM_MCA_SUCCESS:
                    return rc

            # They request us to connect to an existing process manager
            elif DYNRM_CMD_CONN_REQ in params.keys():
                if DYNRM_PARAM_CONN_INFO in params.keys():
                    conn_info = params[DYNRM_PARAM_CONN_INFO]
                    if None == conn_info or 0 == len(conn_info):
                        return DYNRM_MCA_ERR_CONNECTION
                    # loop over provide modules and try to establish a connection
                    for info in conn_info:
                        module = info[DYNRM_PARAM_CONN_MODULE]
                        params = info[DYNRM_PARAM_CONN_PARAMS]
                        if DYNRM_PARAM_CONN_NAME in info:
                            connected_pm_name = info[DYNRM_PARAM_CONN_NAME]
                        else:
                            connected_pm_name = launched_pm_name
                        rc = self.run_component_service(MCACallbackComponent, "REQUEST", "CONNECTION", module, connected_pm_name, self, None, params)
                        if rc == DYNRM_MCA_SUCCESS:
                            rc = self.register_callbacks_func(connected_pm_name)
                            if rc != DYNRM_MCA_SUCCESS:
                                return rc
                            break
                    if rc != DYNRM_MCA_SUCCESS:
                        return rc
                    
                else:
                    return DYNRM_MCA_ERR_BAD_PARAM
            
            # If we have a default "PM" 
            if DYNRM_PARAM_PSETOP_APPLY_CONN in params:
                conn_name = params[DYNRM_PARAM_PSETOP_APPLY_CONN]
            elif None != connected_pm_name:
                conn_name = connected_pm_name
            elif "DEFAULT_PM" in self.run_component_service(MCACallbackComponent, "GET", "CONNECTION_NAMES"):
                conn_name = "DEFAULT_PM"
            else:
                return DYNRM_MCA_ERR_BAD_PARAM
            
            rc = self.run_component_service(MCACallbackComponent, "SEND", "EVENT", conn_name, DYNRM_CMD_PSETOP_APPLY, psetop)
            if rc != DYNRM_MCA_SUCCESS:
                return rc
        return DYNRM_MCA_SUCCESS