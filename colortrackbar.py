import numpy as np
import cv2 
#x is the current position of trackbar value set
def nothing(x):
    print(x)

img=np.zeros((300,512,3),np.uint8)
#to create window with a name
cv2.namedWindow('image')
#name,imageused for trackbar,initial valueset,
# count/finalvalue,
# callbackfunc (for when the trackbar value changes)
cv2.createTrackbar('B','image',0,255,nothing)
cv2.createTrackbar('G','image',0,255,nothing)
cv2.createTrackbar('R','image',0,255,nothing)
cv2.createTrackbar('switch','image',0,1,nothing)
'''

we can also show positon of trackbar on image with font
pos=cv2.createtrackbar('cp','image',0,255,nothing)
and under while(1):
pos=cv2.gettrackbarpos('cp','image')
font=cv2.font_blah_blah
cv2.puttext(img,str(pos),(<index pos on imageto be placed),
font,6,(<color>,),<thickness>)





'''
while(1):
    cv2.imshow('image',img)
    k=cv2.waitKey(1)&0xFF
    #esc key then break out of loop
    if k==27:
        break
    #get position of trackbar     
    b=cv2.getTrackbarPos('B','image')
    g=cv2.getTrackbarPos('G','image')
    r=cv2.getTrackbarPos('R','image')
    s=cv2.getTrackbarPos('switch','image')
    #change color values in image based on pos of trackbar if switch is on
    #0 means on and 1 means off
    """
    we can also use swtich to make grayscale image
    so if 0 then color
    if 1 then cv2.cvtcolor('img',cv2.color_bgr2gray)
    
    
    """
    if s==1:
        img[:]=0
    else:
        img[:]=[b,g,r]

cv2.destroyAllWindows()

