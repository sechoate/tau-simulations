# Tau neutrino simulations 
This is documentation for running $\nu_\tau$ simulations using both stand alone Genie or the full detector simulation. 

## Stand alone genie 
This process will produce the initial particle interaction and those intial decay products. Our goal is just to produce $\nu_\tau$ CC events so we expect to see a $\tau^-$ as a product from the initial interaction and then the decay products of that $\tau^-$, which can be found in the PDG with their associated probabilities.

### Command for running
In general, the command for running genie is:  

gevgen -n *number of events* -p *pdg of interacting particle* -t *pdg for target nucleus* -e *neutrino energy* -f *flux file* --cross-sections *cross section file* --event-generator-list "*type of events you want to generate*"  

In the specific case of generating $\nu_\tau$ CC events, the command becomes the following: 

gevgen -n *number of events* -p 16 -t 1000180400 -e 0,100 -f
/path/to/file/flux_dune_neutrino_FD.root,nutau_fluxosc --cross-sections /path/to/file/gxspl-FNALsmall.xml --event-generator-list "CC"  

where 16 is the PDG code for the $\nu_\tau$ and 1000180400 is the PDG for the argon nucleus. It is possible to run without the flux file and cross section file, however it takes longer because then Genie has to calculate the flux and cross section for each event. The flux and cross section files for $\nu_\tau$, $\nu_\mu$, and $\nu_e$ are included in this repository for completeness. The final component is the event-generator-list where CC corresponds to generating exclusively CC events. 

### Running for muon neutrino or electron neutrino for comparison 
The command would be the same to run for $\nu_\mu$ or $\nu_e$ CC interactions as it was for running $\nu_\tau$ CC interactions with three changes. The first change is for the pdg. For $\nu_\mu$ it is -p 14 and for $\nu_e$ it is -p 11. The second change is to the flux file, rather than using the $\nu_\tau$ flux file it should be replaced with the appropriate $\nu_\mu$ or $\nu_e$ flux file. The final change is for the cross section file which also should be replaced with the appropriate $\nu_\mu$ or $\nu_e$ file. 

### Generating a workable root file 
The root file that is initally generated does not necessarily include all the information required for analysis of the simulation, it should be called something like gntp.0.gst.root. The type of file that is more likely to be useful is a rootracker format. The way to convert the file is through the command:  

gntpc -i *input filename* -f rootracker  

This will produce a file which is called something like gntp.0.gtrac.root which is more appropriate for analysis. 

## Full detector simulation
In order to produce a full simulation, there are three steps. First the intial interactions are created using Genie, then the resulting particles are propagated through Geant allowing more interactions than just the intial ones, and finally the detector geometry and effects are added with detsim. These steps are all accomplished using various fcl files.  

### FCL files
This stands for Fermilab Hierarchical Configuration Language (FHiCL). These are files which contain information like particle types and detector geometry. They can be edited in order to utilize specific types of geometry or specific interaction types. In order to check what parameters are being applied to the simulation, the command fhicl-dump name.fcl can be used. This will print out all the information used in the fcl file without having to go through every included fcl file. For this project, it was necessary to edit fcl files as by default they produce both NC and CC events. This was problematic since CC events are much less likely than NC events, so the amount of events that would have needed to be generated in order to get a reasonable about of CC events was too much. These edited fcl files are included in this repository. 


### Genie step
Running the genie simulation is conceptually the same as running stand alone Genie except here we use larsoft rather than geven. In order to run Genie, a fcl file is required. Again, this can be a default fcl file or one that has been edited. For this project, we used an edited file.  



 
