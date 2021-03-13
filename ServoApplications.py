# Servo Code


import time, busio, adafruit_vl53l0x, threading, board
from adafruit_servokit import ServoKit

class ContinuousServos:
    def __init__(self): self.kit = ServoKit(channels=16, address=0x40)
    def forward(self, whichServo): self.kit.continuous_servo[whichServo].throttle = 1
    def backward(self, whichServo): self.kit.continuous_servo[whichServo].throttle = -1
    def stop(self, whichServo): self.kit.continuous_servo[whichServo].throttle = 0
    
class RobotBase:
    def __init__(self, LeftServo, RightServo):
        self.motors = ContinuousServos()
    def turnLeft(self):
        self.kit.continuous_servo[self.LeftServo].throttle = 1
        self.kit.continuous_servo[self.RightServo].throttle = -1
        time.sleep(1)
    def turnRight(self):
        self.kit.continuous_servo[self.LeftServo].throttle = -1
        self.kit.continuous_servo[self.RightServo].throttle = 1
        time.sleep(1)

class One80:
    def __init__(self):
        self.motors = ContinuousServos()
    def angle(self,port,angles):
        if(angle < 0 or angle > 181):
            raise Exception("Range out of bounds")
        else:
            kit.servo[self.port].angle = self.angles 
        
        
if __name__ == "__main__":
    SpinnyBois = ContinuousServos()
    SpinnyBois.forward(0)
    SpinnyBois.forward(1)
    time.sleep(2)
    SpinnyBois.stop(0)
    SpinnyBois.stop(1)
    time.sleep(2)