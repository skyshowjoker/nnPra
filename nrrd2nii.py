import nrrd
import nibabel as nib
import numpy as np
import matplotlib.pyplot as plt
import SimpleITK as sitk

base_path = r'C:\Users\perlicue\Desktop\戴松玉_2019-06-20_眼眶MRI增强_2280229_0000040310(5599422)'
data_path=base_path + r'\t2_tra-label.nrrd'
save_path=base_path + r'\t2_tra-label_1.nii.gz'
save_path2=base_path + r'\t2_tra-label.nii.gz'

# data, options = nrrd.read(data_path)  # 读取 nrrd 文件
# img = nib.Nifti1Image(data, np.eye(4))  # 将 nrrd 文件转换为 .nii 文件
# print(options)
# nib.save(img, save_path)  # 保存 nii 文件
img = nib.load(save_path2)
print(img)