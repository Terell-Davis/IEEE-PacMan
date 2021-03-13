import board
import busio
import adafruit_pca9685, adafruit_tca9548a
from adafruit_servokit import ServoKit
import adafruit_motor.servo
import time
import gpiozero, adafruit_vl53l0x, threading

i2c = busio.I2C(board.SCL, board.SDA)
tca = adafruit_tca9548a.TCA9548A(i2c)
#pca = adafruit_pca9685.PCA9685(tca[1])

kit = ServoKit(channels=16)



fdistance = adafruit_vl53l0x.VL53L0X(tca[2])

while True:
    fLaser = fdistance.range
    print('The Range to the Left is: {0}'.format(fLaser))
    
    if fLaser > 161:
        kit.continuous_servo[0].throttle = 1
        kit.continuous_servo[1].throttle = 1
    
    if fLaser < 160:
        kit.continuous_servo[0].throttle = 0.5
        kit.continuous_servo[1].throttle = 0.5
        
    if fLaser < 100:
        kit.continuous_servo[0].throttle = 0
        kit.continuous_servo[1].throttle = 0

