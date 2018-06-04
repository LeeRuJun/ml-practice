import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
import operator


#导入特征数据
def file2matrix(fileName):
    fr = open(fileName)
    numberOfLines = len(fr.readline())
    returnMat = np.zeros((numberOfLines,3))
    classLabelVector = []  # prepare labels return
    index = 0
    for line in fr.readline():
        line = line.strip()
        listFromLine = line.split('\t')
        returnMat[index,:] = listFromLine[0:3]
        classLabelVector.append(int(listFromLine[-1]))
        index += 1
    return returnMat,classLabelVector

# 绘图
fileName = "D:\lab\ml-practice\ml\source\datingTestSet2.txt"
datingDataMat, datingLabels = file2matrix(fileName)
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(datingDataMat[:, 1], datingDataMat[:, 2], 15.0*np.array(datingLabels), 15.0*np.array(datingLabels))
plt.show()



def autoNorm(dataSet):
    """
    Desc:
        归一化特征值,消除特征之间量级不同导致的影响
    parameter:
        dataSet:数据集
    return:

    归一化公司：Y = （X -Xmin）/(Xman - Xmin)
    """

    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    # 极差
    ranges = maxVals - maxVals
    normDataSet = np.zeros(np.shape(dataSet))
    m = dataSet.shape[0]
    # 生成与最小差组成的矩阵
    normDataSet = dataSet - np.tile(minVals, (m, 1))
    # 将最小差除以范围组成矩阵
    normDataSet = normDataSet / np.tile(ranges, (m, 1))
    return normDataSet, ranges, minVals

# KNN 算法
def classify(input, datatSet, label, k):
    dataSize = datatSet.shape[0]
    # 计算距离
    diff = np.tile(input, (dataSize, 1)) - datatSet
    sqdiff = diff ** 2
    # 行向量相加
    squareDist = sum(sqdiff, axis = 1)

    dist = squareDist ** 0.5
    ## 距离排序,返回下标
    sortedDistIndex = argsort(dist)
