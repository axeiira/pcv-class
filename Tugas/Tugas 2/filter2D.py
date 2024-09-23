import cv2 as cv
import numpy as np

cam = cv.VideoCapture(0)
img = cv.imread("test.jpg")
img2 = cv.imread("a.jpg")
convert_to_gray = False

kernel_lowpass = np.ones((9,9))/81
kernel_edgeX = np.array(
   [
      [-1,0,1],
      [-2,0,2],
      [-1,0,1],
   ]
)
kernel_edgeY = np.array(
   [
      [-1,-2,-1],
      [0,0,0],
      [1,2,1]
   ]
)
kernel_sharpen = np.array(
   [
      [0,-1,0],
      [-1,5,-1],
      [0,-1,0],
   ]
)
kernel_highpass = np.array(
   [
      [0,-1,0],
      [-1,4,-1],
      [0,-1,0],
   ]
)

while True:
   ret, frame = cam.read()

   if not ret:
      print("error in retrieving frame")
      break

   frame = cv.resize(frame,(620,320))

   blur = cv.filter2D(frame,-1, kernel_lowpass)

   edge_x = cv.filter2D(frame,-1,kernel_edgeX)
   edge_y = cv.filter2D(frame,-1,kernel_edgeY)
   edge = edge_x + edge_y

   sharpen = cv.filter2D(frame,-1,kernel_sharpen)

   highpass = cv.filter2D(frame,-1,kernel_highpass)

   if convert_to_gray:
      blur = cv.cvtColor(blur,cv.COLOR_BGR2GRAY)
      edge = cv.cvtColor(edge,cv.COLOR_BGR2GRAY)
      sharpen = cv.cvtColor(sharpen,cv.COLOR_BGR2GRAY)
      highpass = cv.cvtColor(highpass,cv.COLOR_BGR2GRAY)

   row1 = np.hstack((blur,edge))
   row2 = np.hstack((sharpen,highpass))
   combined_frame = np.vstack((row1,row2))
   cv.imshow("Camera", combined_frame)

   key = cv.waitKey(100) & 0xFF
   if key == ord('q'):
       convert_to_gray = not convert_to_gray
   if key == 27: #ESC
        break

cam.release()
cv.destroyAllWindows()










