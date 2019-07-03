#!/usr/bin/python3

import numpy as np
import cv2

# now read both image
img1=cv2.imread('1.jpg')
img2=cv2.imread('2.jpg')

#reading the height and width of the images
h1, w1 =img1.shape[:2]
h2, w2 =img2.shape[:2]
# taking height and width for cutting the image
h=int(input("Enter the Heigth:"))
w=int(input("Enter the Width:"))

# creating empty images
vis1=np.zeros((h1,w1,3),np.uint8)
vis2=np.zeros((h2,w2,3),np.uint8)

# replacing them on their actual images
vis1[0:h,:w,:]=img2[0:h,:w,:]
vis1[0:h,w:,:]=img1[0:h,w:,:]
vis2[0:h,:w,:]=img1[0:h,:w,:]
vis2[0:h,w:,:]=img2[0:h,w:,:]


# random replacement
img1[0:11,0:21,:]=np.random.randint(low=0,high=255)
#showing the image
cv2.imshow('image1',vis1)
cv2.imshow('image2',vis2)
cv2.imshow('image3',img1)
# holding the image 
cv2.waitKey(0)
