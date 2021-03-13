import threading
import time
import ServoApplications, DistanceSensors
#import IMUClass
from digitalio import DigitalInOut
import board


Pins = [DigitalInOut(board.D23), DigitalInOut(board.D24), DigitalInOut(board.D25)]
Titty = DistanceSensors.Laser(Pins)
SpinnyBois = ServoApplications.ContinuousServos()
#Imu = IMUClass.ImuClass()

def LaserFunction():
    while True:
        print("Laser Distance 1 = " + str(Titty.LaserValue[0]))
        print("Laser Distance 2 = " + str(Titty.LaserValue[1]))
        print("Laser Distance 3 = " + str(Titty.LaserValue[2]))
        time.sleep(1)
        
LaserThread = threading.Thread(target=LaserFunction) # Creating a Sensor Polling Thread that pulls the sensor data
LaserThread.daemon = True # Run this thread as a background process
LaserThread.start() # Start the Thread


    
while True:
#    Imu.euler()
    SpinnyBois.forward(0, 1)
    time.sleep()
    SpinnyBois.stop(0, 1)
    time.sleep(2)
    
