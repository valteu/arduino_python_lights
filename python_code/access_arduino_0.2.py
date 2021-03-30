import serial
import time

ArduinoSerial = serial.Serial('/dev/ttyUSB0',9600)
print(ArduinoSerial.name)
time.sleep(2) #wait for 2 secounds for the communication to get established

data = [0, 0, 0]

print(ArduinoSerial.readline()) #read the serial data and print it as line

while 1 == 1:
	
    var = input("On or off: ")
    data[0] = int(var)
    num_led = input("Number of leds: ")
    data[1] = int(num_led)
    brightness = input("brightness: ")
    data[2] = int(brightness)

    print("you entered", var) #print the intput for confirmation
    
    ArduinoSerial.write(bytearray(data))
    if (var == '0'):
    	print("off")
	elif (var == '1'):
    	print("green")
	elif (var == '2'):
    	print("yellow")
	elif (var == '3'):
    	print("red")
	elif (var == '4'):
    	print("pink")
    elif (var == '5'):
    	print("tortoise")
	elif (var == '6'):
    	print("blue")
	elif (var == '7'):
    	print("white")
    time.sleep(1)
