import serial
import time

ArduinoSerial = serial.Serial('/dev/ttyUSB0',9600)
print(ArduinoSerial.name)
time.sleep(2) #wait for 2 secounds for the communication to get established

data = [0, 0, 0, 0, 0, 0]

print(ArduinoSerial.readline()) #read the serial data and print it as line

while 1 == 1:
    mode = input("mode: ")
    data[0] = int(mode)
    green = input("green value: ")
    data[1] = int(green)
    red = input("red value: ")
    data[2] = int(red)
    blue = input("blue value: ")
    data[3] = int(blue)
    num_led = input("num_led: ")
    data[4] = int(num_led)
    brightness = input("brightness: ")
    data[5] = int(brightness)

    print(type(data))


    data_array = bytearray(data)
    
    ArduinoSerial.write(data)

    time.sleep(1)
