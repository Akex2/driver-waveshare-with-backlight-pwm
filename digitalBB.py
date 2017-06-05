#!/usr/bin/env python2.7
# script by Alex Schointss

#import wiringpi2 as wiringpi
import Adafruit_BBIO.GPIO as GPIO
from time import sleep       # allows us a time delay
from stat import *
import os
import time
#wiringpi.wiringPiSetupGpio()
#wiringpi.pinMode(18, 2)      # sets GPIO 24 to output
#wiringpi.pwmWrite(18, 0) # sets port 24 to 0 (0V, off)
GPIO.setup("P9_17", GPIO.OUT)
GPIO.output("P9_17", GPIO.LOW)
#wiringpi.pinMode(25, 0)      # sets GPIO 25 to input
i = 0
#oinfo = os.stat('toto.txt')
#odate = (oinfo.st_mtime)+30
#limit = time.time()
ofile = open('toto.txt','w')
ofile.close()
try:
    while True:#wiringpi.digitalWrite(4, 1) # switch on LED. Sets port 24 to 1 (3V3, on)
		oinfo = os.stat('toto.txt')
		odate = (oinfo.st_mtime)+300
		limit = time.time()
		#print("odate")
		#print(odate)
		#print("limit")
		#print(limit)
		#print("time")
		#print(time.time())
		#print("i")
		#print(i)
		if odate > limit :
			#print("sup")
			GPIO.output("P9_17", GPIO.LOW)
		else:
			#print("inf")
			GPIO.output("P9_17", GPIO.HIGH)
		sleep(0.5)


finally:  # when you CTRL+C exit, we clean up
	GPIO.output("P9_15", GPIO.HIGH)
	#wiringpi.digitalWrite(4, 0) # sets port 24 to 0 (0V, off)
	#wiringpi.pinMode(4, 0)      # sets GPIO 24 back to input Mode# GPIO 25 is already an input, so no need to change anything
