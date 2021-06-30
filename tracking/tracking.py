
import sys
sys.path.append("C:\\Users\\57165\Desktop\me\ic\year2\\term2\programming\\bb\\niuma\\")

from grid.grid import grid
import numpy as np
import cv2 as cv
with open("C:\\Users\\57165\Desktop\me\ic\year2\\term2\programming\\bb\\niuma\\tracking\\result.txt", 'r') as f:
    L = f.readlines()
    L = [ i.rstrip().split(',') for i in L]

def save_image(image,addr,num):
  address = addr + str(num)+ '.jpg'
  cv.imwrite(address,image)


def print_path(person_index, path_dict):
    path = path_dict[person_index]

    frame_final = path[-1][-1]
    print(frame_final)
    videoCapture = cv.VideoCapture("C:\\Users\\57165\Desktop\me\ic\year2\\term2\programming\\bb\\niuma\\tracking\people.mp4")


    i = 0
    while True:
        ret, frame = videoCapture.read()
        i = i + 1
        if i == frame_final:
            
            save_image(frame, 'C:\\Users\\57165\Desktop\me\ic\year2\\term2\programming\\bb\\niuma\\tracking\output/image',str(i))
            img = cv.imread("C:\\Users\\57165\Desktop\me\ic\year2\\term2\programming\\bb\\niuma\\tracking\output/image"+ str(i)+".jpg")


            for j in range(len(path)-1):
                coor1 = path[j]
                coor2 = path[j+1]
                cv.line(img, pt1=(int(coor1[0]), int(coor1[1])), pt2=(int(coor2[0]), int(coor2[1])), color=(0, 255, 0), thickness=5)

           
    
            cv.imshow('C:\\Users\\57165\Desktop\me\ic\year2\\term2\programming\\bb\\niuma\\tracking\output/image'+str(i), img)
            if cv.waitKey(0) & 0xFF == ord('q'):
                    cv.destroyAllWindows()
            break


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

need_report = []
confirmed_path = []

path_dict = {}
for i in people_list:
    i_path = []
    for j in range(count):
        if L[j][1] == i:
            coordinate = (L[j][2]+L[j][4]/2,L[j][3], L[j][0])
            i_path.append(coordinate)

    path_dict[i] = i_path

n = 20
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

print(path_dict[95])

print_path(95,path_dict)

for i in people_list:
    grid_path = grid_path_dict[i]
    if grid_path not in confirmed_path:
        need_report.append(i)
        need_report.append(grid_path)



    else:
        pass


