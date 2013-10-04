import motorpitx
import time

# STOP
def stopMotor(motor):
	motor(0)

def stopMotor1():
	stopMotor(motorpitx.motor1)

def stopMotor2():
	stopMotor(motorpitx.motor1)

# RUN
def runMotor(motor, speed, direction):
	motor(speed*direction)

def runMotor1(speed, direction):
	print " - Running motor 1, speed " + str(speed) + ", direction " + str(direction)
	runMotor(motorpitx.motor1, speed, direction)

def runMotor2(speed, direction):
	print " - Running motor 2, speed " + str(speed) + ", direction " + str(direction)
	runMotor(motorpitx.motor2, speed, direction)

def runMotorsTogether(speed, direction, duration):
	runMotor1(speed, direction)
	runMotor2(speed, direction)
	time.sleep(duration)
	stopMotor1()
	stopMotor2()

def runForward(speed, duration):
	print "Running forward, speed " + str(speed) + " duration " + str(duration)
	runMotorsTogether(speed, 1, duration)

def runBackward(speed, duration):
	print "Running backward, speed " + str(speed) + " duration " + str(duration)
	runMotorsTogether(speed, -1, duration)

# TURN
def turnLeft(speed, duration):
	print "Turning left, speed " + str(speed) + " duration " + str(duration)
	runMotor1(speed, -1)
	runMotor2(speed, 1)

def turnRight(speed, duration):
	print "Turning right, speed " + str(speed) + " duration " + str(duration)
	runMotor1(speed, 1)
	runMotor2(speed, -1)

runForward(50, 1)
turnLeft(50, 1)
runBackward(50, 1)
turnRight(50, 1)

