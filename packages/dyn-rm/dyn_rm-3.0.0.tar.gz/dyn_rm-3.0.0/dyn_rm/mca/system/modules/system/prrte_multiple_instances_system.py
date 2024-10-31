from dyn_rm.mca.base.logger.component import MCALoggerComponent
from dyn_rm.mca.base.system.module.logging import *
from dyn_rm.mca.base.system.module import MCASystemModule
from dyn_rm.mca.base.callback.component import MCACallbackComponent
from dyn_rm.mca.callback.modules.pmix import PmixCallbackModule
from dyn_rm.mca.base.event_loop.component import MCAEventLoopComponent
from dyn_rm.mca.base.event_loop.module import MCAEventLoopModule
from dyn_rm.mca.base.system.component import MCAProcessManagerComponent
from dyn_rm.mca.system.modules.process_manager.prrte_process_manager_module import PrrteProcessManagerModule
from dyn_rm.mca.base.system.module import *
from dyn_rm.mca.system.modules.psets.psetop_models import *
from dyn_rm.mca.system.modules.psets.pset_models import *
from dyn_rm.util.constants import *
from dyn_rm.util.functions import v_print
import os
import time
from functools import partial

#####################################
###  PrrteMultipleInstancesSystem ###
##################################### 
# Description: 
# This system uses a seperat PRRTE process managers per task
#
###

class PrrteMultipleInstancesSystem(MCASystemModule):

    def __init__(self, parent = None, parent_dir = ".", verbosity = 0, enable_output = False):
        super().__init__(parent = parent, parent_dir = parent_dir, verbosity = verbosity, enable_output = enable_output)

    # Just use the default callbacks of the MCASystemModule
    def register_callbacks_func(self, conn_name):
        return super().register_callbacks_func(conn_name)

    def apply_psetops_epilog(self, psetops):

        if 0 == len(psetops):
            return DYNRM_MCA_SUCCESS
        
        for psetop in psetops:
            task = None
            if len(psetop.run_service("GET","OUTPUT")) > 0:
                task = psetop.run_service("GET", "OUTPUT")[-1].run_service("GET", "TASK")
            if None == task or isinstance(task, MCATaskGraphModule):
                task = psetop.run_service("GET", "INPUT")[0].run_service("GET", "TASK")
            
            task_name = task.run_service("GET", "GID")

            print("Task name vs connections: "+task_name+" - "+str(self.run_component_service(MCACallbackComponent, "GET", "CONNECTION_NAMES")))
            if task_name not in self.run_component_service(MCACallbackComponent, "GET", "CONNECTION_NAMES"):
                # Create the topology graph for the task-local instance
                nodes = set()
                for pset in psetop.run_service("GET", "OUTPUT"):
                    for node in pset.run_service("GET", "ACCESSED_NODES"):
                        nodes.add(node)
                topology = MCATopologyGraphModule(task_name)
                topology.run_service("ADD", "TOPOLOGY_OBJECTS", nodes, assign_graph = False)
                for node in nodes:
                    topology.run_service("ADD", "TOPOLOGY_OBJECTS", node.run_service("GET", "CORES"), assign_graph = False)
                topology.run_service("PRINT", "TOPOLOGY_GRAPH")
                # Add a Task-Local Prrte PM Module 
                rc = self.run_component_service(MCAProcessManagerComponent, "ADD", "PM", task_name, PrrteProcessManagerModule(verbosity = self.verbosity))
                if rc != DYNRM_MCA_SUCCESS:
                    return rc

                # Launch Local Prrte instance
                rc = self.run_component_service(MCAProcessManagerComponent, "LAUNCH", "PM", task_name, topology, {})
                if rc != DYNRM_MCA_SUCCESS:
                    # Remove module if launch fails
                    self.run_component_service(MCAProcessManagerComponent, "REMOVE", "PM", task_name)
                    return rc

                # Get the connection info
                conn_info = self.run_component_service(MCAProcessManagerComponent, "GET", "INFO", task_name, [DYNRM_PARAM_CONN_INFO])
                if None == conn_info or 0 == len(conn_info):
                    return DYNRM_MCA_ERR_CONNECTION

                # Try to establish a connection
                for info in conn_info[DYNRM_PARAM_CONN_INFO]:
                    module = info[DYNRM_PARAM_CONN_MODULE]
                    params = info[DYNRM_PARAM_CONN_PARAMS]
                    params[DYNRM_PARAM_CONN_SCHEDULER] = True

                    rc = self.run_component_service(MCACallbackComponent, "REQUEST", "CONNECTION", module, task_name, self, None, params)
                    if rc == DYNRM_MCA_SUCCESS:
                        break
                    else:
                        return rc

                rc = self.register_callbacks_func(task_name)
                if rc != DYNRM_MCA_SUCCESS:
                    return rc
            
            rc = self.run_component_service(MCACallbackComponent, "SEND", "EVENT", task_name, DYNRM_CMD_PSETOP_APPLY, psetop)
            if rc != DYNRM_MCA_SUCCESS:
                return rc
        return DYNRM_MCA_SUCCESS