/*
This code outputs all properties for a single event using the genie level simulation file 
 */

void singleEvent(){
  TFile* f = new TFile("prodgenie_nutau_dune10kt_gen.root");    //name of genie level file 
  //f->ls();
  TTree* t = (TTree *) f->Get("Events");
  t->Show(30);     //event number, iterates from 0 
}

