import numpy as np
import cv2
#dir is inbuilt to show classes and functions inside cv2 
events = [i for i in dir(cv2) if 'EVENT' in i ]
print(events)

#mousecallbackfunction when mouse events take place
def click_event(event,x,y,flags,param):
    '''if event == cv2.EVENT_LBUTTONDOWN:
        print(x,",",y)
        font=cv2.FONT_HERSHEY_COMPLEX
        strxy=str(x) + ","+str(y)
        cv2.putText(img,strxy,(x,y),font,1,(255,255,0),2)
        cv2.imshow('image',img)'''
    #to make event which show rgb channels instead of coordinates when clicked
    #note:for black channels are always 0
    '''if event==cv2.EVENT_RBUTTONDOWN:
        blue=img[x,y,0]
        green=img[x,y,1]
        red=img[x,y,2]
        font=cv2.FONT_HERSHEY_COMPLEX
        strBGR=str(blue) + ","+str(green)+ ","+str(red)
        cv2.putText(img,strBGR,(x,y),font,0.5,(0,255,255),2)
        cv2.imshow('image',img)'''
    #drawing points and then connecting points using a line
    if event == cv2.EVENT_LBUTTONUP:
        #to make a point or circle in a point when clicked
        cv2.circle(img,(x,y),3,(0,0,255),-1)
        #to join points
        points.append((x,y))
        if len(points)>=2:
            #img,point 1,point 2 coordinate,color,thickness
            cv2.line(img,points[-1],points[-2],(255,0,0),5)
    #to make a new window which will show the color clicked on
    if event== cv2.EVENT_LBUTTONDOWN:
        blue= img[x,y,0]
        green=img[x,y,1]
        red=img[x,y,2]
        cv2.circle(img,(x,y),3,(0,0,255),-1)
        mycolorimg = np.zeros((512,512,3),np.uint8)

        mycolorimg[:]=[blue,green,red]
        cv2.imshow('col',mycolorimg)



#img=np.zeros([512,512,3],np.uint8)
img=cv2.imread(r'download.png')
cv2.imshow("image",img)
points=[]
cv2.setMouseCallback("image",click_event)

cv2.waitKey()
cv2.destroyAllWindows()