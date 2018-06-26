# -*- encoding:utf-8 -*-

from ml.cluster.kmeans import *
import matplotlib.pyplot as plt

fileName = r"../source/testSet.txt"
datMat = mat(loadDataSet(fileName))
bb = randCent(datMat, 2)
cc = distEclud(datMat[0], datMat[1])
clustercents, ClustDist = kMeans(datMat,3)

# 输出生成的ClustDist：对应的聚类中心(列1),到聚类中心的距离(列2),行与dataSet一一对应
color_cluster(ClustDist[:, 0:1], datMat, plt)
# 绘制聚类中心
drawScatter(plt, clustercents, size=60, color='red', mrkr='D')
plt.show()