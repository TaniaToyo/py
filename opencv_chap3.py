import cv2
import numpy as np
img = cv2.imread('/Users/taniatoyo/Desktop/Tanu❤️/MY_CODE/py/img1.png')
print(img.shape)# to resize you should know the dimensions first
imgResize=cv2.resize(img, (500,500)) #(image, width,height)
imgCropped=img[0:200, 200:500]#height,width
cv2.imshow('Cropped',imgCropped)
print(imgResize.shape)
cv2.waitKey(0)

