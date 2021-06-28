import paddlehub as hub
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import moviepy
import os


cap = cv2.VideoCapture("C:\\Users\\57165\Desktop\me\ic\year2\\term2\programming\\bb\\niuma\\grid\people.mp4")
i=1
while True:
    ret, frame = cap.read()
    if frame is None:
        break
    else:
        cv2.imwrite('C:\\Users\\57165\Desktop\me\ic\year2\\term2\programming\\bb\\niuma\\grid\img1/'+str(i)+".jpg", frame)
        i+=1


img1_num = []
img1_list = os.listdir('C:\\Users\\57165\Desktop\me\ic\year2\\term2\programming\\bb\\niuma\\grid\img1')
for i in img1_list:
    img1_num.append('img1/'+str(i))
count = len(img1_num)

print(count)


object_detector = hub.Module(name="yolov3_resnet50_vd_coco2017")

for i in range(count):
    i += 1
    result = object_detector.object_detection(images=[cv2.imread('C:\\Users\\57165\Desktop\me\ic\year2\\term2\programming\\bb\\niuma\\grid\img1/'+str(i)+'.jpg')])
    if i%50 ==0:
        print(result)
    img = mpimg.imread('detection_result/image_numpy_0.jpg')

    cv2.imwrite('C:\\Users\\57165\Desktop\me\ic\year2\\term2\programming\\bb\\niuma\\grid\img2/'+str(i)+'.jpg', img)


# 查看原始视频的参数
cap = cv2.VideoCapture("C:\\Users\\57165\Desktop\me\ic\year2\\term2\programming\\bb\\niuma\\grid\people.mp4")
ret, frame = cap.read()
height=frame.shape[0]
width=frame.shape[1]
fps = cap.get(cv2.CAP_PROP_FPS)  
size=cap.get(cv2.CAP_PROP_FRAME_WIDTH) 
size1=cap.get(cv2.CAP_PROP_FRAME_HEIGHT)  

print(height, width, fps, size, size1)


video = cv2.VideoWriter('C:\\Users\\57165\Desktop\me\ic\year2\\term2\programming\\bb\\niuma\\grid\people.mp4', cv2.VideoWriter_fourcc('m', 'p', '4', 'v'), fps-6, (width,height)) 


#img = mpimg.imread('C:\\Users\\57165\Desktop\me\ic\year2\\term2\programming\\bb\grid\people.mp4\\img2/300.jpg')
#plt.imshow(img)
#plt.axis('off')
#plt.show()



for i in range(count):
    item = 'C:\\Users\\57165\Desktop\me\ic\year2\\term2\programming\\bb\\niuma\\grid\img2/' + str(i+1) + '.jpg' 
    img = cv2.imread(item)
    video.write(img)       
   
video.release() #释放





from moviepy.editor import *
video_o = VideoFileClip("C:\\Users\\57165\Desktop\me\ic\year2\\term2\programming\\bb\\niuma\\grid\people.mp4")     
videoclip = VideoFileClip("C:\\Users\\57165\Desktop\me\ic\year2\\term2\programming\\bb\\niuma\\grid\people.mp4")
audio_o = video_o.audio

videoclip2 = videoclip.set_audio(audio_o)

videoclip2.write_videofile("movie_video/detect_final.mp4")