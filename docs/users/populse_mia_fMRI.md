# fMRI analyses with populse_mia 

This page gathers several example of how to analyse fMRI data in [populse_mia](https://populse.github.io/populse_mia/html/index.html) with the [mia_processes](https://populse.github.io/mia_processes/html/index.html) library. 

## SPM dataset : Famous vs non-famous faces
The aims of this tutorial is to recreate in populse_mia the classical workflow described in the [SPM12 manual](https://www.fil.ion.ucl.ac.uk/spm/doc/manual.pdf#chapter.32) using face dataset that can be downloaded [here](http://www.fil.ion.ucl.ac.uk/spm/data/face_rep/). 


### 1. Download data
- Download the data from http://www.fil.ion.ucl.ac.uk/spm/data/face_rep/.

- The data are in .img/.hdr format. This format can be used in populse_mia but to make things easier we will convert the data to NIfTI format.


```
import glob
import nibabel

anat = nibabel.load('/home/username/face_rep/Structural/sM03953_0007.img' )
nibabel.save(anat, anat.replace('.img','.nii'))
func = glob.glob('/home/username/face_rep/RawEPI/*.img')

for f in func:
   img = nibabel.load(f)
   nibabel.save(img, f.replace('.img','.nii'))

nibabel.concat_images(func)
```

The stimulus onset times and lag are in a '.mat' file, here is a way to get them in a list using python :

```
from scipy.io.matlab import loadmat

mat = loadmat("/home/username/face_rep/sots.mat", struct_as_record=False)
sot = mat['sot'][0]
itemlag = mat['itemlag'][0]
onset_N1 = sot[0].tolist()
onset_N2 = sot[1].tolist()
onset_F1 = sot[2].tolist()
onset_F2 = sot[3].tolist()
lag_1 = itemlag[1].tolist()
lag_2 = itemlag[3].tolist()
```


### 2. Categorical responses 
**a. data Import**

- Create a mia project under the name `face_spm_categorical`. 
- Import the NIfTI data.  

**b. preprocessing**

You can used the [Bold_spatial_preprocessing1 pipeline](https://populse.github.io/mia_processes/html/documentation/documentation.html) or the [Bold_spatial_preprocessing2 pipeline](https://populse.github.io/mia_processes/html/documentation/documentation.html). 

You can also create your own pre-processing pipeline using the different bricks available in populse_mia. 

**c. Modelling categorical responses**

- Open the [Level1Design](https://populse.github.io/mia_processes/html/documentation/documentation.html) brick and complete the field with the parameters described in the SPM manual: 
    - `timing_units` : scans
    - `interscan_interval`: 2.0
    - `microtime_resolution`: 24
    - `microtime_onset`: 12
    - `sess_scans` : select the smoothed functional file 
    - `sess_cond_names`: [['N1', 'N2', 'F1', 'F2']]
    - `sess_cond_onsets`: [[[6.74996667, ..., 238.49996667], [13.49996667, ..., 341.99996667], [-3.33333333e-05, ..., 344.249967], [33.74996667, ..., 346.49996667]]] &rarr; the onset times [[onset_N1, onset_N2, onset_F1, onset_F2]]
    - `sess_cond_duration`: [[[0.0], [0.0], [0.0], [0.0]]]
    - `sess_cond_tmod`: [[0, 0, 0, 0]] &rarr; no time modulation for any of the conditions
    - `sess_cond_orth`: [[1, 1, 1, 1]] &rarr; orthogonalise regressors for each condition
    - `sess_multi_reg`: select the realignment file (rp_afunc_all.txt')
    - `sess_hpf`: [128.0]
    - `factor_info`: [{'name': 'Fame', 'levels': 2}, {'name': 'Rep', 'levels': 2}] --> as we are using the Factorial Design option, contrast will be automatically specified during the estimation of  the model. 
    - `bases`: {'hrf': {'derivs': [1, 1]}} &rarr; use HRF with time and dispersion derivatives

    For others parameters, leave the defaul settings. 
    Launch the brick. A SPM.mat file will be created
    
    Parameters can be found [here](https://github.com/populse/irmage-tools-resources/tree/main/docs/examples/fmri_face_spm/params_face_spm_categorical_Level1Design.json)

- Open the [EstimateModel](https://populse.github.io/mia_processes/html/documentation/documentation.html) brick and complete the following field:
    - `spm_mat_file` : select the file created by the Level1Design brick
    - `estimation method`: {'Classical': 1}
    - `write_residual`: False
    - `factor_info`: [{'name': 'Fame', 'levels': 2}, {'name': 'Rep', 'levels': 2}] --> as we used Factorial Design option in Level1Design we need to add the factor_info and base info in the EstimateModel brick 
    - `bases`: {'hrf': {'derivs': [1, 1]}}

    For others parameters, leave the defaul settings and launch the brick. 
    
    The SPM.mat file will be updateted and images of estimated regression coefficient (beta), image os the variance error (ResMS), image of the estimated resolution elements per voxel (RPV) and a mask image indicating which voxels were included in the analysis will be created. 
    As we used Factorial Design option, T and F contrasts will be also created. 
    
    Parameters can be found [here](https://github.com/populse/irmage-tools-resources/tree/main/docs/params_face_spm_categorical_EstimateModel.json).

It is also possible to create a [pipeline with the two bricks](https://github.com/populse/irmage-tools-resources/tree/main/docs/examples/fmri_face_spm/pipeline_face_spm_categorical_stats.py).

### 3. Parametric responses 
**a. data Import**

- Create a mia project under the name `face_spm_parametric`.
- Import the NIfTI data.

**b. preprocessing**

You can used the [Bold_spatial_preprocessing1 pipeline](https://populse.github.io/mia_processes/html/documentation/documentation.html) or the [Bold_spatial_preprocessing2 pipeline](https://populse.github.io/mia_processes/html/documentation/documentation.html). 

You can also create your own pre-processing pipeline using the different bricks available in populse_mia. 

**c. Parametric responses**

- Open the [Level1Design](https://populse.github.io/mia_processes/html/documentation/documentation.html) brick and complete the field with the parameters described in the SPM manual: 
    - `timing_units` : scans
    - `interscan_interval`: 2.0
    - `microtime_resolution`: 24
    - `microtime_onset`: 12
    - `sess_scans` : select the smoothed functional file 
    - `sess_cond_names`: [['N1', 'N2', 'F1', 'F2']]
    - `sess_cond_onsets`: [[[6.74996667, ..., 238.49996667], [13.49996667, ..., 341.99996667], [-3.33333333e-05, ..., 344.249967], [33.74996667, ..., 346.49996667]]] &rarr; the onset times [[onset_N1, onset_N2, onset_F1, onset_F2]]
    - `sess_cond_duration`: [[[0.0], [0.0], [0.0], [0.0]]]
    - `sess_cond_tmod`: [[0, 0, 0, 0]] &rarr; no time modulation for any of the conditions
    - `sess_cond_pmod_names`: [[None, ['Lag'], None, ['Lag']]] &rarr; parametric modulations name for each conditions (no parametric modulation for N1 and F1)  
    - `sess_cond_pmod_values`: [[None, [[3.0, ..., 50.0]], None, [[11.0, ..., 1.0]]]] &rarr; pmod values [[None, lag_1, None, lag_2]]
    - `sess_cond_pmod_polys`: [[None, [2], None, [2]]]
    - `sess_cond_orth`: [[1, 1, 1, 1]] &rarr; orthogonalise regressors for each condition
    - `sess_multi_reg`: select the realignment file (rp_afunc_all.txt')
    - `sess_hpf`: [128.0]
    - `factor_info`: [{'name': 'Fame', 'levels': 2}, {'name': 'Rep', 'levels': 2}] 
    - `bases`: {'hrf': {'derivs': [0, 0]}} &rarr; use HRF without derivatives

    For others parameters, leave the defaul settings. 
    Launch the brick. A SPM.mat file will be created
    
    Parameters can be found [here](https://github.com/populse/irmage-tools-resources/tree/main/docs/examples/fmri_face_spm/params_face_spm_parametric_Level1Design.json).

- Open the [EstimateModel](https://populse.github.io/mia_processes/html/documentation/documentation.html) brick and complete the field as for categorical responses.
    For others parameters, leave the defaul settings and launch the brick. 
    
    The SPM.mat file will be updateted and images of estimated regression coefficient (beta), image os the variance error (ResMS), image of the estimated resolution elements per voxel (RPV) and a mask image indicating which voxels were included in the analysis will be created. 
    As we used Factorial Design option, T and F contrasts will be also created. 
    
    Parameters can be found [here](https://github.com/populse/irmage-tools-resources/tree/main/docs/examples/fmri_face_spm/params_face_spm_parametric_EstimateModel.json).

- To create F-contrast in populse_mia, we first need to create the T-contrasts used to create the F-contrast.  Open the [EstimateContrast](https://populse.github.io/mia_processes/html/documentation/documentation.html) brick and complete the following field:
    - `spm_mat_file` : select the file SPM.mat updated by the EstimateModel brick
    - `T_contrast_names` : ['Famous_lag1', 'Famous_lag2']
    - `T_conditions_names`: [['F2xLag^1'], ['F2xLag^2']]
    - `T_contrasts_weight`: [[1.0], [1.0]]
    - `F_contrast_names` : ['Famous Lag']
    - `F_contrast_T_names`: [['Famous_lag1', 'Famous_lag2']] &rarr; the T-contrasts used to created the Famous Lag F-contrast
    - `beta_images`: select the beta images created by the EstimateModel brick
    - `residual_image`: select the residual image created by the EstimateModel brick

    For others parameters, leave the defaul settings. 
    Launch the brick. T and F contrasts will be created. 
    Parameters can be found [here](/docs/examples/fmri_face_spm/params_face_spm_parametric_EstimateContrast.json).

It is also possible to create a [pipeline with the three bricks](https://github.com/populse/irmage-tools-resources/tree/main/docs/examples/fmri_face_spm/pipeline_face_spm_parametric_stats.py "download").


## Flanker task dataset 
The aims of this tutorial is to recreate in populse_mia a workflow to analysed an fMRI dataset that used the Flanker task. 
The dataset can be downloaded on the Openneuro website [here](https://openneuro.org/datasets/ds000102/versions/00001). 
Explanation about this dataset can be foun on the [Andy's Brain Book](https://andysbrainbook.readthedocs.io/en/latest/SPM/SPM_Overview.html) website.

### 1. Analysis for one subject 
Here is an example of statistical processing for one subject with two sessions.
We will used the subject 08 of the dataset.  

**a. data Import**

- Create a mia project under the name `flanker_test`

- Import the NIfTI data.  

- Onset times creation: 
    
    Within each subject's `func` directory you can find a `events.tsv`file that contains the timing for each event (incogruent and congruent). 

    For mia_processes, we need to have this onset times in list format:

```
# Onset times for sub-08
sub08_congruent_run1 = [0.0, 10.0, 20.0, 52.0, 88.0, 130.0, 144.0, 174.0, 236.0, 248.0, 260.0, 274.0]
sub08_incongruent_run1 = [32.0, 42.0, 64.0, 76.0, 102.0, 116.0, 154.0, 164.0, 184.0, 196.0, 208.0, 222.0]
sub08_congruent_run2 = [0.0, 10.0, 52.0, 64.0, 88.0, 150.0, 164.0, 174.0, 184.0, 196.0, 232.0, 260.0]
sub08_incongruent_run2 = [20.0, 30.0, 40.0, 76.0, 102.0, 116.0, 130.0, 140.0, 208.0, 220.0, 246.0, 274.0]
# Duration of the trial
duration = [2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0]

```

**b. preprocessing**

You can used the [Bold_spatial_preprocessing1 pipeline](https://populse.github.io/mia_processes/html/documentation/documentation.html) or the [Bold_spatial_preprocessing2 pipeline](https://populse.github.io/mia_processes/html/documentation/documentation.html). 

You can also create your own pre-processing pipeline using the different bricks available in populse_mia. 

**c. Statistical analysis**

- Open the [Level1Design](https://populse.github.io/mia_processes/html/documentation/documentation.html) brick and complete the following field:
    - `timing_units` : secs
    - `interscan_interval`: 2.0
    - `sess_scans` : select the two smoothed functional files (run01 and run02)
    - `sess_cond_names`: [['Inc', 'Con'], ['Inc', 'Con']] &rarr; conditions names for each session 
    - `sess_cond_onsets`: [[[0.0, ..., 274.0], [32.0, ..., 222.0]], [[0.0, ..., 260.0], [20.0, ..., 274.0]]]&rarr; the onset times [[sub08_incongruent_run1, sub08_congruent_run1], [sub08_incongruent_run2, sub08_congruent_run2]]
    - `sess_cond_duration`: [[[2.0, ..., 2.0], [2.0, ..., 2.0]], [[2.0, ..., 2.0], [2.0, ..., 2.0]]] &rarr; duration [[duration, duration], [duration, duration]]
    - `sess_cond_tmod`: [[0, 0], [0, 0]] &rarr; no time modulation for any of the conditions and for any of the sessions
    - `sess_cond_orth`: [[1, 1], [1, 1]] &rarr; orthogonalise regressors for each condition and ecah session
    - `sess_multi_reg`: select the realignment file (rp_afunc_all.txt')
    - `sess_hpf`: [128.0, 128.0]
    - `bases`: {'hrf': {'derivs': [0, 0]}} &rarr; use HRF without derivatives

    For others parameters, leave the defaul settings. 
    Launch the brick. A SPM.mat file will be created
    Parameters can be found [here](https://github.com/populse/irmage-tools-resources/tree/main/docs/examples/fmri_flanker_test/params_flanker_task_sub08_Level1Design.json).

- Open the [EstimateModel](https://populse.github.io/mia_processes/html/documentation/documentation.html) brick and complete the following field:
    - `spm_mat_file` : select the file created by the Level1Design brick
    
    For others parameters, leave the defaul settings and launch the brick. 
    The SPM.mat file will be updateted and images of estimated regression coefficient (beta), image os the variance error (ResMS), image of the estimated resolution elements per voxel (RPV) and a mask image indicating which voxels were included in the analysis will be created. 
    Parameters can be found [here](https://github.com/populse/irmage-tools-resources/tree/main/docs/examples/fmri_flanker_task/params_flanker_task_sub08_EstimateModel.json).

- To create F-contrast in populse_mia, we first need to create the T-contrasts used to create the F-contrast.  Open the [EstimateContrast](https://populse.github.io/mia_processes/html/documentation/documentation.html) brick and complete the following field:
    - `spm_mat_file` : select the file SPM.mat updated by the EstimateModel brick
    - `T_contrast_names` : ['Inc-Con']
    - `T_conditions_names`: [['Inc', 'Con']]
    - `T_contrasts_weight`: [[0.5, -0.5, 0.5, -.05]] 
    - `beta_images`: select the beta images created by the EstimateModel brick
    - `residual_image`: select the residual image created by the EstimateModel brick

    For others parameters, leave the defaul settings. 
    Launch the brick. T and F contrasts will be created. 
    Parameters can be found [here](https://github.com/populse/irmage-tools-resources/tree/main/docs/examples/fmri_flanker_test/params_flanker_task_sub08_EstimateContrast.json).

It is also possible to create a [pipeline with the three bricks](https://github.com/populse/irmage-tools-resources/tree/main/docs/examples/fmri_flanker_test/pipeline_flanker_task_sub08_stats.py).

