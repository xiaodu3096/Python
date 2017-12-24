#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 23/12/2017 21:40
# @Author  : DaBai
# @Site    : 
# @File    : PictureCut.py
# @Software: PyCharm
# import numpy as np
# import PIL.Image as image
# from sklearn.cluster import KMeans
# from sklearn import metrics
# import sklearn.cluster as skc
#
# def loadData(filepath):
#     f = open(filepath,'rb')
#     data = []
#     img = image.open(f)
#     m,n = img.size
#     for i in range(m):
#         for j in range(n):
#             x,y,z = img.getpixel((i,j))
#             data.append([x/256.0,y/256.0,z/256.0])
#         f.close()
#         return np.mat(data),m,n
#
#
# imgData,row,col = loadData(r'xiaodu.jpg')
# print(row,col)
# label = KMeans(n_clusters=20).fit(imgData)
# label = label.reshape([row,col])
# pic_new = image.new("L",(row,col))
# for i in range(row):
#     for j in range(col):
#         print(label[i][j])
#         pic_new.putpixel((i,j),int(256/(label[i][j]+2)))
# pic_new.save("2.jpg","JPEG")

# import numpy as np
# import  pandas as pd
# import copy
# import matplotlib.pyplot as plt
#
# pic = plt.imread('xiaodu.jpg')
#
# data = pic.reshape(-1,3)
#
# def kmeans_wave(n,k,data):
#     data_new = copy.deepcopy(data)
#     data_new = np.column_stack((data_new, np.ones(1200*800)))
#     center_point = np.random.choice(1200*800, k, replace=False)
#     center = data_new[center_point,:]
#     distance = [[] for i in range(k)]
#     for i in range(n):
#         for j in range(k):
#             distance[j] = np.sprt(np.sum(np.square(data_new - np.array(center[j])), axis = 1))
#             # distance[j] = np.sqrt(np.sum(np.square(data_new - np.array(center[j])), axis=1))
#             data_new[:,3] = np.argmin(np.array(distance),axis=0)
#             for l in range(k):
#                 center[l] = np.mean(data_new[data_new[:,3]==1],axis = 0)
#     return data_new
#
#
#
#
# if __name__ == '__main__':
#     data_new = kmeans_wave(100,5,data)
#     print(data_new.shape)
#     pic_new = data_new[:,3].reshape(1200,800)
#     plt.imshow(pic_new)
#     plt.show()

