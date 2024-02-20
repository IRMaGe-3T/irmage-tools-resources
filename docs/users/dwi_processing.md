# Diffusion MRI

This section aims to summarize some information about the processing of diffusion data and to give an idea of what can be done with diffusion.

Please refer to the documentation of each software for more information.

## Resources

- [Pulse sequence explanation](https://mriquestions.com/making-a-dw-image.html)
- [Andy's Brain Book](https://andysbrainbook.readthedocs.io/en/latest/MRtrix/MRtrix_Introduction.html): tutorial about diffusion processing with [MRTrix](https://mrtrix.readthedocs.io/en/latest/)
- [B.A.T.M.A.M tutorial](https://osf.io/fkyht/): tutorial about diffusion processing (tractography) with [MRTrix](https://mrtrix.readthedocs.io/en/latest/)
- [MRTrix user documentation](https://mrtrix.readthedocs.io/en/latest/) with many explanations


## Preprocessing

### Classic steps
Here are some classical steps of DWI preprocessing:

- Denoising: denoising DWI data and estimating the noise map.
- Unringing: remove Gibbs artifacts that generally appear as several thin parallel lines immediately adjacent to high-contrast interfaces.
- Correction of motion and distortion due to field inhomogeneities: 
    - correction of movement between several volumes
    - correction of movement within a single volume
    - correction of eddy current distortion
    - correction of susceptibility distortions
    - replacement of outliers due to subject movement during acquisition of the same slice
- Bias correction 

### Available tools

The list of tools for pre-processing is not exhaustive. Please note that several software (qsiprep, MicaPipe, MIA...) use commands from other software (FSL, MRTRix, Dipy...) to combine the best of each software and make them easier to use.

#### MRTrix - https://mrtrix.readthedocs.io
MRtrix offers several commands for standard pre-processing: dwidenoise, mrdegibbs, dwifslpreproc, dwibiascorrect.. 

Some of this commands used others software in background (for example FSL Eddy and Topup for correction of motion and distortion correction or ANTs for bias correction).

Mrtrix can also be used for further analysis (DTI, tractography .. )

#### QSIPrep - https://qsiprep.readthedocs.io 
Qsiprep enables standard pre-processing (modular). It integrates tools from several other software packages (MRTrix, FSL, Dipy, DSI Studio, etc.).

It is a BIDS-APP, input data should be in [BIDS](BIDS.md) format and it can be used using a Docker container.
Some processes are modular and depend on how data are structured. For example, for susceptibility correction to be performed, it is necessary to have added "IntendedFor" in the json of the fmap used with the name of the diffusion sequence.

A report is also generated. It can help to do quality control.

It is also possible to perform analysis/reconstruction with qsiprep (tractography with MRTrix, pyAFQ, DTI, DKI, NODDI ...).

#### POPULSE-MIA - https://populse.github.io/populse_mia 
Several MRTrix commands are implemented in [POPULSE-MIA](../populse_mia_tutorial/populse.md) (see [Dwi_preprocessing](https://populse.github.io/mia_processes/html/documentation/pipelines/preprocess/Dwi_preprocessing.html) pipeline)

It is also possible to perform further analysis in POLUSE-MIA using MRTrix. 

#### SynB0DISCO - https://github.com/MASILab/Synb0-DISCO
Enable susceptibility distortion correction with datasets that do not include specific sequences for distortion correction. 

#### NORDIC - https://github.com/SteenMoeller/NORDIC_Raw
NORDIC denoisind using Matlab

## Processing
The list of processing is not exhaustive, the aims is to to give an idea of what can be done with diffusion data.

### Diffusion Tensor Imaging (DTI)

#### Brief explanations

Short bibliography:

- Basser PJ, Mattiello J, LeBihan D. Estimation of the effective selfdiffusion tensor from
the NMR spin echo. J Magn Reson B 1994;103: 247-254.
- Horsfield MA, Jones DK. Applications of diffusion-weighted and diffusion tensor MRI to
white matter diseases — A review. NMR Biomed 2002;15:570-577

The diffusion tensor (DT) describes the diffusion of water molecules using a Gaussian model and is used to characterize diffusion (anisotropy coefficient, preferred directions in space...).
DTI is based on the assumption that the diffusion of water particles in the tissue microstructure follows a Gaussian distribution. This is the case in regions where fiber bundles are "coherent".

Several quantitative metrics can be extracted from DTI:

- Fractional Anisotropy (FA): describes the amount of diffusion that is anisotropic and thus the preferred direction of diffusion
- Mean Diffusivity (MD) = Apparent Diffusion Coefficient (ADC): average diffusion
- Axial Diffusivity (AD): diffusion in the axial direction
- Radial Diffusivity (RD): Diffusion in the radial direction (perpendicular to axial diffusion).
- Trace: sum of tensor eigenvalues
- FA color

At least 6 directions are required to obtain a diffusion tensor. 

DTI is very useful in clinical applications.

#### Example of tools

- [MRTrix](https://mrtrix.readthedocs.io):  using [dwi2tensor](https://mrtrix.readthedocs.io/en/latest/reference/commands/dwi2tensor.html#dwi2tensor) command and then [tensor2metric](https://mrtrix.readthedocs.io/en/latest/reference/commands/tensor2metric.html)

- [FSL](https://fsl.fmrib.ox.ac.uk/fsl/fslwiki) using [DTIFIT](https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/FDT/UserGuide) command

### Diffusion Kurtosis Imaging (DKI)

#### Brief explanations

Short bibliography:

- Jensen JH « Diffusional Kurtosis Imaging: The Quantification of Non- Gaussian Water
Diffusion by Means of Magnetic Resonance Imaging » ;Magn Reson Med
2005; https://doi.org/10.1002/mrm.20508 (1er papier sur le DKI)
- Jensen JH « MRI Quantification of Non-Gaussian Water Diffusion by Kurtosis
Analysis » ; NMR Biomed. 2010 https://doi.org/10.1002/nbm.1518
- Loxlan W. Kasa « Evaluating High Spatial Resolution Diffusion Kurtosis Imaging at 3T:
Reproducibility and Quality of Fit » ; Magn Reson Med 2021
https://doi.org/10.1002/jmri.27408
- https://mriquestions.com/diffusion-kurtosis.html#

DTI is based on the assumption that the diffusion of water particles in the tissue microstructure follows a Gaussian distribution. This assumption is incorrect for complex biological tissues. 
This non Gaussian behaviour is even more important for strong gradients and/or if a long echo time is used.
The DKI model is an extension of the DTI model that provides a better quantification of the degree of "non-Gaussianity" of water diffusion using the kurtosis tensor (KT).

Why use DKI?

- To characterise the heterogeneity of tissue microstructure
- To obtain biophysical parameters such as axonal fibre density

The DKI can be used to obtain the "classic" maps of the DTI model (FA, MD, etc.). These maps are similar to those obtained with DTI (but not exactly equal). Other maps are obtained specific to DKI. They depend on microstructural and mesoscopic properties (fibers dispersions and intersections). 

The following maps depend on both the diffusion tensor and the Kurtosis tensor: 

- Mean kurtosis (MK) (more important in WM as it is more compartmentalised)
- Axial Kurtosis (AK)
- Radial Kurtosis (RK) (with values normally greater than AK because the non-Gaussian behaviour is supposed to be more important perpendicular to the
WM fibres)

The following maps depend only on the Kurtosis tensor:

- Mean of the Kurtosis tensor (MKT) (similar to MK)
- Kurtosis fractional anisotropy (KFA)

Good to know: 

-  To use DKI, multi-shell data are needed (at least 3 shells, one can be b = 0 s/mm² and at least 15 differnet directions)
-  The effects of Kurtosis diffusion are more visible for values of b > 1500 s/mm²
-  DKI is sensitive to noise and artefacts. For example, it can be incorrectly estimated and have negative values in regions where radial diffusivity is low.
- To avoid physically impossible DKI values, a constrained fit can be used to estimate DKI (see [here](https://docs.dipy.org/stable/examples_built/reconstruction/reconst_dki.html#constrained-optimization-for-dki))
- Mean signal diffusion kurtosis imaging (MSDKI) characterise the kurtosis from the mean signals of the data acquired in all directions directions for each value of b (= powder-averaged signals) in order to limit sensitivity to noise and artefacts (see [here](https://docs.dipy.org/stable/examples_built/reconstruction/reconst_msdki.html#mean-signal-diffusion-kurtosis-imaging-msdki))


#### Example of tools

- [MRTrix](https://mrtrix.readthedocs.io): using [dwi2tensor](https://mrtrix.readthedocs.io/en/latest/reference/commands/dwi2tensor.html#dwi2tensor) command with the otption "-dkt". 

- [dipy](https://docs.dipy.org/): 
    - [tutorial to get DKI map](https://docs.dipy.org/stable/examples_built/reconstruction/reconst_dki.html#constrained-optimization-for-dki)
    - [tutorial to get MSDKI map](https://docs.dipy.org/stable/examples_built/reconstruction/reconst_msdkihtml#mean-signal-diffusion-kurtosis-imaging-msdki ) 

- [FSL](https://fsl.fmrib.ox.ac.uk/fsl/fslwiki) using [DTIFIT](https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/FDT/UserGuide) command with option "--kurt" and "--kurtdir" 

- Diffusion Kurtosis EStimator [DKE](https://www.nitrc.org/projects/dke): original code [to compute DKI](https://medicine.musc.edu/departments/centers/cbi/dki)

### Fiber orientation distribution and tractography 

#### Brief explanations

Short bibliography:

- Jeurissen, Ben, Maxime Descoteaux, Susumu Mori, and Alexander Leemans. “Diffusion MRI Fiber Tractography of the Brain.” NMR in Biomedicine 32, no. 4 (2019): e3785. https://doi.org/10.1002/nbm.3785.
- Andica, Christina, Koji Kamagata, and Shigeki Aoki. “Automated Three-Dimensional Major White Matter Bundle Segmentation Using Diffusion Magnetic Resonance Imaging.” Anatomical Science International 98, no. 3 (July 1, 2023): 318–36. https://doi.org/10.1007/s12565-023-00715-9.

The aim of tractograpy (= fiber tracking) is to connect voxels based on their principal diffusion direction and their anisotropy to obtain main white matter bundles. 

There are several tracking approaches (deterministic vs probabilistic, global vs local, Anatomically-Constrained Tractography...), they can produce very different tractograms. See the following article for more detail information [“Diffusion MRI Fiber Tractography of the Brain.”](https://doi.org/10.1002/nbm.3785). 

#### Example of tools 

Thera are several solutions for creatating probabilistic or deterministic streamlines and for obtaining segmentation of the white matter bundle, here are juste a few examples: 

- [MRTRix](https://mrtrix.readthedocs.io): fiber orientation distribution (constrained spherical deconvolution), tractography (tckgen command) with or without ATC, creation of connectome (see also [B.A.T.M.A.M tutorial](https://osf.io/fkyht/))
- [FSL - FDT](https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/FDT/UserGuide)
- [Slicer dMRI](https://dmri.slicer.org/)
- [DSI studio](https://dsi-studio.labsolver.org/)
- [Dipy](https://docs.dipy.org/stable/examples_built/fiber_tracking/index.html)
- Automated white matter bundle segmentation with [TractSeg](https://github.com/MIC-DKFZ/TractSeg)
- Automated white matter bundle segmentation with [Tracula](https://surfer.nmr.mgh.harvard.edu/fswiki/Tracula)
- Automated white matter bundle segmentation with [AFQ](https://yeatmanlab.github.io/pyAFQ/)

### NODDI 

#### Brief explanations

Short bibliography:

- Zhang, H., 2012. NODDI: practical in vivo neurite orientation dispersion and density
imaging of the human brain. Neuroimage 61, 1000–1016. https://doi.org/10.1016/j.neuroimage.2012.03.072.
- Kamiya, Kouhei . “NODDI in Clinical Research.” Journal of Neuroscience Methods 346
(December 2020): 108908. https://doi.org/10.1016/j.jneumeth.2020.108908.
- Andica, C., 2019b. Scan-rescan and inter-vendor reproducibility of neurite orientation
dispersion and density imaging metrics. Neuroradiology. https://doi.org/10.1007/s00234-01902350-6.
- Chung, A.W., Seunarine, K.K., Clark, C.A., 2016. NODDI reproducibility and variability
with magnetic field strength: a comparison between 1.5 T and 3 T. Hum. Brain Mapp. 37,
4550–4565. https://doi.org/10.1002/hbm.23328.

NODDI (Neurite Orientation Dispersion and Density Imaging) is a biophysical model which aims to characterize the microstructure within a voxel by providing information on neutrites density and on the dispersion of the orientation using 3 parametres: 

- Intra-cellular volume fraction (ICVF) = neurite density index (NDI): quantifies the neutrites density /estimates the volume fraction of neurites
- Orientation dispersion index (ODI): estimates the variability of neurite orientation (from 0 to 1 with 0 = all perfectly aligned and 1 = completely isotropic)
- Free water fraction (FWF): estimates the extent of contamination of the CSF 

Some of the model's assumptions are debated within the community, for example:

- the number of compartments (intra-neutrite, extra-neutrite, free water)
- the fact that the diffusion distribution follows a Gaussian distribution 
- the fact that certain model parameters have been set and constrained. For example, fixed the parallel diffusivity when it can be different depending on the population (child or adult) and depending on the environment (WM or GM).

#### Example of tools 

- [Orginal Matlab Toolbox](http://mig.cs.ucl.ac.uk/index.php?n=Tutorial.NODDImatlab)

- Accelerated Microstructure Imaging via Convex Optimization ([AMICO](https://github.com/daducci/AMICO))

- FSL [cuDIMOT](https://users.fmrib.ox.ac.uk/~moisesf/cudimot/Installation.html)

- [MDT](https://mdt-toolbox.readthedocs.io/en/latest_release/) (also included HARMED, NODDI, BinghamNODDI, NODDIDA, NODDI-DTI, ActiveAx, AxCaliber, Ball&Sticks, Ball&Rackets, Kurtosis, Tensor, VERDICT,)