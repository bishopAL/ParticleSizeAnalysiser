# -*- coding: utf-8 -*-
import cv2
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import sys
from matplotlib.ticker import FuncFormatter
if sys.argv[1] == None:
    path = 'test.jpg'
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
th = int(area_list[-1]-area_list[0])/3
low = []
mid = []
high = []
for item in area_list:
    if item < th:
        low.append(item**3)
    elif item >= th and item < 2 * th:
        mid.append(item**3)
    else:
        high.append(item**3)
total = sum(low) + sum(mid) + sum(high)
y = [sum(low)/total, sum(mid)/total, sum(high)/total]
rad = ['Low rad', 'Mid rad', 'High rad']
print(y)
 
plt.bar(rad, y, alpha=0.5, width=0.5, label='Partical Size', lw=3)
plt.legend()
def to_percent(temp, position):
    return '%1.0f'%(100*temp) + '%'
plt.gca().yaxis.set_major_formatter(FuncFormatter(to_percent))
plt.show()