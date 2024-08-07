# Quality Control guide

WORK IN PROGRESS

## Introduction

The purpose of this section is to provide advice on how to perform quality control (QC) on raw MRI data for clinical research studies,specifically focusing on anatomical and functional MRI data.
The idea is to suggest a visual QC approach, ideally using existing software that generates quality reports and metrics (e.g., MRIQC software).

There are various methods for conducting quality control on raw data and this section is juste one of them. The most crucial aspect is to closely examine the data to better understand it and accurately interpret the analyses.

## General advices 

- During the acquisition of an MRI sequence, various issues may arise and may affect image quality. These can include artifacts related to the MRI scanner, image reconstruction issues (e.g., folding), or choices made during acquisition (e.g., incorrect field of view). 
Additionally, there may be physiological artifacts related to the patient (e.g., movements). Performing quality control on the data helps identify data that should be excluded because they could interfere with the analyses. The goal is to determine whether the image can be used to answer the study's questions.

- Ideally, an initial data check should be performed during acquisition to potentially redo any problematic sequences (if possible). For example, if a subject moved significantly during one of the main protocol sequences, it might be more useful to redo that sequence rather than completing the optional sequences (if there are any).

- A "good data" from a quality control perspective does not necessarily mean that the chosen sequence is suitable for the intended application. The selected parameters may be inadequate for the planned analyses (e.g., significant signal loss in the area of interest due to the chosen parameters). Therefore, it is important to discuss with an MRI physicist before starting acquisitions to properly set up the sequences and conduct pilot subjects. If a particular area is crucial for data analysis (e.g., if fMRI activation is expected in this area or, for anatomicatl data, if this area should be segmentated), it is useful to add an exclusion criterion for data based on the quality of that specific area.

- Currently, there is no consensus on how to perform QC; there is no single "correct way" to conduct QC (different tools, methodologies, and sometimes different definitions for quantitative values). Some rejection criteria for an image may depend on the study and the analyses to be performed. To maintain consistency in quality control, it is important to follow the same QC steps within the same study.

- It is sometimes useful to use pre-processing to perform QC on raw data because it helps to better understand the data. For example, for an anatomical sequence, it might be useful to check if the segmentation of white/gray matter is done correctly. For a diffusion sequence, it might be useful to look at reconstructions maps like FA.

- This section focuses on image quality, but for functional MRI data, it is also useful to have a method for verifying if the subject performed the task correctly/if the measurements were properly recorded.

- It is important to document the QC steps and results in an understandable manner to share the QC results along with the data (in an Excel file, for example).

## Verification of the data "integrity" and of the parameters

The first step is to verify the "integrity" of the data, meaning ensuring that the data is ready for analysis. Here is a non-exhaustive list of things that are useful to check:

- Verification of the database consistency in terms of subject identifiers and session dates.

- Verification of the sequences received per subject (do all subjects have all the sequences of the protocol? The mandatory sequences? Are any sequences duplicated?). It is useful to document this information (in an Excel table, for example).

- Checking that the DICOM files are complete. In "classic" mode, a DICOM file is generated for each acquired image (slice, dynamic, echo, etc.) and so there are several DICOM files for one sequence. In "Enhanced" mode, a single file is generated for each sequence (with a certain size limit). In classic mode, it is possible that an export or transfer error results in missing some DICOM files, and thus some images. It may be useful to check the size of the images converted to NIfTI to highlight such problems. This check can also be done during the visual inspection of the images.

- Verification of the main acquisition parameters. Some parameter modification may have been made during the coyrse of the study and may influence the analyses (eg, modification of repetion time following an upgrade of the MRI software). Here is a non-exhaustive list of the parameters that may be useful to check: echo time, repetition time, voxel size, number of repetitions for functional MRI, parallel imaging... Depending on the sequence, certain parameters are more important to check than others.


## QC of anatomical and functional data with MRIQC

In this section, we propose to use MRIQC to perform QC of anatomical and functional data. 
The idea is to use the visul report to perform a data QC. However, it is useful to open the image in a specific viewer in case of doubt about image quality, or to see the different dynamics of a functional sequence.

