#!/usr/bin/env python
# coding:utf-8
# @TIME         : 2021/4/25 8:16 下午
# @Author       : BTG
# @Project      : Artificial_dataset
# @File Name    : IOFile.py
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
import pandas as pd


def writeFile(dataset, filename):
    """
    :param dataset:     需要存储的数据集
    :param filename:    文件名
    :return:
    """
    writer = pd.ExcelWriter(filename + '.xlsx')  # 写入Excel文件
    dataset.to_excel(writer, 'page_1', float_format='%.5f', header=True, index=False)  # ‘page_1’是写入excel的sheet名
    writer.save()
    writer.close()


def read_File(filepath):
    """
    :param filepath:    文件路径
    :return:            文件内容
    """
    temp = filepath.split('/')
    temp = temp[-1].split('.')
    dataset = []
    # print(temp)

    if temp[-1] == 'csv':
        dataset = pd.read_csv(filepath)
    else:
        dataset = pd.read_excel(filepath)
    return dataset
