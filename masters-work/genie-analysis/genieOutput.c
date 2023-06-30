#include <fstream>
#include <iostream>

/*
This code outputs properties for particles produced from Genie
 */

void genieOutput(){
  //get file
  TFile* f = new TFile("gntp.0.gtrac.root");         
  // f->ls();
  
  //get tree
  TTree* t = (TTree *) f->Get("gRooTracker");
  //t->Print();
  
  //define the four momentum double
  Double_t p4[100][4];
  t->SetBranchAddress("StdHepP4",p4);

  //define output txt file
  ofstream fout;
  ifstream fin;
        fin.open("genie_out.txt");
        fout.open("genie_out.txt",ios::app);

  
  for (Int_t i=0; i!=t->GetEntries(); ++i){                     //loop over event tree
   t->GetEntry(i);
   Int_t evtnum = t->GetLeaf("EvtNum")->GetValue();             //define event number
   Int_t num_interactions = t->GetLeaf("StdHepN")->GetValue();  //define interaction number 
 
    
   cout << "Event Number " << evtnum << endl;
   cout << "Number of Interctions " << num_interactions;
   cout << "\n";

   
 
   for (Int_t j=0; j!=num_interactions; ++j){                  //loop over number of interactions in each event 
        Int_t pdgcode = t->GetLeaf("StdHepPdg")->GetValue(j);  //pdg code of jth particle in event
 	Int_t fdaughter = t->GetLeaf("StdHepFd")->GetValue(j); //first daughter
	Int_t ldaughter = t->GetLeaf("StdHepLd")->GetValue(j); //last daughter
        cout << "count " << j;
        cout << " | ";
        cout << "Event Number " << evtnum;
        cout << " | ";
        cout << "Pdg " << pdgcode;
	cout << " | ";
	cout << "First Daughter " << fdaughter;
	cout << " | ";
	cout << "Last Daughter " << ldaughter;
	cout << " | ";
	cout << "energy " << p4[j][3];                        //fourth component of the four momentum double is the energy 
        cout << "\n";

	fout << "Event Number: " << evtnum << " Count: " << j << " Pdg: " << pdgcode << " First: " << fdaughter << " Last: " << ldaughter << " Energy: " << p4[j][3] << endl;		
      }   
    
    }

   fin.close();
   fout.close();
}
