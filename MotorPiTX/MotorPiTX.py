#
# motorpitx v0.1 Python module for the MotorPiTX addon board for the Raspberry Pi
# Copyright (c) 2013 Jason Barnett <jase@boeeerb.co.uk>
#
# This module will allow you to control all the interfaces of the MotorPiTX
# addon board easily. This has been tested with a Raspberry Pi Model A with
# MotorPiTX v0.2 beta board. There is no reason why it shouldn't work with 
# other configurations, if it doesn't, email me with as much information and
# let me know!
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.
#
# Servod is a ServoBlaster daemon by Richard Hirst <richardghirst@gmail.com>
# https://github.com/richardghirst/PiBits/tree/master/ServoBlaster
#
# Revisions
#
# 0.1 - Initial release (Functions are; blink, motor1, motor2, out1, out2, in1, in2, servo1, servo2, cleanup)
#
#
#


from time import sleep
import RPi.GPIO as GPIO
import os
from random import randint

class MotorPiTX:
        def __init__(self):
		self.DEBUG = True

		if self.DEBUG:
			print "Setting up pins"

		# Define pins
		self.READY = 7
		self.MOTA1 = 9
		self.MOTA2 = 10
		self.MOTAE = 11
		self.MOTB1 = 24
		self.MOTB2 = 23
		self.MOTBE = 25
		self.OUT1 = 22
		self.OUT2 = 17

		# Take care of rev 1 vs rev 2 Pis
		if GPIO.RPI_REVISION == 1:
			self.IN1 = 21
		else:
			self.IN1 = 27
		self.IN2 = 4
		self.SERVO1 = 18
		self.SERVO2 = 15

		# Set up GPIO ins and outs
		GPIO.setmode(GPIO.BCM)
		GPIO.setwarnings(False)

		GPIO.setup(self.READY, GPIO.OUT)
		GPIO.setup(self.MOTA1, GPIO.OUT)
		GPIO.setup(self.MOTA2, GPIO.OUT)
		GPIO.setup(self.MOTAE, GPIO.OUT)
		GPIO.setup(self.MOTB1, GPIO.OUT)
		GPIO.setup(self.MOTB2, GPIO.OUT)
		GPIO.setup(self.MOTBE, GPIO.OUT)
		GPIO.setup(self.OUT1, GPIO.OUT)
		GPIO.setup(self.OUT2, GPIO.OUT)
		GPIO.setup(self.IN1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
		GPIO.setup(self.IN2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
		GPIO.setup(self.SERVO1, GPIO.OUT, initial=GPIO.LOW)
		GPIO.setup(self.SERVO2, GPIO.OUT, initial=GPIO.LOW)

		self.MOTAPWM = GPIO.PWM(self.MOTAE,100)
		self.MOTAPWM.start(0)
		self.MOTBPWM = GPIO.PWM(self.MOTBE,100)
		self.MOTBPWM.start(0)
		
		self.OUT1PWM = GPIO.PWM(self.OUT1,100)
		self.OUT1PWM.start(0)
		self.OUT2PWM = GPIO.PWM(self.OUT2,100)
		self.OUT2PWM.start(0)

	## Blink the Ready light, perfect first test
	def blink(self):
		GPIO.output(self.READY, GPIO.LOW)
		sleep(1)
		GPIO.output(self.READY, GPIO.HIGH)
		sleep(1)

	def _motor(self, MOTORA, MOTORB, value, motor_name):
		Error = False
		try:
			value = int(value)
		except:
			Error = True
			if self.DEBUG:
				print motor_name + ": Please enter a number - " + str(value) + " isn't valid"

		# value must be an integer now
		if Error != True:
			if -100 <= value <= 100:
				pass
			else:
				Error = True
				if self.DEBUG:
					print motor_name + ": Number must be between -100 and 100. " + str(value) + " is not valid"

		if Error != True:
			if value > 0:
				if self.DEBUG:
					print motor_name + " moving (positive)"
				GPIO.output(MOTORA, GPIO.HIGH)
				GPIO.output(MOTORB, GPIO.LOW)
				self.MOTAPWM.ChangeDutyCycle(value)

			elif value < 0:
				if self.DEBUG:
					print motor_name + " moving (negative)"
				GPIO.output(MOTORA, GPIO.LOW)
				GPIO.output(MOTORB, GPIO.HIGH)
				self.MOTAPWM.ChangeDutyCycle(abs(value))

			else:
				if self.DEBUG:
					print motor_name + " stopping"
				GPIO.output(MOTORA, GPIO.LOW)
				GPIO.output(MOTORB, GPIO.LOW)
				self.MOTAPWM.ChangeDutyCycle(0)

			return True

		else:
			return False
	
	# Control motor output number 1
	def motor1(self, value):
		return self._motor(self.MOTA1, self.MOTA2, value, "Motor 1")

	def motor2(self, value):
		return self._motor(self.MOTB1, self.MOTB2, value, "Motor 2")

	def out1(self, value):
		if value == True:
			self.OUT1PWM.ChangeDutyCycle(100)
		elif value == int(value):
			self.OUT1PWM.ChangeDutyCycle(value)
		else:
			self.GPIO.output(self.OUT1, GPIO.LOW)
	
	def out2(self, value):
		if value == True:
			self.OUT2PWM.ChangeDutyCycle(100)
		elif value == int(value):
			self.OUT2PWM.ChangeDutyCycle(value)
		else:
			GPIO.output(self.OUT2, GPIO.LOW)
	
	def in1(self):
		if GPIO.input(self.IN1):
			return True
		else:
			return False
	
	def in2(self):
		if GPIO.input(self.IN2):
			return True
		else:
			return False

	def _servo(self, servoblaster_no, value):
		Error = False

		try:
			value = int(value)
		except:
			Error = True
			if self.DEBUG:
				print "Servo: Please enter a number - " + str(value) + " isn't valid"

		if Error != True:
			if 0 <= value <= 180:
				pass
			else:
				Error = True
				if self.DEBUG:
					print "Servo: Number must be between 0 and 180 - '" + str(value) + "' isn't valid"

		if Error != True:
			servo = "echo " + str(servoblaster_no) + "=%d > /dev/servoblaster" % value
			os.system(servo)
			sleep(0.2)
			servo = "echo " + str(servoblaster_no) + "=0 > /dev/servoblaster"
			os.system(servo)

			return True
		else:
			return False

	def servo1(self, value):
		return self._servo(0, value)

	def servo2(self, value):
		return self._servo(1, value)

	def cleanup():
		GPIO.cleanup()
