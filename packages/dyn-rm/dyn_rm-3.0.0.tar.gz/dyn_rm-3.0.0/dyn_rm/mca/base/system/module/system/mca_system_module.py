from dyn_rm.mca.base.logger.component import MCALoggerComponent
from dyn_rm.mca.base.callback.component import MCACallbackComponent
from dyn_rm.mca.base.system.component.topology import MCATopologyCreationComponent
from dyn_rm.mca.base.graph.component.graph import MCAGraphComponent
from dyn_rm.mca.base.system.component.tasks import MCATaskGraphCreationComponent
from dyn_rm.mca.base.submission.component import MCASubmissionComponent
from dyn_rm.mca.base.event_loop.component import MCAEventLoopComponent
from dyn_rm.mca.base.system.component.process_manager import MCAProcessManagerComponent

from dyn_rm.mca.base.event_loop.module import MCAEventLoopModule
from dyn_rm.mca.base.graph.module.graph_object import MCAGraphObjectModule
from dyn_rm.mca.base.graph.module.graph import MCAGraphModule
from dyn_rm.mca.base.graph.module.edge import MCAEdgeModule
from dyn_rm.mca.base.graph.module.vertex import MCAVertexModule
from dyn_rm.mca.base.system.module.topology import *
from dyn_rm.mca.base.system.module.psets import *
from dyn_rm.mca.base.system.module.tasks import *
from dyn_rm.mca.base.system.module.logging import *

from dyn_rm.mca.mca import MCAClass

from abc import abstractmethod
from dyn_rm.util.constants import *
from dyn_rm.util.functions import v_print
from functools import partial

