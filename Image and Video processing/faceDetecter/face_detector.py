import cv2

face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
img=cv2.imread("news.jpg")
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces=face_cascade.detectMultiScale(gray_img,
scaleFactor=1.1,
minNeighbors=5)#scaleFactor=1.05 means that phyton will detect the face and then decrese the size of the image by 5% and search for bigger faces (beacuse the picture will be smaller)
print(type(faces))
print(faces)

for x,y,h,w in faces:
    img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
cv2.imshow("gray_img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
