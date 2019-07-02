#!/usr/bin/python3

import cv2

img=cv2.imread('a.jpg',1)

# calling classifier
casClf=cv2.CascadeClassifier('face.xml')
# laoding face data
cap=cv2.VideoCapture(0)
# now we can apply classifier in live 
face = casClf.detectMultiScale(img,1.5,5)  # classifier tuning parameter
#print(face)
for x,y,h,w in face:
    cv2.rectangle(img,(x,y),(x+h,y+w),(0,0,255),2)

cv2.imshow('face',img)
cv2.waitKey(0)

cv2.destroyAllWindows()
cap.release()
