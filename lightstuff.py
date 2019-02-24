#!/usr/bin/python

'''

lightstuff.py

Overlay the view of the Pi camera module on screen

'''

import RPi.GPIO as GPIO		# To interface with Pi GPIO
import time			# To sleep
import os, subprocess			# To manage Pi camera process tracking
import datetime			# To format log dates
import signal

# Global GPIO settings
GPIO.setmode(GPIO.BOARD)	# Set GPIO numbers to board ref
GPIO.setwarnings(False)		# Suppress GPIO error messages

# Set pin numbers
button = 37					# GPIO26

# Set pin channels
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Setup logfile
#log = open("camera2.log", "w+")

# Function to write logfile message
#def write_log_message(message):
#		log.write("[" + datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S') + "] " + message + "\n")
#		print message

#write_log_message("Starting lightstuff.py")
#write_log_message("Waiting for button...")


try:

	running = 0

	while True:

		time.sleep(0.1)

		if GPIO.input(button) == 0 and running == 0:
#			write_log_message("Button pressed")
			camera_command = "/home/pi/LightStuff"
			camera_process=subprocess.Popen(camera_command, shell=True, preexec_fn=os.setsid)
			camera_is_running = 1
#			write_log_message("Script started.")
#			write_log_message("Waiting for button interupt...")

			while GPIO.input(button) == 0:
				time.sleep(0.1)


		if GPIO.input(button) == 1 and running == 1:
#			write_log_message("Button interupted.")
#			write_log_message("Stopping script.")
			os.killpg(camera_process.pid, signal.SIGTERM)
			camera_is_running = 0
#			write_log_message("SCript Stopped")
#			write_log_message("Waiting for button...")

			while GPIO.input(button) == 1:
				time.sleep(0.1)

except KeyboardInterrupt:
#	write_log_message("Received KeyboardInterupt")
#	write_log_message("CLeaning GPIO")
	GPIO.cleanup()
#	write_log_message("GPIO Cleaned")
#	write_log_message("Stopping" + "\n")


