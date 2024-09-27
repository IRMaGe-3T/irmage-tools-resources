# Defacing 

For research project on human, it is important to de-identify MRI data and metadata (no identifying data as name, date of birth, addresses...). 

If your want to share your data outside your lab or outside a consortium, this deidentification can be insuffisante because anatomical data may allow to identify a subject (by reconstructing the skin surface). Identification of a person from a anatmical MRI was shown to be a feasible task (for e.g, [Abramian, D (2019)](https://ieeexplore.ieee.org/document/8759515)).

Three main approaches for face de-identification have been proposed: 

- defacing : completely or partially removing facial features (while preserving the brain voxel)

- refacing: changing the facial features or defacing and inserting a new face

- blurring using spatial filters

This face de-identification is imposed by some data sharing platforms such as OpenNeuro.

The question of the impact of the face de-identification on the outcomes of image processing remains unclear. Some articles compare several software and study the impact of defacing on analysis:

- [Multisite Comparison of MRI Defacing Software Across Multiple Cohorts](https://www.frontiersin.org/articles/10.3389/fpsyt.2021.617997/full) 

- [Impact of defacing on automated brain atrophy estimation](https://insightsimaging.springeropen.com/articles/10.1186/s13244-022-01195-7)

- [Systematic evaluation of the impact of defacing on quality and volumetric assessments on T1-weighted MR-images](https://www.sciencedirect.com/science/article/abs/pii/S0150986121000559)

It seems that defacing can alter volumetric and quality measures. The studies shows different conclusions about significance of this impact. In comparison to defacing, it seems that the refacing mitigates the impact on image post-processing results, 

There are severals de-identification software: [mri_deface](https://surfer.nmr.mgh.harvard.edu/fswiki/mri_deface), [pydeface](https://github.com/poldracklab/pydeface), [quickshear](https://github.com/nipy/quickshear), [mridefacer](https://github.com/mih/mridefacer), [afni_refacer](https://afni.nimh.nih.gov/pub/dist/doc/program_help/@afni_refacer_run.html), [deepdefacer](https://pypi.org/project/deepdefacer/).

Some face de-identification software can struggle with some images and can remove brain voxels. So it is important to do a quality check of the defecing results. 
Note that, not all software give the same result according to the poulation (young, elderly person...).
If the defacing of a image or of a cohort worked poorly with one software, it can be useful to test others.

## AFNI @afni_refacer_run

AFNI (Analysis of Functional NeuroImages) is a suite of programs for analyzing MRI brain images. The [@afni_refacer_run](https://afni.nimh.nih.gov/pub/dist/doc/htmldoc/tutorials/refacer/refacer_run.html#introduction) programme can be used to deface or reface (two modes available) a T1w image. 

Once AFNI is installed, @afni_refacer_run can be run using several modes (mode_all, mode_reface...):

```
@afni_refacer_run -input /bids/sub-02/anat/sub-002_T1w.nii.gz -mode_all -prefix sub-002_T1w
```

Reface and deface images are obtainded and QC images are created to check the results.

## BIDSonym

[BIDSonym](https://peerherholz.github.io/BIDSonym/index.html) is a BIDS App supporting several defacing software (mri_deface, ptdeface, quickshear, mridefacer).

BIDSonym works only with input data in [BIDS](BIDS.md) format.

For installation, follow the instructions in the [documentation](https://peerherholz.github.io/BIDSonym/installation.html). It will be easier to use Docker or Singularity than bare metal installation. 

Notes: depending on how docker is installed on your computer you may need administrator rights to pull and use the image. You may also need to not read your folder in read-only (ro). 


Example with Docker using `mri_deface` and `bet` for brain extraction: 
```
docker run -it --rm -v /bids/directory/:/bids_ds peerherholz/bidsonym:latest /bids_ds participant --participant_label 001 --deid mri_deface --brainextraction bet --bet_frac 0.5
```

The non-defaced images that enter BIDSonym as input will be copied to sourcedata/bidsonym/sub-<subject_label>/ and the defaced image will owerwritte the input image bids_dataset/sub-<subject_label>/anat/sub-<subject_label>_T1w.nii.gz. 

It is also possible to remove metada from json using BIDSonym.
