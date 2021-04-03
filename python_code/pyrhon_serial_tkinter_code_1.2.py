import serial
import time
import tkinter as tk
from tkinter import *

brightness = 100
num_led = 12
WIDTH = 1920
HEIGHT = 1080

root = Tk()

root.geometry(str(WIDTH) + 'x' + str(HEIGHT))

ArduinoSerial = serial.Serial('/dev/ttyUSB0',9600)
print(ArduinoSerial.name)
time.sleep(2)

data = [0, 0, 0, 0, 0, 0]

print(ArduinoSerial.readline())

def data_to_arduino(mode, green, red, blue, num_led, brightness):
    x = 1
    while x == 1:
        data[0] = int(mode)
        data[1] = int(green)
        data[2] = int(red)
        data[3] = int(blue)
        data[4] = int(num_led)
        data[5] = int(brightness)
        x += 1

        print(type(data))


        data_array = bytearray(data)
        
        ArduinoSerial.write(data)

        time.sleep(2)


def light_off():
    data_to_arduino(mode=0, green=0, red=0, blue=0, num_led=0, brightness=0)

def static_green():
    brightness = brightness_slider.get()
    data_to_arduino(mode=1, green=255, red=0, blue=0, num_led=num_led, brightness=brightness)

def static_yellow():
    brightness = brightness_slider.get()
    data_to_arduino(mode=1, green=255, red=255, blue=0, num_led=num_led, brightness=brightness)

def static_red():
    brightness = brightness_slider.get()
    data_to_arduino(mode=1, green=0, red=255, blue=0, num_led=num_led, brightness=brightness)

def static_pink():
    brightness = brightness_slider.get()
    data_to_arduino(mode=1, green=0, red=255, blue=255, num_led=num_led, brightness=brightness)

def static_tortoise():
    brightness = brightness_slider.get()
    data_to_arduino(mode=1, green=255, red=0, blue=255, num_led=num_led, brightness=brightness)

def static_blue():
    brightness = brightness_slider.get()
    data_to_arduino(mode=1, green=0, red=0, blue=255, num_led=num_led, brightness=brightness)

def static_white():
    brightness = brightness_slider.get()
    data_to_arduino(mode=1, green=255, red=255, blue=255, num_led=num_led, brightness=brightness)

def rainbow_chase():
    brightness = brightness_slider.get()
    data_to_arduino(mode=10, green=0, red=0, blue=0, num_led=num_led, brightness=brightness)

def fade():
    brightness = brightness_slider.get()
    data_to_arduino(mode=11, green=0, red=0, blue=0, num_led=num_led, brightness=brightness)

def single_ball():
    brightness = brightness_slider.get()
    data_to_arduino(mode=12, green=0, red=0, blue=0, num_led=num_led, brightness=brightness)


def static_color():
    green_i = entry_green.get()
    red_i = entry_red.get()
    blue_i = entry_blue.get()
    brightness_i = brightness_slider.get()
    data_to_arduino(mode=1, green=green_i, red=red_i, blue=blue_i, num_led=12, brightness=brightness_i)

def brightness_controller(var):
    data_to_arduino(mode=current_mode, green=current_green, red=currnet_red, blue=current_blue, num_led=num_led, brightness=brightness_slider.get())

entry_green = Entry(root, width=3)
entry_green.pack()
entry_red = Entry(root, width=3)
entry_red.pack()
entry_blue = Entry(root, width=3)
entry_blue.pack()


brightness_slider = Scale(root, from_=0, to=100, orient=HORIZONTAL)
brightness_slider.pack()


Static = tk.Button(root, text="Static", padx=10, pady=5, fg="white", bg="#263D42", command=static_color)
Static.pack()

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



root.mainloop()
