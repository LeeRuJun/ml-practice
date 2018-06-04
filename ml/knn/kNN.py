from numpy import *
import operator

def createDataSet():
    group = array([1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1])
    labels = ['A', 'A', 'B', 'B']
    return group, labels

def calssify0(inX, dataSet, labels, k):
    # 矩阵第一维的长度
    dataSetSize = dataSet.shape[0]
    # 重复inX
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat ** 2
    # 将矩阵每一行向量相加
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances ** 0.5
    # 元素从小到大排列
    sortedDistIndicies = distances.argsort()
    classCount = {}
    for i in range(k):
        voteIlabel  = labels[sortedDistIndicies[i]]
        # 次数累加
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
        sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
        # return sortedClassCount[0][0]
        print(sortedClassCount[0][0])


if __name__ == '__main__':
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    calssify0([0, 0], group, labels, 3)

