import numpy as np
import data
import operator


# 使用的哲学思想是物以类聚，人以群分
def classify0(inx, dataSet, labels, k):
    dataSetSzie = dataSet.shape[0]
    print("dataSet shape is:", dataSet.shape)
    dffMat = np.tile(inx, (dataSetSzie, 1)) - dataSet
    sqDiffMat = np.power(dffMat, 2)
    sqDistances = sqDiffMat.sum(axis=1)
    distances = np.power(sqDistances, 0.5)
    # 返回的是排序之后的索引值
    sortedDisIndicies = distances.argsort(axis=0)
    classCount = {}

    for i in range(k):
        voteIlable = labels[sortedDisIndicies[i, 0]]
        # 如果存在返回值否则第二个参数代表的默认值
        classCount[voteIlable] = classCount.get(voteIlable, 0) + 1
    # 降序排列返回，给出字典的可迭代对象，同时按照可迭代对象的第二个值进行排序
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]
