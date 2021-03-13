import threading
import time
import ServoApplications, DistanceSensors
import IMUClass
from digitalio import DigitalInOut
import board


Pins = [DigitalInOut(board.D7), DigitalInOut(board.D9)]
Titty = DistanceSensors.Laser(Pins)
SpinnyBois = ServoApplications.ContinuousServos()
Imu = IMUClass.ImuClass()

def LaserFunction():
    while True:
        print("Laser 1 = " + str(Titty.LaserValue[0]))
        print("Laser 2 = " + str(Titty.LaserValue[1]))
        time.sleep(1)
        
LaserThread = threading.Thread(target=LaserFunction) # Creating a Sensor Polling Thread that pulls the sensor data
LaserThread.daemon = True # Run this thread as a background process
LaserThread.start() # Start the Thread


    
while True:
    Imu.euler()
    SpinnyBois.stop(0)
    SpinnyBois.stop(1)
    time.sleep(2)
    SpinnyBois.stop(0)
    SpinnyBois.stop(1)
    time.sleep(2)
    
