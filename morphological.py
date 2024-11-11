'''basically means simple 
operations based on shape of img usually done in bin img'''
import cv2
from matplotlib import pyplot as plt

img=cv2.imread(r"obj.jpg",cv2.IMREAD_GRAYSCALE)
_,mask=cv2.threshold(img,220,255,cv2.THRESH_BINARY_INV)
img=cv2.resize(img,(512,512))
mask=cv2.resize(mask,(512,512))




titles=['image','mask']
images=[img,mask]
for i in range(2):
    #rows,col,index of img
    plt.subplot(1,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])

plt.show()
