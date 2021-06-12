# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 10:02:00 2021

@author: Neel
"""

import RPi.GPIO as GPIO
from picamera import PiCamera
from time import sleep
import os
import io


os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/home/pi/Downloads/cognitio-7378d-f0c72d841d75.json"

def detect(img):
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()
    file_name = os.path.abspath(img)
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()
    
    image = vision.Image(content=content)
    response = client.label_detection(image=image)
    labels = response.label_annotations
    return labels


def forward():
    GPIO.output(33, 1)
    GPIO.output(10, 0)
    GPIO.output(5, 1)
    GPIO.output(29, 0)


def stop():
    GPIO.output(33, 0)
    GPIO.output(10, 0)
    GPIO.output(5, 0)
    GPIO.output(29, 0)
    
    
def left():
    GPIO.output(33, 0)
    GPIO.output(10, 1)
    GPIO.output(5, 1)
    GPIO.output(29, 0)
    

def right():
    GPIO.output(33, 1)
    GPIO.output(10, 0)
    GPIO.output(5, 0)
    GPIO.output(29, 1)
    

def back():
    GPIO.output(33, 0)
    GPIO.output(10, 1)
    GPIO.output(5, 0)
    GPIO.output(29, 1)
    

camera = PiCamera()
camera.rotation = 180

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(33, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(29, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)

p = GPIO.PWM(11, 50)
p.start(2.5)

camera.start_preview()
sleep(5)
camera.capture('a.jpg')


while True:
    p.ChangeDutyCycle(5)
    sleep(0.5)
    p.ChangeDutyCycle(12.5)
    sleep(0.5)
    p.ChangeDutyCycle(2.5)
    sleep(0.5)
    
    detect = detect("a.jpg")
    for i in detect:
        print(i.description)
        if i.description == "Plastic":
            p.ChangeDutyCycle(12.5)
            forward()
            sleep(0.5)
            stop()
        else:
            break
        
    left()
    sleep(0.5)
    stop()
    sleep(1)
    camera.capture("a.jpg")
    detect = detect("a.jpg")
    for i in detect:
        if i.description == "Plastic":
            p.ChangeDutyCycle(12.5)
            forward()
            sleep(0.5)
            stop()
        else:
            break
        
    left()
    sleep(0.5)
    stop()
    sleep(1)
    camera.capture("a.jpg")
    detect = detect("a.jpg")
    for i in detect:
        if i.description == "Plastic":
            p.ChangeDutyCycle(12.5)
            forward()
            sleep(0.5)
            stop()
        else:
            break
    
    left()
    sleep(0.5)
    stop()
    sleep(1)
    camera.capture("a.jpg")
    detect = detect("a.jpg")
    for i in detect:
        if i.description == "Plastic":
            p.ChangeDutyCycle(12.5)
            forward()
            sleep(0.5)
            stop()
        else:
            break
    