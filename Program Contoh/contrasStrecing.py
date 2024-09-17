import cv2
import copy 
import numpy as np 
from matplotlib import pyplot as plt

##############################
#Fungsi Transformasi 
##############################
def T(r,r1,s1,r2,s2):
    s=0 
    if (0<r)&(r<r1):
        s = s1/r1*r 
    elif (r1<=r)&(r<r2): 
        s =(s2-s1) /(r2-r1)*(r-r1)+s1 
    elif (r2<=r)&(r<=255)&(r2<255): 
        s =(255-s2)/(255-r2)*(r-r2)+s2 
    else: 
        s = s2
    s= np.uint8(np.floor(s))
    return  s 
        
###############################
#Program Utama
###############################    
# Membaca File Citra
ImGray = cv2.imread("itsSurabaya2.jpg",cv2.IMREAD_GRAYSCALE)


b= ImGray.shape[0]
k= ImGray.shape[1]
im = np.zeros((b,k), np.uint8)
#Parameter kontras Streching
r1 = 100
s1 = 5
r2 = 200 
s2 = 230 
#Menerapkan fungsi Transformasi Contrast Streching 
for i in range(b):
    for j in range(k):
        r = ImGray[i,j]
        im[i,j]=T(r,r1,s1,r2,s2)
    #end for 
#end for 

cv2.imshow('Citra Contrast', im)
cv2.imshow('Citra Asli', ImGray)
#Menghitung   Histogram 
Histogram = cv2.calcHist([im],[0],None,[256],[0,256])
plt.bar(np.arange(0, 256, 1), Histogram[:, 0])
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
 