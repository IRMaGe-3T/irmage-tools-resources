# DICOM and NIfTI format

## DICOM format 

The images exported from an MRI scanner will be in DICOM format. 
It is the [international standard format](https://www.dicomstandard.org) for medical images and related information. 

Even if DICOM is a standard, there are a lot of differences between DICOM of each manufacturers (Philips, Siemens, GE...) and between the DICOM for each modality. 
Manufacturers publish DICOM conformance statement for each modality (for example [here](https://www.usa.philips.com/healthcare/resources/support-documentation/dicom-magnetic-resonance-imaging) for Philips MRI).

DICOM file are composed of 2 parts: 

- the image data (sometime compressed)
- the header that contains the metadata. In this part you can find tags fabout the scanner, the subject or the acquistions parameters. Note that each manufacturer has private tags that are not necessarily specified in the standard.

For "Classic DICOM" files, there is a DICOM file for each slice of the volume.  
You can aslo have "Enhanced DICOM" files and in this case, all the slices of the volume are stored in one DICOM file. The header is not structured in the same way forEnhanced and Classic DICOM.


### Others Philips data
Philips also allows to export data in PAR/REC format (an ASCII header (PAR) plus a binary blob (REC)) or  in XML/REC format. There are older formats contening less information than the DICOM format, and are therefore not recommended for use in new studies.

## Conversion into NIfTI 

The Neuroimaging Informatics Technology Initiative (NIfTI) is an open file format commonly used to store brain imaging data. This [article](https://brainder.org/2012/09/23/the-nifti-file-format/) summarizes information about this format. As the NIfTI format does not contain all the metadata, the NIfTI file is often paired with a file in json format that contains metadata information.


### Conversion into NIfTI using dcm2niix 
[dcm2niix](https://github.com/rordenlab/dcm2niix) software can be used to convert data from the DICOM format to the NIfTI format (with a json file).

There are specificities for each manufacturer (for example image scaling or information in json file), for Philips data please see [here](https://github.com/rordenlab/dcm2niix/blob/master/Philips/README.md).

Note that Philips DICOM do not contains some information as slice timing, phase encoding direction or total readout time.


If you want to organize your data in BIDS format, please see [here](BIDS.md)

