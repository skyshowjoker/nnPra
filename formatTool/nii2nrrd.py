import nrrd
import nibabel as nib
import numpy as np
import matplotlib.pyplot as plt

def nii2nrrd(nii_path, nrrd_path):
    img = nib.load(nii_path).get_fdata()
    data = np.asarray(img)
    nrrd.write(nrrd_path, data)



base_path = r'C:\Users\perlicue\Desktop\程加强_2020-08-06_眼眶MRI增强_3631562_0001286303(6550235)\88'
data_path=base_path + r'\t2_tra.nii.gz'
save_path=base_path + r'\t2_tra.nrrd'

nii2nrrd(data_path, save_path)