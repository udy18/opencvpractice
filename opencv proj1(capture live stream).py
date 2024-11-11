import cv2
#either provide file name or device index of camera
#0 or -1 for device camera 1 and then succeeding values such as 2 or 3 for 2nd and 3rd cam
cap=cv2.VideoCapture(0)
#using a codec fourcc for saving
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
#to saving the video(<savedname>,<fourcc code>,<fps we want>,<size of frame>)
out=cv2.VideoWriter('captured.wmv',fourcc,20.0,(640,480))

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

    cv2.imshow('frame', frame)
    # Calculate the elapsed time
    elapsed_time = (cv2.getTickCount() - start_time) / cv2.getTickFrequency()

        # Calculate the FPS
    fps = framect / elapsed_time

        # Print the FPS every second
    if elapsed_time >= 1:
        print(f"FPS: {fps:.2f}")
        start_time = cv2.getTickCount()
        framect = 0
    #if u press q then the window closes
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
print(framect)
cap.release()
cv2.destroyAllWindows()