import cv2 as cv
import numpy as np

cam = cv.VideoCapture(0)

while True:
    ret, image = cam.read()
    if not ret:
        print("error in retrieving frame")
        break
    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    
    lower = np.array([120-15,100,0])
    upper = np.array([120+15,255,255])
    
    mask = cv.inRange(hsv,lower,upper)
    mask = cv.bitwise_not(mask)
    
    kernel = np.array ([[1,1,1],
                        [1,1,1],
                        [1,1,1]], dtype=np.uint8)
    
    m = mask.copy()
    mask = cv.erode(mask,kernel,iterations=2)
    mask = cv.dilate(mask,kernel,iterations=2)
    foreground = cv.bitwise_and(image,image,mask=mask)
    
    cv.imshow('Frame',foreground);
    
    if cv.waitKey(30) == ord('q'):
      break    
  
cam.release()
# cv.destroyAllWindows()