To use MRIQC check out the documentation [here](mriqc.md) or directly the [MRIQC documentation](https://mriqc.readthedocs.io/).

Once the MRIQC's results are available,for each subject, open the MRIQC report (explanation can be found [here](https://mriqc.readthedocs.io/en/latest/reports.html#demo-anatomical-reports)).

The report contains several mosaics (mean signal, zoomed-in on the brain, image with background noise enhancement...). For functional data, there's also a summary graph, including a plot for framewise displacement (FD) and a carpetplot. The FD represents the displacement of the subject's head. Each line of the carpetplot represents the value of a voxel over time (separated by region). 

Check each mosaic and graph and check whether any of the criteria proposed and detailed below are present and whether this should lead to the exclusion of the data for analysis.

Very often, certain artifacts are present on the image but do not imply that the image should be excluded. In such cases, it may be useful to report the presence of the artifact anyway.

One solution is to report the information in an Excel spreadsheet, with a column for reporting excluding criteria and a column for non-excluding criteria (and comments, if needed): 

![Excel example](images/qc_excel_example.png "Excel example")

In case of doubt or if the visual report is not precise enough, open the image in a specific viewer and review the different slices / dynamics.


### Structural T1w MRI

In this section, we consider a non-contrast T1 anatomical sequence.

We propose a list of criteria that may lead to the exclusion of an anatomical image. This list may need to be adjusted according to the study criteria and the planned analyses. If a specific area is critical for the study (e.g., the hippocampus if the study aims to segment the hippocampus), it may be useful to add a QC criterion for this area ("is there an artifact in this area?").

Some criteria are based on the images available in the MRIQC report (alignment in MNI, segmentation, etc.). Other criteria can be used by simply viewing the image in a viewer.

**Proposed Quality Control criterion**:

|    | Descriptions
 -- | -- 
A |Gadolinium-injected sequence
B |Non-compliant brain coverage according to the protocol or abnormal subject positioning (subject rotation)
C |Significant movement artifacts (“wrinkles” or “blur” or cortex duplication) or in a critical area for the study
D |Significant signal loss (susceptibility artifact) or in a critical area for the study
E |Eye artifacts spill over to the brain
F |Significant non-uniformity of intensity (bias inhomogeneity)
G |Background noise or folding ghost artifact with an impact on the brain
H |Very low gray/white matter contrast
I |Inconsistent segmentations
J |Poor alignment in MNI
K |Unexpected anatomical anomalies/pathologies not covered by the protocol
L |Other artifacts

How to check each criteria is detailed below with examples. 

#### A. Gadolinium-injected sequence
Look at the first mosaic ("Zoomed-in mosaic view of the brain") in the report.

/!\ *When you're not an expert, it can be very difficult to see the difference between injected and non-injected sequences.*

![T1w with and without gadolinium](images/qc_T1w_gadolinium.png "T1w with and without gadolinium")

**Figure** :  **A1**: *T1W without gadolinium* **A2**: *Gadolinium-injected T1w (from https://doi.org/10.1016/j.media.2021.102219.)* **A3**: *Gadolinium-injected T1w*.


#### B. Non-compliant brain coverage according to the protocol or abnormal subject positioning (subject rotation)

/!\ *In the case of certain studies, total non-coverage of the brain may be deliberate, so check the acquisition protocol.* 

Look at the first mosaic in the report ("Zoomed-in mosaic view of the brain"), in particular the extreme sections (bottom and top of the brain) and the sagittal mosaic, which allows you to quickly see whether or not the brain is fully covered. 

#### C.Significant movement artifacts (“wrinkles” or “blur” or cortex duplication) or in a critical area for the study

Look at the first mosaic ("Zoomed-in mosaic view of the brain") in the report. 

Head movements during acquisition result in the appearance of lines that are rather concentric ("wrinkles" / "ripples") or a "blur" or duplication in the cortex in certain parts or throughout the image.
Depending on the planned analysis on the anatomical sequence, it may be acceptable to retain sequences with slight movements.

It is important to know the areas of interest in the study (or the subjects' pathology). For example, if the aim of the study is to segment the hippocampus, movement artifacts in the hippocampus will require the image to be excluded, whereas movement artifacts in the cerebellum will not.

![T1w with movements](images/qc_movements.png "T1w with movement")
**Figure**: **A and B**: *Wrinkles, the image is not necessarily to be excluded, it depends on the analyses planned* **C**: *Movement is very important (wrinkles + blur), to be excluded if segmentation analyses are to be carried out.*

We can also sometimes observe a so-called "Gibbs" artifact (truncation artifact), which is sometimes difficult to distinguish from motion (which is why it is discussed here in the same exclusion criterion). 
This artifact generates fine lines at high-contrast interfaces. 

![T1w with Gibbs artifact](images/qc_gibbs.png "T1w with Gibbs atifact")

**Figure**: *Gibbs artifact (from https://doi.org/10.1007/978-3-030-85413-3_102)*


#### D. Significant signal loss (susceptibility artifact) or in a critical area for the study

Look at the first mosaic in the report ("Zoomed-in mosaic view of the brain"). 

Susceptibility artefacts due to the non-uniformity of the field are mainly present at air/tissue interfaces or close to metallic objects and result in a loss of signal. The regions most affected are the prefrontal cortex and the region near the ear cavities.

![T1w suceptibility atifact](images/qc_T1w_suceptibility.png "T1w suceptibility atifact")

**Figure**: **a**. *Very slight susceptibility artefact near the ear cavities (the brain appears to be slightly nibbled), there is no need to exclude the image.* **b**. *Susceptibility artefact near the teeth caused by a metal object. This does not affect the brain, there is no need to exclude the image*

#### E. Eye artifacts spill over to the brain

Look at the first mosaic in the report ("Zoomed-in mosaic view of the brain"). 

If there are stong eyes movements, an overlap pf the eye signal in the brain may be observed. If the overlap is strong and/ or impacts regions of interest, it may be necessary to exclude the image.

![T1w eye spillover](images/qc_eye_spillover.png "T1w eye spillover")

**Figure**: *Eye artifacts spill over to the brain (green arrow) (from https://doi.org/10.1016/j.media.2021.102219)* 

It is also possible that the eyes movements are visible only in the background of the image without impact on the brain, in this case it seems not necessary to exclude the image.

#### F. Significant non-uniformity of intensity (bias inhomogeneity)

Look at the first mosaic in the report ("Zoomed-in mosaic view of the brain"). 

This non-uniformity is characterised by a variation in intensity in the brain, for example the white matter will be darker in the anterior regions than in the posterior regions of the brain. 

There is always a slight bias inhomogeneity on the T1w image. This inhomogeneity can be corrected during post-processing. However, if it is too strong, the correction will not be sufficient and segmentation of white ang grey matter with software such as SPM may be problematic. The image may be excluded if the bias inhomogeneity is too strong. This may be due to an issue with the coil.

#### G. Background noise or folding ghost artifact with an impact on the brain

Look at the "Zoomed-in mosaic view of the brain" and "View of the background of the anatomical image" mosaics.

The term "aliasing ghost" is used when the background noise is structured and appears as a shifted repetition of the brain. The image should be excluded if it spills over into the brain.

![T1w background](images/qc_T1w_background.png "T1w background")

**Figure**: *Aliasing ghost (a shifted repetition of the brain appears in the background). It does not seem to impact the brain, it is not necessary to exclude the image (from https://doi.org/10.1016/j.media.2021.102219)* 

#### H. Very low gray/white matter contrast

Look at the first mosaic in the report ("Zoomed-in mosaic view of the brain"). 

If the contrast between the white and the grey matter is too low, segmentation with software such as SPM may be problematic. In extreme cases, it may be better to exclude the image from the analyses.  

#### I. Inconsistent segmentations

Look at «Brain extraction performance», «Head mask», «Brain tissue segmentation» mosaics.

If the tissue segmentation is not consistent, this may indicate potential issues when segmenting with automatic software. It will be necessary to check carefully the outputs of the segmentation performed in the analyses before using them.

Note that, in the MRIQC report, the head mask often appears to be inconsistent specifically near the teeth  and at the top of the brain.


![T1w head mask](images/qc_head_mask.png "T1w head mask")

**Figure**: *The head mask compute by MRIQC is inconsistent. However, it is not necessary to exclude the image* 

#### J. Poor alignment in MNI

Look at the «Spatial normalisation of the anatomical image» in order to check the MNI realignment.

If the realignment in the MNI space is not consistent, this may indicate potential issues when using automatic software. As the normalisation in the MNI performed in MRIQC is a quick and "dirty" normalisation, it may not be necessary to exclude the image but it will be necessary to check carefully the outputs of the normalisation performed in the analyses before using them.

#### K. Unexpected anatomical anomalies/pathologies not covered by the protocol

Look at the first mosaic in the report ("Zoomed-in mosaic view of the brain").

This may reveal anomalies not anticipated by the protocol (tumour, trace of a stroke).

/!\ Nothe that it is not the role of a non-medical person to detect anomaly and that it is difficult to "name" the anomaly correctly without special medical training. The aim of this stage is simply to exclude images with anomalies that could cause problems in the subsequent analyses and/or to exclude subjects (for example if we want to make an atlas of healthy subjects). **This step is in no way a diagnosis and should not be communicated to the patient without medical advice. In case of doubt, contact the doctor in charge of the study.** 

#### L. Other artifacts

Other rarer artifacts may lead to the exclusion of an image. 

### Functional EPI MRI

In this section, we consider a functional MRI obtained with an EPI sequence.

For fMRI acquisitions, we want to to obtain the highest possible signal-to-noise ratio (SNR) and contrast-to-noise ratio (CNR) while minimising the various artefacts. 

Artefacts may be related to the pulse sequence used, the equipment (antenna/gradient) and the subject (head movements, cardiac and respiratory 'noises'.....). 

Some artefacts are characteristic of EPI sequences:
- Spatial distortions due to inhomogeneity of the static field (susceptibility artefact). They are more significant as the field strength increases. These distortions appear locally in the form of stretched or compressed pixels along the phase encoding axis. It is possible to correct some of these distortions retrospectively.  
- Signal losses due to field inhomogeneities (susceptibility artefacts) near air/tissue interfaces.  Some acquisition parameters can help to reduce these signal losses (choice of an appropriate TE, increase number of slices.....). 
- Phantom images in the phase encoding direction. These are due to the fact that the odd and even lines in k-space are acquired with opposite polarity. Certain acquisition techniques can help to reduce the extent of these effects. 

We propose a list of criteria that may lead to the exclusion of an functional image. This list may need to be adjusted according to the study criteria and the planned analyses (specif ROI...). 

Some criteria are based on the images available in the MRIQC report (mean signal, standard deviation map, alignment in MNI, carpet plot, etc.). Other criteria can be used by simply viewing the image in a viewer.

**Proposed Quality Control criterion**:

|    | Descriptions
 -- | -- 
A |Non-compliant brain coverage according to the protocol or abnormal subject positioning (subject rotation)
B |Significant signal loss (susceptibility artifact) or in a critical area for the study
C |Excessive spatial distortions of the brain (susceptibility artifact)
D |High number of black slices, outliers, or hyperintensity in a slice
E |Significant movements or in a critical area for the study
F |Folding that impacts the brain
G |Background noise or folding ghost artifact with an impact on the brain
H |Unexpected anatomical anomalies/pathologies not covered by the protocol
I |Other artifacts

#### A. Non-compliant brain coverage according to the protocol or abnormal subject positioning (subject rotation)

/!\ *In the case of certain studies, total non-coverage of the brain may be deliberate, so check the acquisition protocol.* 

Look at the first mosaic in the report ("Voxel-wise average of BOLD time-series, zoomed-in covering just the brain") and especially the extreme slices (bottom and top of the brain) and the sagittal mosaic, which allows you to see quickly whether or not the area covered by the study is entirely covered. 

A bad coverage can be problematic for the normalisation of the image in a common space such as the MNI (see "Spatial normalization of the anatomical image" mosaic). Note that, in MRIQC, the normalisation performed is "quick and dirty" (without using anatomical image). If the normalisation is bad in MRIQC, it will be necessary ti check carefully the outputs of the normalisation performed in the analyses but not necessary to exclud the image. 


![fMRI coverage](images/qc_fmri_coverage.png "fMRI coverage")

**Figure**: **A**: *The top of the brain is cut, maybe not necessary to exclud the image* **B**: *Impact on the normalisation in MRIQC(MNI space)* 























