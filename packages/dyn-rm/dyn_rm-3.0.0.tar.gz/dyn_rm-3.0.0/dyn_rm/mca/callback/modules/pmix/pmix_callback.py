from dyn_rm.mca.base.callback.component import MCACallbackComponent
from dyn_rm.mca.base.callback.module import MCACallbackModule
from dyn_rm.mca.base.system.module import MCAPSetopModule, MCAProcModule, MCAColObjectv1
from dyn_rm.mca.system.modules.psets.col_creation import PmixColObjectCreationModule
from dyn_rm.util.constants import *
from dyn_rm.util.functions import *

from pmix import *
from functools import partial

# TODO: Remove after finishing debugging
import os

orig_l_paths = os.environ['LIBRARY_PATH'].split(os.pathsep)
orig_ld_paths = os.environ['LD_LIBRARY_PATH'].split(os.pathsep)
orig_incl_paths = os.environ['C_INCLUDE_PATH'].split(os.pathsep)

try:
    orig_l_paths.remove("/opt/hpc/install/openpmix_noasan/lib")
    orig_ld_paths.remove("/opt/hpc/install/openpmix_noasan/lib")
    orig_incl_paths.remove("/opt/hpc/install/openpmix_noasan/include")
except:
    pass

os.environ['LIBRARY_PATH'] = os.pathsep.join(orig_l_paths)
os.environ['LD_LIBRARY_PATH'] = os.pathsep.join(orig_ld_paths)
os.environ['C_INCLUDE_PATH'] = os.pathsep.join(orig_incl_paths)

