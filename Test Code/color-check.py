import board, busio, adafruit_tcs34725, time

i2c = busio.I2C(board.SCL, board.SDA)
#tca = adafruit_tca9548a.TCA9548A(i2c)
color = adafruit_tcs34725.TCS34725(i2c)

while True:
    print(color.color_rgb_bytes)
    red, green, blue = color.color_rgb_bytes
    print("Red is: {0}".format(red))
    print("Green is: {0}".format(green))
    print("Blue is: {0}".format(blue))
 
    if ((red > green) and (red > blue)):
        print("The Color is Red")
    elif ((green > red) and (green > blue)):
        print("The Color is Green")
    elif ((blue > red) and (blue > green)):
        print("The Color is Blue")

    print("Color: (" + str(red) + ", " + str(green) + ", " + str(blue) + ")")
    print('Temperature: {0}K'.format(color.color_temperature))
    print('Lux: {0}'.format(color.lux))
    time.sleep(2)
