import time, board, busio, adafruit_bno055, adafruit_vl53l0x, adafruit_tca9548a, threading, adafruit_tcs34725

i2c = busio.I2C(3, 2)
tca  = adafruit_tca9548a.TCA9548A(i2c)

color = adafruit_tcs34725.TCS34725(tca[0])
#laserfinder = adafruit_vl53l0x.VL53L0X(tca[4])
#imu = adafruit_bno055.BNO055_I2C(tca[7])

LaserDistance = 2000
last_val = 0XFFFF

def getLaser():
	while True:
		global LaserDistance
		LaserDistance = laserfinder.range
		print(LaserDistance)
		time.sleep(0.5)


def temperature():
	global last_val
	final = imu.temperature
	if abs(final - last_val) == 128:
		final = imu.temperature
		if abs(final - last_val) == 128:
			return 0b00111111 & final
	last_val = final
	return  final

def info():
	while True:
		print("Temperature: {} degrees C".format(temperature()))
		print("Accelerometer (m/s^2): {}".format(imu.acceleration))
		print("Magnetometer (microteslas): {}".format(imu.magnetic))
		print("Gyroscope (rad/sec): {}".format(imu.gyro))
		print("Euler angle: {}".format(imu.euler))
		print("Quaternion: {}".format(imu.quaternion))
		print("Linear acceleration (m/s^2): {}".format(imu.linear_acceleration))
		print("Gravity (m/s^2): {}".format(imu.gravity))
		print()

		time.sleep(1)
def color():
    while True:
        print('Color: ({0}, {1}, {2})'.format(color.color_rgb_bytes))
        print('Temperature: {0}K'.format(color.color_temperature))
        print('Lux: {0}'.format(color.lux))
        time.sleep(1)






