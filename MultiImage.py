#!/usr/bin/python3

import cv2

#starting camera
cap=cv2.VideoCapture(0)

while cap.isOpened():
    status,frame=cap.read()
    #converting image frame into grayscale
    grayimg=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.line(frame,(0,0),(200,300),(0,255,0),3)
    #cv2.imshow('live1',grayimg)
    #rectangle
    cv2.rectangle(frame,(50,50),(150,200),(0,0,255),2)
    #circle
    cv2.circle(frame,(200,300),80,(13,44,123),2)
    font=cv2.FONT_HERSHEY_SIMPLEX  #this is font type
    cv2.putText(frame,'AdHoc',(10,400),font,2,(0,2,55),2,cv2.LINE_AA)
    cv2.imshow('live',frame-10)
    if cv2.waitKey(10) & 0xff == ord('q') :
        break

#cv2.destroyWindow('live')
cv2.destroyAllWindows() # this will destroy all windows
# to close camera
cap.release()
