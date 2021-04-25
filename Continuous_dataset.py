import numpy as np


def Gaussian_Distribution_Dataset(mean, cov, num, classification):
    """

    :param mean:    N维分布的均值
    :param cov:     协方差均值
    :param num:     需要生成的数据数
    :param classification:  类别
    :return:        生成的数据集
    """
    x = np.random.multivariate_normal(mean, cov, num, 'raise')
    y = [classification] * x.shape[0]
    dataset = np.column_stack((x, y))

    return dataset
