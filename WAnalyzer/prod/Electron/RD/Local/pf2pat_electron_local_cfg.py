import FWCore.ParameterSet.Config as cms

from KNUPhy.WAnalyzer.pf2pat_template_RD_cfg import *
from KNUPhy.WAnalyzer.eventContent_cff import *
from KNUPhy.WAnalyzer.tools import *

postfix = "PFlow"
jetAlgo="AK5"
usePF2PAT(process,runPF2PAT=True, jetAlgo=jetAlgo, runOnMC=False, postfix=postfix,typeIMetCorrections=True)

#process.pfPileUpIsoPFlow.checkClosestZVertex = cms.bool(False)
#process.pfPileUpIso.checkClosestZVertex = cms.bool(False)

#change cone size
changeConeSize(process,postfix)

#FastJet!
#applyFastJet(process,postfix)

#rhoFor2011Aeff(process,postfix)
rhoFor2012Aeff(process,postfix)

#useGefElectrons(process,postfix)
#REMOVE ISOLATION FROM PF2PAT!!!
addLooseLeptons(process)

# top projections in PF2PAT:
topProjection(process,postfix)

# output
process.out.outputCommands +=pf2patEventContent

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(3000) )
process.MessageLogger.cerr.FwkReport.reportEvery = 1000

process.patMuonFilter.minNumber = 0
process.patElectronFilter.minNumber = 1

## Source
process.load("KNUPhy.WAnalyzer.Sources.Run2012B_SingleEle_13Jul2012-v1_AOD_CP_local_cff")

#process.p += process.hltHighLevelMuMuRD
process.p += process.nEventsHLT
process.p += getattr(process,"patPF2PATSequence"+postfix)
#process.p += process.looseLeptonSequence
process.p += process.acceptedElectrons
#process.p += process.acceptedMuons
process.p += process.patElectronFilter
process.p += process.allConversions
#process.p += process.patMuonFilter
process.p += process.nEventsFiltered
