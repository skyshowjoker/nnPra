# coding=utf-8
import os
import xlwt  # 操作excel模块
import sys

root = r'C:\joey\master\resource\lymphoma'
dir = r'C:\joey\master\resource\lymphoma\PACS.Lymphoma.Spider\output'
file_path = root + '\\book2.xlsx'  # sys.path[0]为要获取当前路径，filenamelist为要写入的文件
f = xlwt.Workbook(encoding='utf-8', style_compression=0)  # 新建一个excel
sheet = f.add_sheet('sheet1')  # 新建一个sheet
pathDir = os.listdir(dir)  # 文件放置在当前文件夹中，用来获取当前文件夹内所有文件目录

i = 0  # 将文件列表写入test.xls
for s in pathDir:
    s = s.split('.')[0]
    if s.__contains__('MRI'):
        sheet.write(i, 0, s)  # 参数i,0,s分别代表行，列，写入值
        sheet.write(i, 1, i)
        i = i + 1


print(file_path)
print(i)  # 显示文件名数量
f.save(file_path)