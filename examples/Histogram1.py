import cv2
import numpy as np 
from matplotlib import pyplot as plt

def MenghitungHistogram(ImGray):
    Histogram = np.zeros((256,1), np.int32)
    for i in range(0, ImGray.shape[0]):
        for j in range(0, ImGray.shape[1]):
            r = ImGray[i,j]
            Histogram[r]=Histogram[r]+1
    return Histogram

# Membaca File  citra sebagai citra gray 
ImGray = cv2.imread("itsSurabaya2.jpg",cv2.IMREAD_GRAYSCALE)
cv2.imshow('Citra Gray', ImGray)

Histogram=MenghitungHistogram(ImGray)
plt.bar(np.arange(0, 256, 1), Histogram[:, 0])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
 