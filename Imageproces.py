#!/usr/bin/python3
import cv2
import sys

### version
print(cv2.__version__)

### image name as first argument
data=sys.argv[1]

### image read
img=cv2.imread(data,1)  # loading image in color format -- original image 
print(img)
# shape
print(img.shape)
# height, width, color channel
# to show the image
cv2.imshow("windowname",img)
cv2.imshow("Window1",img[0:250,40:210]/5)

#saving image
cv2.imwrite('newbb.jpg',img[0:250,40:210]/5)

cv2.waitKey(0)  # holding window for infinite time
