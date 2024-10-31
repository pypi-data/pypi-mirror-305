from dyn_rm.mca.mca import MCAModule, MCAClass

from dyn_rm.util.constants import *
from abc import abstractmethod

class MCAProcessManagerModule(MCAModule, MCAClass):

    def __init__(self, parent = None, parent_dir = ".", verbosity = 0, enable_output = False):
        super().__init__(parent = parent, parent_dir = parent_dir, verbosity = verbosity, enable_output = enable_output)
        self._running = False
        self._info = {DYNRM_PARAM_CONN_INFO : []}
        MCAProcessManagerModule.register_base_services(self)

        
    def register_base_services(self):
        self.register_service("LAUNCH", "PM", self.launch_process_manager)
        self.register_service("GET", "INFO", self.get_info)
        self.register_service("TERMINATE", "PM", self.terminate_process_manager)


    def launch_process_manager(self, topology, launch_params):
        if self._running:
            return DYNRM_MCA_SUCCESS
        rc = self.launch_process_manager_function(topology, launch_params) 
        if rc != DYNRM_MCA_SUCCESS:
            return rc
        self._running = True
        return DYNRM_MCA_SUCCESS

    def terminate_process_manager(self):
        if not self._running:
            return DYNRM_MCA_SUCCESS
        rc = self.terminate_process_manager_function() 
        if rc != DYNRM_MCA_SUCCESS:
            return rc
        self._running = False
        return DYNRM_MCA_SUCCESS

    def get_info(self, keys = None):
        if None == keys:
            return self._info
        info = dict()
        for key in keys:
            info[key] = self._info.get(key, None)
        return info

    def mca_shutdown(self):
        if self._running:
            self.terminate_process_manager()
        return self.mca_default_shutdown()
    
    @abstractmethod
    def launch_process_manager_function(self, params):
        return DYNRM_MCA_ERR_NOT_IMPLEMENTED

    @abstractmethod
    def terminate_process_manager_function(self):
        return DYNRM_MCA_ERR_NOT_IMPLEMENTED