from ml.tree.trees import *

myDat,labels = createDataSet()
# shannonEent = calcShannonEnt(myDat)
# splitDataSet(myDat, 0, 1)
res = chooseBestFeatureToSplist(myDat)
print(res)