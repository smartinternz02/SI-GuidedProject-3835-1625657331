# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 22:54:19 2021

@author: vighn
"""

import cv2

car_classifier=cv2.CascadeClassifier("cars.xml")


video=cv2.VideoCapture("dataset_video2.avi")
#video=cv2.VideoCapture("dataset_video1.avi")
while True:
    #capture the first frame
    check,frame=video.read()
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Gray', gray)

    #detect the faces from the video using detectMultiScale function
    cars=car_classifier.detectMultiScale(gray,1.3,5)
    print(cars)
    
    #drawing rectangle boundries for the detected face
    for(x,y,w,h) in cars:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 2)
        cv2.imshow('Face detection', frame)
        #picname=datetime.datetime.now().strftime("%y-%m-%d-%H-%M")
        #cv2.imwrite(picname+".jpg",frame)
        
    
    #waitKey(1)- for every 1 millisecond new frame will be captured
    Key=cv2.waitKey(1)
    if Key==ord('q'):
        #release the camera
        #video.release()
        #destroy all windows
        cv2.destroyAllWindows()
        break