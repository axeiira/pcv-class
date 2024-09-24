import cv2 as cv
import numpy as np

def Convolution(frame,kernel):
    column = frame.shape[0]
    rows = frame.shape[1]
    new_frame = np.zeros((column,rows))
    kernel_size = kernel.shape[0]
    kernel_center = kernel_size//2
    for y in range(column):
        for x in range(rows):
            new_frame[y,x] = 0
            for i in range(kernel_size):
                yn = y + i - kernel_center
                if yn < 0 or yn >= column-1:
                    continue
                for j in range(kernel_size):
                    xn = x + j - kernel_center
                    if xn < 0 or xn >= rows-1:
                        continue
                    new_frame[y,x] = new_frame[y,x] + frame[yn,xn] * kernel[i,j]
    new_frame = np.uint8(np.floor(new_frame))
    return new_frame

cam = cv.VideoCapture(0)

blur_kernel = np.ones((9,9))/81

kernel_edge = np.array(
   [
      [-1,0,1],
      [-1,0,1],
      [-1,0,1]
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

    frame = cv.resize(frame,(200,200))
    gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)

    blur = Convolution(gray,blur_kernel)
    edge = Convolution(gray,kernel_edge)
    sharpen = Convolution(gray,kernel_sharpen)
    highpass = Convolution(gray,kernel_highpass)

    row1 = np.hstack((blur,edge))
    row2 = np.hstack((sharpen,highpass))
    combined_frame = np.vstack((row1,row2))

    cv.imshow("Camera", combined_frame)
    if cv.waitKey(100) == ord('q'):
        break

cam.release()
cv.destroyAllWindows()