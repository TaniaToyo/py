
import cv2
import numpy as np

img=cv2.imread('img1.png')


#convert to grey
imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#cvtColor=Changes color
#BGR to Gray

cv2.imshow('Canny', imgDialation)
cv2.waitKey(0)

imgBlur=cv2.GaussianBlur(imgGray,(7,7),0)
#dimension of blur
#odd numbers

imgCanny=cv2.Canny(img,100,100)
kernel=np.ones((5, 5))
imgDialation=cv2.dilate(imgCanny,kernel,iterations=1)
#negative image 100 is intensity of the edge
#dialation is used to increase the edge detection
#kernal is a ones matrix used to define the size. So we use numpy
#iteration=1 is used for the thickness

print('hello')