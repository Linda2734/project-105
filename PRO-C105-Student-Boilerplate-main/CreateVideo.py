import cv2
import os
import time

path = "/Users/lindasabei/Downloads/PRO-C105-Project-Images-main/Images"
images = []
file = os.listdir(path)
file.sort()
print(file)

for x in file:
    name,extension = os.path.splitext(x)
    if extension in [".png",".jpg","jpeg"]:
        file_name = path+"/"+x
        images.append(file_name)

frame = cv2.imread(images[4])
height,width,color = frame.shape
print(frame.shape)
outputVideo = cv2.VideoWriter("friends.mp4",cv2.VideoWriter_fourcc(*"DIVX"),5,(width,height))
count = len(images)-1
for i in range(count,0,-1):
    frame = cv2.imread(images[i])
    outputVideo.write(frame)

outputVideo.release()
print("done")

    