import serial
import time
import os
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

WIDTH = 1920
HEIGHT = 1080
num_led = 12
mode = 0
green = 0
red = 0
blue = 0

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
    data_to_arduino(mode=2, green=0, red=0, blue=0, num_led=num_led, brightness=brightness)

def fade():
    brightness = brightness_slider.get()
    data_to_arduino(mode=3, green=0, red=0, blue=0, num_led=num_led, brightness=brightness)

def single_ball():
    brightness = brightness_slider.get()
    data_to_arduino(mode=4, green=0, red=0, blue=0, num_led=num_led, brightness=brightness)


def static_color():
    green_i = entry_green.get()
    red_i = entry_red.get()
    blue_i = entry_blue.get()
    brightness_i = brightness_slider.get()
    data_to_arduino(mode=1, green=green_i, red=red_i, blue=blue_i, num_led=12, brightness=brightness_i)

def brightness_controller(_):
    current_mode = mode
    current_green = green
    currnet_red = red
    current_blue = blue
    print(_)
    data_to_arduino(mode=current_mode, green=current_green, red=currnet_red, blue=current_blue, num_led=num_led, brightness=brightness_slider.get())

image1 = Image.open("//home//valteu//programming//lights//light_gui_images//background_gui.png")
test = ImageTk.PhotoImage(image1)


label1 = tk.Label(image=test)
label1.image = test

label1.place(x=-1, y=-1)

color_frame = tk.Frame(root, bg="#9e0025")
color_frame.place(relwidth=0.6, relheight=0.3, relx=0.35, rely=0.6)

color_frame_headline = tk.Label(color_frame, text="Color", height=1, width=int(WIDTH*0.6), padx=50, pady=2, bg="#9e0025", fg="white",  borderwidth=3)
color_frame_headline.config(font=("Arial", 24), state=DISABLED, anchor=CENTER, highlightbackground = "red", highlightcolor= "red", fg="white")
color_frame_headline.pack()

entry_green = Entry(color_frame, width=3)
entry_green.pack()
entry_green.place(relx=0.125, rely=0.6)
entry_red = Entry(color_frame, width=3)
entry_red.pack()
entry_red.place(relx=0.125, rely=0.675)
entry_blue = Entry(color_frame, width=3)
entry_blue.pack()
entry_blue.place(relx=0.125, rely=0.75)


brightness_slider = Scale(color_frame, from_=0, to=100, length=400, orient=HORIZONTAL)
brightness_slider.pack()
brightness_slider.place(relx=0.3, rely=0.6)

brightness_slider. set(75)

headline = tk.Label(root, text="Valteu lights", width=15, height=1, bg="#9e0025",  borderwidth=3)
headline.config(font=("Arial", 44), state=DISABLED, anchor=CENTER, highlightbackground = "red", highlightcolor= "red", fg="white")
headline.pack()

Static = tk.Button(color_frame, text="Static", width=5, height=3, fg="white", bg="#263D42", command=static_color)
Static.pack()
Static.place(relx=0.05, rely=0.6)

Off = tk.Button(color_frame, width=5, height=3, bg="grey", command=light_off)
Off.pack()
Off.place(relx=0.05, rely=0.3)

StaticGreen = tk.Button(color_frame, width=5, height=3, bg="green", command=static_green)
StaticGreen.pack()
StaticGreen.place(relx=0.125, rely=0.3)

StaticYellow = tk.Button(color_frame, width=5, height=3, bg="yellow", command=static_yellow)
StaticYellow.pack()
StaticYellow.place(relx=0.2, rely=0.3)

StaticRed = tk.Button(color_frame, width=5, height=3, bg="red", command=static_red)
StaticRed.pack()
StaticRed.place(relx=0.275, rely=0.3)

StaticPink = tk.Button(color_frame, width=5, height=3, bg="#ff00ff", command=static_pink)
StaticPink.pack()
StaticPink.place(relx=0.35, rely=0.3)

StaticTortoise = tk.Button(color_frame, width=5, height=3, bg="#00ffff", command=static_tortoise)
StaticTortoise.pack()
StaticTortoise.place(relx=0.425, rely=0.3)

StaticBlue = tk.Button(color_frame, width=5, height=3, bg="blue", command=static_blue)
StaticBlue.pack()
StaticBlue.place(relx=0.5, rely=0.3)

StaticWhite = tk.Button(color_frame, width=5, height=3, fg="white", bg="white", command=static_white)
StaticWhite.pack()
StaticWhite.place(relx=0.575, rely=0.3)

RainbowChase = tk.Button(color_frame, text="Rainbow Chase", width=5, height=3, fg="white", bg="#263D42", command=rainbow_chase)
RainbowChase.pack()
RainbowChase.place(relx=0.65, rely=0.3)

Fade = tk.Button(color_frame, text="Fade", width=5, height=3, fg="white", bg="#263D42", command=fade)
Fade.pack()
Fade.place(relx=0.725, rely=0.3)

SingleBall = tk.Button(color_frame, text="Singel Ball", width=5, height=3, fg="white", bg="#263D42", command=single_ball)
SingleBall.pack()
SingleBall.place(relx=0.8, rely=0.3)

root.mainloop()
