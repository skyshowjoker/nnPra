import os
path = r"C:\joey\master\resource\lymphoma\dataset\nnUNet_raw_data_base\nnUNet_raw_data\Task02_Lymphoma\imagesTr"
label = r"C:\joey\master\resource\lymphoma\dataset\nnUNet_raw_data_base\nnUNet_raw_data\Task02_Lymphoma\labelsTr"
fileList = os.listdir(path)
n = 0
for file in fileList:
        # 设置旧文件名（就是路径+文件名）
        oldname1 = path + os.sep + file  # os.sep添加系统分隔符
        oldname2 = label + os.sep + file  # os.sep添加系统分隔符
        code = "lymphoma_%03.0d" % n
        newname1 = path + os.sep + code + ".nii.gz"
        newname2 = label + os.sep + code + ".nii.gz"
        os.rename(oldname1, newname1)  # 用os模块中的rename方法对文件改名
        os.rename(oldname2, newname2)
        print(oldname1, '======>', newname1)
        n+=1