This folder contains the edited versions of each fcl file used in the chain for the full detector simulation. When working with a FCL file on a Fermilab machine using cvmfs, the command *fhicl-dump file_name.fcl* can be used on the final file in the FCL file chain to show what properties from the previous FCL files have been applied. 

# $\nu_\tau$ Simulation
The chain given through these files goes:
1. genie\_edits.fcl
2. genie\_dune\_edit.fcl
3. prodgenie\_common\_dunefd\_edit.fcl
4. prodgenie\_nu\_dune10kt\_edit.fcl
5. prodgenie\_nutau\_dune10kt\_edit.fcl 

with the final file being the one used to initiate the GENIE simulation. 
Main edits were made to genie\_edits.fcl to change the EventGeneratorList parameter to only generate CC events. The same pararmeter needs to be changed in genie\_dune\_edit.fcl. The other parameter that needs to be changed in both of these files is the GenFlavors parameter which needs to be changed to 16 to match the PDG code for $\nu_\tau$.

# $\nu_\mu$ Simulation
The chain given through these files goes:
1. genie\_edits.fcl
2. genie\_dune\_edits.fcl
3. prodgenie\_common\_dunefd\_edit.fcl
4. prodgenie\_nu\_dune10kt\_edit.fcl

with the final file being the one used to initiate the GENIE simulation. Main edits were made to genie\_edits.fcl and genie\_dune\_edits.fcl to change the EventGeneratorList paramter to only generate CC events and the GenFlavors parameter needs to be changed to 14 to match the PDG code for $\nu_\mu$.

# $\nu\_e$ Simulation
The chain given through these files goes:
1. genie\_elect\_edits.fcl
2. genie\_dune\_elect\_edit.fcl
3. prodgenie\_common\_dunefd\_elect\_edit.fcl
4. prodgenie\_nu\_dune10kt\_elect\_edit.fcl
5. prodgenie\_nue\_dune10kt.fcl

with the final file being the one used to initiate the GENIE simulation. Main edits were made to genie\_elect\_edits.fcl and genie\_dune\_elect\_edit.fcl to change the EventGeneratorList parameter to only generate CC events and the GenFlavors parameter needs to be changed to 12 to match the PDG code for $\nu\_e$.
