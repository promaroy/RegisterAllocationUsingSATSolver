## This repository contains the implementation for Register Allocation via graph coloring method using SAT Solver Zchaff.

* Step 1:
  The graph constructed from registerData.py is stored in graphdata.txt.
  
* Step 2:
  The graph2cnf.py file converts the graph from graphdata.txt to cnf format and graphdata.cnf file is created in zchaff folder.
  
* Step 3:
  The graphdata.cnf file is then fed into zchaff SAT solver to check whether the number of registers are sufficient for the variables i.e. whether 
  the graph is satisfiable.
  
#### Zchaff is added here as a zip folder.


  

