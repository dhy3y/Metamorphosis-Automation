import cv2

cascade_src='haarcascade_car.xml'
video_src='Traffic - 20581.mp4'
cap = cv2.VideoCapture(video_src)
car_cascade=cv2.CascadeClassifier(cascade_src)

while True:
    ret,frames=cap.read()
    if(type(frames) == type(None)):
        break
    gray=cv2.cvtColor(frames,cv2.COLOR_BGR2GRAY)
    cars = car_cascade.detectMultiScale(gray,1.1,1)
    for(x,y,w,h) in cars:
        plate = frames[y:y+h,x:x+w]
        cv2.rectangle(frames,(x,y),(x+w,y+h),(51,51,255),2)
        cv2.rectangle(frames, (x, y-40),(x + w,y),(51, 51, 255),-2)
        cv2.putText(frames,'Car',(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,0.2,1)
        cv2.imshow('Car',plate)
    frames = cv2.resize(frames,(600,400))
    #cv2.imshow('video',img)
    cv2.imshow('Car Detection',frames)
    if cv2.waitKey(33)==27:
        break
cv2.destroyAllWindows()