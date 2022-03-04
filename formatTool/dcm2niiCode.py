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
save_path = r'C:\Users\perlicue\Desktop\sample_images'

file_root = r"C:\Users\perlicue\Desktop\sample_images\\"

file_list = os.listdir(file_root)
print(file_list)
for img_name in file_list:
    #if img_name.endswith('.dcm'):
    dcm_path = file_root + img_name
    print(dcm_path)


    dcm_images = readdcm(dcm_path)
    sitk.WriteImage(dcm_images, os.path.join(save_path, '{}.nii.gz'.format(dcm_path)))