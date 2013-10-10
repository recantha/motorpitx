from MotorPiTX import MotorPiTX

motorpitx = MotorPiTX()

Count = 0
while Count < 5:
	motorpitx.blink()
	Count = Count + 1

motorpitx.cleanup()
