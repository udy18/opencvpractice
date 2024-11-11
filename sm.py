import cv2
from matplotlib import pyplot as plt
import numpy as np

img=cv2.imread("obj.jpg")
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
img=cv2.resize(img,(512,512))

unnorm = cv2.boxFilter(img,ddepth=-1,ksize=(3,3),normalize=False)
norm = cv2.boxFilter(img,ddepth=-1,ksize=(3,3),normalize=True)
gaussian_image = cv2.GaussianBlur(img,ksize=(5,5),sigmaX=5,sigmaY=5)
sobel_horizontal_image = cv2.Sobel(img,ddepth=-1,ksize=3,dx=0,dy=1)
sobel_vertical_image = cv2.Sobel(img,ddepth=-1,ksize=3,dx=1,dy=0)

'''also look at schar kernel,laplacian kernel'''

titles=['image','unnorm','norm','gaus','sobelh','sobelv']
images=[img,unnorm,norm,gaussian_image,sobel_horizontal_image,sobel_vertical_image]


for i in range(6):
    #rows,col,index of img
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])


plt.show()