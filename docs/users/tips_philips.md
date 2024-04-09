
# Tips for Philips scanner
## Compute Slice order acquistion and slice timing 

In EPI sequences, each 3D volume is acquired as 2D slices sequences (i.e the different slices of the same volume are not acquired simultaneously but successively).
Each manufacturer (Siemens, Philips ...) have specific slice order modes. 

For Philips scanner the following modes are possible:

- Default = the acquistion time between adjacent slices is maximized
- Ascending (FH, AP, LR) = acquistion in linear order from foot to head or from anterior to posterior or from left to right
- Descending (HF, PA, RL) = acquistion in linear order from head to foot or from posterior to anterior or from right to left
- Interleaved =  the acquistion time spacing between neighbor slices acquisition is maximized (interleave number estimated by the square root of the number of slices, rounded to the next integer)


In order to do [slice timing correction](https://www.fil.ion.ucl.ac.uk/spm/docs/tutorials/fmri/block/preprocessing/slice_timing/) during the preprocessing steps, you will need to know the slice order. 

Some BIDS Apps, as fMRIPrep, will directly used the metadata [SliceTiming](https://bids-specification.readthedocs.io/en/stable/glossary.html#slicetiming-metadata) in the BIDS json. SliceTiming is the time at which each slice was acquired within each volume (frame) of the acquisition.

Unfortunately, for Philips scanner, unlike for others manufatures, slice order / slice timing can not be automatically extract from DICOM data. To compute slice order / slice timing you need to know the following parameters:

- acquistion mode (ascending / descending, sequential / interleaved): this information is not in the DICOM so you need to ask the persone in charge of the acquistion

- repetion time

- number of slices 

- multibande factor (acquistion with multibande)

- pause between final slice of volume and start of next in seconds (sparse acquisition)

- number of package

### Script to compute slice order / slice timing for philips 

You can find script to compute slice order and BIDS SliceTiming metadata and to add SliceTiming in a BIDS dataset [here](https://github.com/IRMaGe-3T/irmage-tools?tab=readme-ov-file#data_management)


