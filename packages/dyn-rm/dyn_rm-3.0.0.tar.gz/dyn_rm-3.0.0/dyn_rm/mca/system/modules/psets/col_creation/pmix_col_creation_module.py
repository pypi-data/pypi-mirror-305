from dyn_rm.mca.base.system.module.psets.col_creation import MCAColObjectCreationModule
from dyn_rm.mca.base.system.module.psets.col_object import MCAColObjectv1
from dyn_rm.mca.system.modules.psets.pset_models import *
from dyn_rm.mca.system.modules.psets.psetop_models import *
from dyn_rm.mca.mca import MCAModule
from dyn_rm.util.constants import *
from dyn_rm.util.functions import v_print
from abc import abstractmethod
from functools import partial
class PmixColObjectCreationModule(MCAColObjectCreationModule):
        
    # Abstract Functions
    @abstractmethod
    def create_col_object_function(self, col, object, params):
        for info in object:
            # Get the PSet Operation model
            if info['key'] == 'model':
                col.psetop_model = eval(info['value'])
            # Get the parameters for the PSet Operation Model   
            elif info['key'] == 'model_params':
                kvs = info['value'].split(',')
                for kv in kvs:
                    PmixColObjectCreationModule._insert_kvt(col.psetop_model_params, kvt)
            # Get the priority for the psetop
            elif info['key'] == 'priority':
                col.priority = int(info['value'])

            # Get the output space generator
            elif info['key'] == 'output_space_generator':
                col.output_space_generator = eval(info['value'])        

            # Get the monitoring data
            elif info['key'] == 'monitoring_data':
                kvs = info['value'].split(',')
                for kvt in kvs:
                    PmixColObjectCreationModule._insert_kvt(col.monitoring_data, kvt)
            # Get models for the input PSets
            elif info['key'].startswith('input_pset_models'):
                index = int(info['key'].split('_')[-1])
                col.input_pset_models[int(index)] = eval(info['value'])

            # Update paramters for the input PSet 
            elif info['key'].startswith('input_pset_model_params'):
                index = int(info['key'].split('_')[-1])
                col.input_pset_model_params[index] = dict()
                kvs = info['value'].split(',')
                for kvt in kvs:
                    PmixColObjectCreationModule._insert_kvt(col.input_pset_model_params, kvt)

            # Update paramters for the input PSet 
            elif info['key'].startswith('input_pset_model_monitoring'):
                index = int(info['key'].split('_')[-1])
                col.input_pset_model_monitoring[index] = dict()
                kvs = info['value'].split(',')
                for kvt in kvs:
                    PmixColObjectCreationModule._insert_kvt(col.input_pset_model_monitoring[index], kvt)
            elif info['key'].startswith('task_attribute_'):
                v_print("Task Attributes are depricated and not supported by PmixColObjectCreationModule", 1, self.verbosity)
                return DYNRM_MCA_ERR_BAD_PARAM
            elif info['key'] == 'task_attribute_key_model_expression':
                col.psetop_model_key = info['value']
            elif info['key'] == 'task_attribute_key_model_params':
                col.model_params_key = info['value']    
            elif info['key'] == 'generator_key':
                col.output_space_generator_key = info['value']

        return DYNRM_MCA_SUCCESS
    
    @abstractmethod
    def update_col_object_function(self, object, params):
        return DYNRM_MCA_ERR_NOT_IMPLEMENTED
    
    @abstractmethod
    def create_object_from_col_function(self, col, params):
        return DYNRM_MCA_ERR_NOT_IMPLEMENTED
    

    def _insert_kvt(my_dict, kvt):
        key, val, t = kvt.split(':')
        if t == 'int':
            my_dict[key] = int(val)
        elif t == 'float':
            my_dict[key] = float(val)
        elif t == 'string':
            my_dict[key] = str(val)
        elif t == 'bool':
            my_dict[key] = bool(val)
        else:
            my_dict[key] = val