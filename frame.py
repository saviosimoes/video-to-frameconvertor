import os 
import shutil
directory = input("Enter the Directory name you want: ")
parent_dir = "/home/...../video_data"
path = os.path.join(parent_dir, directory) 
os.mkdir(path) 
print("Directory '% s' created" % directory) 

import cv2

detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

vidcap = cv2.VideoCapture(0)
success, image = vidcap.read()
count = 1
while success:
    ret, img = vidcap.read()      #To detect faces if needed
    #gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(img, 1.3, 5)
    for (x,y,w,h) in faces:
        image = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    cv2.imwrite("/home/......./image_%d.jpg" % count, image)   #Saves the images to the desired folder 
    success, image = vidcap.read()
    print('Saved image ', count)
    count += 1
    if count == 200:        #max no of frames to be generated
        vidcap.release()
  
   
#to transfer the images to another directory if needed

files = os.listdir("/home/.....")     
dir_src = ("/home/......")
for f in files:
    if f.endswith('.jpg'):
        shutil.move( dir_src + f, path)
