import ROOT as root
import numpy as np
from ROOT import TGraph,TVector3,TCanvas,TH1F,THStack,kRed,TLegend,kBlue

f = root.TFile.Open("gntp.0.gtrac.root","READ")   #open the file 
#for comparing to other simulations, open the other files 
f_tau = root.TFile.Open("gntp.0.gtrac_tau.root","READ")
f_elect = root.TFile.Open('gntp.0.gtrac_e.root','READ')


tree = f.Get("gRooTracker")    #get the tree
#for comparting to other simulations, get those trees, could probably just have one definition but for clarity I did three  
tree_tau = f_tau.Get("gRooTracker")
tree_elect = f_elect.Get("gRooTracker")


#define histograms for comparisons 
hist_mu_energy = TH1F('muon_energy','Muon Energy nu_mu CC',200,-5,70)            #energy of the muon from a nu_mu CC interaction
hist_mu_energy.SetLineColor(kRed)                                               
hist_tau_energy_mu = TH1F('tau_mu_energy','Muon Energy nu_tau CC',200,-5,70)     #energy of the muon from the decay of the tau from a nu_tau CC interaction
hist_tau_energy_mu.SetLineColor(kBlue)                                           
hist_tau_energy_e = TH1F('tau_e_energy','Electron Energy nu_tau CC',200,-5,60)   #energy of the electron from the decay of the tau from a nu_tau CC interaction
hist_tau_energy_mu.SetLineColor(kBlue)                                           
hist_elect_energy = TH1F("electron_energy","Electron Energy nu_e CC",200,-5,60)  #energy of the electron from a nu_c CC interaction
hist_elect_energy.SetLineColor(kRed)                                             

#angle is between beam and the particle and calculated using the momentum
hist_mu_momentum = TH1F('muon_angle','Angle Between Beam and Muon from nu_mu CC',500,-5,10)                           #angle calculated from momentum for muon from nu_mu CC interaction
hist_mu_momentum.SetLineColor(kRed)                                                            
hist_tau_momentum_mu = TH1F('tau_muon_angle','Angle Between Beam and Muon from Tau Decay for nu_tau CC',500,-5,10)    #angle claculated from momentum for muon from tau decay in nu_tau CC interacion
hist_tau_momentum_mu.SetLineColor(kBlue)
hist_tau_momentum_e = TH1F('tau_e_angle','Angle Between Beam and Electron from Tau Decay for nu_tau CC',500,-5,10)    #angle calculated from momentum for electron from tau decay in nu_tau CC interaction
hist_tau_momentum_e.SetLineColor(kBlue)
hist_elect_momentum = TH1F('electron_angle','Angle Between Beam and Electron from nu_e CC',500,-5,10)                 #angle claculated from momentum for electron from nu_e CC interaction
hist_elect_momentum.SetLineColor(kRed)



'''
Start with the muon file
'''

#define empty arrays to fill later  
mu_energy = []     #will fill with energy values for the muon 
mu_momentum = []   #will fill with angle values calculated from the momentum for the muon 

