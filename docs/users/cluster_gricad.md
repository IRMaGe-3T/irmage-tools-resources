
# Using GRICAD clusters for neuroimaging tools

This part aims to provide examples and scripts for using neuroimaging tools on [GRICAD](https://gricad.univ-grenoble-alpes.fr) clusters. 

Warning:

- The storages accessible from the clusters are not meant for storing your data. It is only meant for processing your data (the results need to be transferred to your computer)
- Data used on the cluster should be anonymized (no name / no personal info)

## Prerequisites

Please follow the [instructions](https://gricad-doc.univ-grenoble-alpes.fr/hpc/description/) provide by GRICAD team  to access to the clusters. 

The main steps are:

1.	Create an account on [PERSEUS](https://perseus.univ-grenoble-alpes.fr)

2.	Join a project. A project exists for IRMaGe (pr-irmage). If you want to join it, please get in touch with your contact at IRMaGe. If you want to access to the containers and scripts provided by IRMaGe you need to join this project. 

3.	Read the description about the [main infrastructure](https://gricad-doc.univ-grenoble-alpes.fr/hpc/description/) and about the [data management](https://gricad-doc.univ-grenoble-alpes.fr/hpc/data_management/). 

4.	Configure your access to the [Dahu cluster](https://gricad-doc.univ-grenoble-alpes.fr/hpc/connexion/) and test your configuration. 

In the rest of the tutorial, we suggest using Bettik for data storage and the Dahu cluster.

## Use containers for neuroimaging on the clusters (MRIQC, fMRIPrep...)

As Docker containers cannot run on clusters, it is necessary to convert Docker image on a Apptainer image. We provide some classic BIDS application and others containers in Apptainer format that can be used on GRICAD clusters. 

If needed, you can create your own Apptainer container. 

On the PERSEUS IRMaGe project (pr-irmage), the Apptainer images available are in the folder `/bettik/PROJECTS/pr-irmage/COMMON/apptainer_images/`.

Available images:

- fmriprep_24-1-1.sif 

- mriqc_24-1-0.sif

To use these images, follow these instructions:

**1. Prepare your data on your local computer**

Your data must be in BIDS format for fMRIPrep and MRIQC. 

**2. Data transfer to Bettik folder**

Please see [Gricad documentation](https://gricad-doc.univ-grenoble-alpes.fr/hpc/data_management/data_transfer/).
You can use rsync / ftp / scp via `cargo.univ-grenoble-alpes.fr`.

For the IRMaGe project, please transfer your data to your personal repository on the project  `/bettik/PROJECTS/pr-irmage/login-perseus` or create a repository for your project on `/bettik/PROJECTS/pr-irmage/COMMON` (in this case, all the user of pr-irmage will have acess to your data).

`local-login@my-computer:~$ rsync -avxH /path/to/local/data/ login-perseus@cargo.univ-grenoble-alpes.fr:/bettik/PROJECTS/pr-irmage/login-perseus`

**3. Connection to Dahu cluster via SSH bastion**

First, connect to the bastion, it will connect you to either trinity or rotule server:

`local-login@my-computer:~$ ssh login-perseus@access-gricad.univ-grenoble-alpes.fr`

Then, connect to Dahu cluster:

`login-perseus@rotule:~$ ssh dahu`

You are now connected to the Dahu frontal:

`login-perseus@f-dahu:~$`

Do not run directly Apptainer images or others scripts on it ! You need first to request resources.

**4. Request resources using resource manager OAR and prepare .sh script**

Please see [Gricad documentation](https://gricad-doc.univ-grenoble-alpes.fr/hpc/joblaunch/job_management/)

To request resources via OAR, you can either use a script in bash, which will also allow you to run our processes, or you can use interactive way. It is recommended that you use a bash script unless you are running a test.

To use fMRIPrep or MRIQC images, copy on your Bettik repository the corresponding bash script:

- for fMRIPrep: `/bettik/PROJECTS/pr-irmage/COMMON/apptainer_images/run_fmriprep.sh`

- for MRIQC: `/bettik/PROJECTS/pr-irmage/COMMON/apptainer_images/run_mriqc.sh`

For example: 

`login-perseus@f-dahu:~$ cp /bettik/PROJECTS/pr-irmage/COMMON/apptainer_images/run_mriqc.sh /bettik/PROJECTS/pr-irmage/login-perseus/run_mriqc_studyXX.sh`

Open the copied script.

`login-perseus@f-dahu:~$ nano /bettik/PROJECTS/pr-irmage/login-perseus/run_mriqc_studyXX.sh`

Several lines need to be modified:

- `export DATA=/bettik/PROJECTS/pr-irmage/perseus-login/DATA_BIDS`: add the correct path to your data on bettik

- `#OAR --stdout /bettik/PROJECTS/pr-irmage/perseus-login/DATA_BIDS/derivatives/fMRIprep.out`: path to a file with out information (could be in your derivatives directory)

- `#OAR --stderr /bettik/PROJECTS/pr-irmage/perseus-login/DATA_BIDS/derivatives/fMRIprep.err`:  path to a file with potential error(could be in your derivatives directory)
 
- `#OAR -l /nodes=1,walltime=26:00:00`: specify the desired parameters (nodes / CPU, walltime...). 

You can also change the main command (for exemple if you want to run only one subject or if you want to run only bold or anat for MRIQC).In this case, please refer to MRIQC and fMRIPrep documentation. 
 
Nodes / CPU parametres will depend on your number of subjects / number of sequences. Check [gricad documentation](https://gricad-doc.univ-grenoble-alpes.fr/hpc/joblaunch/job_management/#commandes-oar-de-gestion-des-jobs) to chose –l parameter and walltime.

*OAR parameters example for MRIQC:*

- for 4 subjects with one session and with 5 fMRI each: #OAR -l /CPU=2/core=12,walltime=01:00:00


*OAR parameters example for fMRIPrep:*

- for one subject with one fMRI: #OAR -l /CPU=16,walltime=02:00:00

- Please see [fMRIPrep recommendation](https://fmriprep.org/en/stable/faq.html#how-much-cpu-time-and-ram-should-i-allocate-for-a-typical-fmriprep-run)

- /!\ It seems that [running subject in parrallel could be an issue](https://fmriprep.org/en/stable/faq.html#running-subjects-in-parallel). In this case you can try to use the proposed solution.


Then you need to make the script executable:

`login-perseus@f-dahu:~$ chmod +x /bettik/PROJECTS/pr-irmage/login-perseus/run_mriqc_studyXX.sh`

**5. Submit the script**

To submit your job use the oarsub command: 

`login-perseus@f-dahu:~$ oarsub -S /bettik/PROJECTS/pr-irmage/login-perseus/run_mriqc_studyXX.sh`

You will get an OAR_JOB_ID and you can check the job progress with oarstat command:

`login-perseus@f-dahu:~$ oarstat -f -j OAR_JOB_ID`

Or:

`login-perseus@f-dahu:~$ oarstat –u login-perseus`

It will give you information about state (waiting/ running / finishing), scheduledStart.

If there are errors while the spcript is running, you will find the errors in the `.err` file.

**6. Download your results**

From your local computer:

`local-login@my-computer:~$ rsync -avxH  login-perseus@cargo.univ-grenoble-alpes.fr:/bettik/PROJECTS/pr-irmage/login-perseus/DATA_BIDS/derivatives /path/to/local/data/`

**7. Remove your data from bettik**

Once all your processings are done, delete your data: 

`login-perseus@f-dahu:~$ /bettik/PROJECTS/pr-irmage/login-perseus/DATA_BIDS/`


