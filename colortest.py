import board
import busio
import adafruit_tcs34725, adafruit_tca9548a
import time
i2c = busio.I2C(board.SCL, board.SDA)
tca = adafruit_tca9548a.TCA9548A(i2c)
#sensor = adafruit_tcs34725.TCS34725(i2c)
sensor = adafruit_tcs34725.TCS34725(tca[0])
while True:
    print('Color: ({0}, {1}, {2})'.format(*sensor.color_rgb_bytes))
    print('Temperature: {0}K'.format(sensor.color_temperature))
    print('Lux: {0}'.format(sensor.lux))
    time.sleep(1)

