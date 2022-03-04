import dicom2nifti
import zipfile
# original_dicom_directory =
# output_file =
# dicom2nifti.dicom_series_to_nifti(original_dicom_directory, output_file, reorient_nifti=True)

zf = zipfile.ZipFile(r'C:\Users\perlicue\Desktop\a00-hello/陈林珍_2018-10-08_眼眶MRI增强_3093769_0001134217(4958418).zip', 'r')



# Extract all members from the archive to the current working directory
zf.extractall(r"C:\Users\perlicue\Desktop\a00-hello\陈林珍_2018-10-08_眼眶MRI增强_3093769_0001134217(4958418)") # you may want to specify path param