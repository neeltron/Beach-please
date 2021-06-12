# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 10:02:00 2021

@author: Neel
"""

import RPi.GPIO as GPIO

GPIO.setmode( GPIO.BOARD)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(29, GPIO.OUT)

try:
    while True:
        GPIO.output(13, 0)
        GPIO.output(15, 1)
        GPIO.output(5, 0)
        GPIO.output(29, 1)

except KeyboardInterrupt:
    GPIO.cleanup()
