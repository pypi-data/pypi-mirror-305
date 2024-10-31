from dyn_rm.mca.base.system.module.process_manager import MCAProcessManagerModule
from dyn_rm.mca.base.system.module.topology.node import MCANodeModule
from dyn_rm.mca.callback.modules.pmix import PmixCallbackModule
from dyn_rm.util.constants import *
from dyn_rm.util.functions import v_print

from abc import abstractmethod
import time
import os

class PrrteProcessManagerModule(MCAProcessManagerModule):

    def __init__(self, parent = None, parent_dir = ".", verbosity = 0, enable_output = False):
        super().__init__(parent = parent, parent_dir = parent_dir, verbosity = verbosity, enable_output = enable_output)
        self._info["PRRTE_VERSION"] = "5"
        self._pterm_option = ""

    
    @abstractmethod
    def launch_process_manager_function(self, topo_graph, params):
        timeout = 30
        filename = None
        suffix = str(time.time())
        if None != filename:
            filename = os.path.join(self.tmpdir, "pid_"+suffix)
        else:
            filename = os.path.join(os.getcwd(), "pid_"+suffix)
        
        nodes = topo_graph.run_service("GET", "TOPOLOGY_OBJECTS", MCANodeModule)

        if len(nodes) < 1:
            return DYNRM_MCA_ERR_BAD_PARAM
        hosts = ",".join([n.run_service("GET", "NAME")+":"+str(n.run_service("GET", "NUM_CORES"))for n in nodes])
        
        ssh_agent = ""
        ssh_params = ""
        if 'ssh_agent' in params:
            ssh_agent = '--mca plm_ssh_agent '+params['ssh_agent']
        if 'ssh_params' in params:
            ssh_params = '--mca plm_ssh_args '+params['ssh_params']
        #--mca ras timex
        # Start PRRTE
        if self.verbosity > 9:
            cmd = "prte "+ ssh_agent +" "+ssh_params+" --report-pid "+filename+" --debug-daemons \
                --leave-session-attached --mca odls_base_verbose 10 \
                --mca state_base_verbose 10 --prtemca pmix_server_verbose 10 \
                --mca prte_data_server_verbose 100 --mca prte_setop_server_verbose 100 \
                --mca pmix_base_verbose 10 --mca pmix_server_spawn_verbose 100 \
                --mca pmix_client_spawn_verbose 100 --mca pmix_server_base_verbose 100 \
                --mca ras_base_verbose 100 --mca plm_base_verbose 100 \
                --host "+hosts+" \
                > " +topo_graph.run_service("GET", "NAME").replace("/","-")+".out 2>&1 &"
        else:
            cmd = "prte "+ ssh_agent +" "+ssh_params+" --report-pid "+filename+" --daemonize --mca ras timex --host "+hosts+" > /dev/null 2>&1 &"
        v_print(cmd, 9, self.verbosity)
        os.system(cmd)
        start = time.time()
        v_print("Waiting for PID in file "+filename, 20, self.verbosity)
        # get the pid of the PRRTE Master
        pid = -1
        while pid < 0:
            if time.time() - start > timeout:
                raise Exception("PRRTE startup timed out!") 
            
            try:
                pid = int(open(filename, 'r').readlines()[0])
                v_print("PRRTE PID is "+str(pid), 20, self.verbosity)

                conn_info = dict()
                conn_info[DYNRM_PARAM_CONN_MODULE] = PmixCallbackModule
                conn_info[DYNRM_PARAM_CONN_PARAMS] = dict()
                conn_info[DYNRM_PARAM_CONN_PARAMS][DYNRM_PARAM_CONN_PID] = pid
                self._info[DYNRM_PARAM_CONN_INFO].append(conn_info)
                self._pterm_option = "--pid "+str(pid)
            except FileNotFoundError:
                time.sleep(0.1)
                v_print("File not found, try again in 0.1 seconds ", 20, self.verbosity)
        try: 
            if os.path.exists(filename):
                os.remove(filename)
        except FileNotFoundError:
            pass
        except Exception:
            v_print("PrrteProcessManagerModule: Failed to remove pid file: "+str(filename), 5, self.verbosity)
            pass   

        return DYNRM_MCA_SUCCESS

    @abstractmethod
    def terminate_process_manager_function(self):
        os.system("pterm "+self._pterm_option)
        return DYNRM_MCA_SUCCESS