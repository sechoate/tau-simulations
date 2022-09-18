# Tau neutrino simulations 
This is documentation for running $\nu_\tau$ simulations using both stand alone Genie or the full detector simulation. Written documentation is found in the pdf. The following are some possibly useful references. 




## Full detector simulation
In order to produce a full simulation, there are three steps. First the intial interactions are created using Genie, then the resulting particles are propagated through Geant allowing more interactions than just the intial ones, and finally the detector geometry and effects are added with detsim. These steps are all accomplished using various fcl files and the lar command. Full help and additional features not discussed here for the lar command can be found using lar -h in terminal. General instructions on running a simulation can be found at https://wiki.dunescience.org/wiki/DUNE_Computing/Getting_Started_Tutorial#Run_Simulation_and_Reconstruction

### FCL files
This stands for Fermilab Hierarchical Configuration Language (FHiCL). These are files which contain information like particle types and detector geometry. They can be edited in order to utilize specific types of geometry or specific interaction types. In order to check what parameters are being applied to the simulation, the command fhicl-dump name.fcl can be used. This will print out all the information used in the fcl file without having to go through every included fcl file. For this project, it was necessary to edit fcl files as by default they produce both NC and CC events. This was problematic since CC events are much less likely than NC events, so the amount of events that would have needed to be generated in order to get a reasonable about of CC events was too much. These edited fcl files are included in this repository. 


### Genie step
Running the genie simulation is conceptually the same as running stand alone Genie except here we use larsoft rather than geven. In order to run Genie, a fcl file is required. Again, this can be a default fcl file or one that has been edited. For this project, we used an edited file. The command in general is  

lar -n *number of events* -c name-of-fcl-file.fcl  

This will generate a file with the naming scheme name-of-fcl-file-used_gen.root.

### G4 step
Once the inital events and interactions have been created with Genie, they are propagated using Geant. An additional fcl files is required to run this step  

standard_g4_dune10kt.fcl 

which will not be edited. 



 
