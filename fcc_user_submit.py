#!/bin/env python

"""This module aims to propose an example for using FCCDIRAC"""

import os

# It prints DIRAC environment script path available on AFS/CVMFS
# If you have installed the DIRAC client
# environment script must be here : ~/dirac/bashrc

def _initDirac():
  """This function checks DIRAC environment."""

  diracEnvMessage = (
    "\nDIRAC environment :\n"
    "Please ensure that you set up correctly DIRAC environment e.g. :\n"
    "source /afs/cern.ch/eng/clic/software/DIRAC/bashrc\n"
  )
  # DIRAC environment
  try:
    os.environ["DIRAC"]
  except KeyError:
    # Print AFS path of environment script as 'help'
    print(diracEnvMessage)
    quit()

_initDirac()

# After DIRAC environment checking done, we can import DIRAC libraries

from DIRAC.Core.Base import Script
Script.parseCommandLine()

from ILCDIRAC.Interfaces.API.DiracILC import DiracILC
from ILCDIRAC.Interfaces.API.NewInterface.UserJob import UserJob
from ILCDIRAC.Interfaces.API.NewInterface.Applications import FccSw, FccAnalysis

ILC = DiracILC()

# job settings for a user job
job = UserJob()
job.setJobGroup("FCC")
job.setName("Fcc Chain")
job.setPlatform('x86_64-slc5-gcc43-opt')
# e.g. ALWAYS, INFO, VERBOSE, WARN, DEBUG
job.setLogLevel('DEBUG')

job.setOutputSandbox(["*.log","*.root"])

#1st FCC application
FCC_SW = FccSw(
    fccConfFile='/build/YOUR_USERNAME/FCC/FCCSW/Examples/options/geant_pgun_fullsim.py',
    fccSwPath='/build/YOUR_USERNAME/FCC/FCCSW',
)

FCC_SW.logLevel = 'DEBUG'
#FCC_SW.numberOfEvents = 2
#FCC_SW.setOutputFile("output.root")

#2nd FCC application
FCC_PHYSICS1 = FccAnalysis(
    fccConfFile='/cvmfs/fcc.cern.ch/sw/0.8.1/fcc-physics/0.2.1/x86_64-slc6-gcc62-opt/share/ee_ZH_Zmumu_Hbb.txt'
)

#3rd FCC application
FCC_PHYSICS2 = FccAnalysis(
    executable='fcc-physics-read'
)

FCC_PHYSICS2.getInputFromApp(FCC_PHYSICS1)

#applications appending ...
job.append(FCC_PHYSICS1)
job.append(FCC_PHYSICS2)
job.append(FCC_SW)

job.setOutputData(['ee_ZH_Zmumu_Hbb.root', 'output.root'] )

job.submit(ILC,mode='wms')
