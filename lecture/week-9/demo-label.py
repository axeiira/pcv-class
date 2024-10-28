import cv2 as cv
import numpy as np

cam = cv.VideoCapture(0)

def DrawCircle(image,k,b):
    center_coor = (b,k)
    radius = 20
    color = (255,0,0)
    thiqqnes = 2
    image = cv.circle(image,center_coor,radius,color,thiqqnes)
    return image

while True:
    ret, image = cam.read()
    if not ret:
        print("error in retrieving frame")
        break
    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    
    lower = np.array([60-20,40,40])
    upper = np.array([60+20,255,255])
    
    mask = cv.inRange(hsv,lower,upper)
    mask = cv.bitwise_not(mask)
    
    kernel = np.array ([[1,1,1],
                        [1,1,1],
                        [1,1,1]], dtype=np.uint8)
    
    m = mask.copy()
    mask = cv.erode(mask,kernel,iterations=4)
    mask = cv.dilate(mask,kernel,iterations=4)
    foreground = cv.bitwise_and(image,image,mask=mask)
    
    num_labels, labels_im = cv.connectedComponents(mask)
    
    for i in range(1,num_labels):
        b,k = np.where(labels_im == 1)
        bmin = b.min()
        xbmin = k[np.where(b == bmin)[0][0]]
        
        bmax = b.max()
        xbmax = k[np.where(b == bmax)[0][0]]
        
        kmin = k.min()
        ykmin = b[np.where(k == kmin)[0][0]]
        
        kmax = k.max()
        ykmax = b[np.where(k == kmax)[0][0]]

        print(i)
        print("Baris",bmin,bmax)
        print("Kolom",kmin,kmax)
        image = DrawCircle(image, bmin, xbmin)
        image = DrawCircle(image, bmax, xbmax)
        image = DrawCircle(image, ykmin, kmin)
        image = DrawCircle(image, ykmax, kmax)
        
        
    cv.imshow('Frame',image);
    cv.imshow('Mask',mask);
    
    if cv.waitKey(30) == ord('q'):
      break    
  
cam.release()
# cv.destroyAllWindows()