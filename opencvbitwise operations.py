import cv2
import numpy as np


img1=np.zeros((250,500,3),np.uint8)
#creates rectangle with dimensions (200,0),(300,100) in the image
img1=cv2.rectangle(img1,(200,0),(300,100),(255,255,255),-1)
img2=np.ones((250,500,3),np.uint8)*255#made it white
#creates rectangle with dimensions (200,0),(300,100) in the image
cv2.imshow("img1",img1)
cv2.imshow("img2",img2)
#new image after bitwise command "and" just like logical and
bitAnd = cv2.bitwise_and(img1,img2)
cv2.imshow("bitand",bitAnd)
#mking image after bitor
bitor=cv2.bitwise_or(img1,img2)
cv2.imshow("bitor",bitor)
#making image after bit not
bitnot=cv2.bitwise_not(img1,img2)
cv2.imshow("bitnot",bitnot)



cv2.waitKey(0)
cv2.destroyAllWindows()