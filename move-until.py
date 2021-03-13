import gpiozero, time, busio, adafruit_vl53l0x, threading, board
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)

i2c = busio.I2C(board.SCL, board.SDA)
fdistance = adafruit_vl53l0x.VL53L0X(i2c)

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
        
        
       
    

