import cv2
import numpy as np
def empty(a):
    pass

cv2.namedWindow('Trackbars')
cv2.resizeWindow('Trackbars',640,240)
cv2.createTrackbar('Hue Minimum','Trackbars',0,179,empty )#empty is called everytime you change the trackback
cv2.createTrackbar('Hue Max','Trackbars',179,179,empty )#empty is called everytime you change the trackback
cv2.createTrackbar('Saturation Minimum','Trackbars',0,255,empty )#empty is called everytime you change the trackback
cv2.createTrackbar('Saturation Max','Trackbars',255,255,empty )#empty is called everytime you change the trackback
cv2.createTrackbar('Value Minimum','Trackbars',0,255,empty )#empty is called everytime you change the trackback
cv2.createTrackbar('Value Max','Trackbars',255,255,empty )#empty is called everytime you change the trackback


while True:
    img= cv2.imread('/Users/taniatoyo/Desktop/nuts.png')
    imgHSV=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    h_min=cv2.getTrackbarPos('Hue Minimum','Trackbars')
    h_max=cv2.getTrackbarPos('Hue Max','Trackbars')
    s_min=cv2.getTrackbarPos('Saturation Minimum','Trackbars')
    s_max=cv2.getTrackbarPos('Saturation Max','Trackbars')
    v_min=cv2.getTrackbarPos('Value Minimum','Trackbars')
    v_max=cv2.getTrackbarPos('Value Max','Trackbars')
    lower = np.array([h_min,s_min,v_min])
    upper=np.array([h_max,s_max,v_max])
    mask= cv2.inRange(imgHSV,lower,upper)

    cv2.imshow('NewImage',imgHSV)

    cv2.imshow('Mask',mask)
#TODO work more 1:12 mins

    cv2.waitKey(1)