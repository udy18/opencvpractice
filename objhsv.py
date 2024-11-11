import cv2
import numpy as np
'''hsv is used to seperate image 
 luminencse from color info
hue(base pigment) 0-360,
saturation(depth of pigment) 0-100%
value(brightness)0-100%'''
def nothing(x):
    pass
cap=cv2.VideoCapture(0)
cv2.namedWindow('tracking')


cv2.createTrackbar('lh','tracking',0,255,nothing)
cv2.createTrackbar('ls','tracking',0,255,nothing)
cv2.createTrackbar('lv','tracking',0,255,nothing)
cv2.createTrackbar('uh','tracking',255,255,nothing)
cv2.createTrackbar('us','tracking',255,255,nothing)
cv2.createTrackbar('uv','tracking',255,255,nothing)
while True:

    #frame=cv2.imread(r"obj.jpg")
    #frame=cv2.resize(frame,(512,512))
    _,frame=cap.read()



    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
 #lower and upper limit of
 #  blue colorspace(to threshold hsv for range of blue)
    l_h=cv2.getTrackbarPos('lh','tracking')
    l_s=cv2.getTrackbarPos('ls','tracking')
    l_v=cv2.getTrackbarPos('lv','tracking')
    u_h=cv2.getTrackbarPos('uh','tracking')
    u_s=cv2.getTrackbarPos('us','tracking')
    u_v=cv2.getTrackbarPos('uv','tracking')
    l_b=np.array([l_h,l_s,l_v])
    u_b=np.array([u_h,u_s,u_v])

#The cv2.inRange() function returns 
# a white binary image where the colors are detected and 0 otherwise
    mask=cv2.inRange(hsv,l_b,u_b)
    '''We perform bitwise and of the input image and 
    mask the output with the image present in the mask
      variable to highlight the area where the color is 
      detected in the input image.
      This can be achieved using the cv2.bitwise_and() function'''
    res=cv2.bitwise_and(frame,frame,mask=mask)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)


    key=cv2.waitKey(1)
    if key==27:
        break
cap.release()
cv2.destroyAllWindows()