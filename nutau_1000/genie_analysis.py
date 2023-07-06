import os
import ROOT
import numpy as np
import itertools
from ROOT import TVector3,TH1F

ROOT.gInterpreter.AddIncludePath(os.environ.get('GALLERY_INC'))
ROOT.gInterpreter.AddIncludePath(os.environ.get('CANVAS_INC'))
ROOT.gInterpreter.AddIncludePath(os.environ.get('FHICLCPP_INC'))
ROOT.gInterpreter.AddIncludePath(os.environ.get('CETLIB_INC'))
	 
ROOT.gROOT.ProcessLine('#include "gallery/ValidHandle.h"')
ROOT.gROOT.ProcessLine('#include "gallery/Handle.h"')


ROOT.gROOT.ProcessLine('template gallery::ValidHandle<simb::MCTruth> gallery::Event::getValidHandle<simb::MCTruth>(art::InputTag const&) const;')
ROOT.gROOT.ProcessLine('template bool gallery::Event::getByLabel<simb::MCTruth>(art::InputTag const&, gallery::Handle<simb::MCTruth>&) const;')

#open file
filename = ROOT.vector(ROOT.string)()
filename.push_back("prodgenie_nutau_dune10ktvd_gen.root")
ev = ROOT.gallery.Event(filename)

inputTagGenerator = ROOT.art.InputTag("generator");

ev.toBegin()

numEvent = 0

neut_energy_hist = TH1F('neutrino_energy', 'Initial Neutrino Energy',200,-5,90)

while ( not ev.atEnd()):
	get_mctruths = ev.getValidHandle[ROOT.vector(ROOT.simb.MCTruth)]
	mctruth = get_mctruths(inputTagGenerator)

	#print('========== Event', numEvent, '==========')
	numPart = mctruth.product()[0].NParticles()
	mc_neutrino = mctruth.product()[0].GetNeutrino()
	#print("number of particles: {}".format(numPart))
	for i in range(numPart):
		mc_particle = mctruth.product()[0].GetParticle(i)
		print(numEvent,i,mc_particle.PdgCode(),mc_particle.Momentum()[3],mc_particle.Mother())	
		#print("Event: {} Count: {} Pdg: {} Energy: {}".format(numEvent,i,mc_particle.PdgCode(),mc_particle.Momentum()[3]))
		#if mc_particle.PdgCode() == 16 and i == 0:
			#neut_energy_hist.Fill(mc_particle.Momentum()[3])
			#print("Event: {} Count: {} Pdg: {} Energy: {}".format(numEvent,i,mc_particle.PdgCode(),mc_particle.Momentum()[3]))

	ev.next()
	numEvent+=1

#neut_energy_hist.Draw()