class MCASystemModule(MCAGraphModule, MCAClass):

    def __init__(self, parent = None, parent_dir = ".", verbosity = 0, enable_output = False):
        super().__init__(parent = parent, parent_dir = parent_dir, verbosity = verbosity, enable_output = enable_output)

        self.procs = dict()
        self.nodes = dict()
        self.jobs = dict()
        self.psets = dict()
        self.psetops = dict()
        self.time = 0

        if None != parent:
            parent.register_module(self)
        
        # Register our components
        self.register_components()
        
        logger_comp = self.get_component(MCALoggerComponent)
        logger_comp.register_module(MCANodeLogger(parent = logger_comp, enable_output = self.enable_output))
        logger_comp.register_module(MCASetOpLogger(parent = logger_comp, enable_output = self.enable_output))
        logger_comp.register_module(MCASetLogger(parent = logger_comp, enable_output = self.enable_output))
        logger_comp.register_module(MCATaskLogger(parent = logger_comp, enable_output = self.enable_output))

        loop_comp = self.get_component(MCAEventLoopComponent)
        loop_comp.register_module(MCAEventLoopModule())
        self.register_component(loop_comp)
        self.run_component_service(MCAEventLoopComponent, "REGISTER", "EVENT_LOOP", MCAEventLoopModule, "MAIN_LOOP")
        self.run_component_service(MCAEventLoopComponent, "START", "EVENT_LOOP", "MAIN_LOOP")

        topology_graph = MCATopologyGraphModule(self._get_topology_graph_name())         
        self.run_component_service(MCAGraphComponent, "ADD", "GRAPH", self._get_topology_graph_name(), topology_graph)
        
        self.run_service("ADD", "GRAPH_VERTICES", [topology_graph])
        self.run_service("MAKE", "EDGE", [self], [topology_graph])

        MCASystemModule.register_base_services(self)



    @staticmethod
    def register_base_services(self):

        self.register_service("EXECUTE", "IN_LOOP", partial(self.execute_in_loop, "MAIN_LOOP"))

        # Topology
        self.register_service("REGISTER", "TOPOLOGY_CREATION_MODULE", partial(self.execute_in_loop, "MAIN_LOOP", self.get_component(MCATopologyCreationComponent).register_module))  
        self.register_service("CREATE", "SYSTEM_TOPOLOGY", partial(self.execute_in_loop, "MAIN_LOOP", self.create_system_topology))
        self.register_service("SET", "TOPOLOGY_GRAPH", partial(self.execute_in_loop, "MAIN_LOOP", self._set_system_topology))        
        self.register_service("GET", "TOPOLOGY_GRAPH", partial(self.execute_in_loop, "MAIN_LOOP", lambda: self.run_component_service(MCAGraphComponent, "GET", "GRAPH", self._get_topology_graph_name())))


        # Tasks
        self.register_service("SUBMIT", "TASK_GRAPH", partial(self.execute_in_loop, "MAIN_LOOP", self._submit_task_graph))
        self.register_service("GET", "TASK_GRAPHS", partial(self.execute_in_loop, "MAIN_LOOP", self.get_task_graphs))


        # Psets
        self.register_service("GET", "PSET_GRAPHS", partial(self.execute_in_loop, "MAIN_LOOP", self.get_pset_graphs))
        self.register_service("ADD", "PSETOPS", partial(self.execute_in_loop, "MAIN_LOOP", self.add_psetops))
        self.register_service("APPLY", "PSETOPS", partial(self.execute_in_loop, "MAIN_LOOP", self.apply_psetops))
        self.register_service("FINALIZE", "PSETOP", partial(self.execute_in_loop, "MAIN_LOOP", self.finalize_psetop))

        # Print
        self.register_service("PRINT", "SYSTEM", partial(self.execute_in_loop, "MAIN_LOOP", self.print_system))

    def register_components(self):
        self.register_component(MCALoggerComponent(parent = self, enable_output = self.enable_output, verbosity=self.verbosity))
        self.register_component(MCACallbackComponent(parent = self, verbosity=self.verbosity))
        self.register_component(MCATopologyCreationComponent(parent = self, verbosity=self.verbosity))
        self.register_component(MCASubmissionComponent(parent = self, verbosity=self.verbosity))
        self.register_component(MCATaskGraphCreationComponent(parent = self,verbosity=self.verbosity))
        self.register_component(MCAEventLoopComponent(parent = self, verbosity=self.verbosity))
        self.register_component(MCAGraphComponent(parent = self, verbosity=self.verbosity))
        self.register_component(MCAProcessManagerComponent(parent = self, verbosity=self.verbosity))


    def execute_in_loop(self, loop_name, func, *args, **kwargs):
        
        # Avoid deadlock we are already running in this loop 
        current_loop = self.run_component_service(MCAEventLoopComponent,
                                                     "GET", "CURRENT_LOOP",
                                                     MCAEventLoopModule)
        if loop_name == current_loop:
            return func(*args, **kwargs) 

        return self.run_component_service(MCAEventLoopComponent,
                                   "RUN", "FUNC", loop_name,
                                   func, *args, **kwargs)

    def _set_system_topology(self, topo_graph, params = {}):
        # Add the topology graph to our graph component 
        self.run_component_service(MCAGraphComponent, "ADD", "GRAPH",self._get_topology_graph_name(), topo_graph)
    
        # Insert everything into the system graph
        new_objects = []
        new_objects.extend(topo_graph.run_service("GET", "ALL_GRAPH_VERTICES"))
        new_objects.extend(topo_graph.run_service("GET", "ALL_GRAPH_EDGES"))
        for object in new_objects:
            object.run_service("SET", "STATUS", MCAGraphObjectModule.STATUS_NEW)
        self.run_service("UPDATE", "GRAPH", new_objects)

        # Finally connect us to the graph roots
        self.run_service("MAKE", "EDGE", [self], [topo_graph])


        rc = self.set_topology_graph_epilog(topo_graph, params)
        if rc != DYNRM_MCA_ERR_NOT_IMPLEMENTED and rc != DYNRM_MCA_SUCCESS:
            return rc

        nodes = topo_graph.run_service("GET", "TOPOLOGY_OBJECTS", MCANodeModule)
        self.run_component_service( MCALoggerComponent, "LOG", "EVENTS",
                            MCANodeLogger, "NODE_STARTED", 
                            nodes)   
        return DYNRM_SUCCESS


    def get_task_graphs(self):
        return [g for g in self.run_component_service(MCAGraphComponent, "GET", "GRAPHS") if isinstance(g, MCATaskGraphModule)]

    def _submit_task_graph(self, task_graph):
        
        pset_graph = MCAPSetGraphModule()
        pset_graph.run_service("SET", "GID", self._get_new_object_id())
        pset_graph.run_service("ADD", "PSET_MODEL", "DEFAULT_MODEL", MCANullPSetModel())

        # Update Task Status
        tasks = task_graph.run_service("GET", "TASKS")

        self.run_component_service( MCALoggerComponent, "LOG", "EVENTS",
                MCATaskLogger, "TASK_SUBMITTED", 
                tasks)

        if len(tasks) > 0:
            task_graph.run_service("SET", "TASK_STATUS", MCATaskModule.TASK_STATUS_WAITING)
        else:
            task_graph.run_service("SET", "TASK_STATUS", MCATaskModule.TASK_STATUS_TERMINATED)

        for t in tasks:
            if t != task_graph and 0 == len(t.run_service("GET", "PREDECESSOR_TASKS")):
                # Task is ready to run
                t.run_service("SET", "TASK_STATUS", MCATaskModule.TASK_STATUS_READY)

                # create an ADD PSet operation and assign the launch_ouput_generator
                psetop = pset_graph.run_service("CREATE", "PSETOP", DYNRM_PSETOP_ADD, [pset_graph])
                psetop_model = MCALaunchPsetopModel()
                psetop_model.run_service("SET", "OUTPUT_SPACE_GENERATOR", t.run_service("GET", "TASK_LAUNCH_OUTPUT_SPACE_GENERATOR"))
                psetop.run_service("ADD", "PSETOP_MODEL", "USER_MODEL", psetop_model)

                self.run_component_service( MCALoggerComponent, "LOG", "EVENT",
                    MCASetOpLogger, "SETOP_DEFINED", 
                    psetop)


            else:
                # task needs to wait for depenencies
                t.run_service("SET", "TASK_STATUS", MCATaskModule.TASK_STATUS_WAITING)
        
        # Add the task graph to our task 
        self.run_component_service(MCAGraphComponent, "ADD", "GRAPH", task_graph.run_service("GET", "GID"), task_graph)
        self.run_component_service(MCAGraphComponent, "ADD", "GRAPH", pset_graph.run_service("GET", "GID"), pset_graph)
    
        # Insert everything into the system graph
        new_objects = []
        new_objects.extend(task_graph.run_service("GET", "ALL_GRAPH_VERTICES"))
        new_objects.extend(task_graph.run_service("GET", "ALL_GRAPH_EDGES"))
        new_objects.extend(pset_graph.run_service("GET", "ALL_GRAPH_VERTICES"))
        new_objects.extend(pset_graph.run_service("GET", "ALL_GRAPH_EDGES"))

        for object in new_objects:
            object.run_service("SET", "STATUS", MCAGraphObjectModule.STATUS_NEW)
        self.run_service("UPDATE", "GRAPH", new_objects)

        # Finally connect us to the graph roots
        self.run_service("MAKE", "EDGE", [self], [task_graph])
        self.run_service("MAKE", "EDGE", [self], [pset_graph])
        edge = self.run_service("MAKE", "EDGE", [pset_graph], [task_graph])
        edge.run_service("SET", "ATTRIBUTE", MCAPSetModule.PSET_ATTRIBUTE_TASK, True)


        return DYNRM_MCA_SUCCESS


    
    def _get_topology_graph_name(self):
        return self.run_service("GET", "GID") + "/"+"hw"

    def create_system_topology(self, module, object, params):
        graph = self.run_service("GET", "TOPOLOGY_GRAPH")
        
        # Let our topology component create the graph
        self.run_component_service(MCATopologyCreationComponent, "CREATE", "TOPOLOGY_GRAPH", module, graph, object, params)
        
        vertices = graph.run_service("GET", "ALL_GRAPH_VERTICES")
        edges = graph.run_service("GET", "ALL_GRAPH_EDGES")

        # Insert the graph in our graph component
        #self.run_component_service(MCAGraphComponent, "ADD", "GRAPH", self._get_topology_graph_name(), graph)

        # make an edge from us to the hw_topology root
        #edge = MCAEdgeModule()
        #edge.run_service("SET", "GID", self.run_service("GET", "NEW_GID"))

        # insert all vertices and edges in our global graph
        self.run_service("ADD", "GRAPH_VERTICES", vertices)
        self.run_service("ADD", "GRAPH_EDGES", edges)

        return DYNRM_MCA_SUCCESS



    def get_pset_graphs(self):
        return [g for g in self.run_component_service(MCAGraphComponent, "GET", "GRAPHS") if isinstance(g, MCAPSetGraphModule)]

    def add_psetops(self, psetops):
        for psetop in psetops:
            rc = self.add_psetop(psetop)
            if rc != DYNRM_MCA_SUCCESS:
                return rc

    def add_psetop(self, new_psetop):
        v_print("Adding PSetOP "+new_psetop.run_service("GET", "GID")+ " to system", 5, self.verbosity)

        # For now, assume processes do not specify operations on the null psets
        in_psets = new_psetop.run_service("GET", "INPUT")
        in_names = [pset.run_service("GET", "GID") for pset in in_psets]
        for name in in_names:
            if None == self.run_service("GET", "GRAPH_VERTEX", name):
                v_print("Cannot add psetop: Input Pset "+name+" not found in system graph")
                return DYNRM_ERR_BAD_PARAM

        op = new_psetop.run_service("GET", "PSETOP_OP")

        task = new_psetop.run_service("GET", "TASK")
        if None == task:
            v_print("Task is None", 10, self.verbosity)
            return DYNRM_ERR_BAD_PARAM

        pset_graph = in_psets[0].run_service("GET", "PSET_GRAPH")
        if None == pset_graph:
            v_print("Pset Graph is None", 10, self.verbosity)
            return DYNRM_ERR_BAD_PARAM
        
        existing_psetops = pset_graph.run_service("GET", "PSETOPS")

        # Handle CANCELATION here
        if new_psetop.run_service("GET", "PSETOP_OP") == DYNRM_PSETOP_CANCEL:
            cancel_psetop = new_psetop
            rc =  self.insert_psetops([cancel_psetop])
            if rc != DYNRM_MCA_SUCCESS:
                return rc
            
            self.run_component_service( MCALoggerComponent, "LOG", "EVENT",
                MCASetOpLogger, "SETOP_DEFINED", 
                cancel_psetop) 

            psetops_to_apply = [cancel_psetop]
            output_lists = [[]]
            a_lists = [[]]

            psetop_to_cancel = self.find_psetop_to_cancel(in_psets, existing_psetops)
            
            # We are successfully cancelling the PSet Operation
            if None != psetop_to_cancel and (
                psetop_to_cancel.run_service("GET", "PSETOP_STATUS") == MCAPSetopModule.PSETOP_STATUS_DEFINED or
                psetop_to_cancel.run_service("GET", "PSETOP_STATUS") == MCAPSetopModule.PSETOP_STATUS_SCHEDULED):
                psetop_to_cancel.run_service("SET", "PSETOP_STATUS", MCAPSetopModule.PSETOP_STATUS_CANCELED)
                psetops_to_apply.append(psetop_to_cancel)
                output_lists.append([])
                a_lists.append([])
                self.run_component_service( MCALoggerComponent, "LOG", "EVENT",
                    MCASetOpLogger, "SETOP_CANCELED", 
                    psetop_to_cancel) 
            # There was no PSet Operation to cancel
            else:
                cancel_psetop.run_service("SET", "PSETOP_STATUS", MCAPSetopModule.PSETOP_STATUS_CANCELED)
                self.run_component_service( MCALoggerComponent, "LOG", "EVENT",
                    MCASetOpLogger, "SETOP_CANCELED", 
                    cancel_psetop)

            rc = self.apply_psetops(psetops_to_apply, output_lists, a_lists)
            if rc != DYNRM_MCA_SUCCESS:
                return rc
            
            return DYNRM_MCA_SUCCESS

        # See if we already have such a set operation, i.e. it's an update
        psetop = self.find_psetop_strict(   new_psetop.run_service("GET", "PSETOP_OP"), 
                                            new_psetop.run_service("GET", "INPUT"),
                                            existing_psetops)
        if None == psetop:
            # The PsetOp does not yet exist in the system
            psetop = new_psetop
        else:
            # This is an update: Just apply all col objects that were applied to new_psetop
            v_print("Updating Existing PSetOP "+psetop.run_service("GET", "GID"), 8, self.verbosity)
            cols = new_psetop.run_service("GET", "COL_OBJECTS")
            for col in cols:
                psetop.run_service("APPLY", "COL_OBJECT", col)

    
        rc =  self.insert_psetops([psetop])
        if rc != DYNRM_MCA_SUCCESS:
            return rc
        
        # LOG EVENT
        self.run_component_service( MCALoggerComponent, "LOG", "EVENT",
                        MCASetOpLogger, "SETOP_DEFINED", 
                        psetop)

        # APPLY SETOP IF IT DOES NOT REQUIRE RESOURCE SCHEDULING
        if (op == DYNRM_PSETOP_UNION or 
            op == DYNRM_PSETOP_SPLIT or
            op == DYNRM_PSETOP_DIFFERENCE):

            model = psetop.run_service("GET", "PSETOP_MODEL", "USER_MODEL")
            if None == model:
                model = psetop.run_service("GET", "PSETOP_MODEL", "DEFAULT_MODEL")

            o_lists, a_lists = model.run_service("GENERATE", "OUTPUT_SPACE", 
                                                            psetop, 
                                                            psetop.run_service("GET", "INPUT"),
                                                            None)

            rc = self.apply_psetops([psetop], [o_lists], [a_lists])
            if rc != DYNRM_MCA_SUCCESS:
                return rc
            rc = self.finalize_psetop(psetop.run_service("GET", "GID"))
            return rc
        rc = self.run_component_service(MCACallbackComponent, "BCAST", "EVENT", DYNRM_EVENT_PSETOP_DEFINED, self, psetop)
        if rc != DYNRM_MCA_SUCCESS:
            print("System Bcast event 'PSETOP_DEFINED' failed ", rc)
        return rc


    def insert_psetops(self, psetops):
        for psetop in psetops:
            if psetop.run_service("GET", "PSETOP_STATUS") != MCAPSetopModule.PSETOP_STATUS_ORDERED:
                psetop.run_service("SET", "PSETOP_STATUS", MCAPSetopModule.PSETOP_STATUS_DEFINED)
            pset = psetop.run_service("GET", "INPUT")[0]
            for graph in pset.run_service("GET", "GRAPHS"):
                if isinstance(graph, MCAPSetGraphModule):
                    psetop.run_service("SET", "GID", graph.run_service("GET", "NEW_GID"))
                    graph.run_service("ADD", "PSETOPS", [psetop])
        
        
        self.run_service("UPDATE", "GRAPH", psetops)
        return DYNRM_MCA_SUCCESS

    def apply_psetops(self, psetops, output_lists, adapted_objects_lists):
        adapted_objects = dict()
        
        adapted_statuses = {    MCAGraphObjectModule.STATUS_NEW, 
                                MCAGraphObjectModule.STATUS_ADD,
                                MCAGraphObjectModule.STATUS_UPDATE,
                                MCAGraphObjectModule.STATUS_DELETE
                            }
        

        # Todo: Add Psets, Membership Edge and Procs to Pset Graph
        # Todo: Go over vertices/edges in adapted objects and add all edges/vertices with NEW/UPDATE STATUS
                # -> Then throw it into graph update
        # Loop over all psetops
        for psetop, output_list, adapted_objects_list in zip(psetops, output_lists, adapted_objects_lists):
            sys_psetop = self.run_service("GET", "GRAPH_EDGE", psetop.run_service("GET", "GID"))

            # Get the pset graph for this psetop
            pset_graph = psetop.run_service("GET", "PSET_GRAPH")
            if None == pset_graph:
                return DYNRM_MCA_ERR_NOT_FOUND

            # Get the task graph for this psetop
            task_graph = pset_graph.run_service("GET", "TASK")
            if None == pset_graph:
                return DYNRM_MCA_ERR_NOT_FOUND
            
            # Assign GIDs for any new objects
            for object in adapted_objects_list:
                if object.run_service("GET", "GID") == MCAGraphObjectModule.GRAPH_OBJECT_DEFAULT_GID:
                    self._assign_subgid(pset_graph, task_graph, None, object)
            psetop.run_service("SET", "OUTPUT", output_list)
            if psetop.run_service("GET", "PSETOP_STATUS") == MCAPSetopModule.PSETOP_STATUS_DEFINED:
                psetop.run_service("SET", "PSETOP_STATUS", MCAPSetopModule.PSETOP_STATUS_PENDING)

            for output in output_list:
                output.run_service("ADD", "IN_EDGE", psetop)

            extended_adapted_objects = {o.run_service("GET", "GID"): o for o in adapted_objects_list}
            for object in adapted_objects_list:
                if isinstance(object, MCAVertexModule):
                    edges = object.run_service("GET", "EDGES")
                    for edge in edges:
                        if edge.run_service("GET", "STATUS") in adapted_statuses and \
                        edge.run_service("GET", "GID") not in extended_adapted_objects:

                            # Assign GIDs for any new objects
                            if edge.run_service("GET", "GID") == MCAGraphObjectModule.GRAPH_OBJECT_DEFAULT_GID:
                                self._assign_subgid(pset_graph, task_graph, None, edge)
                            extended_adapted_objects[edge.run_service("GET", "GID")] = edge
                elif isinstance(object, MCAEdgeModule):
                    vertices = object.run_service("GET", "INPUT") + object.run_service("GET", "OUTPUT")
                    for vertex in vertices:
                        if vertex.run_service("GET", "STATUS") in adapted_statuses and \
                        vertex.run_service("GET", "GID") not in extended_adapted_objects:
                            # Assign GIDs for any new objects
                            if vertex.run_service("GET", "GID") == MCAGraphObjectModule.GRAPH_OBJECT_DEFAULT_GID:
                                self._assign_subgid(pset_graph, task_graph, None, vertex)
                            extended_adapted_objects[vertex.run_service("GET", "GID")] = vertex

            # Update the pset graph for this psetop
            pset_graph_updates = []
            for gid in extended_adapted_objects.keys():
                object = extended_adapted_objects[gid]
                if isinstance(object, MCAPsetGraphObject):
                    pset_graph_updates.append(object)
            pset_graph.run_service("UPDATE", "GRAPH", pset_graph_updates, update_statuses = False)
            # Update the task graph for this psetop
            task_graph_updates = []
            for gid in extended_adapted_objects.keys():
                object = extended_adapted_objects[gid]

                if isinstance(object, MCATaskGraphObject):
                    task_graph_updates.append(object)
            task_graph.run_service("UPDATE", "GRAPH", task_graph_updates, update_statuses = False)

            adapted_objects.update(extended_adapted_objects)

        self.run_service("UPDATE", "GRAPH", list(adapted_objects.values()))


        # Log the new PSets
        new_psets = dict()
        for output in output_lists:
            for pset in output:
                if isinstance(pset, MCAPSetGraphModule):
                    continue
                new_psets[pset.run_service("GET", "GID")] = pset
        
        self.run_component_service( MCALoggerComponent, "LOG", "EVENTS",
                        MCASetLogger, "SET_DEFINED", 
                        new_psets.values())

        # Track dependencies between setops 
        for predecessor in psetops:
            if predecessor.run_service("GET", "PSETOP_STATUS") != MCAPSetopModule.PSETOP_STATUS_PENDING:
                continue
            input = predecessor.run_service("GET", "INPUT")
            input_nodes = [n.run_service("GET", "GID") for n in input[0].run_service("GET", "ACCESSED_NODES")]
            for successor in psetops:
                if predecessor.run_service("GET", "GID") == successor.run_service("GET", "GID"):
                    continue
                output = successor.run_service("GET", "OUTPUT")
                if len(output) == 0:
                    continue
                output_nodes = [n.run_service("GET", "GID") for n in output[len(output) - 1].run_service("GET", "ACCESSED_NODES")]
                if 0 != len([n for n in input_nodes if n in output_nodes]):
                    predecessor.run_service("EXTEND", "ATTRIBUTE_LIST", MCAPSetopModule.PSETOP_ATTRIBUTE_SUCCESSORS, [successor])
                    successor.run_service("EXTEND", "ATTRIBUTE_LIST", MCAPSetopModule.PSETOP_ATTRIBUTE_PREDECESSORS, [predecessor])
                    successor.run_service("SET", "PSETOP_STATUS", MCAPSetopModule.PSETOP_STATUS_SCHEDULED)


        self.run_component_service(MCALoggerComponent, "LOG", "EVENTS",
                        MCASetOpLogger, "SETOP_SCHEDULED", 
                        psetops) 
        
        psetops_to_execute = []
        for psetop in psetops:
            if psetop.run_service("GET", "PSETOP_STATUS") == MCAPSetopModule.PSETOP_STATUS_ORDERED:
                psetop.run_service("SET", "PSETOP_STATUS", MCAPSetopModule.PSETOP_STATUS_FINALIZED)
                self.run_component_service(MCALoggerComponent, "LOG", "EVENT",
                        MCASetOpLogger, "SETOP_FINALIZED", 
                        psetop)
                continue
                 
            # skip psetops with predecessors
            if len(psetop.run_service("GET", "ATTRIBUTE", MCAPSetopModule.PSETOP_ATTRIBUTE_PREDECESSORS)) > 0:
                continue

            psetops_to_execute.append(psetop)
            
        # LOG EVENT 'SETOP_EXECUTION_START'
        self.run_component_service( MCALoggerComponent, "LOG", "EVENTS",
                    MCASetOpLogger, "SETOP_EXECUTION_START", 
                    psetops_to_execute) 

        rc = self.apply_psetops_epilog(psetops_to_execute)
        if rc != DYNRM_MCA_SUCCESS:
            # If the system impleentation does not provide an epilog simply finalize the PSetOps
            if rc == DYNRM_ERR_NOT_IMPLEMENTED:
                for psetop in psetops_to_execute:
                    psetop.run_service("SET", "PSETOP_STATUS", MCAPSetopModule.PSETOP_STATUS_PENDING)
                
                self.run_component_service( MCALoggerComponent, "LOG", "EVENTS",
                    MCASetOpLogger, "SETOP_EXECUTION_START", psetops_to_execute)
                
                for psetop in psetops_to_execute:
                    self.finalize_psetop(psetop.run_service("GET", "GID"))
            else:
                v_print("apply_psetops_epilog failed with "+str(rc), 2, self.verbosity)
                return rc
        return DYNRM_MCA_SUCCESS


    def _assign_subgid(self, pset_graph, task_graph, topo_graph, object):

        if object.run_service("GET", "STATUS"):
            if isinstance(object, MCAPsetGraphObject):
                object.run_service("SET", "GID", pset_graph.run_service("GET", "NEW_GID"))
            elif isinstance(object, MCATaskGraphObject):
                object.run_service("SET", "GID", task_graph.run_service("GET", "NEW_GID"))
            elif isinstance(object, MCATopologyGraphObject):
                object.run_service("SET", "GID", topo_graph.run_service("GET", "NEW_GID"))
            else:
                object.run_service("SET", "GID", self.run_service("GET", "NEW_GID"))
        return DYNRM_MCA_SUCCESS

    def finalize_task(self, task_id):

        v_print("Finalizing task "+str(task_id), 2, self.verbosity)

        task = self.run_service("GET", "GRAPH_VERTEX", task_id)
        if None == task:
            return DYNRM_MCA_ERR_NOT_FOUND
        if task.run_service("GET", "TASK_STATUS") == MCATaskModule.TASK_STATUS_TERMINATED:
            return DYNRM_MCA_SUCCESS
        
        task.run_service("SET", "TASK_STATUS", MCATaskModule.TASK_STATUS_TERMINATED)

        task_graph = task.run_service("GET", "TASK_GRAPH")
        pset_graph = task_graph.run_service("GET", "PSETS")[0]

        # LOG TASK TERMINATION
        self.run_component_service( MCALoggerComponent, "LOG", "EVENT",
                MCATaskLogger, "TASK_TERMINATED", 
                task) 

        # Set Proc Statuses
        nodes = dict()
        procs = task.run_service("GET", "PROCS")
        for proc in procs:
            proc.run_service("SET", "PROC_STATUS", MCAProcModule.PROC_STATUS_TERMINATED)
            cores = proc.run_service("GET", "CORE_ACCESS")
            if len(cores) > 0:
                for core in cores:
                    node = core.run_service("GET", "NODE")
                    nodes[node.run_service("GET", "GID")] = node
                       
        # LOG NODES
        self.run_component_service( MCALoggerComponent, "LOG", "EVENTS",
                MCANodeLogger, "NODE_OCCUPATION_CHANGED", 
                list(nodes.values()))        

        # Finalize all outstanding setops
        psets = task.run_service("GET", "PSETS")
        for pset in psets:
            psetops = pset.run_service("GET", "EDGES_BY_FILTER", lambda e: isinstance(e, MCAPSetopModule))
            for psetop in psetops:
                status = psetop.run_service("GET", "PSETOP_STATUS")
                if  status != MCAPSetopModule.PSETOP_STATUS_CANCELED and\
                    status != MCAPSetopModule.PSETOP_STATUS_FINALIZED:
                
                    psetop.run_service("SET", "PSETOP_STATUS", MCAPSetopModule.PSETOP_STATUS_FINALIZED)
        

        # Start successor tasks
        ready_successors = dict()
        successors = task.run_service("GET", "SUCCESSOR_TASKS")
        for successor in successors:
            if successor.run_service("GET", "TASK_STATUS") != MCATaskModule.TASK_STATUS_WAITING:
                continue
            preds = successor.run_service("GET", "PREDECESSOR_TASKS")
            all_satisfied = True
            for pred in preds:
                if pred.run_service("GET", "TASK_STATUS") != MCATaskModule.TASK_STATUS_TERMINATED:
                    all_satisfied = False
                    break
            if all_satisfied:
                # This means the whole task graph has been completed
                if successor == task_graph:
                    task_graph.run_service("SET", "TASK_STATUS", MCATaskModule.TASK_STATUS_TERMINATED)
                else:
                    ready_successors[successor.run_service("GET", "GID")] = successor
        
        new_psetops = []
        for successor in ready_successors.values():
            successor.run_service("SET", "TASK_STATUS", MCATaskModule.TASK_STATUS_READY)

            # create an ADD PSet operation and assign the launch_ouput_generator
            psetop = pset_graph.run_service("CREATE", "PSETOP", DYNRM_PSETOP_ADD, [pset_graph])
            psetop_model = MCALaunchPsetopModel()
            psetop_model.run_service("SET", "OUTPUT_SPACE_GENERATOR", successor.run_service("GET", "TASK_LAUNCH_OUTPUT_SPACE_GENERATOR"))
            psetop.run_service("ADD", "PSETOP_MODEL", "USER_MODEL", psetop_model)

            new_psetops.append(psetop)

        if len(new_psetops) > 0:
            self.add_psetops(new_psetops)
            self.run_component_service( MCALoggerComponent, "LOG", "EVENTS",
                    MCASetOpLogger, "SETOP_DEFINED", 
                    new_psetops)

        # Tell everyone about the task termination
        rc = self.run_component_service(MCACallbackComponent, "BCAST", "EVENT", DYNRM_EVENT_TASK_TERMINATED, self, task)
        if rc != DYNRM_MCA_SUCCESS:
            print("System Bcast event 'PSETOP_DEFINED' failed ", rc)
        
        return rc

    def finalize_psetop(self, psetop_id):

        psetop = self.run_service("GET", "GRAPH_EDGE", psetop_id)
        if None == psetop:
            return DYNRM_MCA_ERR_BAD_PARAM
        
        status = psetop.run_service("GET", "PSETOP_STATUS")
        op = psetop.run_service("GET", "PSETOP_OP")
        if status == MCAPSetopModule.PSETOP_STATUS_FINALIZED:
            return DYNRM_MCA_SUCCESS 

        # LOG SETOP FINALIZED EVENT
        self.run_component_service( MCALoggerComponent, "LOG", "EVENT",
                MCASetOpLogger, "SETOP_FINALIZED", 
                psetop)

        psetop.run_service("SET", "PSETOP_STATUS", MCAPSetopModule.PSETOP_STATUS_FINALIZED)
        
        # If it was just a cancelation there is nothing further to do
        if status == MCAPSetopModule.PSETOP_STATUS_CANCELED or op == DYNRM_PSETOP_CANCEL:
            return DYNRM_MCA_SUCCESS

        psets = psetop.run_service("GET", "OUTPUT")
        task = psetop.run_service("GET", "TASK") 

        
        # LOG EVENTS
        if psetop.run_service("GET", "PSETOP_OP") == DYNRM_PSETOP_SUB:
            sub_pset = psetop.run_service("GET", "INPUT")[0]
            psets = [sub_pset]
            
            # LOG NODE EVENTS
            self.run_component_service( MCALoggerComponent, "LOG", "EVENTS",
                    MCANodeLogger, "NODE_OCCUPATION_CHANGED", 
                    sub_pset.run_service("GET", "ACCESSED_NODES"))  

        elif  psetop.run_service("GET", "PSETOP_OP") == DYNRM_PSETOP_ADD and \
            psetop.run_service("GET", "INPUT")[0].run_service("GET", "NAME") == "":
            launch_pset = psetop.run_service("GET", "OUTPUT")[0]
            
            # LOG TASK STARTED
            self.run_component_service( MCALoggerComponent, "LOG", "EVENT",
                    MCATaskLogger, "TASK_STARTED", 
                    task)

            # LOG NODE EVENT
            self.run_component_service( MCALoggerComponent, "LOG", "EVENTS",
                        MCANodeLogger, "NODE_OCCUPATION_CHANGED", 
                        launch_pset.run_service("GET", "ACCESSED_NODES"))      

        else:
            print("Log nodes ", len(psetop.run_service("GET", "OUTPUT")))
            nodes = {n.run_service("GET", "NAME") : n for n in psetop.run_service("GET", "OUTPUT")[0].run_service("GET", "ACCESSED_NODES")}
            print("Nodes")
            if len(psetop.run_service("GET", "OUTPUT")) > 0:
                print("If : ", len(psetop.run_service("GET", "OUTPUT")))
                for pset in psetop.run_service("GET", "OUTPUT")[1:-1]:
                    nodes.update({n.run_service("GET", "NAME") : n for n in pset.run_service("GET", "ACCESSED_NODES")})

            if 0 < len(nodes):
                # LOG NODE EVENT
                self.run_component_service( MCALoggerComponent, "LOG", "EVENTS",
                        MCANodeLogger, "NODE_OCCUPATION_CHANGED", 
                        list(nodes.values()))

        print("update procs")
        # Update proc statuses
        for pset in psets:
            procs = pset.run_service("GET", "PROCS")
            for proc in procs:
                if proc.run_service("GET", "PROC_STATUS") == MCAProcModule.PROC_STATUS_LAUNCH_REQUESTED:
                   proc.run_service("SET", "PROC_STATUS", MCAProcModule.PROC_STATUS_RUNNING) 
                elif proc.run_service("GET", "PROC_STATUS") == MCAProcModule.PROC_STATUS_TERMINATION_REQUESTED:
                   proc.run_service("SET", "PROC_STATUS", MCAProcModule.PROC_STATUS_TERMINATED)
        
        # Bcast the Finalization to everyone who's interestd
        rc = self.run_component_service(MCACallbackComponent, "BCAST", "EVENT", 
                                        DYNRM_EVENT_PSETOP_FINALIZED, self, psetop)
        if rc != DYNRM_MCA_SUCCESS:
            print("System Bcast event 'PSETOP_FINALIZED' failed ", rc)
            return rc

        # Finally check if successors can be applied
        successors = psetop.run_service("GET", "ATTRIBUTE", MCAPSetopModule.PSETOP_ATTRIBUTE_SUCCESSORS)
        ready_successors = []
        for successor in successors:
            if successor.run_service("GET", "PSETOP_STATUS") != MCAPSetopModule.PSETOP_STATUS_SCHEDULED:
                continue
            successor.run_service("SHRINK", "ATTRIBUTE_LIST", MCAPSetopModule.PSETOP_ATTRIBUTE_PREDECESSORS, [psetop])
            if len(successor.run_service("GET", "ATTRIBUTE", MCAPSetopModule.PSETOP_ATTRIBUTE_PREDECESSORS)) == 0:
                ready_successors.append(successor)
                # LOG SETOP EXECUTION START
                self.run_component_service( MCALoggerComponent, "LOG", "EVENT",
                        MCASetOpLogger, "SETOP_EXECUTION_START", 
                        successor)

        print("Run seccessor epilog")
        # Run the system-specific implementation for applying successor PSetOPs
        rc = self.apply_psetops_epilog(ready_successors)
        if rc != DYNRM_MCA_SUCCESS:
            if rc == DYNRM_ERR_NOT_IMPLEMENTED:
                for successor in successors:
                    if successor.run_service("GET", "PSETOP_STATUS") == MCAPSetopModule.PSETOP_STATUS_SCHEDULED:
                        self.finalize_psetop(successor.run_service("GET", "GID"))
            else:
                print("apply_psetops_epilog failed with ", rc)
                return rc

        print("Check term")
        # Check if all procs in task terminated, if so terminate task
        pset_graph = psetop.run_service("GET", "PSET_GRAPH")
        procs = pset_graph.run_service("GET", "GRAPH_VERTICES_BY_FILTER", 
                                       lambda x : isinstance(x, MCAProcModule))
        proc_running = False
        for proc in procs:
            if proc.run_service("GET", "PROC_STATUS") != MCAProcModule.PROC_STATUS_TERMINATED:
                proc_running = True
                break
        
        if not proc_running:
            rc = self.finalize_task(task.run_service("GET", "GID"))
            if rc != DYNRM_MCA_SUCCESS:
                return rc
            
        return DYNRM_MCA_SUCCESS

    def print_system(self):
        print("=============================")
        print("=========== SYSTEM ==========")
        print("=============================")

        topo_graph = self.run_service("GET", "TOPOLOGY_GRAPH")
        if None == topo_graph:
            print("===== NO TOPOLOGY GRAPH =====")
        else:
            topo_graph.run_service("PRINT", "TOPOLOGY_GRAPH")
            
        pset_graphs = self.run_service("GET", "PSET_GRAPHS")
        for pset_graph in pset_graphs:
            task_graph = pset_graph.run_service("GET", "TASK")
            task_graph.run_service("PRINT", "TASK_GRAPH")
            pset_graph.run_service("PRINT", "PSET_GRAPH")


        print("=============================")
        print("=============================")
        print("=============================")

        return DYNRM_MCA_SUCCESS


    @abstractmethod
    def set_topology_graph_epilog(self, topo_graph, params = {}):
        return DYNRM_ERR_NOT_IMPLEMENTED

    @abstractmethod
    def register_callbacks_func(self, conn_name):
        
        info = "Callback of Conncetion "+str(conn_name) 

        # PSETOP DEFINED
        cbfunc = partial(self.run_component_service, MCAEventLoopComponent, "RUN", "FUNC_NB", "MAIN_LOOP", 
                         partial(self.report_error_cbfunc, func=self.default_psetop_defined_cbfunc, info=info), None, 
                         self.default_psetop_defined_cbfunc)        
        rc = self.run_component_service(
            MCACallbackComponent, "REGISTER", "CONNECTION_CALLBACK", conn_name, 
            DYNRM_EVENT_PSETOP_DEFINED, cbfunc)
        if rc != DYNRM_MCA_SUCCESS:
            return rc

        # PSETOP FINALIZED
        cbfunc = partial(self.run_component_service, MCAEventLoopComponent, "RUN", "FUNC_NB", "MAIN_LOOP", 
                         partial(self.report_error_cbfunc, func=self.default_psetop_finalized_cbfunc, info=info), None, 
                         self.default_psetop_finalized_cbfunc)
        rc = self.run_component_service(
            MCACallbackComponent, "REGISTER", "CONNECTION_CALLBACK", conn_name, 
            DYNRM_EVENT_PSETOP_FINALIZED, cbfunc)
        if rc != DYNRM_MCA_SUCCESS:
            return rc

        # TASK TERMINATED
        #cbfunc = partial(self.run_component_service, MCAEventLoopComponent, "RUN", "FUNC_NB", "MAIN_LOOP", 
        #                 partial(self.report_error_cbfunc, func=self.default_task_finalized_cbfunc, info=info), None, 
        #                 self.default_task_finalized_cbfunc)
        #rc = self.run_component_service(
        #    MCACallbackComponent, "REGISTER", "CONNECTION_CALLBACK", conn_name, 
        #    DYNRM_EVENT_TASK_TERMINATED, cbfunc)
        #if rc != DYNRM_MCA_SUCCESS:
        #    return rc

        return DYNRM_MCA_SUCCESS
    
    @abstractmethod
    def apply_psetops_epilog(self, psetops):
        return DYNRM_ERR_NOT_IMPLEMENTED    



    def find_psetop_strict(self, op, input, psetops):
        for _psetop in psetops:
            # Not the same op
            if _psetop.run_service("GET", "PSETOP_OP") != op:
                continue

            # Different number of Input PSets => Must be a different setop
            existing_input = _psetop.run_service("GET", "INPUT")
            if len(existing_input) != len(input):
                continue

            diff = 0
            for name in input:
                if name not in [s.run_service("GET", "GID") for s in existing_input]:
                    diff = 1 
                    break
            
            # Input PSets are not the same
            if diff > 0:
                continue

            # Only look for active set operations
            if  (_psetop.run_service("GET", "PSETOP_STATUS") != MCAPSetopModule.PSETOP_STATUS_DEFINED and
                _psetop.run_service("GET", "PSETOP_STATUS") != MCAPSetopModule.PSETOP_STATUS_SCHEDULED):
                continue
            
            # We found the set operation
            return _psetop
        return None

    def find_psetop_to_cancel(self, input_psets, psetops):
        for _psetop in psetops:
            diff = 0
            existing_input = _psetop.run_service("GET", "INPUT")
            for name in [pset.run_service("GET", "GID") for pset in input_psets]:
                if name not in [s.run_service("GET", "GID") for s in existing_input]:
                    diff = 1 
                    break
            
            # Input PSets are not the same
            if diff > 0:
                continue

            # Only look for active set operations
            if  (_psetop.run_service("GET", "PSETOP_STATUS") != MCAPSetopModule.PSETOP_STATUS_DEFINED and
                _psetop.run_service("GET", "PSETOP_STATUS") != MCAPSetopModule.PSETOP_STATUS_SCHEDULED):
                continue
            
            # We found the set operation
            return _psetop
        return None
    
    def default_psetop_finalized_cbfunc(self, conn_name, event_name, psetop_id):
        return self.finalize_psetop(psetop_id)
 
    def default_task_finalized_cbfunc(self, conn_name, event_name, task_id):
        return self.finalize_task(task_id)
        
    def default_psetop_defined_cbfunc(self, conn_name, event_name, op, input, col):
        v_print("default_psetop_defined_cbfunc for "+str(input), 11, self.verbosity)
        psets = [self.run_service("GET", "GRAPH_VERTEX", name) for name in input]
        if None in psets:
            print("Not all psets defined: "+str(input))
            return DYNRM_MCA_ERR_NOT_FOUND
        psetop = MCAPSetopModule("new_op", op, psets)
        psetop.run_service("APPLY", "COL_OBJECT", col)
        return self.add_psetop(psetop)
    
    def report_error_cbfunc(self, rc, func, info = "", cbdata = None):
        if rc != DYNRM_MCA_SUCCESS:
            v_print("Function "+str(func)+" failed with error "+str(rc)+"! Additional Info: "+info, 2, self.verbosity)

    def add_core(self, core):
        hw_graph = self.run_component_service(MCAGraphComponent, "GET", "GRAPH", self._get_topology_graph_name())
        return hw_graph.run_service("UPDATE", "GRAPH", [core])

    def add_node(self, node):
        hw_graph = self.run_component_service(MCAGraphComponent, "GET", "GRAPH", self._get_topology_graph_name())
        return hw_graph.run_service("UPDATE", "GRAPH", [node])

    def add_cores(self, cores):
        hw_graph = self.run_component_service(MCAGraphComponent, "GET", "GRAPH", self._get_topology_graph_name())
        return hw_graph.run_service("UPDATE", "GRAPH", cores)

    def add_nodes(self, nodes):
        hw_graph = self.run_component_service(MCAGraphComponent, "GET", "GRAPH", self._get_topology_graph_name())
        return hw_graph.run_service("UPDATE", "GRAPH", nodes)


    def get_core_ids(self):
        hw_graph = self.run_component_service(MCAGraphComponent, "GET", "GRAPH", self._get_topology_graph_name())
        if None == hw_graph:
            return []
        cores = hw_graph.run_service("GET", "GRAPH_VERTICES_BY_FILTER", lambda x: isinstance(x, MCANodeModule))
        return [c.run_service("GET", "GID") for c in cores]

    def get_node_ids(self):
        hw_graph = self.run_component_service(MCAGraphComponent, "GET", "GRAPH", self._get_topology_graph_name())
        if None == hw_graph:
            return []
        nodes = hw_graph.run_service("GET", "GRAPH_VERTICES_BY_FILTER", lambda x: isinstance(x, MCANodeModule))
        return [n.run_service("GET", "GID") for n in nodes]

    def get_core(self, id):
        hw_graph = self.run_component_service(MCAGraphComponent, "GET", "GRAPH", self._get_topology_graph_name())
        if None == hw_graph:
            return None
        return hw_graph.run_service("GET", "GRAPH_VERTEX", id)

    def get_node(self, id):
        hw_graph = self.run_component_service(MCAGraphComponent, "GET", "GRAPH", self._get_topology_graph_name())
        if None == hw_graph:
            return []
        return hw_graph.run_service("GET", "GRAPH_VERTEX", id)


    def get_cores(self):
        hw_graph = self.run_component_service(MCAGraphComponent, "GET", "GRAPH", self._get_topology_graph_name())
        if None == hw_graph:
            return []
        return hw_graph.run_service("GET", "GRAPH_VERTICES_BY_FILTER", lambda x: isinstance(x, MCACoreModule))

    def get_nodes(self):
        hw_graph = self.run_component_service(MCAGraphComponent, "GET", "GRAPH", self._get_topology_graph_name())
        if None == hw_graph:
            return []
        return hw_graph.run_service("GET", "GRAPH_VERTICES_BY_FILTER", lambda x: isinstance(x, MCANodeModule))

    def get_node(self, id):
        return self.run_service("GET", "GRAPH_VERTEX", id)

    def get_node(self, id):
        return self.run_service("GET", "GRAPH_VERTEX", id)

    def remove_core(self, id):
        core = self.run_service("GET", "GRAPH_VERTEX", id)
        core.run_service("SET", "STATUS", MCAVertexModule.MCA_VERTEX_STATUS_INVALID)
        return self.run_service("UPDATE", "GRAPH", [core])

    def remove_node(self, id):
        node = self.run_service("GET", "GRAPH_VERTEX", id)
        node.run_service("SET", "STATUS", MCAVertexModule.MCA_VERTEX_STATUS_INVALID)
        return self.run_service("UPDATE", "GRAPH", [node])


