import os
#import sys
#BaseName="WpToMuNu"
#UnfoldFile="MuonLowPU/Muon_WpToMuNu_S8_Unfold.root"
#AcceptFile="../Acceptance_WpT/MuonLowPU/Muon_WpToMuNu_S8_Acceptance.root"
#DataFile="../RstSelection/SigYields_Muon_Nominal.root"
#BaseName="WmToMuNu"
#UnfoldFile="MuonLowPU/Muon_WmToMuNu_S8_Unfold.root"
#AcceptFile="../Acceptance_WpT/MuonLowPU/Muon_WmToMuNu_S8_Acceptance.root"
#DataFile="../RstSelection/SigYields_Muon_Nominal.root"
BaseName="WpToEleNu"
UnfoldFile="ElectronLowPU/Ele_WpToEleNu_S8_Unfold.root"
AcceptFile="../Acceptance_WpT/ElectronLowPU/Ele_WpToEleNu_S8_Acceptance.root"
DataFile="../RstSelection/SigYields_Electron_Nominal.root"
#BaseName="WmToEleNu"
#UnfoldFile="ElectronLowPU/Ele_WmToEleNu_S8_Unfold.root"
#AcceptFile="../Acceptance_WpT/ElectronLowPU/Ele_WmToEleNu_S8_Acceptance.root"
#DataFile="../RstSelection/SigYields_Electron_Nominal.root"
#InFile="ElectronLowPU/Ele_WpToEleNu_S8_Unfold.root"
cmd_string = "root -l -q wPtUnfoldStudy.C+\(\\\"%s\\\",\\\"%s\\\",\\\"%s\\\",\\\"%s\\\"\)" %(UnfoldFile,AcceptFile,DataFile,BaseName)
#cmd_string = "root -l -q wPtUnfoldStudy.C+\(\\\"%s\\\",\\\"%s\\\"\)" %(InFile,BaseName)
os.system(cmd_string)

