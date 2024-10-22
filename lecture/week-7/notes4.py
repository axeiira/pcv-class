import cv2 as cv
import numpy as np

cam = cv.VideoCapture(0)

def segment_color(image, lower_bound, upper_bound):
    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    mask = cv.inRange(hsv, lower_bound, upper_bound)
    foreground = cv.bitwise_and(image, image, mask=mask)
    return foreground

while True:
    ret, image = cam.read()
    if not ret:
        print("error in retrieving frame")
        break
    
    yellow = segment_color(image,np.array([30-15,100,100]),np.array([30+15,255,255]))
    
    lower_red = segment_color(image,np.array([0-15,100,100]),np.array([0+15,255,255]))
    upper_red = segment_color(image,np.array([(345/2)-15,100,100]),np.array([(345/2)+15,255,255]))
    red = lower_red + upper_red
    
    
    
    if cv.waitKey(30) == ord('q'):
      break
  
cam.release()
cv.destroyAllWindows()
