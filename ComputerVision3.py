#!/usr/bin/python3

import numpy as np
import cv2

# now read both image
img1=cv2.imread('1.jpg')
img2=cv2.imread('2.jpg')

#reading the height and width of the images
h1, w1 =img1.shape[:2]
h2, w2 =img2.shape[:2]

# creating a blank image for difference
vis1 = np.zeros((h2,w2,3),np.uint8)

# creating a blank image for merging both images
vis2= np.zeros((max(h1,h2),w1+w2,3),np.uint8)

# findind the difference between both images
vis1[:h2,:w2,:]=img1[:,:,:]-img2[:,:,:]

#Merging both images
vis2[0:h1,:w1,:]=img1
vis2[0:h2,w1:w1+w2,:]=img2

#showing the difference of image 
cv2.imshow('imagediff',vis1)
cv2.imshow('imagemerge',vis2)
# holding the image
cv2.waitKey(0)
