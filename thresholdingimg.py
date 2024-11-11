import cv2 
import numpy as np

img=cv2.imread("cg.jpeg",0)
frame=cv2.imread("product.jpg")
frame=cv2.resize(frame,(512,512))
gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
'''threshold:segmentation technique used for speerating object from background'''
_,th1=cv2.threshold(img,50,255,cv2.THRESH_BINARY)
#value inv means black is white and white is black
_,th2=cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
'''
_,th3=cv2.threshold(img,127,255,cv2.THRESH_MASK)'''

#pixel less than threshold value is 0 so black
_,th4=cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
#thresh trunc is that after set value all values above it or below it can be made 
# to be the closest value of threshold
_,th5=cv2.threshold(img,200,255,cv2.THRESH_TRUNC)


a=cv2.Canny(gray,60,190)
'''We use mean thresholding when:

We want to sort toys quickly
The room light is the same everywhere
We don't mind if sometimes we make small mistakes


We use Gaussian thresholding when:

We want to be really careful about sorting
The room has different lights in different areas
We want to handle tricky toys that are partly light and partly dark



In the grown-up world of computers, mean thresholding is faster and simpler,
 but Gaussian thresholding is often better at handling tricky pictures, especially 
 when the lighting isn't even'''
#makes threshold per block size of 7 in this case with a constant 2 subtracted from
#only works on grayscale img


adt=cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,7,2)

adt1=cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,7,2)



'''adaptive thresholding:calculated for smaller regions 
so different regions can have different threshold 
for img with varied illumination at different regions'''
cv2.imshow('frame',frame)
cv2.imshow('image',img)
cv2.imshow('th1',th1)
cv2.imshow('th2',th2)
#cv2.imshow('th3',th3)
cv2.imshow('th4',th4)
cv2.imshow('th5',th5)
cv2.imshow('adt',adt)
cv2.imshow('adt1',adt1)
cv2.imshow('a2',a)
cv2.waitKey(0)
cv2.destroyAllWindows()