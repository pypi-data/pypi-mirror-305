# Time-X EuroHPC project: Dynamic Resource Manager

This repo contains the source code of DynRM: a modular, Python-based dynamic resource manager to be used with the [Time-X dynamic MPI Extensions](https://gitlab.inria.fr/dynres/dyn-procs/ompi). DynRM supports the [DPP design principles for dynamic resource management](https://arxiv.org/abs/2403.17107).


## DynRM System Representation
DynRM uses a graph-based system Representation:
* **Topology Graph:** The topology graph contains system components (such as nodes, cores, ...) as vertices and relations between components (such as containment) as edges.
When only considering containment relations, the topology graph is a tree.
* **Task Graphs:** The Task Graphs represent user submissions, i.e. a set of one or more jobs/tasks (vertices) possibly with dependencies (edges). This representation therefore also covers workflows.
* **PSet Graphs:** The PSet Graphs consists of Process Sets (vertices) and Process Set Operations (edges). The PSet Graphs establish a mapping between the Task Graphs and the Topology Graph and is the basis of the DPP-based approach for dynamic resources. 

## DynRM Modular Design
DynRM uses a modular design inpired by the Modular Component Architecture (MCA) used in the Open-MPI, OpenPMIx and PRRTE projects:

**List of Modules**:
* Resource Manager: Provides resource mananagement functions
    * Base
* Callback: Provides functions for callback/rpc mechanisms
    * Base
    * PMIx
* Event Loop: Provides functions for Managing Event Loops
    * Base
    * Asyncio
* Logger: Provides functions for logging events
    * Node
    * SetOp
    * Set
    * Task
    * Policy
* Submission: Provides functions for submitting jobs and job mixes
    * Base
    * ElastiSim
* System: Provides functions for interacting with system management software
    * PRRTE
    * ElastiSim
* TopologyCreation: Provides functions for creating a topology graph from a certain representation
    * Default
    * ElastiSim
* TaskGraphCreation: Provides funtions for converting submissions to task graphs
    * Default
    * ElastiSim
* Policy: Provides a scheduling policy 
    * DiscreteSteepestAscend
    * EasyBackfilling
    * FirstFitFirst
    * DMRPolicy
* Graph/Vertex/Edge: Provides functions for managing graphs/vertices/edges
    * Base
* VertexModel: Provides Models for Vertices
    * PSetModel: Provides Models for Psets
        * Amdahl
        * Linear
        * Constant
        * InverseAmdahl
* EdgeModel: Provides Models for Edges
    * PSetOpModel: Provides Models for PsetOps
        * ADD
        * SUB
        * GROW
        * SHRINK
        * REPLACE
        * LAUNCH
        * SUB
        * TERMINATION
        * UNION
        * DIFFERENCE
        * INTERSECTION


## Installation

### Installation using `pip`
We provide regular releases of this package.
Dynamic Resources require changes in the whole system software stack.
Thus, changes in our 
[dynamic MPI Extensions](https://gitlab.inria.fr/dynres/dyn-procs/ompi),
[dynamic PMIx Extensions](https://gitlab.inria.fr/dynres/dyn-procs/openpmix) and
[dynamic PRRTE Extensions](https://gitlab.inria.fr/dynres/dyn-procs/prrte)
might break compatibility with the dynamic resource manager.
We give our best to provide up to date releases and version information.
However, to be on the save site we recommend to manually install the package (see below)
and run it with the most recent versions of our dynamic extensions.

If you want to use pip for the installation run:

```
pip install dyn_rm
```
### (Recommended) Manual Installation
To ensure compatibility with our dynamic MPI, PMIx and PRRTE Extensions it is recommended 
to use a manual installation. This version is tested with the corresponding most recent versions
of the dynamic extensions.

* Clone this repository:
```
git clone https://gitlab.inria.fr/dynres/dyn-procs/dyn_rm
```
* Then, from this directory run:
```
python3 setup.py install --user
```

### Installation with Spack
coming soon ...

## Running the resource manager
To run the resource manager, it first needs to be composed using the provided modules.
The examples directory provides some ready to use scripts.
A description of the basic steps is provided below:
* Create a Resource Manager instance:
```
resource_manager = MCAResourceManagerModule()
```
* Add a system module, for some topology description using a TopologyGraphCreation module:
```
resource_manager.run_service("ADD", "SYSTEM", "my_system", PrrteSystem, DefaultTopologyGraphCreationModule, topology_file)
```

* Add a policy module:
```
resource_manager.run_service("ADD", "POLICY", "my_policy", EasyBackfilling)
```

* Submit a job representation to be run on the registered systen using a particular submission module:
```
resource_manager.run_service("SUBMIT", "OBJECT", "my_system", DefaultSubmissionModule, submission_file)
```

## Contact:
domi.huber@tum.de