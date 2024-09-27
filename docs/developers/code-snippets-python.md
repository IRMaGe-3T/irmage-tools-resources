# Useful code snippets Python

## NIfTI related

###  Set xyzt_units field of the NIfTI file to mm/s (BIDS format)

I want set xyzt_units field of the NIfTI file to mm/s:

```
from bids import BIDSLayout
import nibabel as nb

def set_xyzt_units(img, xyz='mm', t='sec'):
    header = img.header.copy()
    header.set_xyzt_units(xyz=xyz, t=t)
    return img.__class__(img.get_fdata().copy(), img.affine, header)    

def fix_xyzt_units(bids_root):
    layout = BIDSLayout(bids_root)
    for nii in layout.get(extension=['.nii', '.nii.gz']):
        metadata = layout.get_metadata(nii.path)
        img = nb.load(nii.path)
        fixed_img = set_xyzt_units(img)
        fixed_img.to_filename(nii.path)

fix_xyzt_units('path/to/your/bids/root')
```

### Set repetition time in the NIfTI header using json file (BIDS format)

I want the repetition time in the NIfTI file header (pixdim[4]) to be equal to the value found in the associated json file:

  - All bold files will be explored
  
  - Old files are not overwritten, new images with an additional _fixed suffix will be created. After reviewing all the modified files, the user can manually overwrite the old files.

```
from pathlib import Path
from bids import BIDSLayout
import numpy as np

layout = BIDSLayout("path/to/your/bids/root")
bold_images = layout.get(suffix="bold", extension=[".nii", ".nii.gz"])
for bold in bold_images:
    TR = bold.get_metadata()["RepetitionTime"]
    img = bold.get_image()
    zooms = img.header.get_zooms()
    if not np.isclose(zooms[3], TR):
        old_path = Path(bold)
        new_path = old_path.with_name(f"{old_path.stem}_fixed.nii")
        img.header.set_zooms(zooms[:3] + (TR,))
        img.to_filename(new_path)
```

 