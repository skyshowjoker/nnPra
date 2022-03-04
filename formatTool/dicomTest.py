import pydicom as dicom
import os
import shutil
import zipfile
INPUT_FOLDER = r"C:\joey\master\resource\lymphoma\PACS.Lymphoma.Spider\output\\"
OUTPUT_FOLDER = r"C:\joey\master\resource\lymphoma\t2_tra_data\\"
label_folder = r"C:\joey\master\resource\lymphoma\tag\label_file"
unzip_path = r"C:\joey\master\resource\lymphoma\PACS.Lymphoma.Spider\unzip_output\\"
patients = os.listdir(label_folder)
patients.sort()




# Load the scans in given folder path
def load_scan(path, out_path):

    # slices = [dicom.read_file(path + '/' + s) for s in os.listdir(path)]
    # slices = [s.pixel_array for s in slices if hasattr(s, 'SeriesDescription') and s.SeriesDescription == 't2_tse_fs_tra']

    for s in os.listdir(path):
        slice = dicom.read_file(path + '/' + s)
        if slice.SeriesDescription == 't2_tse_fs_tra':
            shutil.copy(path + '/' + s, out_path + '/' + s)


for patient in patients:
    path = INPUT_FOLDER + patient
    zf = zipfile.ZipFile(path + '.zip', 'r')

    # Extract all members from the archive to the current working directory

    zf.extractall(unzip_path + patient)
    in_path = unzip_path + patient
    out_path = OUTPUT_FOLDER + patient
    if os.path.isdir(out_path) == False:
        os.mkdir(out_path)
    load_scan(in_path, out_path)
