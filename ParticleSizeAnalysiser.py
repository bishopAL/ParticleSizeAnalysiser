# -*- coding: utf-8 -*-
from ctypes import sizeof
import cv2
import matplotlib
import numpy as np
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import sys
from matplotlib.ticker import FuncFormatter

def to_percent(temp, position):
    return '%1.0f'%(100*temp) + '%'

temp = len(sys.argv)
if len(sys.argv) < 2:
    path = 'c40.jpg'
else:
    path = sys.argv[1]
plt.rcParams['font.family'] = ['Times New Roman']
plt.rcParams.update({'font.size': 14})

pic = cv2.imread(path, 0)
ret, bw = cv2.threshold(pic, 50, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(bw, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
area_list = []
for item in contours:
    temp = cv2.contourArea(item)
    if temp<5000 and temp > 0:
        area_list.append(temp ** 0.5)
area_list.sort()

point_num = 12
th = int(area_list[-1]-area_list[0])/point_num
temp_volume_list = [[] for i in range(point_num)]
temp_deviation_list = []
for item in area_list:
    for i in range(point_num):
        if (area_list[0]+th*i)<item and (area_list[0]+th*(i+1))>=item:
            temp_volume_list[i].append(item**3)
    if (area_list[0]+th*3)<item and (area_list[0]+th*7)>=item:
        temp_deviation_list.append(item)


sum_volume_list = []
for i in range(point_num):
    sum_volume_list.append(sum(temp_volume_list[i]))
temp_sum = sum(sum_volume_list)
for i in range(point_num):
    sum_volume_list[i] /= temp_sum
grade = sum(sum_volume_list[4:8])
standard_deviation = np.std(np.array(temp_deviation_list))
print(grade,standard_deviation)

plt.plot(sum_volume_list)
plt.ylabel("Volume Ratio %")
plt.xlabel("Relative Volume")
plt.gca().yaxis.set_major_formatter(FuncFormatter(to_percent))
plt.show()



# plt.bar(rad, y, alpha=0.5, width=0.5, label='Partical Size', lw=3)
# plt.legend()
