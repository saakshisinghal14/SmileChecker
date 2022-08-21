import random,cv2 as cv,time


face_cascade=cv.CascadeClassifier('haarcascade_frontalface_default.xml')
smile_cascade=cv.CascadeClassifier('smile.xml')

video=cv.VideoCapture(0);

num=0

#smile meter funtion
def smile_meter(frame,x1,y1,x2):
    global num
    if num==100:
    #opencv display text as a string
     
     
     font=cv.FONT_HERSHEY_SIMPLEX
     color=(255,0,255)
     text=cv.putText(frame,"your smile is",(int(x1)+15,int(y1)+70),font,1,color,2,cv.LINE_AA)
     text=cv.putText(frame,str((x2)%100)+" %",(int(x1)+50,int(y1)+20),font,1,color,4,cv.LINE_AA)
     time.sleep(7)
     num=0
     return num
    else:
        
        font=cv.FONT_HERSHEY_SIMPLEX
        color=(255,0,255)
        text=cv.putText(frame,"Smile Meter",(int(x1)+15,int(y1)+50),font,1,color,2,cv.LINE_AA)
        text=cv.putText(frame,str((x2)%100)+" %",(int(x1)+50,int(y1)+20),font,1,color,4,cv.LINE_AA)
        num=num+5
        return num







while True:
    check,frame=video.read();
    gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)

#face
    face=face_cascade.detectMultiScale(gray,scaleFactor=1.5, minNeighbors=5)
    for x,y,w,h in face:
        img=cv.rectangle(frame,(x,y),(x+(w+20),y+(h+30)),(0,0,255),thickness=2)
        #smile
        smile=smile_cascade.detectMultiScale(gray,scaleFactor=1.8, minNeighbors=20)
        for x1,y1,w1,h1 in smile:
          img=cv.rectangle(frame,(x1,y1),((x1+w1),(y1+h1)),(255,0,0),thickness=3)
          smile_meter(frame,x,y,x1)
    cv.imshow("smile meter",frame)
    key=cv.waitKey(1)

    if key==ord('q'):
        break

video.release()
cv.destroyAllWindows







