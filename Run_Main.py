#!/usr/bin/env python
# coding:utf-8
# @TIME         : 2021/4/25 7:49 下午
# @Author       : BTG
# @Project      : Artificial_dataset
# @File Name    : Run_Main.py
"""
# Code is far away from bugs with the god animal protecting.
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃        ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""
import numpy as np
import pandas as pd

from Continuous_dataset import Gaussian_Distribution_Dataset
from IOFile import writeFile
from PlotImage import Display

if __name__ == '__main__':
    num = 500
    mean_1 = [1.0, 1.0]
    cov_1 = [[0.6, -0.2], [-0.2, 0.6]]

    mean_2 = [2.5, 2.5]
    cov_2 = [[0.2, -0.1], [-0.1, 0.2]]

    X1 = Gaussian_Distribution_Dataset(mean_1, cov_1, num, '1')
    X2 = Gaussian_Distribution_Dataset(mean_2, cov_2, num, '2')
    ans = np.concatenate((X1, X2), axis=0)
    dataset = pd.DataFrame(ans, columns=['a1', 'a2', 'c'])
    # 写入文件
    writeFile(dataset, 'fuck_1')
    Display(X1, X2, 'fuck_1')
