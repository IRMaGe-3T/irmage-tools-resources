
# Tips for Philips scanner

## Phase encoding Direction 

Philips DICOM contains the phase encoding axis (i.e anterior-posterior (AP) vs left-right (LR)) but it does not contain the polarity (A->P vs P->A pr R->L vs L->R).
So the metadata [PhaseEncodingDirection](https://bids-specification.readthedocs.io/en/stable/glossary.html#phaseencodingdirection-metadata) will not be automatically added to the BIDS json. 

However, some BIDS Apps, as fMRIPrep or QSIPrep, will directly used this metadata and so, if you know the phase encoding direction (can be found on the scanner), you will need to add this metadata. 

For an image that conforms to the [RAS (Right-Anterior-Superior) convention](https://www.slicer.org/wiki/Coordinate_systems): 

|                           |  Philips sanner  | BIDS json |
|:-------------------------:|:----------------:|:---------:|
|A>>P (anterior-posterior)  | APA              | j-        |
|P>>A (posterior-anterior)  | APP              | j         |
|R>>L (right-left)          | RLR              | i-        |
|L>>R (left-righ)           | RLL              | i         |

## Slice order acquisition and slice timing for BIDS

In EPI sequences, each 3D volume is acquired as 2D slices sequences (i.e the different slices of the same volume are not acquired simultaneously but successively).
Each manufacturer (Siemens, Philips ...) have specific slice order modes. 

For Philips scanner the following modes are possible:

- Default = the acquisition time between adjacent slices is maximized
- Ascending (FH, AP, LR) = acquisition in linear order from foot to head or from anterior to posterior or from left to right
- Descending (HF, PA, RL) = acquisition in linear order from head to foot or from posterior to anterior or from right to left
- Interleaved =  the acquisition time spacing between neighbor slices acquisition is maximized (interleave number estimated by the square root of the number of slices, rounded to the next integer)


In order to do [slice timing correction](https://www.fil.ion.ucl.ac.uk/spm/docs/tutorials/fmri/block/preprocessing/slice_timing/) during the preprocessing steps, you will need to know the slice order. 

Some BIDS Apps, as fMRIPrep, will directly used the metadata [SliceTiming](https://bids-specification.readthedocs.io/en/stable/glossary.html#slicetiming-metadata) in the BIDS json. SliceTiming is the time at which each slice was acquired within each volume (frame) of the acquisition.

Unfortunately, for Philips scanner, unlike for others manufactures, slice order / slice timing can not be automatically extract from DICOM data. To compute slice order / slice timing you need to know the following parameters:

- acquisition mode (ascending / descending, sequential / interleaved): this information is not in the DICOM so you need to ask the persone in charge of the acquisition

- repetition time

- number of slices 

- multibande factor (acquisition with multibande)

- pause between final slice of volume and start of next in seconds (sparse acquisition)

- number of package

### Script to compute slice order / slice timing for philips 

You can find script to compute slice order and BIDS SliceTiming metadata and to add SliceTiming in a BIDS dataset [here](https://github.com/IRMaGe-3T/irmage-tools?tab=readme-ov-file#data_management)


## Echo Spacing and Total Readout Time for BIDS

The [TotalReadoutTime](https://bids-specification.readthedocs.io/en/latest/glossary.html#objects.metadata.TotalReadoutTime) as defined in BIDS specification, is the readout duration that would have generated data with the given level of distortion (and not the actual duration of the readout train). 

This information can not be found directly in the Philips DICOM. 
If you used [dcm2niix](https://github.com/rordenlab/dcm2niix/tree/master/Philips#missing-information), EstimatedTotalReadoutTime and EstimatedEffectiveEchoSpacing are populated in the json.

For [TOPUP correction with fsl](https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/topup/TopupUsersGuide), this information is not required if the readout time is the same for the main image to correct and the images used for estimate the field (you can used 1 for example). However, some BIDS Apps, as fMRIPrep, will required this information is fmap are used. 