for i in range(0,tree_mu.GetEntries()):      #loop over event tree for muon CC file 
	tree_mu.GetEntry(i)
	evtnum_mu = getattr(tree_mu,"EvtNum")    #define event number
	numint_mu = getattr(tree_mu,"StdHepN")   #define interaction number 

		
	for j in range(0,numint_mu):                                                    #loop over the number of interactions in each event 
		pdg_mu = getattr(tree_mu,"StdHepPdg")                                       #define pdg
		momentum_mu = getattr(tree_mu,"StdHepP4")                                   #define four momentum 
		momentum_cast_mu = np.frombuffer(momentum_mu,dtype=float)                   #convert four momentum from a buffer to an array 
		energy_mu = momentum_cast_mu[3::4][j]                                       #energy is the 4th value in the array 
		momentum_x_mu = momentum_cast_mu[0::4][j]                                   #x component of the momentum is the first value in the array 
		momentum_y_mu = momentum_cast_mu[1::4][j]                                   #y component of the momentum is the second value in the array 
		momentum_z_mu = momentum_cast_mu[2::4][j]                                   #z component of the momentum is the third value in the array 
		beam = TVector3(0,0,1)                                                      #define the beam along the z axis 
		momentum_vec_mu = TVector3(momentum_x_mu,momentum_y_mu,momentum_z_mu)       #create 3 vector of x,y,z momentum
		angle_mu = root.Math.VectorUtil.Angle(momentum_vec_mu,beam)                 #calculate the angle between the momentum vector and beam 
		

        if(pdg_mu[j] == 13):                   #if muon resulted from nu_mu CC interaction
			hist_mu_energy.Fill(energy_mu)     #fill the energy histogram
			hist_mu_momentum.Fill(angle_mu)    #fill the angle histogram 
			mu_energy.append(energy_mu)        #append energy values to empty array
			mu_momentum.append(angle_mu)       #append angle values to empty array 
			#print(evtnum_mu)


#print('the energy array is: {}'.format(mu_energy))
#print('the angle array is: {}'.format(mu_momentum))

'''
Move to electron file
'''

#follows the same format as the muon file 

e_energy = []
e_momentum = []

for w in range(0,tree_elect.GetEntries()):
	tree_elect.GetEntry(w)
	evtnum_e = getattr(tree_elect,"EvtNum")
	numint_e = getattr(tree_elect,"StdHepN")

	for n in range(0,numint_e):
		pdg_e = getattr(tree_elect,"StdHepPdg")
		momentum_e = getattr(tree_elect,"StdHepP4")
		momentum_cast_e = np.frombuffer(momentum_e,dtype=float)
		energy_e = momentum_cast_e[3::4][n]
		momentum_x_e = momentum_cast_e[0::4][n]
		momentum_y_e = momentum_cast_e[1::4][n]
		momentum_z_e = momentum_cast_e[2::4][n]
		beam4 = TVector3(0,0,1)
		momentum_vec_e = TVector3(momentum_x_e,momentum_y_e,momentum_z_e)
		angle_e = root.Math.VectorUtil.Angle(momentum_vec_e,beam4)

		if(pdg_e[n] == 11):                       #if electron resulted from nu_e CC interaction
			hist_elect_energy.Fill(energy_e)
			hist_elect_momentum.Fill(angle_e)
			e_energy.append(energy_e)
			e_momentum.append(angle_e)
			#print(evtnum_e)

#print('the energy aray is: {}'.format(e_energy))
#print('the angle array is: {}'.format(e_momentum))


'''
Move to tau file
Need to compare electrons from tau decay and muons from tau decay 
'''

#define empty arrays for the energy and angle for resulting muons from tau decay
tau_mu_energy = []
tau_mu_momentum = []

#define empty arrays for the energy and angle for resulting electrons from tau decay 
tau_e_energy = []
tau_e_momentum = []


