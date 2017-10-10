
import nibabel as nib
import numpy as np

f = 'lh.pial'

vtx,tri = nib.freesurfer.read_geometry(f)

np.savetxt('fsav5_lh_pial_vtx.txt', vtx)
np.savetxt('fsav5_lh_pial_tri.txt', tri)



