import gpiozero, time, busio, adafruit_vl53l0x, threading

i2c = busio.I2C(board.SCL, board.SDA)
tca = adafruit_tca9548a.TCA9548A(i2c)

ldistance = adafruit_vl53l0x.VL53L0X(tca[2])
rdistance = adafruit_vl53l0x.VL53L0X(tca[3])
fdistance = adafruit_vl53l0x.VL53L0X(tca[4])

while True:
    lLaser = ldistance.range
    rLaser = ldistance.range
    fLaser = ldistance.range

    print('The Range to the Left is: {0}'.format(lLaser))
    time.sleep(0.5)
    print('The Range to the Right is: {0}'.format(rLaser))
    time.sleep(0.5)
    print('The Range in the Front is: {0}'.format(fLaser))
    time.sleep(0.5)
