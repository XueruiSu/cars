import cv2
import numpy as np
import os
car_cascade = cv2.CascadeClassifier('cars3.xml')


 
#def video_split(video_path,save_path):
#	'''
#	对视频文件切割成帧
#	'''
#	'''
#	@param video_path:视频路径
#	@param save_path:保存切分后帧的路径
#	'''
#	vc=cv2.VideoCapture(video_path)
#	#一帧一帧的分割 需要几帧写几
#	c=0
#	if vc.isOpened():
#		rval,frame=vc.read()
#	else:
#		rval=False
#	while rval:
#		rval,frame=vc.read()
		
#		cv2.imwrite(save_path + "/" + str(c)+'.jpg',frame)
#		c=c+1

#video_split("vid1.mp4","C:/Users/86137/Desktop/cars/ved1")


input_path="C:/Users/86137/Desktop/cars/ved1"
car=cv2.CascadeClassifier("cars.xml")
for f in range(305):
    input_file = input_path + '/' + str(f)+".jpg"
    img = cv2.imread(input_file, 1)

    gray =  cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    cars = car.detectMultiScale(gray, 1.05, 1)
    for (x, y, w, h) in cars:
        print(2)
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 2)
        cv2.imshow("video", img)
        print(1)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

