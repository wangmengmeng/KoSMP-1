{    
 // if(gSystem->Getenv("CMSSW_VERSION")) {
  //   cout << endl;
   //  cout << " *** RooFit version in CMSSW is too old! ***" << endl;
   //  cout << "  Please use a non-CMSSW environment." << endl;
   //  cout << endl;
   //  
  //} else {
    gROOT->Macro("../Utils/CPlot.cc++");
    gROOT->Macro("../Utils/RooCMSShape.cc++");
    gROOT->Macro("../Utils/MitStyleRemix.cc++");  
    gROOT->Macro("../Utils/RooVoigtianShape.cc++");  
    gROOT->Macro("../EventSelection/WLepNeu.C++");  
  //}
               
  // Show which process needs debugging
  gInterpreter->ProcessLine(".! ps |grep root.exe");
}
