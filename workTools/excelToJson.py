#-*- encoding:utf-8 -*-
import json
import xlrd

def readExcel():
    # 打开excel表单
    filename = u'D:\\Users\\rj_li\\Desktop\\每月活动数据\\六月下旬游乐园视频商品列表180615.xlsx'
    excel = xlrd.open_workbook(filename)

    # 得到第一张表单
    sheet1 = excel.sheets()[1]
    #找到有几列几列
    nrows = sheet1.nrows #行数
    ncols = sheet1.ncols #列数

    totalArray=[]
    title=[]
    # 标题
    for i in range(0,ncols):
        title.append(sheet1.cell(0,i).value);

    #数据
    for rowindex in range(1,nrows):
        dic={}
        for colindex in range(0,ncols):
            s=sheet1.cell(rowindex,colindex).value
            dic[title[colindex]]=s
        totalArray.append(dic);

    return json.dumps(totalArray,ensure_ascii=False)

print(readExcel());
