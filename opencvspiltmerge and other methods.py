import numpy as np
import cv2
img=cv2.imread('download.png')

print(img.shape)#tuple of totalrows,columns, and channels
print(img.size)#returns total pixels accessed
print(img.dtype)#imag datatype obtained
b,g,r=cv2.split(img)
print(b,g,r)
img=cv2.merge((b,g,r))
img=cv2.resize(img,(512,512))
#to take region of interest or some thing from the pic and 
# copy it in another location within the same pic
ball=img[280:340,330:390]
img[273:333,100:160]=ball


#to put one pic on another 
'''new pic'''
img1=cv2.imread('download.jpeg')
img1=cv2.resize(img1,(512,512))
dst=cv2.add(img,img1)
dst=cv2.addWeighted(img,.9,img1,.1,0)

cv2.imshow('image',dst)
cv2.waitKey()
cv2.destroyAllWindows()