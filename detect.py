#!/bin/env python

import cv2, time

cap = cv2.VideoCapture(0)
time.sleep(1)
cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")

def detect(image):
    #faces = cascade.detectMultiScale(img, 1.1, 2, cv2.cv.CV_HAAR_SCALE_IMAGE, (20,20), (200,200))
    faces = cascade.detectMultiScale(image)
    for _face in faces:
        cv2.rectangle(image, (_face[0], _face[1]), (_face[0]+_face[2], _face[1]+_face[3]), (255,255,255))

def repeat():
    ret, image = cap.read()
    detect(image)
    cv2.imshow("w1", image)
    cv2.waitKey(1)

while True:
    repeat()
