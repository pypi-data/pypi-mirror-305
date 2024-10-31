from dyn_rm.mca.mca import MCAModule
from dyn_rm.util.constants import *
from abc import abstractmethod

class MCAColObjectCreationModule(MCAModule):

    def __init__(self, parent = None, parent_dir = ".", verbosity = 0, enable_output = False):
        super().__init__(parent = parent, parent_dir = parent_dir, verbosity = verbosity, enable_output = enable_output)
        self.params = dict()
        MCAColObjectCreationModule.register_base_services(self)

    @staticmethod    
    def register_base_services(self):
        self.register_service("SET", "PARAMETERS", self.set_parameters)
        self.register_service("GET", "PARAMETERS", self.set_parameters)
        self.register_service("UNSET", "PARAMETERS", self.unset_parameters)
        self.register_service("CREATE", "COL_OBJECT", self.create_col_object)
        self.register_service("UPDATE", "COL_OBJECT", self.update_col_object) 

    def set_parameters(self, params: dict):
        self.params.update(params)
        return DYNRM_MCA_SUCCESS
    
    def get_parameters(self, params: dict):
        return self.params
    
    def unset_parameters(self, keys: list):
        for key in keys:
            self.params.pop(key)
        return DYNRM_MCA_SUCCESS
    
    

    def create_col_object(self, col_object, object, params):
        return self.create_col_object_function(col_object, object, params)
    
    def update_col_object(self, col_object, object, params):
        return self.update_col_object_function(col_object, object, params)
    
    def create_object_from_col(self, col, params):
        return self.create_object_from_col(self, col, params)
        
    # Abstract Functions
    @abstractmethod
    def create_col_object_function(self, object, params):
        return DYNRM_MCA_ERR_NOT_IMPLEMENTED
    
    @abstractmethod
    def update_col_object_function(self, object, params):
        return DYNRM_MCA_ERR_NOT_IMPLEMENTED
    
    @abstractmethod
    def create_object_from_col_function(self, col, params):
        return DYNRM_MCA_ERR_NOT_IMPLEMENTED