import time, board, busio, adafruit_bno055, adafruit_tcs34725, adafruit_tca9548a, adafruit_vl53l0x

i2c = busio.I2C(board.SCL, board.SDA)
tca = adafruit_tca9548a.TCA9548A(i2c)

imu = adafruit_bno055.BNO055_I2C(tca[0])
color = adafruit_tcs34725.TCS34725(tca[1])

ldistance = adafruit_vl53l0x.VL53L0X(tca[2])
rdistance = adafruit_vl53l0x.VL53L0X(tca[3])
fdistance = adafruit_vl53l0x.VL53L0X(tca[4])

# servo = Adafruit_PCA9685.PCA9685()

last_val = 0xFFFF
LaserDistance = 2000


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
    print('Color: ({0}, {1}, {2})'.format(*color.color_rgb_bytes))
    print('Temperature: {0}K'.format(color.color_temperature))
    print('Lux: {0}'.format(color.lux))
    time.sleep(1)

    ldistance = laserfinder.range
    print('Left Range is: {0}'.format(LaserDistance))
    time.sleep(0.5)

    rdistance = laserfinder.range
    print('Right Range is: {0}'.format(LaserDistance))
    time.sleep(0.5)

    fdistance = laserfinder.range
    print('Front Range is: {0}'.format(LaserDistance))
    time.sleep(0.5)

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
