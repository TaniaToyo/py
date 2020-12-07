import cv2
img = cv2.imread('/Users/taniatoyo/Desktop/Tanu❤️/MY_CODE/py/img1.png')
cv2.imshow('trial', img)
cv2.waitKey(0)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray', imgGray)
cv2.waitKey(0)

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 500)
cap.set(10, 100)
while True:
    success,img=cap.read()
    cv2.imshow('Webcam', img)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break



