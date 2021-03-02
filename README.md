# GSU IEEE-PacMan
This repository if for GSU'S IEEE to share and manage the code we will use for SoutheastCon 2021.
The rule for the competition are located [here](https://attend.ieee.org/southeastcon-2021/wp-content/uploads/sites/213/Hardware-Rules-v4.1.pdf).

## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the required libraries needed for "PacMan". Use [pacman-setup.sh](https://github.com/Terell-Davis/IEEE-PacMan/blob/main/pacman-setup.sh) to install all libraries.


```bash
./pacman-setup.sh
```

## Connections
To get started connect the multiplexer to SDA and SCL on the Raspberry Pi. 

![PinOut](https://github.com/Terell-Davis/IEEE-PacMan/blob/main/Assets/GPIO-Pinout.png)

Below is what each sensor is connected to on the multiplexer.:
* IMU = SD0, SC0
* Color Sensor = SD1, SC1
* Left Distance Sensor = SD2, SC2
* Right Distance Sensor = SD3, SC3
* Front Distance Sensor = SD4, SC4
* Servo Controller = (TBD)

## Usage
To get started make sure that the multiplexer is connected to SDA & SCL on the pi with the following command.

```bash
i2cdetect -y 1
```

Either open Terminal and cd into "Start Scripts" or open the folder on a desktop environment.

```bash
cd /IEEE-PacMan/Start\ Scripts/ 
```
Use any of the following script to test each sensor/servo.


## Contributors
Thank you to all who help with this project! Below will be their names and link to their github pages.
[Add Later]

Note: There are those who were not mentioned due to not having a github account or any projects they would like to show on github.