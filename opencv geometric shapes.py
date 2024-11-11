import cv2
import numpy as np
#0 means grayscale,1 means some color
img= cv2.imread(r'download.png')
#to makea resized image of the necessary height and width to display
resized_img = cv2.resize(img, (640, 480))
#[height,width,channels in the array],datatype
resized_img=np.zeros([512,512,3],np.uint8)

#cv2.line(<img variable name>,<startpointcoordinatesintupe>,
# <endpointcoordinateintuple>,<colorinBGR>,<thickness>)
resized_img=cv2.line(resized_img,(70,70),(450,480),(255,0,0),7)
#same parameters but gives an arrowed line
resized_img=cv2.arrowedLine(resized_img,(70,70),(450,480),(255,0,0),7)
#cv2.rectangle(<img variable name>,<startpointcoordinatesintuple(x1,y1)>,
#<endpoinrightdowncorner(xn,yn)>,<colorinBGR>,<thickness>,<linetype>)
resized_img=cv2.rectangle(resized_img,(70,70),(450,480),(255,0,0),7)
#cv2.rectangle(<img variable name>,<centre point(x1,y1)>,<radius>,<color>,<filling>)
resized_img=cv2.circle(resized_img,(70,70),57,(255,0,0),-1)
#text on img cv2.putText(<imgvariablename>,<text to put in quotes>,
# <startpoint>,<fontphase>,<fontsize>,<color>,<thickness>,<linetype>)
font=cv2.FONT_HERSHEY_SCRIPT_COMPLEX
resized_img=cv2.putText(resized_img,"helloworld",(95,98),font,2,(255,75,78),1,cv2.LINE_8)


cv2.imshow('image',resized_img)

cv2.waitKey()
cv2.destroyAllWindows()