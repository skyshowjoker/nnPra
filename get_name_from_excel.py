# 改文件名为序号
import os
import xlwt  # 操作excel模块
import xlrd
import sys
import numpy as np
def get_excel():
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




input_file_name = r'C:\joey\master\resource\lymphoma\book2.xlsx'

dir_path = r"C:\joey\master\resource\lymphoma\dcm_slice"
def read_excel(input_file_name, path):
    """
    从xls文件中读取数据
    """
    workbook = xlrd.open_workbook(input_file_name)
    print(workbook)
    # 可以使用workbook对象的sheet_names()方法获取到excel文件中哪些表有数据
    print(workbook.sheet_names())
    # 可以通过sheet_by_index()方法或sheet_by_name()方法获取到一张表，返回一个对象
    # table = workbook.sheet_by_index(0)
    # print(table)
    table = workbook.sheet_by_name('sheet1')
    print(table)
    # 通过nrows和ncols获取到表格中数据的行数和列数
    rows = table.nrows
    cols = table.ncols
    print(cols)



    fileList = os.listdir(path)
    n = 0
    for file in fileList:
        # 设置旧文件名（就是路径+文件名）
        oldname = path + os.sep + file  # os.sep添加系统分隔符
        for i in range(rows):
            if table.cell(i, 0).value == file:
                newname = path + os.sep + str(int(table.cell(i, 1).value))
                os.rename(oldname, newname)  # 用os模块中的rename方法对文件改名
                print(oldname, '======>', newname)
        # 设置新文件名





        n += 1




read_excel(input_file_name, dir_path)