class PmixCallbackModule(MCACallbackModule):

    PMIX_EVENT_PSETOP_DEFINED       =       PMIX_EXTERNAL_ERR_BASE - 1
    PMIX_EVENT_PSETOP_GRANTED       =       PMIX_EXTERNAL_ERR_BASE - 2
    PMIX_EVENT_PSETOP_CANCELED      =       PMIX_EXTERNAL_ERR_BASE - 3
    PMIX_EVENT_PSETOP_FINALIZED     =       PMIX_PSETOP_FINALIZED
    
    SERVER_FUNCS = [DYNRM_EVENT_PSETOP_DEFINED]

    def __init__(self, parent = None, parent_dir = ".", verbosity = 0, enable_output = False):
        super().__init__(parent = parent, parent_dir = parent_dir, verbosity = verbosity, enable_output = enable_output)
        self.connections_my_peer = dict()
        self.connections_my_procid = dict()
        self.connections_params = dict()
        self.local_reqs = dict()
        self.aliases = dict()
        self.tool = PMIxTool()
        self.col_obj_creator = PmixColObjectCreationModule()
        self.active_conn = None
        rc, self.proc_id = self.tool.init(
            [
                {'key' : PMIX_TOOL_DO_NOT_CONNECT, 'value' : True, 'val_type' : PMIX_BOOL},
                {'key' : PMIX_TOOL_NSPACE, 'value' : 'DYN_RM', 'val_type' : PMIX_STRING},
                {'key' : PMIX_TOOL_RANK, 'value' : 0, 'val_type' : PMIX_PROC_RANK},
                {'key' : PMIX_SERVER_SCHEDULER, 'value' : True, 'val_type': PMIX_BOOL}
            ]
        )
        if rc != PMIX_SUCCESS:
            raise Exception("pmix_tool_init returned ", rc)
        
        # Register our suported server functions
        rc = self.tool.set_server_module({"allocate" : partial(self._psetop_defined_proxy, self=self)})
        if rc != PMIX_SUCCESS:
            raise PMIx_Error(rc, "PMIx_set_server_module")
        
    # simply call PMIx's connect to server function
    def request_connection_function(self, conn_name, mypeer, peer, params):
        
        info = []
        for key in params.keys():
            if DYNRM_PARAM_CONN_PID == key:
                info.append(
                    {'key' : PMIX_SERVER_PIDINFO, 'value' : params[key], 'val_type' : PMIX_PID}
                )
            if DYNRM_PARAM_CONN_TCP == key:
                info.append(
                    {'key' : PMIX_TCP_URI, 'value' : params[key], 'val_type' : PMIX_STRING}
                )
            elif DYNRM_PARAM_CONN_SCHEDULER == key:
                info.append(
                    {'key' : PMIX_SERVER_SCHEDULER, 'value' : True, 'val_type' : PMIX_BOOL}
                )

        rc, myprocid, server = self.tool.attach_to_server(info)
        if rc != PMIX_SUCCESS:
            return DYNRM_MCA_ERR_NOT_FOUND

        self.connections_my_peer[conn_name] = mypeer
        self.connections_my_procid[conn_name] = myprocid
        
        self.add_connection(conn_name, server, params)

        return DYNRM_MCA_SUCCESS

    # We accept all connection so just add it
    def accept_connection_function(self, conn_name, peer, params):
        self.add_connection(conn_name, peer, params)
        return DYNRM_MCA_SUCCESS
    
    # We accept all connection terminations so just remove it
    def accept_connection_termination_function(self, conn_name):
        return self.remove_connection(conn_name)


    # We register PMIx callbacks or server callbacks
    #   a) For DynRM events / cmds we register proxy callbacks
    #   b) For unknown events we just register the provided PMIx callback   
    def register_callback_function(self, conn_name, event_name, callback):
        # Set our PMIx Server to the Proc Master of this connection
        rc = self._activate_connection(conn_name)
        if rc != DYNRM_MCA_SUCCESS:
            return rc
        if event_name in PmixCallbackModule.SERVER_FUNCS:
            return self.add_callback(conn_name, event_name, callback)
        if event_name == DYNRM_EVENT_PSETOP_FINALIZED:
                event = PmixCallbackModule.PMIX_EVENT_PSETOP_FINALIZED 
                pmix_cb = partial(self._psetop_finalized_proxy, callback = callback, conn_name = conn_name, event_name = event_name, self = self)
        elif event_name == DYNRM_EVENT_TASK_TERMINATED:
            event = PMIX_EVENT_JOB_END
            pmix_cb = partial(self._task_terminated_proxy, callback = callback, conn_name = conn_name, event_name = event_name, self = self)
        else:
            event = event_name
            pmix_cb = callback
        print("Register event for peer "+str(self.get_peer(conn_name)))
        rc, id = self.tool.register_event_handler(  [int(event)], 
                                                    [
                                                      {'key' : PMIX_EVENT_CUSTOM_RANGE, 'value' : self.get_peer(conn_name), 'val_type' : PMIX_PROC}
                                                    ], 
                                                    pmix_cb)
        if rc != PMIX_SUCCESS:
            raise PMIx_Error(rc, "PMIx_Register_event_handler")
        return self.add_callback(conn_name, event_name, callback)
    
    # We call send:
    #   a) proxies for well-known DYNRM EVENTS/CMDS
    #   b) PMIx Notification for unknown EVENTS/CMDS  
    def send_event_function(self, conn_name, event_name, *args, **kwargs):
        
        # Not yet implemented
        if event_name in [
                            DYNRM_EVENT_PSETOP_FINALIZED,
                            DYNRM_EVENT_PSETOP_DEFINED,
                            DYNRM_EVENT_TASK_TERMINATED
                        ]:
            return DYNRM_SUCCESS
        
        # Set our PMIx Server to the Proc Master of this connection
        rc = self._activate_connection(conn_name)
        if rc != DYNRM_MCA_SUCCESS:
            return rc

        # We either spawn or send an alloc request response
        if event_name == DYNRM_CMD_PSETOP_APPLY:
            return self._psetop_apply_cmd_proxy(*args)
        else:
            if len(args) != 1:
                return DYNRM_MCA_SUCCESS
            myprocid = self.connections_my_procid.get(conn_name)
            if None == myprocid:
                return DYNRM_MCA_ERR_BAD_PARAM
            rc = self.tool.notify_event(event_name, myprocid, PMIX_RANGE_RM, *args)
            if rc != PMIX_SUCCESS:
                return DYNRM_MCA_ERR_BAD_PARAM
        return DYNRM_MCA_SUCCESS

    # simply call PMIx_Tool_disconnect function
    def terminate_connection_function(self, conn_name):
        peer = self.get_peer(conn_name)
        rc = self.tool.disconnect(peer)
        if rc != PMIX_SUCCESS:
            return DYNRM_MCA_ERR_NO_PERM
        return DYNRM_MCA_SUCCESS

    def _activate_connection(self, conn_name):
        if self.active_conn != conn_name:
            rc = self.tool.set_server(self.get_peer(conn_name), [])
            if rc != PMIX_SUCCESS:
                raise PMIx_Error(rc, "PMIx_set_server")
            self.active_conn = conn_name
        return DYNRM_MCA_SUCCESS

    # CALLBACK PROXIES
    # Proxy functions to convert a PMIx message to the parameters expected by the DynRM Callback
    @staticmethod
    def _psetop_defined_proxy(args, cbfunc, cbdata, self=None):
        event_name = DYNRM_EVENT_PSETOP_DEFINED

        directive = args['action']
        # We only support set operations
        if directive != PMIX_ALLOC_SETOP:
            v_print("Received alloc request with wrong directive "+str(directive), 11, self.verbosity)
            cbfunc(PMIX_ERR_NOT_SUPPORTED, [], cbdata)
            return PMIX_SUCCESS

        v_print("Received alloc request "+str(args), 11, self.verbosity)

        # Find all callbacks registered for this event and peer 
        callbacks = dict()
        for conn_name in self.connections.keys():
            peer = self.get_peer(conn_name)
            if peer == args['source'] and event_name in self.connections[conn_name]["CALLBACKS"]:
                callbacks[conn_name] = self.connections[conn_name]["CALLBACKS"][event_name]

        if 0 == len(callbacks):
            v_print("Received alloc request but now callbacks are registed for this peer", 11, self.verbosity)
            cbfunc(PMIX_ERR_NOT_SUPPORTED, [], cbdata)
            return PMIX_SUCCESS            
     
        op = None
        input = []
        obj = []
        for info in args['directives']:
            v_print("Check info Key "+str(info['key']), 11, self.verbosity)
            if info['key'] == PMIX_PSETOP_TYPE.decode("utf-8"):
                op = PmixCallbackModule._pmix_dynrm_convert_psetop(info['value'])
            elif info['key'] == PMIX_PSETOP_INPUT.decode("utf-8"):
                input = info['value'].split(',')
            elif info['key'] == PMIX_PSETOP_COL.decode("utf-8"):
                obj = info['value']['array']

        # Set Operation is not fully specified
        if None == op or 0 == len(input):
            v_print("ERROR RECEIVED INCOMPLETE SETOP", 11, self.verbosity)
            cbfunc(PMIX_ERR_BAD_PARAM, [], cbdata)
            return PMIX_SUCCESS

        col_object = MCAColObjectv1()
        try:
            self.col_obj_creator.run_service("CREATE", "COL_OBJECT", col_object, obj, {})
        except:
            v_print("ERROR creating COL object for input "+str(input)+" and obj "+str(obj) , 11, self.verbosity)
            cbfunc(PMIX_ERR_BAD_PARAM, [], cbdata)
            return PMIX_SUCCESS
        col_object.psetop_attributes_add[MCACallbackComponent.ATTRIBUTE_PSETOP_CBFUNC] = cbfunc
        col_object.psetop_attributes_add[MCACallbackComponent.ATTRIBUTE_PSETOP_CBDATA] = cbdata

        for conn_name in callbacks:
            print("Calling psetop_defined callback of conection "+str(conn_name))
            rc = callbacks[conn_name](conn_name, event_name, op, input, col_object)
            if rc != DYNRM_MCA_SUCCESS:
                return PMIX_ERR_INTERNAL
        
        return PMIX_SUCCESS  
    
    @staticmethod
    def _task_terminated_proxy(callback, conn_name, event_name, evhdlr, status, source, info, results, self=None):
        event_task_id = None
        print("TASK finalized proxy source vs. conn ", str(source), " - ", str(self.get_peer(conn_name)))
        for item in info:
            if item['key'] == PMIX_EVENT_AFFECTED_PROC.decode("utf-8"):
                task_id = item['value']['nspace']
        if None == task_id:
            return PMIX_ERR_BAD_PARAM, []
        else:
            return callback(conn_name, event_name, task_id)

    @staticmethod
    def _psetop_finalized_proxy(evhdlr, status, source, info, results, callback = None, conn_name = None, event_name = None,  self=None):
        setopid = None
        peer = self.get_peer(conn_name)
        print("PSETOP finalized proxy source vs. conn ", str(source), " - ", str(self.get_peer(conn_name))+ " : "+str(info))
        if source['nspace'] != peer['nspace'] or source['rank'] != peer['rank']:
            return PMIX_SUCCESS, []
        print("PSETOP finalized proxy source vs. conn ", str(source), " - ", str(self.get_peer(conn_name)))
        for item in info:
            if item['key'] == PMIX_ALLOC_ID.decode("utf-8"):
                setopid = item['value']

        if None == setopid:
            return PMIX_ERR_BAD_PARAM, []
        
        rc = callback(conn_name, event_name, setopid)
        if rc != DYNRM_MCA_SUCCESS:
            return PMIX_ERR_BAD_PARAM, []
        
        return PMIX_SUCCESS, []

    # SEND PROXIES
    # Proxy functions to convert a DYNRM EVENT/CMD to a PMIx notification/server_callback
    def _psetop_apply_cmd_proxy(self, psetop):
        # PMIx_Spawn
        if  psetop.run_service("GET", "PSETOP_OP") == DYNRM_PSETOP_ADD and \
            psetop.run_service("GET", "INPUT")[0].run_service("GET", "NAME") == "":

            job_infos, apps, task, hosts = self._get_spawn_params(psetop)
            
            v_print("Launching Task "+task.run_service("GET", "NAME")+ " on hosts "+hosts+ "with info "+str(job_infos)+ " and apps "+str(apps), 11, self.verbosity)
            rc, jobid = self.tool.spawn(job_infos, apps)
            if rc != PMIX_SUCCESS:
                v_print("Launch of Task "+task.run_service("GET", "NAME")+" failed with "+str(rc), 11, self.verbosity)
                return DYNRM_MCA_ERR_BAD_PARAM
            v_print("Launch of Task "+task.run_service("GET", "NAME")+" successful", 11, self.verbosity)

        # PMIx_Allocation_request callback
        else:
            v_print("Send PSetop Apply cmd for setop "+psetop.run_service("GET", "GID"), 11, self.verbosity)
            rc, info, cbfunc, cbdata = self._get_alloc_resp_params(psetop)
            v_print("Cbfunc = "+str(cbfunc)+ " for PSet Op "+psetop.run_service("GET", "GID")+" "+str(psetop.run_service("GET", "ATTRIBUTES")), 11, self.verbosity)
            v_print("Calling cbfunc with status "+str(rc), 11, self.verbosity)
            cbfunc(rc, info, cbdata)
        
        return DYNRM_MCA_SUCCESS 

    def _get_spawn_params(self, psetop):
        psetop_id = psetop.run_service("GET", "GID")
        launch_pset = psetop.run_service("GET", "OUTPUT")[0]
        num_procs = launch_pset.run_service("GET", "NUM_PROCS")
        hosts = ",".join([n.run_service("GET", "NAME")+":"+str(n.run_service("GET", "NUM_CORES")) for n in launch_pset.run_service("GET", "ACCESSED_NODES")])
        task = launch_pset.run_service("GET", "TASK")
        executable = task.run_service("GET", "TASK_EXECUTABLE")
        arguments = task.run_service("GET", "TASK_EXECUTION_ARGUMENTS")
        hdict_add = dict()
        for proc in launch_pset.run_service("GET", "PROCS"):
            host = proc.run_service("GET", "CORE_ACCESS")[0].run_service("GET", "NODE").run_service("GET", "NAME")
            if host not in hdict_add:
                hdict_add[host] = dict()
            hdict_add[host][proc] = proc
        ppr = str(len(next(iter(hdict_add.values()))))+":node"
        expand = None != psetop.run_service("GET", "ATTRIBUTE", DYNRM_CMD_PM_EXPAND)

        #env = []    
        #env.append(options[i + 1]+"="+str(os.environ.get(options[i + 1])))
        
        job_infos = []
        job_infos.append({'key': PMIX_NOTIFY_JOB_EVENTS, 'flags': 0, 'value': True, 'val_type': PMIX_BOOL})
        job_infos.append({'key': PMIX_SETUP_APP_ENVARS, 'flags': 0, 'value': True, 'val_type': PMIX_BOOL})
        job_infos.append({'key': PMIX_FWD_STDOUT, 'flags': 0, 'value': True, 'val_type': PMIX_BOOL})
        job_infos.append({'key': PMIX_PERSONALITY, 'flags': 0, 'value': 'ompi', 'val_type': PMIX_STRING})
        job_infos.append({'key': PMIX_PSET_NAME, 'flags' : 0, 'value': launch_pset.run_service("GET", "GID"), 'val_type': PMIX_STRING})
        job_infos.append({'key': PMIX_PPR, 'flags': 0, 'value': ppr, 'val_type': PMIX_STRING})
        job_infos.append({'key': PMIX_RANKBY, 'flags': 0, 'value': "slot", 'val_type': PMIX_STRING})
        job_infos.append({'key': PMIX_REQUESTOR_IS_TOOL, 'flags' : 0, 'value' : True, 'val_type' : PMIX_BOOL})
        job_infos.append({'key': PMIX_PSETOP_ID, 'flag': 0, 'value': psetop_id, 'val_type': PMIX_STRING})
        if self.verbosity > 5:
            job_infos.append({'key': PMIX_DISPLAY_MAP, 'flags': 0, 'value': True, 'val_type': PMIX_BOOL})
        #job_infos.append({'key': PMIX_NSPACE, 'flags' : 0, 'value': task.run_service("GET", "GID"), 'val_type': PMIX_STRING})
        app = dict()
        app['maxprocs'] = num_procs
        app['cmd'] = executable
        #app['env'] = en
        app['argv'] = arguments
        app['info'] = []
        if expand:
            app['info'].append({'key': PMIX_ADD_HOST, 'flags': 0, 'value': hosts, 'val_type': PMIX_STRING})
        app['info'].append({'key': PMIX_HOST, 'flags': 0, 'value': hosts, 'val_type': PMIX_STRING})
        app['info'].append({'key': PMIX_SETUP_APP_ENVARS, 'flags': 0, 'value': True, 'val_type': PMIX_BOOL})

        return job_infos, [app], task, hosts

    def _get_alloc_resp_params(self, psetop):
        cbfunc = psetop.run_service("GET", "ATTRIBUTE", MCACallbackComponent.ATTRIBUTE_PSETOP_CBFUNC)
        cbdata = psetop.run_service("GET", "ATTRIBUTE", MCACallbackComponent.ATTRIBUTE_PSETOP_CBDATA)
        if psetop.run_service("GET", "PSETOP_STATUS") == MCAPSetopModule.PSETOP_STATUS_CANCELED:
            return PMIX_ERR_ALLOC_CANCELED, [], cbfunc, cbdata

        hdict_add = dict()
        hdict_sub = dict()
        for pset in psetop.run_service("GET", "OUTPUT"):
            if 0 == pset.run_service("GET", "NUM_PROCS"):
                continue
            for proc in pset.run_service("GET", "PROCS"):
                if proc.run_service("GET", "PROC_STATUS") == MCAProcModule.PROC_STATUS_LAUNCH_REQUESTED:
                    host = proc.run_service("GET", "CORE_ACCESS")[0].run_service("GET", "NODE").run_service("GET", "NAME")
                    if host not in hdict_add:
                        hdict_add[host] = dict()
                    hdict_add[host][proc] = proc
                elif proc.run_service("GET", "PROC_STATUS") == MCAProcModule.PROC_STATUS_TERMINATION_REQUESTED:
                    host = proc.run_service("GET", "CORE_ACCESS")[0].run_service("GET", "NODE").run_service("GET", "NAME")
                    if host not in hdict_sub:
                        hdict_sub[host] = dict()
                    hdict_sub[host][proc] = proc
        hosts_add = ",".join(hdict_add.keys())
        ppr_add = ",".join([str(len(val)) for val in hdict_add.values()])
        num_add = sum([len(val) for val in hdict_add.values()])
        
        hosts_sub = ",".join(hdict_sub.keys())
        ppr_sub = ",".join([str(len(val)) for val in hdict_sub.values()])
        num_sub = sum([len(val) for val in hdict_sub.values()])
        output = ",".join([s.run_service("GET", "GID") if s.run_service("GET", "NAME") != '' else '' for s in psetop.run_service("GET", "OUTPUT")])
        alloc_id = psetop.run_service("GET", "GID")

        info = []
        info.append({'key': PMIX_ALLOC_ID, 'value': alloc_id, 'val_type': PMIX_STRING})
        info.append({'key': PMIX_NODE_LIST, 'value': hosts_add, 'val_type': PMIX_STRING})
        info.append({'key': PMIX_NODE_LIST_SUB, 'value': hosts_sub, 'val_type': PMIX_STRING})
        info.append({'key': PMIX_PPR, 'value': ppr_add, 'val_type': PMIX_STRING})
        info.append({'key': PMIX_PPR_SUB, 'value': ppr_sub, 'val_type': PMIX_STRING})
        info.append({'key': PMIX_PSETOP_OUTPUT, 'value': output, 'val_type': PMIX_STRING})
        info.append({'key': 'mpi_num_procs_add', 'value': str(num_add), 'val_type': PMIX_STRING})
        info.append({'key': 'mpi_num_procs_sub', 'value': str(num_sub), 'val_type': PMIX_STRING})

        return PMIX_SUCCESS, info, cbfunc, cbdata


    def _pmix_dynrm_convert_psetop(op):
        if op == PMIX_PSETOP_NULL:
            return DYNRM_PSETOP_NULL
        elif op == PMIX_PSETOP_ADD:
            return DYNRM_PSETOP_ADD
        elif op == PMIX_PSETOP_SUB:
            return DYNRM_PSETOP_SUB
        elif op == PMIX_PSETOP_GROW:
            return DYNRM_PSETOP_GROW
        elif op == PMIX_PSETOP_SHRINK:
            return DYNRM_PSETOP_SHRINK
        elif op == PMIX_PSETOP_REPLACE:
            return DYNRM_PSETOP_REPLACE
        elif op == PMIX_PSETOP_SPLIT:
            return DYNRM_PSETOP_SPLIT
        elif op == PMIX_PSETOP_UNION:
            return DYNRM_PSETOP_UNION
        elif op == PMIX_PSETOP_DIFFERENCE:
            return DYNRM_PSETOP_DIFFERENCE
        elif op == PMIX_PSETOP_INTERSECTION:
            return DYNRM_PSETOP_INTERSECTION
        elif op == PMIX_PSETOP_CANCEL:
            return DYNRM_PSETOP_CANCEL
        else:
            return DYNRM_PSETOP_NULL

    class PMIx_Error(Exception):
        def __init__(self, error_code, pmix_function):
            message = "PMIx function '"+pmix_function+"' returned error code: "+str(error_code)
            super().__init__(message)