import cv2
a = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")#load the xml file
vdo = cv2.VideoCapture(0)

while True:
    rect,img=vdo.read()
    cnvrt=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#converting the color of image from video to gray scale image
    c=a.detectMultiScale(cnvrt,1.3,6)

    for (x1,y1,w1,h1) in c:
        cv2.rectangle(img,(x1,y1),(x1+w1,y1+h1),(255,0,0),3)

    cv2.imshow("img",img)
    if cv2.waitKey(10) & 0xFF==ord("d"):
        break
vdo.release()
cv2.destroyAllWindows()