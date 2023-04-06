This folder contains the edited versions of each fcl file used in the chain for the full detector simulation. 

# $\nu_\tau$ Simulation
The chain given through these files goes:
1. genie\_edits.fcl
2. genie\_dune\_edit.fcl
3. prodgenie\_common\_dunefd\_edit.fcl
4. prodgenie\_nu\_dune10kt\_edit.fcl
5. prodgenie\_nutau\_dune10kt\_edit.fcl 

with the final file being the one used to initiate the GENIE simulation. 
Main edits were made to genie\_edits.fcl to change the EventGeneratorList parameter to only generate pdg code = 16.

# $\nu_\mu$ Simulation
The chain given through these files goes:
1. genie\_edits.fcl
2. genie\_dune\_edits.fcl
3. prodgenie\_common\_dunefd\_edit.fcl
4. prodgenie\_nu\_dune10kt\_edit.fcl

with the final file being the one used to initiate the GENIE simulation. Main edits were made to genie\_edits.fcl to change the EventGeneratorList paramter to only generate pdg code = 14.

# $\nu\_e$ Simulation
The chain given through these files goes:
1. genie\_elect\_edits.fcl
2. genie\_dune\_elect\_edit.fcl
3. prodgenie\_common\_dunefd\_elect\_edit.fcl
4. prodgenie\_nu\_dune10kt\_elect\_edit.fcl
5. prodgenie\_nue\_dune10kt.fcl

with the final file being the one used to initiate the GENIE simulation. Main edits were made to genie\_elect\_edits.fcl to change the EventGeneratorList parameter to only generate pdg code = 12.
