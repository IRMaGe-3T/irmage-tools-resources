
# The Brain Imaging Data Structure (BIDS)

## BIDS main principles 

The Brain Imaging Data Structure ([BIDS](https://bids.neuroimaging.io/)) is a standardized format for organizing and describing neuroimaging data and study outputs.
Having a standardized format facilitates data reuse/sharing. 

Moreover, [several software](https://bids-apps.neuroimaging.io/apps/ ) take a BIDS formatted dataset as input.

You can follow [BIDS starter kit](https://bids-standard.github.io/bids-starter-kit/) to learn about BIDS. 

Note that BIDS specifications are not perfect and may be not detailed enough for complex dataset, so you may have to adapt a little bit BIDS specifications for complex dataset. 
You can also participated to [extend BIDS specification]( https://bids.neuroimaging.io/get_involved.html) (for example for CT data). 

[BIDS specification](https://bids-specification.readthedocs.io/en/stable/) define how a dataset should be organized. 

Overall directories hierarchy is ([] when non mandatory):
```
├──<dataset>/
|  ├──[sourcedata] /	         → non modified data (for example DICOM files)
|  ├──[code/]	                 → Source code of scripts 
|  ├──[derivatives/]	         → Analysis result 
|  ├──rawdata/                   → data converted (data converted in NifTI format)
|  ├──participants.tsv	         → Subjects list 
|  ├──dataset_description.json   → JSON file describing the dataset
|  ├──[README]                   → Text file describing the dataset in more details 
|  ├──[CHANGES]	                 → Version history of the dataset
```

All imaging data are stored using the NIfTI file format in the rawdata directory.  
Since the NIfTI standard offers limited support for the various image acquisition parameters available in DICOM files, additional meta information extracted from DICOM files are stored in a JSON file (with the same file name as the .nii[.gz] file, but with a “.json” extension).
The hierarchy of rawdata directories is the following: 
```
├──rawdata/
|  ├──sub-<participant_label>/
|  |   ├──ses-<session_label>/
       |   ├──<data_type>/
```
with the following definitions:

- sub: subject pseudonym code;

- ses: time point, representing one visit of a subject for an exam.

- datatype: functional group of different types of data (anat, func, dwi, ct ...)

Each filename consists of a chain of entity instances and a suffix all separated by underscores, and an extension. 
The [entities](https://bids-specification.readthedocs.io/en/stable/appendices/entity-table.html) used depends on the file datatype and the file modality (category of brain data recorded such as T1w, T2W, bold for MRI data). 

 
Example for one subject with one session : 
```
├──sub-0010001AA/
|   ├──ses-M00/
|   |   ├──anat/
|   |   |   ├──sub-0010001AA_ses-M00_run-1_T1w.nii.gz
|   |   |   ├──sub-0010001AA_ses-M00_run-1_T1w.json
|   |   |   ├──sub-0010001AA_ses-M00_run-1_T2w.nii.gz
|   |   |   ├──sub-0010001AA_ses-M00_run-1_T2w.json
|   |   |   ├──sub-0010001AA_ses-M00_run-1_FLAIR.nii.gz
|   |   |   ├──sub-0010001AA_ses-M00_run-1_FLAIR.json
|   |   ├──func/
|   |   |   ├──sub-0010001AA_ses-M00_task-rs_run-1_bold.nii.gz
|   |   |   ├──sub-0010001AA_ses-M00_task-rs_run-1_bold.json
|   |   ├──dwi/
|   |   |   ├──sub-0010001AA_ses-M00_run-1_dwi.nii.gz
|   |   |   ├──sub-0010001AA_ses-M00_run-1_dwi.bval
|   |   |   ├──sub-0010001AA_ses-M00_run-1_dwi.bvec
|   |   |   ├──sub-0010001AA_ses-M00_run-1_dwi.json
```

Note that there is specific recomendation for [field map data](https://bids-specification.readthedocs.io/en/stable/04-modality-specific-files/01-magnetic-resonance-imaging-data.html#fieldmap-data) and for [ASL data](https://bids-specification.readthedocs.io/en/stable/04-modality-specific-files/01-magnetic-resonance-imaging-data.html#arterial-spin-labeling-perfusion-data).

## Validate BIDS folder

Before to use your dataset with a BIDS-apps, you can use the [BIDS validator](https://bids-standard.github.io/bids-validator/) to ensure that your data are BIDS-compilant.

## Convert dataset in BIDS format

Several [software](https://bids.neuroimaging.io/benefits#mri-and-pet-converterss) exist to convert DICOM or NIfTI in BIDS format. 
Each software have pro and cons and it is not fully automatic

### Using dcm2bids (Linux)

[dcm2bids](https://unfmontreal.github.io/Dcm2Bids/) reorganizes NIfTI files using dcm2niix into BIDS.

#### Installation 

Install dcm2bids using pip : 

`pip3 install --user dcm2bids`

Dependencies : 

[dcm2niix](https://github.com/rordenlab/dcm2niix) should be installed and dcm2niix path should be included in your $PATH (in your .bashr)


#### Use 
You will need to have a directory with your subject DICOM (DICOM_DIR, one folder by subject) 

Create your [config file](https://unfmontreal.github.io/Dcm2Bids/3.1.0/how-to/create-config-file/). 
Each description in this file tells dcm2bids how to group a set of acquisitions and how to label them.
You can used several criteria (that corresponds to json field in the json creating by dcm2niix) to describe your acquisition (SeriesDescription, EchoTime, ImageType..)  

Example of a simple config file (BIDS_config.json): 
```
{
    "descriptions": [
        {
            "datatype": "anat",
            "suffix": "T1w",
            "criteria": {
                "SeriesDescription": "*3DT1*",
                "EchoTime": 0.1
            }
        },
        {
            "datatype": "func",
            "suffix": "bold",
            "custom_entities": "task-rest",
            "criteria": {
                "ProtocolName": "func_task-*",
                "ImageType": ["ORIG*", "PRIMARY", "M", "MB", "ND", "MOSAIC"]
            }
        }
    ]
}
```

Create your BIDS directory (OUTOUT_DIR): `mkdir OUTPUT_DIR`

Create the BIDS structure : `dcm2bids_scaffold -o OUTPUT_DIR`

Run dcm2bids: `dcm2bids -d DICOM_DIR -p PARTICIPANT_ID -c CONFIG_FILE -o OUTPUT_DIR`

If your config file is precise enough, your data should be now organized in BIDS.

You can check the data not renamed (and so not integreted in your BIDS databse) in the `tmp_dcm2bids` folder create in the OUTOUT_DIR.
If you want to included some of this data in your BIDS database you should add more crietria in your config file. 

#### How to do in practice for a big dataset ? 

There are several methods to run dcm2bids quickly on several subject, here is one:

- Organise your DICOM data as follows (where "subject1" is the desired name in the BIDS architecture): 
```
├──DICOM_sourcedata/
|   ├──subject1/
|   |   ├──DICOM/
|   ├──subject2/
|   |   ├──DICOM/
|   ├──subject3/
|   |   ├──DICOM/
|   ├──subject4/
|   |   ├──DICOM/
```

- Create your config file, your BIDS directory and structure as explain above. 

- Use this python code:
```
import glob
import os

CONFIG_FILE = '/home/username/dataset_bids/config.json'
OUTPUT_DIR = '/home/username/dataset_bids'
DICOM = glob.glob('/home/username/DICOM_sourcedata/*/*')

for folder in DICOM:
    if os.path.isdir(folder):
        id_sub = folder.split('/')[-2].replace('_','')

        cmd = 'dcm2bids -d ' + folder + ' -p ' + id_sub + \
            ' -c ' + CONFIG_FILE + ' -o ' + OUTPUT_DIR
            
        os.system(cmd)
```

