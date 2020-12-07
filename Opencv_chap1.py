import cv2
img = cv2.imread('/Users/taniatoyo/Desktop/Tanu❤️/MY_CODE/py/img1.png')
cv2.imshow('trial', img)
cv2.waitKey(0)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray', imgGray)
cv2.waitKey(0)
