import cv2
import numpy as np

camera = cv2.VideoCapture("VID_20211207_082919.mp4")
camera.open("VID_20211207_082919.mp4")
car_cascade = cv2.CascadeClassifier('cars.xml')

while True:
    (grabbed, frame) = camera.read()
    print(frame)
    grayvideo =  cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)
    # grayvideo = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    cars = car_cascade.detectMultiScale(grayvideo, 5, 1)


    for (x, y, w, h) in cars:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)
        cv2.imshow("video", frame)

    if cv2.waitKey(1) == ord('q'):
        break
camera.release()
cv2.destroyAllWindows()

