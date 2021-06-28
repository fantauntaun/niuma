import paddlehub as hub
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import moviepy
import os

# 查看原始视频的参数

cap = cv2.VideoCapture("C:\\Users\\57165\Desktop\me\ic\year2\\term2\programming\\bb\\niuma\\grid\p2.mp4")
ret, frame = cap.read()
height=frame.shape[0]
width=frame.shape[1]
fps = cap.get(cv2.CAP_PROP_FPS)  
size=cap.get(cv2.CAP_PROP_FRAME_WIDTH) 
size1=cap.get(cv2.CAP_PROP_FRAME_HEIGHT)  

print(height, width, fps, size, size1)


video = cv2.VideoWriter('C:\\Users\\57165\Desktop\me\ic\year2\\term2\programming\\bb\\niuma\\grid\p2.mp4', cv2.VideoWriter_fourcc('m', 'p', '4', 'v'), fps-6, (width,height)) 


#img = mpimg.imread('C:\\Users\\57165\Desktop\me\ic\year2\\term2\programming\\bb\grid\people.mp4\\img2/300.jpg')
#plt.imshow(img)
#plt.axis('off')
#plt.show()



for i in range(1010):
    item = 'C:\\Users\\57165\Desktop\me\ic\year2\\term2\programming\\bb\\niuma\\grid\img2/' + str(i+1) + '.jpg' 
    img = cv2.imread(item)
    video.write(img)       
   
video.release() #释放





