#!/bin/bash

#due to memory constraints, simulation needed to be run in pieces rather than all at once
#this code automates that process beginning with generating the Genie file then moving through the geant, detsim, and reco steps in pieces

#genie
lar -n 50 -c prodgenie_nutau_dune10kt.fcl &&


#geant
lar -n 10 -c standard_g4_dune10kt.fcl prodgenie_nutau_dune10kt_gen.root -o prodgenie_nutau_dune10kt_10_gen_g4.root &&
for i in {11..50..10};
do
	lar -n 10 -e 1:0:${i} -c standard_g4_dune10kt.fcl prodgenie_nutau_dune10kt_gen.root -o prodgenie_nutau_dune10kt_$(($i+9))_gen_g4.root 
done	


#detsim
for j in {1..50..10};
do
	lar -n 10 -c standard_detsim_dune10kt.fcl prodgenie_nutau_dune10kt_$(($j+9))_gen_g4.root -o prodgenie_nutau_dune10kt_$(($j+9))_gen_g4_detsim.root
done


#reco
for k in {1..50..10};
do
	lar -n 10 -c standard_reco_dune10kt.fcl prodgenie_nutau_dune10kt_$(($k+9))_gen_g4_detsim.root -o prodgenie_nutau_dune10kt_$(($k+9))_gen_g4_detsim_reco.root 
done







