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
GPIO.setup(33, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(29, GPIO.OUT)

camera.start_preview()
sleep(5)
camera.capture('a.jpg')

while True:
    # stop
# =============================================================================
#     GPIO.output(33, 0)
#     GPIO.output(10, 0)
#     GPIO.output(5, 0)
#     GPIO.output(29, 0)
# =============================================================================

    # forward
# =============================================================================
#     GPIO.output(33, 1)
#     GPIO.output(10, 0)
#     GPIO.output(5, 1)
#     GPIO.output(29, 0)
# =============================================================================
    
    # backward
    
    GPIO.output(33, 0)
    GPIO.output(10, 1)
    GPIO.output(5, 0)
    GPIO.output(29, 1)
    
# =============================================================================
#     sleep(5)
#     GPIO.output(13, 0)
#     GPIO.output(15, 0)
#     GPIO.output(5, 0)
#     GPIO.output(29, 0)
# =============================================================================
