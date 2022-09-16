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
where 16 is the PDG code for the $\nu_\tau$ and 1000180400 is the PDG for the argon nucleus. It is possible to run without the flux file and cross section file, however it takes longer because then Genie has to calculate the flux and cross section for each event. 

### Running for muon neutrino or electron neutrino for comparison 
The command would be the same to run for $\nu_\mu$ or $\nu_e$ CC interactions as it was for running $\nu_\tau$ CC interactions with three changes. The first change is for the pdg. For $\nu_\mu$ it is -p 14 and for $\nu_e$ it is -p 11




 
