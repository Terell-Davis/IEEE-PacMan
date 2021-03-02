import board, busio, adafruit_tcs34725, time

i2c = busio.I2C(board.SCL, board.SDA)
tca = adafruit_tca9548a.TCA9548A(i2c)
color = adafruit_tcs34725.TCS34725(tca[1])

while True:
    print(color.color_rgb_bytes)
    red, green, blue = color.color_rgb_bytes
    print("Red is: {0}".format(red))
    print("Green is: {0}".format(green))
    print("Blue is: {0}".format(blue))
    ired = int(red)
    igreen = int(green)
    iblue = int(blue)

    if ired > (igreen and iblue):
        print("The Color is Red")
    elif igreen > (ired and iblue):
        print("The Color is Green")
    elif iblue > (ired and igreen):
        print("The Color is Blue")

    print("Color: (" + str(ired) + ", " + str(igreen) + ", " + str(iblue) + ")")
    print('Temperature: {0}K'.format(color.color_temperature))
    print('Lux: {0}'.format(color.lux))
    time.sleep(4)
