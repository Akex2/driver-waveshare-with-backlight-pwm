import wiringpi2 as wiringpi
from time import sleep       # allows us a time delay
from stat import *
import os
import time
wiringpi.wiringPiSetupGpio()
wiringpi.pinMode(4, 1)      # sets GPIO 24 to output
wiringpi.digitalWrite(4, 1) # sets port 24 to 0 (0V, off)

wiringpi.pinMode(25, 0)      # sets GPIO 25 to input
try:
    while True:#wiringpi.digitalWrite(4, 1) # switch on LED. Sets port 24 to 1 (3V3, on)
		oinfo = os.stat('toto.txt')
		odate = (oinfo.st_mtime)+60
		limit = time.time()
		print("odate")
		print(odate)
		print("limit")
		print(limit)
		print("time")
		print(time.time())
		if odate < limit :
			wiringpi.digitalWrite(4, 1)
			print("inferieur")
		else:
			wiringpi.digitalWrite(4, 0)
			print("superieur")
		sleep(10)


finally:  # when you CTRL+C exit, we clean up
	wiringpi.digitalWrite(4, 0) # sets port 24 to 0 (0V, off)
	wiringpi.pinMode(4, 0)      # sets GPIO 24 back to input Mode# GPIO 25 is already an input, so no need to change anything
