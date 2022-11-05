void outProperties(){
  TFile* f = new TFile("prodgenie_nutau_dune10kt_gen.root");
  //f->ls();
  TTree* t = (TTree *) f->Get("Events");
  //TH1F* h1 = new TH1F("h1", "histogram", 5000,0,50000);
  //t->Print();
  for (Int_t i=0; i!=t->GetEntries(); ++i){
   t->GetEntry(i);
   t->GetBranch("simb::MCTruths_generator__GenieGen.obj");
   Int_t pdgcode =  t->GetLeaf("simb::MCTruths_generator__GenieGen.obj.fMCNeutrino.fLepton.fpdgCode")->GetValue();
   Int_t decay = t->GetLeaf("simb::MCFluxs_generator__GenieGen.obj.fndecay")->GetValue();
   Int_t type = t->GetLeaf("simb::MCFluxs_generator__GenieGen.obj.fntype")->GetValue();
   //cout << "lepton pdg: " << pdgcode << " fndecay: " << decay << " fntype: " << type;
   cout << i << " " << decay;
   cout << "\n";
    //cout << t->GetEntry(i);
    //cout << pdgcode;
    //h1->Fill(pdgcode);
    //h1->Draw();

     
    
    
  }
}
