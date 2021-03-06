#!/usr/bin/env python

# MotorPiTX is in a convenient subfolder so insert that folder into the importable paths
import sys
sys.path.insert(0, 'MotorPiTX')
from MotorPiTX import MotorPiTX

import time

class Rupert:
	def __init__(self):
		self.motorpitx = MotorPiTX()
		self.motor1 = self.motorpitx.motor1
		self.motor2 = self.motorpitx.motor2
		self.debug = True

	# STOP
	def stopMotor(self, motor):
		motor(0)
	
	def stopMotor1(self):
		self.stopMotor(self.motor1)
	
	def stopMotor2(self):
		self.stopMotor(self.motor2)
	
	def stopMotors(self):
		if self.debug:
			print "All stop"
		self.stopMotor1()
		self.stopMotor2()

	# RUN
	def runMotor(self, motor, speed, direction):
		motor(speed*direction)

	def runMotor1(self, speed, direction):
		if self.debug:
			print " - Running motor 1, speed " + str(speed) + ", direction " + str(direction)
		self.runMotor(self.motor1, speed, direction)
	
	def runMotor2(self, speed, direction):
		if self.debug:
			print " - Running motor 2, speed " + str(speed) + ", direction " + str(direction)
		self.runMotor(self.motor2, speed, direction)
	
	def runMotorsTogether(self, speed, direction, duration):
		self.runMotor1(speed, direction)
		self.runMotor2(speed, direction)
		time.sleep(duration)
		self.stopMotors()
	
	def runForward(self, speed, duration):
		if self.debug:
			print "Running forward, speed " + str(speed) + " duration " + str(duration)
		self.runMotorsTogether(speed, 1, duration)
	
	def runBackward(self, speed, duration):
		if self.debug:
			print "Running backward, speed " + str(speed) + " duration " + str(duration)
		self.runMotorsTogether(speed, -1, duration)
	
	# TURN
	def turnLeft(self, speed, duration):
		if self.debug:
			print "Turning left, speed " + str(speed) + " duration " + str(duration)
		self.runMotor1(speed, -1)
		self.runMotor2(speed, 1)
		time.sleep(duration)
		self.stopMotors()
	
	def turnRight(self, speed, duration):
		if self.debug:
			print "Turning right, speed " + str(speed) + " duration " + str(duration)
		self.runMotor1(speed, 1)
		self.runMotor2(speed, -1)
		time.sleep(duration)
		self.stopMotors()

