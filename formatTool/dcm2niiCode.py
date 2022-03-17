# -*- coding: utf-8 -*-
import SimpleITK as sitk
import os

def readdcm(filepath):
    reader = sitk.ImageSeriesReader()
    reader.MetaDataDictionaryArrayUpdateOn()
    reader.LoadPrivateTagsOn()
    series_id = reader.GetGDCMSeriesIDs(filepath)
    print(series_id)
    series_file_names = reader.GetGDCMSeriesFileNames(filepath, series_id[0])

    reader.SetFileNames(series_file_names)
    images = reader.Execute()

    return images

#dcm_path = r'F:\test'
save_path = r'C:\joey\master\resource\lymphoma\dataset\data_file'

file_root = r"C:\joey\master\resource\lymphoma\dataset\t2_tra_data"

file_list = os.listdir(file_root)
print(file_list)
for img_name in file_list:
    #if img_name.endswith('.dcm'):
    dcm_path = file_root + os.sep + img_name
    print(dcm_path)


    dcm_images = readdcm(dcm_path)
    os.mkdir(save_path + os.sep + img_name)
    sitk.WriteImage(dcm_images, os.path.join(save_path + os.sep + img_name + os.sep + "t2_tra", '{}.nii.gz'.format(save_path + os.sep + img_name + os.sep + "t2_tra")))