import ROOT as root
import numpy as np

'''
Code for calculating the branching ratios
Get expected branching ratios from the PDG
'''

#open file and get the tree
f = root.TFile.Open("gntp.0.gtrac.root","READ")
tree = f.Get("gRooTracker")

 
e = 0    #initialize counter for electron interactions
mu = 0   #initialize counter for muon interactions
pi = 0   #initialize counter for tau + pi- interactions
pi2 = 0  #initialize counter for tau + pi- + pi0 interactions



for i in range(0,tree.GetEntries()):   #loop over event tree
	tree.GetEntry(i)
	evtnum = getattr(tree,"EvtNum")    #define event number
	numint = getattr(tree,"StdHepN")   #define interaction number
	
    for j in range(0,numint):                   #loop over interaction number
		fdaughter = getattr(tree,"StdHepFd")    #define first daughter
		ldaughter = getattr(tree,"StdHepLd")    #define last daughter
		pdg = getattr(tree,"StdHepPdg")         #define pdg
		
		if(pdg[j]==15):                                      #if the daughter is a tau 
			daughter = []                                    #create empty array for resulting values
			cnt = 0                                          #initialize counter to zero, this counter is the the number of daughter particles resulting from the tau decay 
			for k in range(fdaughter[j],ldaughter[j]+1):     #loop from first daughter to last daughter resulting from tau decay 
				d = pdg[k]                                   #define the pdg of the particle under these conditions 
				daughter.append(d)                           #append daughters to the previous empty array
				cnt = cnt+1                                  
			daughter = np.asarray(daughter)                  #convert list to array
		
            if(cnt==3):                                      #if there are three daughter particles 
				if(daughter[0]==-12):                        #if the first daughter is an electron
					e = e+1                                  #count as electron interaction
				if(daughter[0]==-14):                        #if the first daughter is a muon
					mu = mu+1                                #count as a muon interaction
				if(daughter[1]==-211 and daughter[2]==111):  #if the second daughter is a pi- and the third is a pi0
					pi2 = pi2+1                              #count as a pi- + pi0 interaction
		
            if(cnt==2):                                      #if there are two daughter partciles 
				if(daughter[1]==-211):                       #the second daughter is a pi-
					pi = pi+1                                #count as a pi- interaction


print("number of electron interactions: {}".format(e))
print("number of muon interactions: {}".format(mu))
print("number of tau + pi- interactions: {}".format(pi))
print("number of tau + pi- + pi0 interactions: {}".format(pi2))
