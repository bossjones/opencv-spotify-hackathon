#!/bin/env python

import cv2, time
import pygame
pygame.mixer.init()
pygame.mixer.music.load("audio/scream.wav")


## # play scream sound once
## pygame.mixer.music.play(0)

# start video capture from webcam
cap = cv2.VideoCapture(0)
time.sleep(1)
face_cascade   = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")

# return image as is, without alpha channel
scary_girl_img = cv2.imread('scary-girl.jpg', -1)

def detect(image):
    #faces = face_cascade.detectMultiScale(img, 1.1, 2, cv2.cv.CV_HAAR_SCALE_IMAGE, (20,20), (200,200))
    faces = face_cascade.detectMultiScale(image)

    for _face in faces:
        cv2.rectangle(image, (_face[0], _face[1]), (_face[0]+_face[2], _face[1]+_face[3]), (255,255,255))

def repeat():
    ret, image = cap.read()
    detect(image)
    cv2.imshow("w1", image)
    cv2.waitKey(1)

while True:
    repeat()
