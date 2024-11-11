import cv2
import datetime
#either provide file name or device index of camera
#0 or -1 for device camera 1 and then succeeding values such as 2 or 3 for 2nd and 3rd cam
cap=cv2.VideoCapture(0)
#(3 means width 4 means height),value(when value exceeds 
# computer then max computer value is taken so if i put height 3000 then
#  computer will display of height 1280 only)
cap.set(3,1208)
cap.set(4,720)

start_time = cv2.getTickCount()
while(True):
    #ret is a variable with either true or false to show if a frame is captured or not
    #frame is the actual frame processed
    ret,frame = cap.read()
    #converting rgb to grayscale in realtime
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    print(frame)
    #to count number of frames captured
    framect=0
    if ret:
        framect+=1
    tt=str(datetime.datetime.now())
    font=cv2.FONT_HERSHEY_SCRIPT_COMPLEX
    v=cv2.putText(gray,tt,(95,98),font,2,(255,75,78),1,cv2.LINE_8)
    cv2.imshow('frame', gray)
    #if u press q then the window closes
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
print(framect)
cap.release()
cv2.destroyAllWindows()