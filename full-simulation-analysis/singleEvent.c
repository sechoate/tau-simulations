void singleEvent(){
  TFile* f = new TFile("prodgenie_nutau_dune10kt_gen.root");
  //f->ls();
  TTree* t = (TTree *) f->Get("Events");
  t->Show(30);
}

