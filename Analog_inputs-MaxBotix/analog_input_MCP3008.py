#!/usr/bin/env python
import time
import os
import RPi.GPIO as GPIO

# GPIO
GPIO.setmode(GPIO.BCM)
DEBUG = 1


# read SPI data from MCP3008 chip, 8 possible adc's (0 thru 7)
def readadc(adcnum, clockpin, mosipin, misopin, cspin):
        if ((adcnum > 7) or (adcnum < 0)):
                return -1
        GPIO.output(cspin, True)

        GPIO.output(clockpin, False) # start clock low
        GPIO.output(cspin, False) # bring CS low

        commandout = adcnum
        commandout |= 0x18 # start bit + single-ended bit
        commandout <<= 3 # we only need to send 5 bits here
        for i in range(5):
                if (commandout & 0x80):
                        GPIO.output(mosipin, True)
                else:
                        GPIO.output(mosipin, False)
                commandout <<= 1
                GPIO.output(clockpin, True)
                GPIO.output(clockpin, False)

        adcout = 0
        # read in one empty bit, one null bit and 10 ADC bits
        for i in range(12):
                GPIO.output(clockpin, True)
                GPIO.output(clockpin, False)
                adcout <<= 1
                if (GPIO.input(misopin)):
                        adcout |= 0x1

        GPIO.output(cspin, True)
        
        adcout >>= 1 # first bit is 'null' so drop it
        return adcout

# change these as desired - they're the pins connected from the
# SPI port on the ADC to the Cobbler
SPICLK = 18
SPIMISO = 23
SPIMOSI = 24
SPICS = 25
SENSOR_SYNC = 17

# set up the SPI interface pins
GPIO.setup(SPIMOSI, GPIO.OUT)
GPIO.setup(SPIMISO, GPIO.IN)
GPIO.setup(SPICLK, GPIO.OUT)
GPIO.setup(SPICS, GPIO.OUT)
GPIO.setup(SENSOR_SYNC, GPIO.OUT)

# 10k trim pot connected to adc #0
ultrasonic_adc_0 = 0;

last_read_0 = 0 # this keeps track of the last sensor value
tolerance = 0 # to keep from being jittery we'll only change
              # volume when the pot has moved more than 5 'counts'
avgrange = 200 # Quantity of values to avarage

try:
	while True:
		
		GPIO.output(SENSOR_SYNC, False) # Synchronisation des ultrasonics 
		GPIO.output(SENSOR_SYNC, True)
		time.sleep(0.00002)
		
		time.sleep(0.090) # ultrasonic needs time to adjust voltage
		distance_0 = readadc(ultrasonic_adc_0, SPICLK, SPIMOSI, SPIMISO, SPICS)
		distance_1 = readadc(ultrasonic_adc_1, SPICLK, SPIMOSI, SPIMISO, SPICS)
		print "distance 0:", distance_0 	# le MB1200 renvoie une distance en cm 
#	        print "distance 1:", distance_1
#		print "sensor value:", sensor_avg
	
   		# OSC -> Pd
#		try:
#			msg.setAddress("/distance1")
#			msg.append(sensor_avg)
#			localClient.send(msg)
#			artministrator.send(msg)
#			msg.clearData()
#		except:
#			print 'connection refused'
#			pass		

		# hang out and do nothing
	        time.sleep(0.01)
	
except KeyboardInterrupt:
	GPIO.cleanup()
