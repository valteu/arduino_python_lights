import serial
import time
import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()

def light_off():
	data_to_arduino(mode=0, num_led=0, brightness=0)

def static_green():
	data_to_arduino(mode=1, num_led=12, brightness=100)

def static_yellow():
	data_to_arduino(mode=2, num_led=12, brightness=100)

def static_red():
	data_to_arduino(mode=3, num_led=12, brightness=100)

def static_pink():
	data_to_arduino(mode=4, num_led=12, brightness=100)

def static_tortoise():
	data_to_arduino(mode=5, num_led=12, brightness=100)

def static_blue():
	data_to_arduino(mode=6, num_led=12, brightness=100)

def static_white():
	data_to_arduino(mode=7, num_led=12, brightness=100)

def rainbow_chase():
	data_to_arduino(mode=10, num_led=12, brightness=100)

def fade():
	data_to_arduino(mode=11, num_led=12, brightness=100)

def single_ball():
	data_to_arduino(mode=12, num_led=12, brightness=100)

canvas = tk.Canvas(root, height=700, width=700, bg="#263D42")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

Off = tk.Button(root, text="Off", padx=10, pady=5, fg="white", bg="#263D42", command=light_off)
Off.pack()

StaticGreen = tk.Button(root, text="Static Green", padx=10, pady=5, fg="white", bg="#263D42", command=static_green)
StaticGreen.pack()

StaticYellow = tk.Button(root, text="Static Yellow", padx=10, pady=5, fg="white", bg="#263D42", command=static_yellow)
StaticYellow.pack()

StaticRed = tk.Button(root, text="Static Red", padx=10, pady=5, fg="white", bg="#263D42", command=static_red)
StaticRed.pack()

StaticPink = tk.Button(root, text="Static Pink", padx=10, pady=5, fg="white", bg="#263D42", command=static_pink)
StaticPink.pack()

StaticTortoise = tk.Button(root, text="Static Tortoise", padx=10, pady=5, fg="white", bg="#263D42", command=static_tortoise)
StaticTortoise.pack()

StaticBlue = tk.Button(root, text="Static Blue", padx=10, pady=5, fg="white", bg="#263D42", command=static_blue)
StaticBlue.pack()

StaticWhite = tk.Button(root, text="Static White", padx=10, pady=5, fg="white", bg="#263D42", command=static_white)
StaticWhite.pack()

RainbowChase = tk.Button(root, text="Rainbow Chase", padx=10, pady=5, fg="white", bg="#263D42", command=rainbow_chase)
RainbowChase.pack()

Fade = tk.Button(root, text="Fade", padx=10, pady=5, fg="white", bg="#263D42", command=fade)
Fade.pack()

SingleBall = tk.Button(root, text="Singel Ball", padx=10, pady=5, fg="white", bg="#263D42", command=single_ball)
SingleBall.pack()

ArduinoSerial = serial.Serial('/dev/ttyUSB0',9600)
print(ArduinoSerial.name)
time.sleep(2) #wait for 2 secounds for the communication to get established

data = [0, 0, 0]

print(ArduinoSerial.readline()) #read the serial data and print it as line



def data_to_arduino(mode, num_led, brightness):
		
    # mode = input("Color/ effect: ")
    data[0] = int(mode)
    # num_led = input("Number of leds: ")
    data[1] = int(num_led)
    # brightness = input("brightness: ")
    data[2] = int(brightness)
    data_array = bytearray(data)


    print("you entered", mode) #print the intput for confirmation
    
    ArduinoSerial.write(data_array)

    time.sleep(1)

root.mainloop()
