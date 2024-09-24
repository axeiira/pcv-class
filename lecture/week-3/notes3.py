import cv2 as cv
import numpy as np
pic = "asset/Tower2-2.jpg"
ImGray = cv.imread(pic,cv.IMREAD_GRAYSCALE)
ImGray = np.float32(ImGray)/255

roberts_x = np.array(
    [
        [0,1],
        [-1,0]
    ]
)

roberts_y = np.array(
    [
        [1,0],
        [0,-1]
    ]
)

grad_x = cv.filter2D(ImGray,-1,roberts_x)
grad_y = cv.filter2D(ImGray,-1,roberts_y)
grad_xy = grad_x + grad_y

cv.imshow("Grayscale",ImGray)
cv.imshow("Gradient X", grad_x)
cv.imshow("Gradient Y", grad_y)
cv.imshow("Gradient XY", grad_xy)
cv.waitKey(0)
cv.destroyAllWindows()