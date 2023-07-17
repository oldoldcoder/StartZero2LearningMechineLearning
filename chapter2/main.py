import data
import k_nn
import numpy as np
# 总结，Python里面没有类型的规范或许是最大的弊端
# 我很不喜欢这个特性，这让我有些时候连自己处理的数据都不知道是什么样子的
# 而且py2与py3版本之间的更替使得部分老代码不能重用在新的代码之后，这让我恶心
if __name__ == "__main__":
    a = k_nn.classify0([-1,-1],np.mat(data.create_data_set()[0]),data.create_data_set()[1],1)
    print(a)