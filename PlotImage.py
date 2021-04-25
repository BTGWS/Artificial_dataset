#!/usr/bin/env python
# coding:utf-8
# @TIME         : 2021/4/25 8:30 下午
# @Author       : BTG
# @Project      : Artificial_dataset
# @File Name    : PlotImage.py
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
import matplotlib.pyplot as plt
import numpy as np


def Display(X1, X2, imageName):
    """
    :param X1:          数据集1
    :param X2:          数据集2
    :param imageName:   图片名
    :return:
    """
    # 绘图函数
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    # matplotlib画图中中文显示会有问题，需要这两行设置默认字体

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.xlim(xmax=5, xmin=-1)
    plt.ylim(ymax=5, ymin=-1)
    # 画两条（-1,5）的坐标轴并设置轴标签x，y

    x_1, y_1, _ = X1.T
    x_2, y_2, _ = X2.T
    colors1 = '#00CED1'  # 点的颜色
    colors2 = '#DC143C'
    area = np.pi * 4 ** 2  # 点面积
    # 画散点图
    plt.scatter(x_1, y_1, s=area, c=colors1, alpha=0.4, label='类别1', marker='+')
    plt.scatter(x_2, y_2, s=area, c=colors2, alpha=0.4, label='类别2', marker='_')
    # plt.plot([-1,4.5],[4.5,-1],linewidth = '0.5',color='#000000')
    plt.legend()
    plt.savefig(imageName + '.jpg', dpi=600)
    # plt.show()
    plt.clf()
