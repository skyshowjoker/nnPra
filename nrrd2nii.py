import nrrd
import nibabel as nib
import numpy as np
import matplotlib.pyplot as plt
import SimpleITK as sitk

base_path = r'C:\Users\perlicue\Desktop\蔡端新_2016-06-28_眼眶MRI平扫_2463041_0000959189(3374407)'
data_path=base_path + r'\t2_tra.seg.nrrd'
save_path=base_path + r'\t2_tra.seg.nii'

data, options = nrrd.read(data_path)  # 读取 nrrd 文件
img = nib.Nifti1Image(data, np.eye(4))  # 将 nrrd 文件转换为 .nii 文件
nib.save(img, save_path)  # 保存 nii 文件
print(data)
# plt.imshow(data, cmap=plt.cm.gray)
# plt.show()
# def load_nii(path_folder):
#     return sitk.GetArrayFromImage(sitk.ReadImage(str(path_folder)))
#
# path = r"C:\joey\master\resource\lymphoma\tag\dataset_test2\2280229_0000040310(5599422)\\t2_tra.nii.gz"
# img = load_nii(path)
# print(img.shape)
# path = r"C:\joey\master\resource\lymphoma\tag\dataset_test2\2280229_0000040310(5599422)\\t2_tra-label.nii.gz"
# img = load_nii(path)
# print(img.shape)