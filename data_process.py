import os
from glob import glob
import numpy as np
import vtk
import tqdm
import numpy as np
import nrrd  #pip install pynrrd
import h5py
from os import path

import nibabel as nb


def readnrrd(filename):
    """Read image in nrrd format."""
    #reader = vtk.vtkNrrdReader()
    reader = vtk.vtkNIFTIImageReader()
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

def covert_h5():
    listt = glob(r'D:\Tumor_Dataset\CT')
    print(listt)

    for item in tqdm(listt):
        image, img_header = nrrd.read(item)
        label, gt_header = nrrd.read(item.replace('lgemri.nrrd', 'laendo.nrrd'))
        label = (label == 255).astype(np.uint8)
        w, h, d = label.shape

        tempL = np.nonzero(label)  # 得到数组array中非零元素的位置（下标）
        minx, maxx = np.min(tempL[0]), np.max(tempL[0])
        miny, maxy = np.min(tempL[1]), np.max(tempL[1])
        minz, maxz = np.min(tempL[2]), np.max(tempL[2])

        px = max(output_size[0] - (maxx - minx), 0) // 2
        py = max(output_size[1] - (maxy - miny), 0) // 2
        pz = max(output_size[2] - (maxz - minz), 0) // 2
        minx = max(minx - np.random.randint(10, 20) - px, 0)
        maxx = min(maxx + np.random.randint(10, 20) + px, w)
        miny = max(miny - np.random.randint(10, 20) - py, 0)
        maxy = min(maxy + np.random.randint(10, 20) + py, h)
        minz = max(minz - np.random.randint(5, 10) - pz, 0)
        maxz = min(maxz + np.random.randint(5, 10) + pz, d)

        image = (image - np.mean(image)) / np.std(image)  # 标准化/0均值化，将数据中心转移到原点处，np.std计算标准差
        image = image.astype(np.float32)
        image = image[minx:maxx, miny:maxy]
        label = label[minx:maxx, miny:maxy]
        print(label.shape)
        f = h5py.File(item.replace('lgemri.nrrd', 'mri_norm2.h5'), 'w')
        f.create_dataset('image', data=image, compression="gzip")
        f.create_dataset('label', data=label, compression="gzip")
        f.close()


if __name__ == '__main__':
    '''
    #baseDir = os.path.normpath(r'D:\Tumor_Dataset\CT')
    rootdir = r'D:\Tumor_Dataset\label_1'

    file = os.listdir(rootdir)
    for f in file:
        # 字符串拼接
        real_url = path.join(rootdir, f)
        # 打印出来
        print(real_url)

        files = real_url
        #for file in files:
        m, info = readnrrd(files)
        writenifti(m,  files.replace('.nii', '.nrrd'), info)
    '''

    rootdir = r'D:\Tumor_Dataset\CT'
    file = os.listdir(rootdir)
    for xs in file:
        # 字符串拼接
        real_url = path.join(rootdir, xs)
        # 打印出来
        print(real_url)

        CT = real_url
        label1 = CT.replace('CT','label_2')
        str = xs.replace('.nii','')
        h5 = r'D:\Tumor_Dataset\label2_h5\xxxx\mri_norm2.h5'
        h5_dir = r'D:\Tumor_Dataset\label2_h5\xxxx'
        h5 = h5.replace('xxxx',str)
        h5_dir = h5_dir.replace('xxxx',str)
        if os.path.exists(label1):  # 如果文件存在
            os.makedirs(h5_dir)
            print(label1,h5)


            nii_img = nb.load(CT)
            nii_data = nii_img.get_fdata()
            image = nii_data.copy()


            nii_img = nb.load(label1)
            nii_data = nii_img.get_fdata()
            label = nii_data.copy()

            f = h5py.File(h5, 'w')
            f.create_dataset('image', data=image, compression="gzip")
            f.create_dataset('label', data=label, compression="gzip")
            f.close()

