from numpy import *
import matplotlib as plt

# 导入数据
def loadDataSet(fileName):
    dataMat = [];
    fr = open(fileName, "r")
    for line in fr.readlines():
        curline = line.strip().split('\t')
        aa = [float(i) for i in curline]
        dataMat.append(aa)
    return dataMat # // 注意对齐！

# 计算欧式距离
def distEclud(vecA, vecB):
    return sqrt(sum(power(vecA - vecB, 2)))

# 构建K个随机质心
def randCent(dataSet, k):
    n = shape(dataSet)[1]
    centroids = mat(zeros((k, n)))
    for j in range(n):
        minJ = min(dataSet[:,j])
        rangeJ  = float(max(dataSet[:,j]) - minJ)
        centroids[:, j] = minJ + rangeJ * random.rand(k, 1)
    return centroids

# 绘制散点图
def drawScatter(plt, mydata, size=20, color='blue', mrkr='o'):
    plt.scatter(mydata.T[0].tolist(), mydata.T[1].tolist(), s=size, c=color, marker=mrkr) # 需要先把矩阵转换成list

# 以不同颜色绘制数据集里的点
def color_cluster(dataindx, dataSet, plt):
    datalen = len(dataindx)
    for indx in range(datalen):
        if int(dataindx[indx]) == 0:
            plt.scatter(dataSet[indx, 0], dataSet[indx, 1], c='blue', marker='o')
        elif int(dataindx[indx]) == 1:
            plt.scatter(dataSet[indx, 0], dataSet[indx, 1], c='green', marker='o')
        elif int(dataindx[indx]) == 2:
            plt.scatter(dataSet[indx, 0], dataSet[indx, 1], c='red', marker='o')
        elif int(dataindx[indx]) == 3:
            plt.scatter(dataSet[indx, 0], dataSet[indx, 1], c='cyan', marker='o')


 #K均值聚类
def kMeans(dataSet, k, distMeas=distEclud, createCent=randCent):
    m = shape(dataSet)[0]
    clusterAssment = mat(zeros((m,2)))
    centroids = createCent(dataSet, k)
    clusterChanged = True
    while clusterChanged:
        clusterChanged = False
        for i in range(m):#寻找最近的质心
            minDist = inf; minIndex = -1
            for j in range(k):
                distJI = distMeas(centroids[j,:],dataSet[i,:])
                if distJI < minDist:
                    minDist = distJI; minIndex = j
            if clusterAssment[i,0] != minIndex: clusterChanged = True
            clusterAssment[i,:] = minIndex,minDist**2
        for cent in range(k):# 更新质心位置
            ptsInClust = dataSet[nonzero(clusterAssment[:,0].A==cent)[0]]#把所有点放在这个簇里
            centroids[cent,:] = mean(ptsInClust, axis=0) #分配质心, mean()求平均值
    return centroids, clusterAssment