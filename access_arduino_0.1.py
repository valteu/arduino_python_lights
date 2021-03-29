import serial
import time
 
ArduinoSerial = serial.Serial('/dev/ttyUSB0',9600)
print(ArduinoSerial.name)
time.sleep(2) #wait for 2 secounds for the communication to get established

print(ArduinoSerial.readline()) #read the serial data and print it as line

while 1 == 1:
	
    var = input()
    print("you entered", var) #print the intput for confirmation
    
    if (var == '1'):
    	print('ok2')
    	ArduinoSerial.write(var.encode())
    	print ("LED turned ON")
    	time.sleep(1)
    
    elif (var == '0'):
    	print('ok3')
    	ArduinoSerial.write(var.encode())
    	print ("LED turned OFF")
    	time.sleep(1)
