from dyn_rm.mca.base.callback.component import MCACallbackComponent
from dyn_rm.mca.callback.modules.pmix import PmixCallbackModule
from dyn_rm.mca.base.system.module import MCASystemModule
from dyn_rm.mca.base.event_loop.component import MCAEventLoopComponent
from dyn_rm.mca.base.event_loop.module import MCAEventLoopModule
from dyn_rm.mca.base.system.module.topology.node import MCANodeModule
from pmix import *
from functools import partial
from dyn_rm.util.constants import *
import os

PMIX_PSETOP_EXTERNAL        =       128

PMIX_EVENT_PSETOP_DEFINED   =       PMIX_EXTERNAL_ERR_BASE - 1
PMIX_EVENT_PSETOP_GRANTED   =       PMIX_EXTERNAL_ERR_BASE - 2
PMIX_EVENT_PSETOP_CANCELED  =       PMIX_EXTERNAL_ERR_BASE - 3
PMIX_EVENT_PSETOP_EXECUTED  =       PMIX_PSETOP_FINALIZED

class OARSystem(MCASystemModule):
    def __init__(self, parent = None, parent_dir = ".", verbosity = 0, enable_output = False):
        super().__init__(parent = parent, parent_dir = parent_dir, verbosity = verbosity, enable_output = enable_output)

        # Initialize the PMIx Tool library
        self.tool = PMIxTool()
        # Register the PMIx Callback Module. We use it later to interact with PRRTE
        self.get_component(MCACallbackComponent).register_module(PmixCallbackModule())
    
    # Start PRRTE, connect to it as PMIx Tool and register our callbacks 
    def _set_system_topology(self, topo_graph):
        # Add it to the base system
        rc = super()._set_system_topology(topo_graph)
        if rc != DYNRM_MCA_SUCCESS:
            return rc
        
        # Create a host list from the topology graph
        nodes = topo_graph.run_service("GET", "TOPOLOGY_OBJECTS", MCANodeModule)
        if len(nodes) < 1:
            return DYNRM_MCA_ERR_BAD_PARAM
        hosts = ",".join([n.run_service("GET", "NAME")+":"+str(n.run_service("GET", "NUM_CORES"))for n in nodes])
        
        # Launch PRRTE
        pid_file = "pid.txt"
        cmd = "prte --report-pid "+pid_file+" --daemonize --mca ras timex --host "+hosts+" > /dev/null 2>&1 &"
        os.system(cmd)
        os.sleep(10)

        try:
            pid = int(open(pid_file, 'r').readlines()[0])
            self.run_service("SET", "ATTRIBUTE", "PRRTE_PID", pid)

            # Request a connection to the PRRTE Master (PMIx Server) via the PMIxCallbackModule using the pid
            rc = self.run_component_service(MCACallbackComponent, "REQUEST", "CONNECTION", PmixCallbackModule, "PRRTE_MASTER", self.get_pmix_tool(), None, {"pid" : pid})
            if rc != DYNRM_MCA_SUCCESS:
                print("request connetion failed")
                return rc

            # register the callbacks for events sent by PRRTE MASTER
            rc = self.register_callbacks()
            if rc != DYNRM_MCA_SUCCESS:
                print("register callbacks failed")
                return rc
        except FileNotFoundError:
            print("PRRTE STARTUP failed")
            return DYNRM_MCA_ERR_NOT_FOUND
        
        try: 
            if os.path.exists(pid_file):
                os.remove(pid_file)
        except Exception:
            pass
        return DYNRM_MCA_SUCCESS

    # Registers the PMIx callbacks
    def register_callbacks(self):
        # PSET DEFINED
        rc = self.run_component_service(
            MCACallbackComponent, "REGISTER", "CONNECTION_CALLBACK", "PRRTE_MASTER", 
            PMIX_PROCESS_SET_DEFINE, partial(OARSystem.set_defined_evhandler, self=self))
        if rc != DYNRM_MCA_SUCCESS:
            return rc
        
        # PSETOP DEFINED
        rc = self.run_component_service(
            MCACallbackComponent, "REGISTER", "CONNECTION_CALLBACK", "PRRTE_MASTER", 
            PMIX_EVENT_PSETOP_DEFINED, partial(OARSystem.psetop_defined_evhandler, self=self))
        if rc != DYNRM_MCA_SUCCESS:
            return rc

        # PSETOP FINALIZED
        rc = self.run_component_service(
            MCACallbackComponent, "REGISTER", "CONNECTION_CALLBACK", "PRRTE_MASTER", 
            PMIX_EVENT_PSETOP_EXECUTED, partial(OARSystem.psetop_finalized_evhandler, self=self))
        if rc != DYNRM_MCA_SUCCESS:
            return rc

        # TASK TERMINATED
        rc = self.run_component_service(
            MCACallbackComponent, "REGISTER", "CONNECTION_CALLBACK", "PRRTE_MASTER", 
            PMIX_EVENT_JOB_END, partial(OARSystem.task_terminated_evhandler, self=self))
        if rc != DYNRM_MCA_SUCCESS:
            return rc

        return DYNRM_MCA_SUCCESS  

    # PMIx callback functions
    @staticmethod
    def task_terminated_evhandler(evhdlr, status, source, info, results, self=None):
        
        alias = None
        for item in info:
            if item['key'] == PMIX_EVENT_AFFECTED_PROC.decode("utf-8"):
                alias = item['value']['nspace']

        if None == alias:
            return
        
        #task_id = self._pmix_aliases.get(alias)
        task_id = alias

        if None == task_id:
            return PMIX_ERR_BAD_PARAM, []

        rc = self.run_component_service(MCAEventLoopComponent, "RUN", "FUNC_NB", "MAIN_LOOP", 
                                       self.null_cbfunc, None, 
                                       self._finalize_task, task_id)
        if rc != DYNRM_MCA_SUCCESS:
            return PMIX_ERR_BAD_PARAM, []
        
        return PMIX_SUCCESS, []

    @staticmethod
    def psetop_finalized_evhandler(evhdlr, status, source, info, results, self=None):
        alias = None
        for item in info:
            if item['key'] == PMIX_ALLOC_ID.decode("utf-8"):
                alias = item['value']
        if None == alias:
                return PMIX_ERR_BAD_PARAM, []
        
        setopid = self._pmix_aliases.get(alias)

        if None == setopid:
            return DYNRM_MCA_ERR_NOT_FOUND, []
        
        rc = self.run_component_service(MCAEventLoopComponent, "RUN", "FUNC_NB", "MAIN_LOOP", 
                                       self.null_cbfunc, None, 
                                       self._finalize_psetop, setopid)
        if rc != DYNRM_MCA_SUCCESS:
            return PMIX_ERR_BAD_PARAM, []
        
        return PMIX_SUCCESS, []
    
    @staticmethod
    def set_defined_evhandler(evhdlr, status, source, info, results, self=None):
        pset_name = None
        members = None
        for item in info:

            if item['key'] == PMIX_PSET_NAME.decode("utf-8"):
                pset_name = item['value']
            elif item['key'] == PMIX_PSET_MEMBERS.decode("utf-8"):
                members = item['value']['array']
        return PMIX_SUCCESS, []
    
    @staticmethod 
    def psetop_defined_evhandler(evhdlr, status, source, event_infos, results, self=None):
        
        id = op = input = None
        for event_info in event_infos:
            if event_info['key'] == "prte.alloc.reservation_number":
                id = event_info['value']
            elif event_info['key'] == "prte.alloc.client":
                jobid = event_info['value']['nspace'] 
            elif event_info['key'] == "mpi.rc_op_handle":
                for info in event_info['value']['array']:
                    if info['key'] == "pmix.psetop.type":
                        op = info['value']
                    if info['key'] == "mpi.op_info":
                        for mpi_op_info in info['value']['array']:
                            if mpi_op_info['key'] == "mpi.op_info.input":
                                input = mpi_op_info['value'].split(',')
                            elif mpi_op_info['key'] == "mpi.op_info.output":
                                output = mpi_op_info['value'].split(',')
                            elif mpi_op_info['key'] == "mpi.op_info.info":
                                op_info = mpi_op_info['value']['array']
        
        # Create a pset operation. Need to run it in the system Main Loop
        if op != None and input != None:
            rc = self.run_component_service(MCAEventLoopComponent, "RUN", "FUNC_NB", "MAIN_LOOP", 
                                       self.null_cbfunc, None, 
                                       self._define_new_psetop, id, self._pmix_dynrm_convert_psetop(op), input, op_info)
        return PMIX_SUCCESS, []


    ######## These functions need to be implemented for oar to react to the events ######
    # A pset operation has been applied
    def _finalize_psetop(self, psetop_id):
        pass

    # A task terminated
    def _finalize_task(self, task_id):
        pass

    # A new psetop has been defined
    def _define_new_psetop(self, id, op, input, op_info):
        pass

    ####### These functions can be used by oar to interact with PRRTE
    def _launch_job(self, pset_name, procs_per_node, hosts, num_procs, executable, arguments):
        job_infos = []
        job_infos.append({'key': PMIX_NOTIFY_COMPLETION, 'flags': 0, 'value': True, 'val_type': PMIX_BOOL})
        job_infos.append({'key': PMIX_SETUP_APP_ENVARS, 'flags': 0, 'value': True, 'val_type': PMIX_BOOL})
        job_infos.append({'key': PMIX_PERSONALITY, 'flags': 0, 'value': 'ompi', 'val_type': PMIX_STRING})
        job_infos.append({'key': PMIX_PSET_NAME, 'flags' : 0, 'value': pset_name, 'val_type': PMIX_STRING})
        job_infos.append({'key': PMIX_PPR, 'flags': 0, 'value': procs_per_node, 'val_type': PMIX_STRING})
        job_infos.append({'key': PMIX_RANKBY, 'flags': 0, 'value': "slot", 'val_type': PMIX_STRING})
        app = dict()
        app['maxprocs'] = num_procs
        app['cmd'] = executable
        app['argv'] = arguments
        app['info'] = []
        app['info'].append({'key': PMIX_HOST, 'flags': 0, 'value': hosts, 'val_type': PMIX_STRING})
        app['info'].append({'key': PMIX_SETUP_APP_ENVARS, 'flags': 0, 'value': True, 'val_type': PMIX_BOOL})
        # PMIx_Spawn
        rc, jobid = self.tool.spawn(job_infos, [app])
        if rc != PMIX_SUCCESS:
            return DYNRM_MCA_ERR_BAD_PARAM
        return DYNRM_MCA_SUCCESS

    def _apply_setop(self, id, hosts_add, hosts_sub, ppr_add, ppr_sub, output, num_add, num_sub, canceled):
        info = []
        info.append({'key': 'SETOP_ID', 'value': id, 'val_type': PMIX_SIZE})
        info.append({'key': PMIX_NODE_LIST, 'value': hosts_add, 'val_type': PMIX_STRING})
        info.append({'key': PMIX_NODE_LIST_SUB, 'value': hosts_sub, 'val_type': PMIX_STRING})
        info.append({'key': PMIX_PPR, 'value': ppr_add, 'val_type': PMIX_STRING})
        info.append({'key': PMIX_PPR_SUB, 'value': ppr_sub, 'val_type': PMIX_STRING})
        info.append({'key': PMIX_PSETOP_OUTPUT, 'value': output, 'val_type': PMIX_STRING})
        info.append({'key': 'mpi_num_procs_add', 'value': str(num_add), 'val_type': PMIX_STRING})
        info.append({'key': 'mpi_num_procs_sub', 'value': str(num_sub), 'val_type': PMIX_STRING})
        
        if canceled:
            info.append({'key': 'PMIX_PSETOP_CANCELED', 'value' : True, 'val_type': PMIX_BOOL})
        
        return self.run_component_service(MCACallbackComponent, "SEND", "EVENT", "PRRTE_MASTER", PMIX_EVENT_PSETOP_GRANTED, info)


    # This shuts down the OAR system module and terminates the PRRTE instance
    def mca_shutdown(self):
        pid = self.run_service("GET", "ATTRIBUTE", "PID")
        if None != pid:
            os.system("pterm --pid "+str(pid))

        return self.mca_default_shutdown()        