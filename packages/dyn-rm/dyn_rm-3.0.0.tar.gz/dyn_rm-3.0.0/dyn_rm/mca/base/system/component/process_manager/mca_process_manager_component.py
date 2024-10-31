from dyn_rm.mca.mca import MCAComponent
from dyn_rm.mca.mca import MCAClass

from dyn_rm.util.constants import *

class MCAProcessManagerComponent(MCAComponent, MCAClass):

    def __init__(self, parent = None, parent_dir = ".", verbosity = 0, enable_output = False):
        super().__init__(parent = parent, parent_dir = parent_dir, verbosity = verbosity, enable_output = enable_output)
        self._process_managers = dict()
        MCAProcessManagerComponent.register_base_services(self)

        
    def register_base_services(self):
        self.register_service("ADD", "PM", self.add_process_manager)
        self.register_service("GET", "PM", self.get_process_manager)
        self.register_service("REMOVE", "PM", self.remove_process_manager)

        self.register_service("LAUNCH", "PM", self.launch_process_manager)
        self.register_service("GET", "INFO", self.get_info)
        self.register_service("TERMINATE", "PM", self.terminate_process_manager)


    def add_process_manager(self, name, pm_module):
        self.register_module(pm_module)
        self._process_managers[name] = pm_module
        return DYNRM_MCA_SUCCESS

    def get_process_manager(self, name):
        return self._process_managers.get(name)

    def remove_process_manager(self, name):
        return self._process_managers.pop(name)

    def launch_process_manager(self, name, topology, launch_params):
        pm_module = self.get_process_manager(name)
        if None == pm_module:
            return DYNRM_ERR_NOT_FOUND
        return self.run_module_service(pm_module, "LAUNCH", "PM", topology, launch_params) 

    def terminate_process_manager(self, name):
        pm_module = self.get_process_manager(name)
        if None == pm_module:
            return DYNRM_ERR_NOT_FOUND
        return self.run_module_service(pm_module, "TERMINATE", "PM") 

    def get_info(self, name, keys):
        pm_module = self.get_process_manager(name)
        if None == pm_module:
            return None
        return self.run_module_service(pm_module, "GET", "INFO", keys = keys) 

    def mca_shutdown(self):
        for process_manager in self._process_managers.values():
            process_manager.run_service("MCA", "SHUTDOWN")
        return self.mca_default_shutdown()