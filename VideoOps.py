#!/usr/bin/python3

import cv2

#starting camera
cap=cv2.VideoCapture(0)
#adding plugin
plugin=cv2.VideoWriter_fourcc(*'XVID')
# now saving video                             width , height 
output=cv2.VideoWriter('class.avi',plugin,20,(640,480))


while cap.isOpened():
    status,frame=cap.read()
    cv2.imshow('live',frame)
    #draw pattern
    output.write(frame) # sending data to  VideoWriter 
    if cv2.waitKey(10) & 0xff == ord('q') :
        break

#cv2.destroyWindow('live')
cv2.destroyAllWindows() # this will destroy all windows
# to close camera
cap.release()
