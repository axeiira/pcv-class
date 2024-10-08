import cv2 as cv
import numpy as np

cam = cv.VideoCapture(0)
kernel_lowpass = np.ones((11,11))/121
convert_to_gray = False


while True:
    ret, frame = cam.read()

    if not ret:
        print("error in retrieving frame")
        break

    frame = cv.resize(frame,(1920,1080))
    gFrame = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    
    if convert_to_gray:
        original = np.double(gFrame)/255
        
    if not convert_to_gray:
        original = np.double(frame)/255
    
    #Lowpass
    lowpass = cv.filter2D(original,-1, kernel_lowpass)

    #Highpass
    highpass = cv.absdiff(original,lowpass)
    
    #Band-Reject
    band_reject = lowpass + highpass
    
    #Band-Pass
    band_pass = cv.absdiff(original,band_reject)
    
    row1 = np.hstack((lowpass,highpass*5))
    row2 = np.hstack((band_reject,band_pass*5))
    combined_frame = np.vstack((row1,row2))
    cv.imshow("Lowpass & Highpass & Band Reject & Band Pass", combined_frame)

    key = cv.waitKey(100) & 0xFF
    if key == ord('q'):
       convert_to_gray = not convert_to_gray
    if key == 27: #ESC
            break

cam.release()
cv.destroyAllWindows()
