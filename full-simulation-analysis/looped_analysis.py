import os
import glob
import ROOT
import numpy as np
import itertools
from ROOT import TVector3,TH1F,TChain

ROOT.gInterpreter.AddIncludePath(os.environ.get('GALLERY_INC'))
ROOT.gInterpreter.AddIncludePath(os.environ.get('CANVAS_INC'))
ROOT.gInterpreter.AddIncludePath(os.environ.get('FHICLCPP_INC'))
ROOT.gInterpreter.AddIncludePath(os.environ.get('CETLIB_INC'))
	 
ROOT.gROOT.ProcessLine('#include "gallery/ValidHandle.h"')
ROOT.gROOT.ProcessLine('#include "gallery/Handle.h"')


ROOT.gROOT.ProcessLine('template gallery::ValidHandle<simb::MCParticle> gallery::Event::getValidHandle<simb::MCParticle>(art::InputTag const&) const;')
ROOT.gROOT.ProcessLine('template bool gallery::Event::getByLabel<simb::MCParticle>(art::InputTag const&, gallery::Handle<simb::MCParticle>&) const;')


files = glob.glob('*detsim.root')
#print(files)

#files = ["prodgenie_nutau_dune10kt_10_gen_g4_detsim.root","prodgenie_nutau_dune10kt_20_gen_g4_detsim.root","prodgenie_nutau_dune10kt_30_gen_g4_detsim.root",
	#"prodgenie_nutau_dune10kt_40_gen_g4_detsim.root","prodgenie_nutau_dune10kt_50_gen_g4_detsim.root"]


	
energy_hist = TH1F('muon_energy','Muon Energy nu_tau CC',200,-5,75)

for j in np.arange(0,len(files)):
	#open file
	filename = ROOT.vector(ROOT.string)()
	filename.push_back(files[j])
	ev = ROOT.gallery.Event(filename)

	inputTagGenerator = ROOT.art.InputTag("largeant");



	#angle_hist = TH1F('muon_angle', 'Muon Angle nu_tau CC',200,-5,75)

	#energy_hist_elect = TH1F('electron_energy','Electron Energy nu_tau CC',200,-5,75)
	#angle_hist_elect = TH1F('electron_angle', 'Electron Angle nu_tau CC',200,-5,75)


	#momentum_hist_z = TH1F('z_momentum','Muon z Momentum nu_tau CC',200,-5,75)
	#momentum_elect_hist_z = TH1F('z_momentum','Electron z Momentum nu_tau CC',200,-5,75)

	

	ev.toBegin()

	numEvent = j*10+1
	#cnt_elect = 0
	#cnt_muon = 0


	while ( not ev.atEnd()):
	
		get_mctruths = ev.getValidHandle[ROOT.vector(ROOT.simb.MCParticle)]
		mctruth = get_mctruths(inputTagGenerator)

		print('========== Event', numEvent, '==========')
		numPart = len(mctruth.product())
		print('found',numPart,'particles')

		for i in range(numPart):
			x = mctruth.product()[i] 
			pdg = x.PdgCode()
			energy = x.E()
			z_momentum = x.Pz()
			mother = x.Mother()
			fdaughter = x.FirstDaughter()
			beam = TVector3(0,0,1)
			y_momentum = x.Py()
			x_momentum = x.Px()
			momentum_vec = TVector3(x_momentum,y_momentum,z_momentum)
			angle_momentum = ROOT.Math.VectorUtil.Angle(momentum_vec,beam)
			#print(energy_arr)
			#if pdg < 1000000000 and pdg != 22:
			#if pdg < 1000000000 and pdg != 22 and pdg != 2112 and pdg != 2212 and pdg != 3122 and pdg != 3212:
			#if mother == 0 and pdg == 16:
			#print('Event: {} Count: {} Pdg: {:<20}  Energy: {:<30} Mother: {:<20} First Daughter: {:<20} Angle: {}'.format(numEvent,i,pdg,energy,mother,fdaughter,angle_momentum)) 
			#if mother == 0:
				#if pdg == 13:
					#energy_hist.Fill(energy)	
					#print(numEvent, i, energy)
					#angle_hist.Fill(angle_momentum)
					#momentum_hist_z.Fill(z_momentum)
					#print(angle_momentum)
			energy_hist.Fill(energy)
			#if mother == 0:
				#if pdg == 11:
					#energy_hist_elect.Fill(energy)	 
					#angle_hist_elect.Fill(angle_momentum)
					#momentum_elect_hist_z.Fill(z_momentum)
					#print(energy,angle_momentum)
		
			
			
			#if pdg == 11 or pdg == -11:
				#cnt_elect += 1
				#print('Event: {} Count: {} Pdg: {:<20}  Energy: {:<30} Mother: {:<20} First Daughter: {:<20} Angle: {}'.format(numEvent,i,pdg,energy,mother,fdaughter,angle_momentum))
			
			#if pdg == 13 or pdg == -13:	
				#cnt_muon += 1
				#print('Event: {} Count: {} Pdg: {:<20}  Energy: {:<30} Mother: {:<20} First Daughter: {:<20} Angle: {}'.format(numEvent,i,pdg,energy,mother,fdaughter,angle_momentum))
			
		
		#	print(numEvent,pdg)
			#if pdg == 16 or pdg == -16:
			#	print(numEvent)
		ev.next()
		numEvent+=1


	#print("number of electrons: {}".format(cnt_elect))
	#print("number of muons: {}".format(cnt_muon))
	if j==0:
		energy_hist.Draw()
	else:
		energy_hist.Draw("SAME")
	#angle_hist.Draw()

	#energy_hist_elect.Draw()
	#angle_hist_elect.Draw()
	#momentum_elect_hist_z.Draw()

