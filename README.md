# Getting Started with DIRAC


Contents:

  * [DIRAC](#dirac)
    * [Overview](#overview)
    * [1 - Existing Infrastructure](#1---existing-infrastructure)
      * [a - Introduction](#a---introduction)
      * [b - DIRAC](#b---dirac)
    * [2 - FCC JOB](#2---fcc-job)
      * [a - Job](#a---job)
      * [b - Application](#b---application)
    * [3 - Prerequisites](#3---prerequisites)
      * [a - GRID access](#a---grid-access)
      * [b - Setting up DIRAC environment](#b---setting-up-dirac-environment)
    * [4 - Examples](#4---examples)
      * [a - Simple FCC job](#a---simple-fcc-job)
      * [b - Complex FCC Jobs](#b---complex-fcc-jobs)
    * [5 - Sandboxes and Data](#5---sandboxes-and-data)
      * [a - Sandboxes](#a---sandboxes)
      * [b - Data](#b---data)
	      * [1 - Output Data](#1---output-data)
	      * [2 - Input Data](#2---input-data)
    * [6 - Monitoring](#6---monitoring)
      * [a - Command Line Interface](#a---command-line-interface)
      * [b - Web Portal](#b---web-portal)
    * [7 - Advanced](#7---advanced)
      *	[a - Job splitting](#a---job-splitting)
      * [b - HTCondor submission with DIRAC](#b---htcondor-submission-with-dirac)
    * [8 - Developer Notes](#8---developer-notes)
      * [a - FCC integration in image](#a---fcc-integration-in-image)
      * [b - FCC integration in words](#b---fcc-integration-in-words)
	


## Overview



## 1 - Existing Infrastructure


### a - Introduction

This tutorial is intented for people interested in submitting FCC jobs on the GRID.

GRID submission relies on GRID framework providing an intuitive user interface quite similar to BATCH submission.

This tutorial aims to show you how to use this interface in order to submit FCC jobs.

In brief, it consists of :

-	[Getting GRID certificate](#a---grid-access)
-	[Registering to ILC VO](#register-to-ilc-vo)
-	[Setting DIRAC environment](#dirac-environment)
-	[Running examples](#4---examples)

### b - DIRAC

DIRAC project was initially developed for the LHCb Collaboration and became a general-purpose Grid Middleware.

DIRAC builds a layer between the users and the resources offering a homogeneous interface to an heterogeneous set of computing resources (Middlewares, VMs, laptops,...).

It is now used by several communities, more than 20 VOs (Virtual Organizations) like CLIC, LHCb, Belle ...

FCC group choose to use DIRAC because of its many benefits (Non-exhaustive list) :

- Workload Management
- Transformations
- Monitoring
- Accounting
- Security (DISET)
- BookKeeping
- Webportal (a Friendly Web interface to monitor your jobs)

DIRAC is VO oriented so generally, an instance of the DIRAC framework is managed by a VO :

- ILCDirac (managed by CLIC VO)
- LHCbDirac (managed by LHCb VO)

They manage DIRAC servers configuring for doing job scheduling, data bookkeeping ...

Because it is too redundant to create a new instance of DIRAC for each VO, FCC group decided to collaborate with CLIC group.

So CLIC group is sharing ILCDirac with FCC group.

A multi VO installation is possible with DIRAC and it is a matter of server configuration.

For more informations, please look at :

[Multi VO installation](http://dirac.readthedocs.io/en/latest/AdministratorGuide/MultiVO/)

## 2 - FCC JOB

### a - JOB

Basic building blocks for specifying jobs are already present in DIRAC.

An other concept defined more or less by VOs is the Application concept.

An application can be considered as a step for a job.

We are used to know that jobs are simple executables running with input/output files. 

Now you can specify a job like a chain of applications or a succession of steps where each step can be an executable.

It is also possible to have dependencies between each step.

### b - Application

VOs created many applications in their DIRAC instance with a specific purpose :

- Simulation
- Reconstruction
- Analysis
- etc...

Then a physics process is easy to define with DIRAC because we have the job representing the whole physics process and a step in the process (reconstruction or analysis) is represented by an Application.
 
Usually, users just have to "configure" the application, add user libraries if needed and submit the job.

Indeed, applications are pre-defined (environment, executable ...)

For FCC group, 2 applications have been designed :

- FccSw
- FccAnalysis

However, in order to use them and submit a FCC job, you need to fulfill the prerequisites.

## 3 - Prerequisites


### a - GRID access

First, to be authorized to use the GRID, you need to have :
 
- a GRID certificate 


Second, to be able to submit jobs through DIRAC interware, in general you need :

- to register to a VO (Virtual Organization) which has already set up on their servers an instance of DIRAC for its members

#### Register to ILC VO

Instructions for registering to ILC VO (also getting GRID access) can be found here :

- [CLIC tutorial](https://twiki.cern.ch/twiki/bin/view/CLIC/IlcdiracRegistration)

or here (lhcb users) :

- [LHCB tutorial](https://twiki.cern.ch/twiki/bin/view/LHCb/FAQ/Certificate)


Because FCC group collaborated with CLIC group, FCC users have to register to the ILC VO.


So, in the next section, the instructions of the client installation are specific to the ILC VO.


If you encounter some problems with the client installation, very good tutorials are also available here :


[DIRACGrid tutorial](https://github.com/DIRACGrid/DIRAC/wiki/DIRAC-Tutorials)

or here :

[LCD tutorial](http://lcd-data.web.cern.ch/lcd-data/doc/HeadFirstTalk.pdf)


### b - Setting up DIRAC environment

ILCDirac is the  extension/instance of  the DIRAC framework for ILC VO, it is  built  on  top  of  the  workflow  API  from Dirac.

It offers a set of applications used in the LC community and 14 applications are currently supported.

Among  them  are  :

-	SLIC and Mokka (detector  simulation  frameworks  based  on Geant4)
-	Marlin and org.lcsim (reconstruction and analysis frameworks)
-	Monte Carlo generators (Whizard, Pythia) and ROOT


Here are the minimum requirements if you want to continue this tutorial :

-	a computer running Linux or MacOS X
-	a working version of Python (v2.4 minimum)
-	to be able to install some software on your computer


As you guess, DIRAC works in client-server architecture.

ILCDirac servers are running somewhere while users submit their jobs through a local client which relays jobs to the servers.

At the end of this tutorial, you will be able from your seat to run a job on a machine located at the other side of the planet without paying attention about **WHERE** or **HOW** it works,
all this thanks to the GRID infrastructure and Abstraction layer built by DIRAC.

In order to use ILCDirac, you need first to get the client.

The client is already installed on AFS/CVMFS, you can follow the instructions here :

[CLIC twiki tutorial](https://twiki.cern.ch/twiki/bin/view/CLIC/IlcdiracEnvironment#Using_a_pre_existing_installatio)

Indeed, you only have to set the environment and configure the client with the proxy and the GRID certificate.

If you do not have access to AFS neither CVMFS, you can download and install the client locally.

The following installation is scpecific to ILC VO but it is quite similar to the general procedure.
Installation scripts (e.g. **ilcdirac-install.sh**) and cfg files (e.g. **defaults-ILCDIRAC.cfg**) may differ according to your VO.

This client is composed of a set of commands which allows you to manage your jobs as well as your data.

ILCDirac client requires your certificate in a specific format, you need to convert your GRID certificate from p12 format (as you exported it from your browser) to PEM format.

But don't worry, the client has already a tool for that :D (**dirac-cert-convert.sh**).

It will store your converted certificate to the **.globus** directory.

Here are the instructions of how to install the client and configure it with your GRID certificate (even the certificate conversion is included, no need to make it before):

#### DIRAC environment

If you want to use the client of AFS/CVMFS skip step 1 and execute step 22 instead of step 2.


```

#1) install client
mkdir -p $HOME/DIRAC
cd  $HOME/DIRAC
wget http://www.cern.ch/lcd-data/software/ilcdirac-install.sh
chmod +x ilcdirac-install.sh
./ilcdirac-install.sh

#2) set ILCDirac environment from your local client
# bash users
source bashrc

# (t)csh users
#source cshrc

#22) set ILCDirac environment from the AFS/CVMFS client
#source /afs/cern.ch/eng/clic/software/DIRAC/bashrc

#3) set GRID user proxy
# conversion of the grid certificate from p12 to PEM files
dirac-cert-convert.sh /path/to/your_grid_certificate.p12
dirac-proxy-init -x
dirac-configure defaults-ILCDIRAC.cfg
dirac-proxy-init
cd ..

```

**ilcdirac-install.sh** will install the client in your machine.

Replace **/path/to/your_grid_certificate.p12** by the path of your certificate.

The file **defaults-ILCDIRAC.cfg** is specific to ILC and it is a configuration file which help users to configure DIRAC client according to the VO they are affiliated with.

Each VO using DIRAC should have such a file which helps their users to configure DIRAC client quickly.

If you are affiliated with a VO different from ILC, please refer to the tutorial dedicated for the instance of DIRAC of your VO or contact your VO  manager to get this file.

If you encounter some problems during the installation (e.g. ImportError: No module named GSI) please refer to these discussions :

[DIRAC client installation issue](https://groups.google.com/forum/#!topic/diracgrid-forum/J2hDZc6WbaM)

## 4 - Examples


Let's go step by step with 2 examples.

With the 2 following examples, the user has to consider that there exist a "UserJob" (inheriting from DIRAC Job) that may contain one or several applications.

Before using ILCDirac, ensure that you set the environment and updated the proxy (if it is outdated, after 24h ) !

	# each time you open a new shell
	source /afs/cern.ch/eng/clic/software/DIRAC/bashrc
	# each day
	dirac-proxy-init

### a - Simple FCC Job


In this simple example, we want to run **FCCSW** on the GRID.

```
#!/bin/env python

from DIRAC.Core.Base import Script
Script.parseCommandLine()

from ILCDIRAC.Interfaces.API.DiracILC import DiracILC
from ILCDIRAC.Interfaces.API.NewInterface.UserJob import UserJob
from ILCDIRAC.Interfaces.API.NewInterface.Applications import FccSw, FccAnalysis

ILC = DiracILC()

# job settings for a user job
job = UserJob()
job.setJobGroup("FCC")
job.setName("FccSW")
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

#applications appending ...
job.append(FCC_SW)

job.setOutputData('output.root')

job.submit(ILC,mode='wms')


```

### b - Complex FCC Jobs


Now, let us complicate things in doing chaining between **FCC Analysis** applications !

The first application generates events with **fcc-pythia8-generate** (the default executable of FccAnalysis) and the given card file **ee_ZH_Zmumu_Hbb.txt**.

The second application reads these events. 


```
#!/bin/env python

from DIRAC.Core.Base import Script
Script.parseCommandLine()

from ILCDIRAC.Interfaces.API.DiracILC import DiracILC
from ILCDIRAC.Interfaces.API.NewInterface.UserJob import UserJob
from ILCDIRAC.Interfaces.API.NewInterface.Applications import FccSw, FccAnalysis

ILC = DiracILC()

# job settings for a user job
job = UserJob()
job.setJobGroup("FCC")
job.setName("FccAnalysis Chain")
job.setPlatform('x86_64-slc5-gcc43-opt')
# e.g. ALWAYS, INFO, VERBOSE, WARN, DEBUG
job.setLogLevel('DEBUG')

job.setOutputSandbox(["*.log","*.root"])

#1st FCC application
FCC_PHYSICS1 = FccAnalysis(
    fccConfFile='/cvmfs/fcc.cern.ch/sw/0.8.1/fcc-physics/0.2.1/x86_64-slc6-gcc62-opt/share/ee_ZH_Zmumu_Hbb.txt'
)

FCC_PHYSICS1.setOutputFile("ee_ZH_Zmumu_Hbb.root")

#2nd FCC application
FCC_PHYSICS2 = FccAnalysis(
    executable='fcc-physics-read'
)

FCC_PHYSICS2.getInputFromApp(FCC_PHYSICS1)

#applications appending ...
job.append(FCC_PHYSICS1)
job.append(FCC_PHYSICS2)

job.setOutputData('ee_ZH_Zmumu_Hbb.root')

job.submit(ILC,mode='wms')

```

Indeed, the input card file of the second FccAnalysis application is the output file of the first FccAnalysis application.

Then, let us do chaining between **FCCSW** applications !

The first FCCSW application generates root file from the configuration file **geant_fullsim_ecal_singleparticles.py**.

The second one reads the generated root file **output_ecalSim_e50GeV_1events.root** and do the reconstruction.

```

#!/bin/env python
from DIRAC.Core.Base import Script
Script.parseCommandLine()

from ILCDIRAC.Interfaces.API.DiracILC import DiracILC
from ILCDIRAC.Interfaces.API.NewInterface.UserJob import UserJob
from ILCDIRAC.Interfaces.API.NewInterface.Applications import FccSw, FccAnalysis

ILC = DiracILC()

job = UserJob()

job.setJobGroup("FCC")
job.setName("FccSw Chain")
job.setPlatform('x86_64-slc5-gcc43-opt')
# e.g. ALWAYS, INFO, VERBOSE, WARN, DEBUG
job.setLogLevel('DEBUG')

job.setOutputSandbox(["*.log","*.root"])

#1st FCC application
simulation = FccSw(
    fccConfFile='/build/YOUR_USERNAME/FCC/FCCSW/Reconstruction/RecCalorimeter/tests/options/geant_fullsim_ecal_singleparticles.py',
    fccSwPath='/build/YOUR_USERNAME/FCC/FCCSW',
)

#sim.numberOfEvents = 500
simulation.setOutputFile("output_ecalSim_e50GeV_1events.root")

reconstruction = FccSw(
    fccConfFile='/build/YOUR_USERNAME/FCC/FCCSW/Reconstruction/RecCalorimeter/tests/options/runEcalReconstructionWithoutNoise.py',
    fccSwPath='/build/YOUR_USERNAME/FCC/FCCSW',
    read=True
)

reconstruction.getInputFromApp(simulation)

job.append(simulation)
job.append(reconstruction)

print job.submit(ILC,mode='wms')


```

You can set the number of events like this :

	simulation.numberOfEvents = 500

Setting the number of events of the first application set it also for all the others.

The application's dependancy is done using conjointly :

	simulation.setOutputFile("output_ecalSim_e50GeV_1events.root")

and

	reconstruction.getInputFromApp(simulation)

Contrary to ILC applications, **setOutputFile()** method can not be use for naming the output file of the FCC application.

The name of the FCC application is specified in the steering file (e.g. **PodioOutput().filename**).

Then the output file you enter has to be generated by the application.

For the moment, **setOutputFile()** method is only used for creating the dependancy.

It is not possible to specify list for these methods then dependancy with many input/output files does not work the moment we wrote this tutorial.

Nevertheless, we implemented FCC applications in such a way that FCC applications can have dependancies with many input/output files (in the case where the signature of these methods could be modified).

Notice that we set the parameter **read** to True in the 2nd application.

Because this application is reading ouput of the previous application, setting this parameter give this file as input to **FCCDataSvc**.

If you set the parameter **read** to True without getting output of the previous application, it will give input data to **FCCDataSvc** if there are.

Output files are renamed by default in pre-pending the ID of the job, the application's name, application's version and the application's step.

Here is an exerpt of the output sandbox of a job running the third example :

	FccSw_v0.8.1_Step_1.log
	FccSw_v0.8.1_Step_2.log
	JobID_0_FccSw_v0.8.1_2_output_ecalReco_noNoise_test.root
	JobID_0_FccSw_v0.8.1_Step_1_output_ecalSim_e50GeV_1events.root
	...

In these examples, FCCSW installation is located at **/build/&lt;YOUR_USERNAME&gt;/FCC**.

Change it to make it point to your local FCCSW location.

You can also use FCCSW installation of CVMFS (this is the fccSwPath):

	/cvmfs/fcc.cern.ch/sw/0.8.1/fccsw/0.8.1/x86_64-slc6-gcc62-opt

However, this tutorial was written during **v0.8.1** release.

And some folders like **Detector** and **Generation** are missing in this release, so some examples requesting these folders will not run.

You will see a warning message before the submission saying that :

	WARN: Sandboxing : The folder 'Detector' does not exist, it is not present in the FCCSW installation
	WARN: Then you should have added it manually to the input sandbox !

Please, read the log before confirming the submission to be sure that everything is ok !

In this case you have to upload the missing folder **Detector** into the input sandbox like this :

	job.setInputSandbox('/build/<YOUR_USERNAME>/FCC/FCCSW/Detector')


If you run 2 FccAnalysis applications followed by one FccSw application, you should get a display similar to this one :

![IMAGE NOT AVAILABLE](tutorial_images/diracsub.png "submission confirmation")


Notice that these examples are submitting to the grid, you can also submit to your local machine by changing the mode like this :

	job.submit(ILC,mode='local')

If for some reasons these applications are not convenient for you, you can always set a generic application and add it to the workflow :

[Generic Application](https://twiki.cern.ch/twiki/bin/view/CLIC/ILCDiracApplicationInterface#Generic_application)

**WARNING**

Applications are getting FCCSW environment by asking this configuration file :

- /path/to/DIRAC_INSTALLATION/etc/dirac.cfg

It contains sections where the path of the environment script is hardcoded.

Each application is looking for this file for setting the environment and FCC applications use by default the release **v0.8.1**.

If your are using CVMFS/AFS DIRAC installation, it contains already the default path of the FCCSW environment script :

	/cvmfs/fcc.cern.ch/sw/0.8.1/init_fcc_stack.sh

If your are not using CVMFS/AFS DIRAC installation, then ensure that **dirac.cfg** file contains the path of the FCCSW environment script else applications won't run.

For each new release, the release manager has to update **dirac.cfg** file of the CVMFS/AFS DIRAC installation by contacting CLIC group.

And you have to set the version of the application (if you do not want to use by default the version **v0.8.1**)

So if the current release of FCC software is different from the default, release manager should have updated **dirac.cfg** of CVMFS/AFS DIRAC installation.

Here is an excerpt of the **dirac.cfg** file :


```
Operations
{
    Defaults
    {
        AvailableTarBalls
        {
            x86_64-slc5-gcc43-opt
            {       
                 fccanalysis
                 {
                      v0.8.1
	              {
	     	          CVMFSEnvScript = /cvmfs/fcc.cern.ch/sw/0.8.1/init_fcc_stack.sh
	                  CVMFSPath = /cvmfs/fcc.cern.ch/sw/0.8.1
         	      }
         	 }
         	 fccsw
		 {
		     v0.8.1
		     {
		         CVMFSEnvScript = /cvmfs/fcc.cern.ch/sw/0.8.1/init_fcc_stack.sh
		         CVMFSPath = /cvmfs/fcc.cern.ch/sw/0.8.1
		     }
		 }
         
            } 
        }
    }
}

```

Then, if you want to run FCC software with the last release (or a specific one), which is different from the default, you have to ensure that **dirac.cfg** is updated with this release and

**YOU HAVE ALSO TO SET THE VERSION OF THE APPLICATION LIKE THIS :**

	application.setVersion("vX.X.X")

else FCC software will run by default with the release **v0.8.1** !

Do not take care of the default application's platform here **x86_64-slc5-gcc43-opt** because software will be taken from CVMFS with the platform specified in the FCC environment script.

But if you want to change this value, 

**YOU HAVE ALSO TO SET THE PLATFORM OF THE JOB LIKE THIS :**

	job.setPatform("architecture-OS-compiler-type")

You should not change this because ILCDirac supports a pre-defined set of platforms !

Suppose you want to update the **dirac.cgf** file with the release **v0.9.1** :

      v0.8.1
      {
          CVMFSEnvScript = /cvmfs/fcc.cern.ch/sw/0.8.1/init_fcc_stack.sh
          CVMFSPath = /cvmfs/fcc.cern.ch/sw/0.8.1
      }

      v0.9.1
      {
          CVMFSEnvScript = /cvmfs/fcc.cern.ch/sw/0.9.1/init_fcc_stack.sh
          CVMFSPath = /cvmfs/fcc.cern.ch/sw/0.9.1
      }

You should add a new section (the last one) keeping the old one to ensure backward compatibility.

ILCDirac contains tests for all existing applications.

The tests of FCC applications are using the release **v0.8.1**.

When reading the **dirac.cfg** file, the path of the FCCSW environment script have to be present else tests will failed.

If you want to remove the section containing the release **v0.8.1**, you have also to update these tests :

[LocalTestObjects.py](https://gitlab.cern.ch/CLICdp/iLCDirac/ILCDIRAC/blob/Rel-v26r0/Interfaces/API/NewInterface/Tests/LocalTestObjects.py)

in setting the version of the application :

	def getFccSw( self ):
	    ...
	    fccsw = FccSw()
	    fccsw.setVersion("v0.9.1")
	    ...

and

	def getFccAnalysis( self ):
	    ...
            fccanalysis = FccAnalysis()
	    fccanalysis.setVersion("v0.9.1")
	    ...

[Test_FullCVMFSTests.py](https://gitlab.cern.ch/CLICdp/iLCDirac/ILCDIRAC/blob/Rel-v26r0/Interfaces/API/NewInterface/Tests/Test_FullCVMFSTests.py)

in updating the path of FCCSW CVMFS installation :

	myFccSwPath = "/cvmfs/fcc.cern.ch/sw/0.8.1/fccsw/0.8.1/x86_64-slc6-gcc62-opt"

to

	myFccSwPath = "/cvmfs/fcc.cern.ch/sw/0.9.1/fccsw/0.9.1/x86_64-slc6-gcc62-opt"


## 5 - Sandboxes and Data


As you know, a job may have input files and/or output files.

These files can be part of the sandbox or the data.

By default, log file, application script and output file follow this convention for the naming :

JobID_ID_APPLICATIONNAME_APPLICATIONVERSION_APPLICATIONSTEP**.**(log, root or sh)


### a - Sandboxes

There are the input sandbox and the output sandbox.

The input sandbox contains files the job may use as input like a configuration file or a steering file coming usually from your local machine.

The output sandbox contains files generated by the job, you want to retrieve.

Generally, we have here "small" files like log files, standard output, standard error.

The input sandox is uploaded with the job to the worker node (executing machine).

How to set the input sandbox :

	job.setInputSandbox('my_input_file')

Notice that you can also specify a list for the input files (folders are also accepted).

The output sandbox is uploaded to the DIRAC database.

How to set the output sandbox :

	job.setOutputSandbox('my_input_file')

Notice that you can also specify a list for the output files.

**WARNING**

Your output files (job's results) are not getting back to your local machine when the job is finished, they are stored :
	
-	in the DIRAC database if you set the output sandbox and if this one is smaller than 10 Mb
-	in the DIRAC File Catalog (as data) if you set the output sandbox and if this one is bigger than 10 Mb

You have to use a specific command if you want to download the output sandbox (see [Monitoring section](#6---monitoring)).

### b - Data

Sandboxes can not exceed 10 Mb, so if your job generates output files with a total size bigger than 10 Mb (e.g. root file), or need input files
with a total size bigger than 10 Mb, you need to use respectively output data and input data.

In general, these files reside in permanent storage elements like EOS, CASTOR etc...

#### 1 - Output Data

Files **produced** by the job are known as **Output Data** that can be specified like this :

	job.setOutputData(lfns = "my_root_file.root", OutputPath = "Simulation", OutputSE = "CERN-DST-EOS")

Here is a list of CERN storage elements :

[Storage Elements](https://twiki.cern.ch/twiki/bin/view/CLIC/DiracForUsers#Storage_Elements)

Notice that you can also specify a list for the output data (lfns parameter).

You can specify the ouptut file name you want to store permanently in the storage of your choice (e.g. CERN EOS resources).

**my_root_file.root** has to be generated by the job else an error will be raised.

Here is the workflow of outputing data :

First the file **my_root_file.root** is registered to the DIRAC File Catalog with a LFN (Logical File Name) :

	/ilc/user/u/username/Simulation/my_root_file.root

As DIRAC is VO oriented, its components like the File Catalog is VO oriented as well.

So this LFN is choosen by the system, it takes the VO name followed by the initial and the username.

You can only specify a subpath which is the OuputPath e.g. : "Simulation"

Finally the file will be uploaded to these physical locations :

For **Castor** :

	/castor/cern.ch/grid

For **EOS** :

	/eos/experiment/clicdp/grid

For our case, it will be :

	/eos/experiment/clicdp/grid/ilc/user/u/username/Simulation/my_root_file.root

Precisely, these are the StorageElements used by the File Catalog which are VO specific.

So once the FCC VO will be created (if it is not yet the case), these physical locations will change and specified into :

**Resources/StorageElements** section of the **dirac.cfg** file used by the DIRAC configuration service on the server.

#### 2 - Input Data

Files **consumed** by the job are known as **Input Data** that can specified like this :

	job.setInputData("/ilc/user/u/username/my_root_file.root")

Notice that you can also specify a list for the input data (folders are also accepted).

In specifying file by its LFN, it will look for this input data into the File Catalog then it will download the data with the job from the closest site (e.g. CERN).

Data can also have replicas in many sites.

## 6 - Monitoring

### a - Command Line Interface


How to check your job status :

	dirac-wms-job-status YOUR_JOB_ID


How to get back the output sandbox :

	dirac-wms-job-get-output YOUR_JOB_ID

How to browse the File Catalog (data) :

	dirac-dms-filecatalog-cli

Basic operations on the File Catalog can be found here :

[DIRAC File Catalog tutorial](https://github.com/DIRACGrid/DIRAC/wiki/FileCatalog)


### b - Web Portal


Here is the link to monitor ILCDirac jobs and data from the web. If you are not affiliated with ILC, please refer to your tutorial dedicated for DIRAC of your VO or contact your VO manager to know the right web address.


[ILCDirac web portal](https://ilcdirac.cern.ch/DIRAC/?view=tabs&theme=Grey&url_state=1|*DIRAC.FileCatalog.classes.FileCatalog:*DIRAC.JobMonitor.classes.JobMonitor:,)



On the left side, click on **Job Monitor** :

![IMAGE NOT AVAILABLE](tutorial_images/jobmonitor.png "job monitoring")


On the right side, click on 'refresh' :

![IMAGE NOT AVAILABLE](tutorial_images/refresh.png "job status")

By right-clicking on the job id, you can download logs and sandboxes.


On the left side, click on **File Catalog** :

![IMAGE NOT AVAILABLE](tutorial_images/fcbr.png "file catalog monitoring")


On the right side, browse your file by looking for its LFN :

![IMAGE NOT AVAILABLE](tutorial_images/fcdata.png "file catalog data")


**Congratulations !!!**

You ran FCC Jobs on the GRID.

DIRAC is a powerfull framework and we decided to show you here only some basic functionalities.

Notice that we are using user jobs (UserJob) and it could be interesting to test production jobs (ProductionJob) with FCC applications for people interested in doing productions.

## 7 - Advanced


### a - Job Splitting

Bulk submission is natively implemented in DIRAC.

In designing Fcc applications, we introduced a simplified interface for job splitting to make your life easier :)

How to send 2 jobs with each a number of events of 4 :

	job.setSplitEvents(numberOfJobs = 2, eventsPerJob = 4) 

How to send 2 jobs with a total number of events of 5 (it will compute 3 events for the 1st job and 2 events for the second) :

	job.setSplitEvents(numberOfJobs = 2, totalNumberOfEvents = 5)

How to send a set of input data per job :

	job.setSplitInputData(['/ilc/user/u/username/data1.root','/ilc/user/u/username/data2.root','/ilc/user/u/username/data3.root'], NUMBER_OF_DATA_PER_JOB)

When splitting is used, the seed is set differently for each job, it is equal to the ID of the job which supposed to be unique.

The setting of the event and the seed is automatically set by :

- appending another configuration file to GAUDI for FccSw (for the seed, the default random generator used is : **HepRndm::Engine&lt;CLHEP::RanluxEngine&gt;**)
- overwritting card files for Pythia


### b - HTCondor submission with DIRAC

Dirac proposes also python interfaces for Condor, LSF and others BATCH systems to submit jobs to local BATCH system.

```

from DIRAC.Core.Base import Script
Script.parseCommandLine()


from DIRAC.Resources.Computing.BatchSystems.Condor import Condor

exe = os.path.realpath('temp.sh')
out = os.path.realpath('condor_dirac')
options = ''

condor = Condor()
condor.submitJob(Executable=exe, OutputDir=out, SubmitOptions=options)

```

Do not forget to set the DIRAC environment and check the status of your condor job by typing :

	condor_q

There exists already a python API for HTCondor but at the moment we wrote this tutorial, submission was not possible until the next release of HTCondor.

## 8 - Developer Notes

### a - FCC integration in image

![IMAGE NOT AVAILABLE](tutorial_images/integration.png "FCC inside ILCDirac")

### b - FCC integration in words

The DIRAC instance of ILC called ILCDirac is available on gitlab :

[ILCDirac](https://gitlab.cern.ch/CLICdp/iLCDirac)

FCC software in ILCDirac consists of 2 modules :

[Fcc.py](https://gitlab.cern.ch/CLICdp/iLCDirac/ILCDIRAC/blob/Rel-v26r0/Interfaces/API/NewInterface/Applications/Fcc.py)

[FccAnalysis.py](https://gitlab.cern.ch/CLICdp/iLCDirac/ILCDIRAC/blob/Rel-v26r0/Workflow/Modules/FccAnalysis.py)

and their corresponding tests :

[Test_Fcc.py](https://gitlab.cern.ch/CLICdp/iLCDirac/ILCDIRAC/blob/Rel-v26r0/Interfaces/API/NewInterface/Tests/Test_Fcc.py)

[Test_FccAnalysis.py](https://gitlab.cern.ch/CLICdp/iLCDirac/ILCDIRAC/blob/Rel-v26r0/Workflow/Modules/Test/Test_FccAnalysis.py)

Adding splitting stuff implied to update user job of ILCDirac :

[UserJob.py](https://gitlab.cern.ch/CLICdp/iLCDirac/ILCDIRAC/blob/Rel-v26r0/Interfaces/API/NewInterface/UserJob.py)

and its corresponding test :

[Test_UserJob.py](https://gitlab.cern.ch/CLICdp/iLCDirac/ILCDIRAC/blob/Rel-v26r0/Interfaces/API/NewInterface/Tests/Test_UserJob.py)

Adding FCC applications implied to update modules testing all existing applications :

[LocalTestObjects.py](https://gitlab.cern.ch/CLICdp/iLCDirac/ILCDIRAC/blob/Rel-v26r0/Interfaces/API/NewInterface/Tests/LocalTestObjects.py)

[Test_FullCVMFSTests.py](https://gitlab.cern.ch/CLICdp/iLCDirac/ILCDIRAC/blob/Rel-v26r0/Interfaces/API/NewInterface/Tests/Test_FullCVMFSTests.py)

And for these tests, we upload the following files to make the applications run :

For FccAnalysis :

[ee_ZH_Zmumu_Hbb.txt](https://gitlab.cern.ch/CLICdp/iLCDirac/ILCDIRAC/tree/Rel-v26r0/Testfiles/ee_ZH_Zmumu_Hbb.txt)

For FccSw :

[geant_fastsim.py](https://gitlab.cern.ch/CLICdp/iLCDirac/ILCDIRAC/tree/Rel-v26r0/Testfiles/geant_fastsim.py)


**IMPORTANT**

FccSw needs Detector folder which is not present on the release **v0.8.1**, so it will not run.

Then, from the next release, you have to uncomment this method (of the module [Test_FullCVMFSTests.py](https://gitlab.cern.ch/CLICdp/iLCDirac/ILCDIRAC/blob/Rel-v26r0/Interfaces/API/NewInterface/Tests/Test_FullCVMFSTests.py) Line 308 to Line 315) :

```

# TO UNCOMMENT when Detector folder of FCCSW will be on CVMFS
#def runFccSwTest():
#  """runs the fccsw test only"""
#  #Script.parseCommandLine()
#  suite = unittest.TestSuite()
#  suite.addTest(JobTestCase('test_fccsw'))
#  testResult = unittest.TextTestRunner( verbosity = 1 ).run( suite )
#  print testResult

```

And you have also to update the FCCSW installation path if you want to use an other release (Line 65) :

    myFccSwPath = "/cvmfs/fcc.cern.ch/sw/0.8.1/fccsw/0.8.1/x86_64-slc6-gcc62-opt"


Adding FCC applications implied to update module's namespace :

[__init__.py](https://gitlab.cern.ch/CLICdp/iLCDirac/ILCDIRAC/blob/Rel-v26r0/Interfaces/API/NewInterface/Applications/__init__.py)


For any questions or any further informations, please contact us at : fcc-experiments-sw-devATSPAMNOTcern.ch
