import sys
sys.path.append("C:\\Users\\57165\Desktop\me\ic\year2\\term2\programming\\bb\\niuma\\")

from grid.grid import grid
import numpy as np
import cv2 as cv
with open("C:\\Users\\57165\Desktop\me\ic\year2\\term2\programming\\bb\\niuma\\tracking\\result.txt", 'r') as f:
    L = f.readlines()
    L = [ i.rstrip().split(',') for i in L]


count = len(L)
for i in range(count):
    for j in range(10):
        L[i][j] = int(L[i][j])


people_list = []
for i in range(count):
    if L[i][1] not in people_list:
        people_list.append(L[i][1])
people_list.sort()

#提取每个人帧数及对应坐标 (x,y,t)



path_dict = {}
for i in people_list:
    i_path = []
    for j in range(count):
        if L[j][1] == i:
            coordinate = (L[j][2]+L[j][4]/2,L[j][3], L[j][0])
            i_path.append(coordinate)

    path_dict[i] = i_path

n = 100
mat = np.zeros((n,n))
cap = cv.VideoCapture("C:\\Users\\57165\Desktop\me\ic\year2\\term2\programming\\bb\\niuma\\grid\p2.mp4")
ret, frame = cap.read()
height=frame.shape[0]
width=frame.shape[1]

G = grid(width, height, mat)
grid_path_dict = {}
for i in people_list:
    people_grid_path = []
    path_list = [(k[0], k[1]) for k in path_dict[i]]
    for j in path_list:
        grid_coordinate = G.get_grid_index(j)
        people_grid_path.append((grid_coordinate[0], grid_coordinate[1]))
    grid_path_dict[i] = people_grid_path

print(grid_path_dict[5])


