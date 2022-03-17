import shutil
import SimpleITK as sitk
import dicom2nifti
import zipfile
import os
origin_dir = r"C:\joey\master\resource\lymphoma\dataset\VT-dataset"
target_dir = r"C:\joey\master\resource\lymphoma\dataset\ct"
def move_file(origin_dir, target_dir):
    fileList = os.listdir(origin_dir)
    for file in fileList:
        seg = sitk.ReadImage(origin_dir+os.sep+file+os.sep+"t2_tra.nii.gz",sitk.sitkUInt8)
        seg_arr = sitk.GetArrayFromImage(seg)
        print(file)
        print(seg_arr.shape)
        # shutil.copy(origin_dir+os.sep+file+os.sep+"t2_tra.nii.gz", target_dir+os.sep+file+".nii.gz")


move_file(origin_dir, target_dir)