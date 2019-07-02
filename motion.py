#!/usr/bin/python3

import cv2
# start camera
cap=cv2.VideoCapture(0)

tp1=cap.read()[1] #take1
tp2=cap.read()[1] #take2
tp3=cap.read()[1] #take3
# to make more perfect
gray1=cv2.cvtColor(tp1,cv2.COLOR_BGR2GRAY)   # converting into gray
gray2=cv2.cvtColor(tp2,cv2.COLOR_BGR2GRAY)   # converting into gray
gray3=cv2.cvtColor(tp3,cv2.COLOR_BGR2GRAY)   # converting into gray

# now creating image diff
def img_diff(x,y,z):
    # diff btw x,y --gray1,gray2 --d1
    d1=cv2.absdiff(x,y)
    # diff btw y,z --gray2,gray3 --d2
    d2=cv2.absdiff(y,z)
    # abs diff d1-d2  
    finalimg=cv2.bitwise_and(d1,d2)
    return finalimg

# now apply fuction:
while cap.isOpened():
    status, frame =cap.read()
    motionimg=img_diff(gray1,gray2,gray3)
    # replacing image frame 
    gray1=gray2
    gray2=gray3
    gray3=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)   # passing the live image
    cv2.imshow('live',frame)
    cv2.imshow('motion',motionimg) # motion detect
    if cv2.waitKey(10) & 0xff==ord('q'):
        break

cv2.destroyAllWindows()
cap.release()

