import cv2 as cv
cam = cv.VideoCapture(0)
if not cam.isOpened():
   print("error opening camera")
   exit()
while True:
   # Capture frame-by-frame
   ret, frame = cam.read()
   # if frame is read correctly ret is True
   if not ret:
      print("error in retrieving frame")
      break
   cv.imshow('Test Window', frame)
   if cv.waitKey(1) == ord('q'):
      break
cam.release()
cv.destroyAllWindows()