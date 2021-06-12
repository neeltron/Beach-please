# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 10:02:00 2021

@author: Neel
"""

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(03, GPIO.OUT)
GPIO.setup(05, GPIO.OUT)
GPIO.setup(07, GPIO.OUT)

pwm=GPIO.PWM(07, 100)
pwm.start(0)

GPIO.output(03, True)
GPIO.output(05, False)

pwm.ChangeDutyCycle(50)

GPIO.output(07, True)
sleep(2)
GPIO.output(07, False)
GPIO.output(03, False)
GPIO.output(05, True)

pwm.ChangeDutyCycle(75)
GPIO.output(07, True)
sleep(3)
GPIO.output(07, False)
pwm.stop()
GPIO.cleanup()
