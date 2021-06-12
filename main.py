# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 10:02:00 2021

@author: Neel
"""

import RPi.GPIO as GPIO

GPIO.setmode( GPIO.BOARD)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)

try:
	while True:
		GPIO.output(13, 0)
		GPIO.output(15, 1)
        GPIO.output(17, 0)
		GPIO.output(27, 1)

except KeyboardInterrupt:
	GPIO.cleanup()
