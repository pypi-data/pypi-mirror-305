
from dyn_rm.mca.base.graph.module.edge import MCAEdgeModule
from dyn_rm.mca.base.system.module.psets.pset import MCAPSetModule
from dyn_rm.mca.base.system.module.psets.pset_graph_object import MCAPsetGraphObject

from dyn_rm.util.constants import *

import time

class MCAPSetopModule(MCAEdgeModule, MCAPsetGraphObject):

    PSETOP_STATUS_DEFINED = 0
    PSETOP_STATUS_CANCELED = 1
    PSETOP_STATUS_SCHEDULED = 2
    PSETOP_STATUS_PENDING = 3
    PSETOP_STATUS_ORDERED = 4
    PSETOP_STATUS_FINALIZED = 5
    

    PSETOP_ATTRIBUTE_OP = "PSETOP_OP"
    PSETOP_ATTRIBUTE_STATUS = "PSETOP_STATUS"
    PSETOP_ATTRIBUTE_JOBID = "PSETOP_JOBID"
    PSETOP_ATTRIBUTE_PREDECESSORS = "PSETOP_PREDECESSORS"
    PSETOP_ATTRIBUTE_SUCCESSORS = "PSETOP_SUCCESSORS"
    PSETOP_ATTRIBUTE_PRIORITY = "PSETOP_PRIORITY"

    PSETOP_OP_NULL = 0
    PSETOP_OP_ADD = 1
    PSETOP_OP_SUB = 2
    PSETOP_OP_GROW = 3
    PSETOP_OP_SHRINK = 4
    PSETOP_OP_REPLACE = 5
    PSETOP_OP_UNION = 6
    PSETOP_OP_DIFFERENCE = 7
    PSETOP_OP_INTERSECTION = 8
    PSETOP_OP_SPLIT = 9
    PSETOP_OP_CANCEL = 10

    def __init__(self, name, op, input, output = [], model_name = None, model_module = None, parent = None, parent_dir = ".", verbosity = 0, enable_output = False):
        super().__init__(parent = parent, parent_dir = parent_dir, verbosity = verbosity, enable_output = enable_output)
        self.__class__.register_base_services(self)
        self.run_service("SET", "ATTRIBUTE", MCAPSetopModule.PSETOP_ATTRIBUTE_OP, op)
        self.run_service("SET", "ATTRIBUTE", MCAPSetopModule.PSETOP_ATTRIBUTE_STATUS, MCAPSetopModule.PSETOP_STATUS_DEFINED)
        self.run_service("SET", "ATTRIBUTE", MCAPSetopModule.PSETOP_ATTRIBUTE_PREDECESSORS, [])
        self.run_service("SET", "ATTRIBUTE", MCAPSetopModule.PSETOP_ATTRIBUTE_SUCCESSORS, [])
        self.run_service("SET", "ATTRIBUTE", MCAPSetopModule.PSETOP_ATTRIBUTE_PRIORITY, 1)

        self.run_service("SET", "NAME", name)
        if None != model_module and None != model_name:
            self.run_service("ADD", "EDGE_MODEL", model_name, model_module)

        self.run_service("SET", "INPUT", input)
        self.run_service("SET", "OUTPUT", output)
        self._cbfunc = None
        self._cbdata = None
        self._col_objects = []

    @staticmethod    
    def register_base_services(self):
        self.register_service("SET", "PSETOP_OUTPUT", self.set_psetop_output)
        self.register_service("GET", "PSETOP_OP", self.get_psetop_op)
        self.register_service("ADD", "PSETOP_MODEL", self.add_psetop_model)
        self.register_service("GET", "PSETOP_MODEL", self.get_psetop_model)
        self.register_service("SET", "PSETOP_STATUS", self.set_psetop_status)
        self.register_service("GET", "PSETOP_STATUS", self.get_psetop_status)
        self.register_service("SET", "PSETOP_CBFUNC", self.set_cbfunc)
        self.register_service("SET", "PSETOP_CBDATA", self.set_cbdata)
        self.register_service("GET", "PSETOP_CBFUNC", self.get_cbfunc)
        self.register_service("GET", "PSETOP_CBDATA", self.get_cbdata)
        self.register_service("GET", "PSET_GRAPH", self.get_pset_graph)
        self.register_service("GET", "PRIORITY", self.get_priority)
        self.register_service("SET", "PRIORITY", self.set_priority)
        self.register_service("GET", "TASK", self.get_task)
        self.register_service("ADD", "COL_OBJECT", self.add_col_object)
        self.register_service("GET", "COL_OBJECT", self.get_col_objects)
        self.register_service("APPLY", "COL_OBJECT", self.apply_col_object)

    def get_priority(self):
        return self.run_service("GET", "ATTRIBUTE", MCAPSetopModule.PSETOP_ATTRIBUTE_PRIORITY)
    def set_priority(self, priority):
        return self.run_service("SET", "ATTRIBUTE", MCAPSetopModule.PSETOP_ATTRIBUTE_PRIORITY, priority)


    def set_psetop_output(self, output):
        return self.run_service("SET", "OUTPUT", output)
    
    def get_psetop_op(self):
        return self.run_service("GET", "ATTRIBUTE", MCAPSetopModule.PSETOP_ATTRIBUTE_OP)

    def add_psetop_model(self, model_name, model):
        return self.run_service("ADD", "EDGE_MODEL", model_name, model)

    def get_psetop_model(self, model_name):
        return self.run_service("GET", "EDGE_MODEL", model_name)

    def set_psetop_status(self, status):
        return self.run_service("SET", "ATTRIBUTE", MCAPSetopModule.PSETOP_ATTRIBUTE_STATUS, status)
    
    def get_psetop_status(self):
        return self.run_service("GET", "ATTRIBUTE", MCAPSetopModule.PSETOP_ATTRIBUTE_STATUS)

    def set_cbfunc(self, cbfunc):
        self._cbfunc = cbfunc
        return DYNRM_MCA_SUCCESS
    
    def set_cbdata(self, cbdata):
        self._cbdata = cbdata
        return DYNRM_MCA_SUCCESS

    def get_cbfunc(self):
        return self._cbfunc

    def get_cbdata(self):
        return self._cbdata
    
    def get_pset_graph(self):
        graphs = self.run_service("GET", "GRAPHS")
        for graph in graphs:
            if isinstance(graph, MCAPSetModule):
                return graph
        return None
    
    def get_task(self):
        return self.input[0].run_service("GET", "TASK")

    def add_col_object(self, col):
        self._col_objects.append(col)
    def get_col_objects(self, col):
        return self._col_objects

    def apply_col_object(self, col):
        # TODO:        
        #if None == model:
            # Assign defaut model for the operation 
        #if None == model_params:
            # Set some default parameters if necessary
        #if None == output_space_generator:
            # Set Default output_space_generator for this PSetop
        task = self.get_task()

        model = self.get_psetop_model("USER_MODEL")
        if None != col.psetop_model:
            model = col.psetop_model
            self.add_psetop_model("USER_MODEL", model)
        elif None != col.psetop_model_key and None != task:
            model = task.run_service("GET", "ATTRIBUTE". col.psetop_model_key)
            self.add_psetop_model("USER_MODEL", model)

        if model != None:

            if None != col.psetop_model_params:
                model.run_service("ADD", "MODEL_PARAMS", col.psetop_model_params)
            elif None != col.psetop_model_params_key and None != task:
                model.run_service("ADD", "MODEL_PARAMS", 
                                  task.run_service("GET", "ATTRIBUTE", col.psetop_model_params_key))

            if None != col.output_space_generator:
                model.run_service("SET", "OUTPUT_SPACE_GENERATOR", col.output_space_generator)
            elif None != col.output_space_generator_key and None != task:
                model.run_service("SET", "OUTPUT_SPACE_GENERATOR", 
                                  task.run_service("GET", "ATTRIBUTE", col.output_space_generator_key))


            if None != col.monitoring_data and len(col.monitoring_data) > 0:
                model.run_service("ADD", "MONITORING_ENTRY", time.time(), col.monitoring_data)

        if None != col.priority:
            self.set_priority(col.priority)

        # Update models of input sets
        for index in col.input_pset_models.keys():
            self.input[index].run_service("ADD", "PSET_MODEL", "USER_MODEL", col.input_pset_models[index])

        # update parameters of input pset models
        for index in col.input_pset_model_params.keys():
            pset_model = self.input[index].run_service("GET", "PSET_MODEL", "USER_MODEL")
            for k,v in col.input_pset_models[index]:
                pset_model.run_service("SET", "MODEL_PARAM", k, v)

        # update monitoting data of input pset models
        for index in col.input_pset_model_monitoring.keys():
            pset_model = self.input[index].run_service("GET", "PSET_MODEL", "USER_MODEL")
            if None != pset_model:
                pset_model.run_service("ADD", "MONITORING_DATA", col.input_pset_model_monitoring[index])
                pset_model.run_service("EVAL", "MODEL_PARAMS")

        for key, val in col.psetop_attributes_add.items():
            self.set_attribute(key, val)
        for key in col.psetop_attributes_remove:
            self.unset_attribute(key)

        self.add_col_object(col)
        return DYNRM_MCA_SUCCESS


    

        



    

