import cv2 as cv
import numpy as np

cam = cv.VideoCapture(0)

while True:
    ret, image = cam.read()
    if not ret:
        print("error in retrieving frame")
        break
    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    lower = np.array([60-15,50,0])
    upper = np.array([60+15, 255, 255])
    mask = cv.inRange(hsv,lower,upper)
    foreground = cv.bitwise_and(image,image,mask=mask)
    
    cv.imshow('image',image)
    cv.imshow('foreground', foreground)
    cv.imshow('mask', mask)
    
    if cv.waitKey(30) == ord('q'):
      break
  
cam.release()
cv.destroyAllWindows()
