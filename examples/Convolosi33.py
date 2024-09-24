import cv2
from matplotlib import pyplot as plt
import numpy as np 

def Convolusi(f,w):
    baris = f.shape[0]
    kolom = f.shape[1]
    g = np.zeros((baris,kolom))
    for y in range(baris):
        for x in range(kolom):
            g[y,x] = 0 
            for i in range(3):
                yy =y+i-1
                if (yy<0)|(yy>=baris-1):
                    continue 
                for j in range(3):
                    xx =x+j - 1
                    if (xx<0)|(xx>=kolom-1): 
                        continue 
                    g[y,x]=g[y,x]+f[yy,xx]*w[i,j]
                #end for
            #end for 
        #end for
    #end for
    g= np.uint8(np.floor(g))
    return g
# Membaca File Citra
f   = cv2.imread("a.jpg",cv2.IMREAD_GRAYSCALE)
w   = np.ones((3,3))/9

#   |1/9 1/9 1/9 | 
#w =|1/9 1/9 1/9 |
#   |1/9 1/9 1/9 | 
    
g = Convolusi(f,w)
cv2.imshow('Citra Asli', f)

cv2.imshow('Hasil Convolosi', g)
cv2.waitKey(0)
cv2.destroyAllWindows()
 