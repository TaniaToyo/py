import cv2
import numpy as np
#wrap perspective is used to crop but get the image flat
img=cv2.imread('/Users/taniatoyo/Desktop/cards.png')
#define the points
pts1=np.float32([[322,102],[603,160],[519,560],[235,495]])
#default of card
width,height=250,350
#define which points corresponds which point
pts2=np.float32([[0,0],[width,0],[width,height],[0,height]])
#Get the matrix for the points
matrix=cv2.getPerspectiveTransform(pts1,pts2)
#wrap them
imgOutput=cv2.warpPerspective(img,matrix,(width,height))
cv2.imshow('Output',imgOutput)
cv2.waitKey(0)