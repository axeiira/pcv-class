import cv2 as cv
import numpy as np

def Transform(r, r1, s1, r2, s2):
   s = 0
   if (0 < r) and (r < r1):
      s = s1 / r1 * r
   elif (r1 <= r) and (r < r2):
      s = (s2 - s1) / (r2 - r1) * (r - r1) + s1
   elif(r2 <= r) and (r <= 255) and (r2 < 255):
      s = (255 - s2) / (255 - r2) * (r - r2) + s2
   else:
      s = s2
   s = np.uint8(np.floor(s))
   return s

r1,s1,r2,s2 = 80,20,175,240

cam = cv.VideoCapture(0)

while True:
   # Capture frame-by-frame
   ret, frame = cam.read()

   # if frame is read correctly ret is True
   if not ret:
      print("error in retrieving frame")
      break

   frameGray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
   frameGray = cv.resize(frameGray, (500,250))
   b = frameGray.shape[0]
   k = frameGray.shape[1]
   cs = np.zeros((b,k),np.uint8)

   for i in range(b):
       for j in range(k):
           r = frameGray[i,j]
           cs[i,j] = Transform(r, r1, s1, r2, s2)

   cv.imshow('original', frameGray)
   cv.imshow('contrast streched', cs)
   if cv.waitKey(0) == ord('q'):
      break
   
cam.release()
cv.destroyAllWindows()