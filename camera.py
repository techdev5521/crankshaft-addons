#!/usr/bin/python

'''

camera.py

Overlay the view of the Pi camera module on screen

'''

import RPi.GPIO as GPIO		# To interface with Pi GPIO
import time			# To sleep
import os			# To manage Pi camera process tracking
import datetime			# To format log dates
import signal

# Global GPIO settings
GPIO.setmode(GPIO.BOARD)	# Set GPIO numbers to board ref
GPIO.setwarnings(False)		# Suppress GPIO error messages

# Set pin numbers
camera = 40					# GPIO21

# Set pin channels
GPIO.setup(camera, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Setup logfile
#log = open("camera2.log", "w+")

# Function to write logfile message
#def write_log_message(message):
#		log.write("[" + datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S') + "] " + message + "\n")
#		print message

#write_log_message("Starting camera.py")
#write_log_message("Waiting for camera signal...")


try:

	camera_is_running = 0

	while True:

		time.sleep(0.1)

		if GPIO.input(camera) == 0 and camera_is_running == 0:
#			write_log_message("Camera signal received")
			os.system("crankshaft rearcam show")
			camera_is_running = 1
#			write_log_message("Camera started.")
#			write_log_message("Waiting for signal interupt...")

			while GPIO.input(camera) == 0:
				time.sleep(0.1)


		if GPIO.input(camera) == 1 and camera_is_running == 1:
#			write_log_message("Signotal interupted.")
#			write_log_message("Stopping Camera")
			os.system("crankshaft rearcam hide")
			camera_is_running = 0
#			write_log_message("Camera Stopped")
#			write_log_message("Waiting for camera signal...")

			while GPIO.input(camera) == 1:
				time.sleep(0.1)

except KeyboardInterrupt:
#	write_log_message("Received KeyboardInterupt")
#	write_log_message("CLeaning GPIO")
	GPIO.cleanup()
#	write_log_message("GPIO Cleaned")
#	write_log_message("Stopping" + "\n")

