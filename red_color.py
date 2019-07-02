#!/usr/bin/python3

import cv2
# start camera
cap=cv2.VideoCapture(0)

# status of camera

while cap.isOpened():
    status, frame = cap.read()
    # detecting red color
    redimg=cv2.inRange(frame,(0,0,0),(40,40,255))
    cv2.imshow('liveredcolor',redimg)
    if cv2.waitKey(10) & 0xff==ord('q'):
        break

cv2.destroyAllWindows()
cap.release()
