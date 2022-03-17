import vtk
import SimpleITK as sitk
def readnrrd(filename):
    """Read image in nrrd format."""
    reader = vtk.vtkNrrdReader()
    reader.SetFileName(filename)
    reader.Update()
    info = reader.GetInformation()
    return reader.GetOutput(), info

def writenifti(image,filename, info):
    """Write nifti file."""
    writer = vtk.vtkNIFTIImageWriter()
    writer.SetInputData(image)
    writer.SetFileName(filename)
    writer.SetInformation(info)
    writer.Write()

base_path = r'C:\Users\perlicue\Desktop\戴松玉_2019-06-20_眼眶MRI增强_2280229_0000040310(5599422)'
data_path=base_path + r'\t2_tra-label.nrrd'
save_path=base_path + r'\t2_tra-label.nii.gz'
m, info = readnrrd(data_path)
writenifti(m, save_path, info)