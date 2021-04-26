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
import numpy as np
import matplotlib.pyplot as plt


# 绘图函数
def Display(dataset, Y, save_path):
    # 绘制散点图
    """
    :param dataset:     numpy数组格式的源数据集
    :param Y:           类别
    :param save_path:   图片存储路径
    :return:
    """
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    # matplotlib画图中中文显示会有问题，需要这两行设置默认字体

    plt.xlabel('x1')
    plt.ylabel('x2')
    # plt.xlim(xmax=4.5,xmin=-1.5)
    # plt.ylim(ymax=2.5,ymin=0.5)
    # 画两条（-1,5）的坐标轴并设置轴标签x，y
    colors = ['#00CED1', '#DC143C', 'k', 'limegreen', '#000000', '#006400', 'peru', 'c', 'orange', 'lightpink']

    area = np.pi * 4 ** 2  # 点面积

    GA_S = np.array(dataset)
    markers = ['+', '_', 'o', 'v', '<', '*', 'p', 'D', '^', '>']
    index = 0
    for i in Y:
        # i = int(i)
        # color=plt.cm.Set1(GA_S[i,2] / 10.)
        x_1, x_2, c = GA_S[np.where(GA_S[:, 2] == i)].T
        plt.scatter(x_1, x_2, s=area, color=colors[index], alpha=0.4, label='类别: ' + str(i), marker=markers[index])
        index += 1

    # x_1,y_1,c_1 = GA_S[np.where(GA_S[:,2] == 1)].T
    # x_2,y_2,c_2 = GA_S[np.where(GA_S[:,2] == 2)].T

    # 画散点图
    # plt.scatter(x_1, y_1, s=area, c=colors1, alpha=0.4, label='类别1', marker='+')
    # plt.scatter(x_2, y_2, s=area, c=colors2, alpha=0.4, label='类别2', marker='_')
    # plt.scatter(a1_test, Y_test, s=area, c=colors3, alpha=0.4, label='Training goal', marker='o')
    # plt.scatter(a1_test, Fl_test+0.05, s=area, c=colors4, alpha=0.4, label='ELM output', marker='v')

    # plt.plot([-1,4.5],[4.5,-1],linewidth = '0.5',color='#000000')
    plt.legend()
    plt.savefig(save_path, dpi=600)
    plt.clf()
    # plt.show()
