import cv2
import numpy as np
img=cv2.imread('/Users/taniatoyo/Desktop/nuts.png')

imgHor=np.hstack((img, img))
imgVer=np.vstack((img,img))
cv2.imshow('horizontal', imgHor)
cv2.imshow('Vertical',imgVer)
cv2.waitKey(0)