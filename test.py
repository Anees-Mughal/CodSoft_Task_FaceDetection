import cv2
import os
dectect = cv2.CascadeClassifier("C:/Users/Devil/AppData/Local/Programs/Python/Python311/Lib/site-packages/"
                                "cv2/data/haarcascade_frontalface_default.xml")
video = cv2.VideoCapture(0)
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("Trainerss.yml")
name_list = ["", "Devils P1", "Devils P2", "Devils P3"]
background = cv2.imread("background1.jpg")
while True:
    ret, frame = video.read()
    video_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face = dectect.detectMultiScale(video_gray,1.3, 5)
    for (x, y, w, h) in face:
        serial, conf = recognizer.predict(video_gray[y:y+h, x:x+w])
        if conf<90:
            cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,255), 1)
            cv2.rectangle(frame, (x,y), (x+w, y+h), (50,50,255), 2)
            cv2.rectangle(frame,(x,y-40), (x+w, y), (50,50,255), -1)
            cv2.putText(frame, name_list[serial], (x,y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 250, 255), 2)
        else:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 1)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (50, 50, 255), 2)
            cv2.rectangle(frame, (x, y - 40), (x + w, y), (50, 50, 255), -1)
            cv2.putText(frame, "Unknown", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 250, 255), 2)
    background[150:150 + 480, 55:55 + 640] = frame
    cv2.imshow("Test Data", background)
    k = cv2.waitKey(1)
    if k ==ord("q"):
        break
video.release()
cv2.destroyAllWindows()
print("Test successfullly .............")