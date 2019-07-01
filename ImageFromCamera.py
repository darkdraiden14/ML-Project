#!/usr/bin/python3

import cv2

# starting camera
cap=cv2.VideoCapture(0)
#       first camera
# to check camera is started or not
if cap.isOpened() :
    print("Camera is ready to take pictures")
else:
    print("Check your webcam drivers:")

# now we can take read input from camera
status,img=cap.read() # it will take first picture
status1,img1=cap.read() # it will take 2nd picture
# now showing
cv2.imshow("img",img)
cv2.imshow("img1",img1)
cv2.waitKey(0)
# to close camera
cap.release()
