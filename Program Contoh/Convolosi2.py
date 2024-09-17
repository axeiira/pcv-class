import cv2
from matplotlib import pyplot as plt
import numpy as np 
def Convolosi(f,w):
    baris = f.shape[0]
    kolom = f.shape[1]
    dkernel = w.shape[0]
    dkernel2= np.int32(np.floor(dkernel/2)) 

    g =np.zeros((baris,kolom))
    for y in range(baris):
        for x in range(kolom):
            g[y,x] = 0 
            for i in range(dkernel):
                yy =y+i-dkernel2
                if (yy<0)|(yy>=baris-1):
                    continue 
                for j in range(dkernel):
                    xx =x+j - dkernel2
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
cv2.imshow('Citra Asli', f)


dkernel = 3
w = np.ones((dkernel,dkernel))/(dkernel*dkernel)
g3 = Convolosi(f,w)
cv2.imshow('Hasil Convolosi w=3x3', g3)


dkernel = 5
w = np.ones((dkernel,dkernel))/(dkernel*dkernel)
g5 = Convolosi(f,w)
cv2.imshow('Hasil Convolosi w=5x5', g5)


dkernel = 7
w = np.ones((dkernel,dkernel))/(dkernel*dkernel)
g5 = Convolosi(f,w)
cv2.imshow('Hasil Convolosi w=7x7', g5)

cv2.waitKey(0)
cv2.destroyAllWindows()
 