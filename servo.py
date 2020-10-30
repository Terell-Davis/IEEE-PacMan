import gpiozero
import time
import busio
import adafruit_vl53l0x
import threading

# Global Varribales
leftServoPin = 14
rightServoPin = 27
LaserDistance = 2000

leftServo = gpiozero.Servo(leftServoPin)  # Create Left Servo Object
rightServo = gpiozero.Servo(rightServoPin)  # Create Right Servo Object
LaserRangeFinder = adafruit_vl53l0x.VL53L0X(busio.I2C(3, 2))  # Create i2c Lase$


def getLaser(): # Get Laser Distance 10 times a second (not really....)
        while True: # Infinite loop, foreva? Forevaeva? For EVA EVA?
                global LaserDistance  # Get Global Laser Distance Variable
                LaserDistance = LaserRangeFinder.range  # Grab Laser Distance a$
                print(LaserDistance)  # Print it (This can be commented out, is$
                time.sleep(0.02) # Wait for 0.02 seconds


def robotAlgorithm():
        while True:
                if LaserDistance >= 250:
                        leftServo.max()
                        rightServo.min()
                else:
                        leftServo.min()
                        rightServo.min()
                time.sleep(.1)


sensorPolling = threading.Thread(target=getLaser) # Creating a Sensor Polling Thread that pulls the sensor data
sensorPolling.daemon = True # Run this thread as a background process
sensorPolling.start() # Start the Thread

algorithmThread = threading.Thread(target=robotAlgorithm)
algorithmThread.daemon = True # Run this thread as a background process
algorithmThread.start() # Start the Thread

if __name__ == '__main__':
        while True:
                pass