for k in range(0,tree.GetEntries()):         #loop over event tree
	tree.GetEntry(k)
	evtnum_tau = getattr(tree,"EvtNum")      #define event number
	numint_tau = getattr(tree,"StdHepN")     #define interaction count
	
	for l in range(0,numint_tau):                                      #loop over the number of interactions in the event 
		pdg_tau = getattr(tree,"StdHepPdg")                            #define pdg
		fdaughter_tau = getattr(tree,"StdHepFd")                       #define the first daughter 
		ldaughter_tau = getattr(tree,"StdHepLd")                       #define the last daughter
		momentum_tau = getattr(tree,"StdHepP4")                        #define the four momentum 
		momentum_cast_tau = np.frombuffer(momentum_tau,dtype=float)    #convert momentum from buffer to array 
		energy_tau = momentum_cast_tau[3::4][l]                        #define energy from four momentum 


		if(pdg_tau[l] == 15):                                                                                                             #if the resulting particle from the nu_tau CC interaction is a tau 
			#print("event: {:<4} first daughter: {:<5} last daughter: {:<5}".format(evtnum_tau,fdaughter_tau[l],ldaughter_tau[l]))	
			for p in range(fdaughter_tau[l],ldaughter_tau[l]+1):                                                                          #loop over the tau's first daughter to last daughter to get all decay products 
				#print(evtnum_tau,pdg_tau[p])
				energy_new = momentum_cast_tau[3::4][p]                                                                                   #redefine energy so it's just for the tau's daughters
				momentum_x_tau = momentum_cast_tau[0::4][p]                                                                               #define x momentum
				momentum_y_tau = momentum_cast_tau[1::4][p]                                                                               #define y momentum 
				momentum_z_tau = momentum_cast_tau[2::4][p]                                                                               #define z momentum 
				beam2 = TVector3(0,0,1)                                                                                                   #define beam in the z direction 
				momentum_vec_tau = TVector3(momentum_x_tau,momentum_y_tau,momentum_z_tau)                                                 #create a three vector of the momentum components 
				angle_tau = root.Math.VectorUtil.Angle(momentum_vec_tau,beam2)		                                                      #angle between beam and momentum vector 
									
				#muon comparison	
				if(pdg_tau[p] == 13):                      #if the daughter of the tau is a muon 
					#print(evtnum_tau,energy_new)
					hist_tau_energy.Fill(energy_new)       #fill the energy histogram
					hist_tau_momentum.Fill(angle_tau)      #fill the angle histogram 
					tau_mu_energy.append(energy_new)       #append the energy values to the array 
					tau_mu_momentum.append(angle_tau)      #append the angle values to the array 
					#print(evtnum_tau)
				
				#electron comparison
				if(pdg_tau[p] == 11):                      #if the daughter of the tau is an electron 
					hist_tau_energy_e.Fill(energy_new)     #fill the energy histogram 
					hist_tau_momentum_e.Fill(angle_tau)    #fill the angle histogram
					tau_e_energy.append(energy_new)        #append the energy values to the array
					tau_e_momentum.append(angle_tau)       #append the angle values to the array 
					#print(evtnum_tau)
				
				

#print(tau_mu_energy)
#print(tau_mu_momentum)
#print(tau_e_energy)
#print(tau_e_momentum)


'''
Plotting
'''
							
'''
#single histograms

#hist_mu.Draw()
#hist_tau.Draw()

#hist_tau_energy.Draw()
#hist_tau_momentum.Draw()




#plot energy of muon from nu_mu CC interaction on same plot as energy of muon from tau decay in nu_tau CC interaction 
hs = THStack("hs","Energy Comparison for Muons")
hs.Add(hist_mu_energy)
hs.Add(hist_tau_energy_mu)

#legend = TLegend(0.6,0.1,0.9,0.3)

#plot energy of electron from nu_e CC interaction on same plot as energy of electron from tau decay in nu_tau CC interaction 
hs_e = THStack('hs', 'Energy Comparison for Electrons')
hs_e.Add(hist_elect_energy)
hs_e.Add(hist_tau_energy_e)

#legend.AddEntry(hist_mu,"nu_mu","l")
#legend.AddEntry(hist_tau,"nu_tau","l")
#hs.Draw("NOSTACK")
#legend.Draw()
#hist_mu_momentum.Draw()
#hist_tau_momentum.Draw()


#plot angle of muon from nu_mu CC interaction on same plot as angle of muon from tau decau in nu_tau CC interaction
hs_momentum = THStack('hs','Angle from Momentum Comparison for Muons')
hs_momentum.Add(hist_mu_momentum)
hs_momentum.Add(hist_tau_momentum_mu)

#plot angle of electron from nu_e CC interaction on same plot as angle of electron from tau decay in nu_tau CC interaction 
#hs_e_momentum = THStack('hs','Angle from Momentum Comparison for Electrons')
#hs_e_momentum.Add(hist_elect_momentum)
#hs_e_momentum.Add(hist_tau_momentum_e)
'''

