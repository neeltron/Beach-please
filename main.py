# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 10:02:00 2021

@author: Neel
"""

import RPi.GPIO as GPIO
from picamera import PiCamera
from time import sleep

camera = PiCamera()

GPIO.setmode(GPIO.BOARD)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(29, GPIO.OUT)

camera.start_preview()
sleep(5)
camera.capture('a.jpg')

while True:
    GPIO.output(13, 0)
    GPIO.output(15, 0)
    GPIO.output(5, 0)
    GPIO.output(29, 0)
