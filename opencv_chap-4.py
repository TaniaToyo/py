import cv2
import numpy as np
img=np.zeros((512,512,3),np.uint8)# for color must give it 3 channels
#print(img.shape)
#img[:]=255,0,0# colors the whole image
#cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(44,25,10),3)#draw a line
#cv2.rectangle(img,(0,0),(250,350),(24,9,239),cv2.FILLED)
#cv2.circle(img,(250,350),40,(255,255,255),8)
cv2.putText(img,'OPENCV',(300,300),cv2.FONT_HERSHEY_SIMPLEX,1,(245,0,0),1)
cv2.imshow('image',img)
cv2.waitKey(0)