import cv2,time

video=cv2.VideoCapture(0,cv2.CAP_DSHOW)#0 is defalut camera on pc if i want something else i can choose 1-3 also , also i can instand adding a int enter a path of a Video
a=1
while True:
    a=a+1
    check,frame = video.read()
    print(check)
    print(frame)

    grey=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("Capturing",grey)

    key=cv2.waitKey(1)
    if key==ord('q'):
        break
print(a)
video.release()
cv2.destroyAllWindows()
