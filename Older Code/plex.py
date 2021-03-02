import time, board, busio, adafruit_bno055, adafruit_vl53l0x, adafruit_tca9548a, threading

i2c = busio.I2C(3, 2)
tca  = adafruit_tca9548a.TCA9548A(i2c)
LaserDistance = 2000
last_val = 0XFFFF

laserfinder = adafruit_vl53l0x.VL53L0X(tca[0])
sensor = adafruit_bno055.BNO055_I2C(tca[1 ])

def getLaser():
	while True:
		global LaserDistance
		LaserDistance = laserfinder.range
		print(LaserDistance)
		time.sleep(0.5)


def temperature():
	global last_val
	final = sensor.temperature
	if abs(final - last_val) == 128:
		final = sensor.temperature
		if abs(final - last_val) == 128:
			return 0b00111111 & final
	last_val = final
	return  final

def info():
	while True:
		print("Temperature: {} degrees C".format(temperature()))
		print("Accelerometer (m/s^2): {}".format(sensor.acceleration))
		print("Magnetometer (microteslas): {}".format(sensor.magnetic))
		print("Gyroscope (rad/sec): {}".format(sensor.gyro))
		print("Euler angle: {}".format(sensor.euler))
		print("Quaternion: {}".format(sensor.quaternion))
		print("Linear acceleration (m/s^2): {}".format(sensor.linear_acceleration))
		print("Gravity (m/s^2): {}".format(sensor.gravity))
		print()

		time.sleep(1)

sensorPolling = threading.Thread(target=getLaser)
sensorPolling.daemon = True
sensorPolling.start()

infoThread = threading.Thread(target=info)
infoThread.daemon = True
infoThread.start()

if __name__ == '__main__':
	while True:
		pass
