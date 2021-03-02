import gpiozero, time, busio, adafruit_vl53l0x, threading

i2c = busio.I2C(board.SCL, board.SDA)
tca = adafruit_tca9548a.TCA9548A(i2c)

fdistance = adafruit_vl53l0x.VL53L0X(tca[4])

status = True

while True:
	Laser = fdistance.range
	if Laser < 160:
		print("You are Coming to close to a wall!")
		status = False
		print(status)
		print('The Range is: {0}'.format(Laser))
		time.sleep(0.5)
	else:
		print("Lets Keep going!")
		print('The Range is: {0}'.format(Laser))
		status = True
		print(status)
