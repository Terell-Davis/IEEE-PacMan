import time, board, busio, adafruit_bno055, adafruit_tcs34725, adafruit_tca9548a

i2c = busio.I2C(board.SCL, board.SDA)
tca = adafruit_tca9548a.TCA9548A(i2c)
imu = adafruit_bno055.BNO055_I2C(i2c)
imu.mode = adafruit_bno055.COMPASS_MODE

last_val = 0xFFFF


def temperature():
    global last_val
    final = imu.temperature
    if abs(final - last_val) == 128:
        final = imu.temperature
        if abs(final - last_val) == 128:
            return 0b00111111 & final
    last_val = final
    return final


while True:
   # print("Temperature: {} degrees C".format(temperature()))
    print("Accelerometer (m/s^2): {}".format(imu.acceleration))
    print("Magnetometer (microteslas): {}".format(imu.magnetic))
   # print("Gyroscope (rad/sec): {}".format(imu.gyro))
   # print("Euler angle: {}".format(imu.euler))
   # print("Quaternion: {}".format(imu.quaternion))
   # print("Linear acceleration (m/s^2): {}".format(imu.linear_acceleration))
   # print("Gravity (m/s^2): {}".format(imu.gravity))

    time.sleep(1)
