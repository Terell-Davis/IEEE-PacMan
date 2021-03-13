import time
import board
import threading
from digitalio import DigitalInOut
from adafruit_vl53l0x import VL53L0X

class Laser:
    def __init__(self, ShutDownPinArray):
        i2c = board.I2C()
        self.xshut = ShutDownPinArray
        self.LaserValue = [8190]*len(self.xshut)
        for power_pin in self.xshut: power_pin.switch_to_output(value=False)
        self.LaserArray = []

        for i, power_pin in enumerate(self.xshut):
            power_pin.value = True
            print(i)
            self.LaserArray.insert(i, VL53L0X(i2c))
            self.LaserArray[i].set_address(i + 0x30)
            
        self.LaserPollingThread = threading.Thread(target=self.LaserPolling) # Creating a Sensor Polling Thread that pulls the sensor data
        self.LaserPollingThread.daemon = True # Run this thread as a background process
        self.LaserPollingThread.start() # Start the Thread
            
    def LaserPolling(self):
        while True:
            for index, sensor in enumerate(self.LaserArray):
                self.LaserValue[index] = sensor.range
            time.sleep(0.1)

#   >>> import board
#   >>> i2c = board.I2C()
#   >>> if i2c.try_lock():
#   >>>     [hex(x) for x in i2c.scan()]
#   >>>     i2c.unlock()
if __name__ == "__main__":
    Pins = [DigitalInOut(board.D7), DigitalInOut(board.D9)]
    Titty = Laser(Pins)
    while True:
        print("Laser 1 = " + str(Titty.LaserValue[0]))
        print("Laser 2 = " + str(Titty.LaserValue[1]))
        print("Laser 3 = " + str(Titty.LaserValue[2]))
        time.sleep(1)


    