import time
import board
import busio
import adafruit_bno055
import adafruit_tcs34725, adafruit_tca9548a
 
# Use these lines for I2C
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_bno055.BNO055_I2C()
 
# User these lines for UART
# uart = busio.UART(board.TX, board.RX)
#sensor = adafruit_bno055.BNO055_UART(uart)

last_val = 0xFFFF

def temperature():
	global last_val
	final = sensor.temperature
	if abs(final - last_val) == 128:
		final = sensor.temperature
		if abs(final - last_val) == 128:
			return 0b00111111 & final
	last_val = final
	return  final

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

