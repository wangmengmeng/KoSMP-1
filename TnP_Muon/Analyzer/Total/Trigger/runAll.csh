#! /bin/tcsh -f
root -l -q 'trig_pt.C(1)'
root -l -q 'trig_pt.C(-1)'
root -l -q 'trig_eta.C(20,1)'
root -l -q 'trig_eta.C(20,-1)'
root -l -q 'trig_eta.C(40,1)'
root -l -q 'trig_eta.C(40,-1)'
root -l -q 'trig_eta.C(55,1)'
root -l -q 'trig_eta.C(55,-1)'
root -l -q 'trig_eta.C(1000,1)'
root -l -q 'trig_eta.C(1000,-1)'