import serial
import time
import os
import os.path
from os import path
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import pickle

WIDTH = 1920
HEIGHT = 1080
num_led = 12
mode = 0
green = 0
red = 0
blue = 0
custome_button_place_1 = False
custome_button_place_2 = False
custome_button_place_3 = False
custome_button_place_4 = False
custome_button_place_5 = False
custome_button_place_6 = False
custome_button_place_7 = False
custome_button_place_8 = False

os.system("clear")

if path.exists("valteu_lights_gui_saves.dat") == True:
    saved_data = pickle.load(open("valteu_lights_gui_saves.dat", "rb"))
    print(saved_data)
    custom_green = saved_data[0]
    custom_red = saved_data[1]
    custom_blue = saved_data[2]
    custom_brightness = saved_data[3]
    custome_button_place_1 = saved_data[4]

else:
    first_entry = [0]
    pickle.dump(first_entry, open("valteu_lights_gui_saves.dat", "wb"))

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
        print(data)

        time.sleep(2)


def light_off():
    data_to_arduino(mode=0, green=0, red=0, blue=0, num_led=0, brightness=0)

def static_green():
    brightness = int(brightness_slider.get() * 0.9)
    data_to_arduino(mode=1, green=255, red=0, blue=0, num_led=num_led, brightness=brightness)

def static_yellow():
    brightness = int(brightness_slider.get() * 0.9)
    data_to_arduino(mode=1, green=255, red=255, blue=0, num_led=num_led, brightness=brightness)

def static_red():
    brightness = int(brightness_slider.get() * 0.9)
    data_to_arduino(mode=1, green=0, red=255, blue=0, num_led=num_led, brightness=brightness)

def static_pink():
    brightness = int(brightness_slider.get() * 0.9)
    data_to_arduino(mode=1, green=0, red=255, blue=255, num_led=num_led, brightness=brightness)

def static_tortoise():
    brightness = int(brightness_slider.get() * 0.9)
    data_to_arduino(mode=1, green=255, red=0, blue=255, num_led=num_led, brightness=brightness)

def static_blue():
    brightness = int(brightness_slider.get() * 0.9)
    data_to_arduino(mode=1, green=0, red=0, blue=255, num_led=num_led, brightness=brightness)

def static_white():
    brightness = int(brightness_slider.get() * 0.9)
    data_to_arduino(mode=1, green=255, red=255, blue=255, num_led=num_led, brightness=brightness)

def rainbow_chase():
    brightness = int(brightness_slider.get() * 0.9)
    data_to_arduino(mode=2, green=0, red=0, blue=0, num_led=num_led, brightness=brightness)

def fade():
    brightness = int(brightness_slider.get() * 0.9)
    data_to_arduino(mode=3, green=0, red=0, blue=0, num_led=num_led, brightness=brightness)

def single_ball():
    brightness = int(brightness_slider.get() * 0.9)
    data_to_arduino(mode=4, green=0, red=0, blue=0, num_led=num_led, brightness=brightness)

def two_color_fade_command():
    brightness = int(brightness_slider.get() * 0.9)
    data_to_arduino(mode=5, green=0, red=0, blue=0, num_led=num_led, brightness=brightness)

def rainbow_fade_command():
    brightness = int(brightness_slider.get() * 0.9)
    data_to_arduino(mode=6, green=0, red=0, blue=0, num_led=num_led, brightness=brightness)

def juggle_command():
    brightness = int(brightness_slider.get() * 0.9)
    data_to_arduino(mode=7, green=0, red=0, blue=0, num_led=num_led, brightness=brightness)

def fire_command():
    brightness = int(brightness_slider.get() * 0.9)
    data_to_arduino(mode=8, green=0, red=0, blue=0, num_led=num_led, brightness=brightness)

def beat_command():
    brightness = int(brightness_slider.get() * 0.9)
    data_to_arduino(mode=9, green=0, red=0, blue=0, num_led=num_led, brightness=brightness)

def custom_mode(green, red, blue, brightness):
    brightness = int(brightness_slider.get() * 0.9)
    data_to_arduino(mode=1, green=green, red=red, blue=blue, num_led=num_led, brightness=brightness)

def save_custom_color(custom_color_number):
    custom_green = entry_green.get()
    custom_red = entry_red.get()
    custom_blue = entry_blue.get()
    custom_brightness = int(custom_brightness_slider.get() * 0.9)
    custome_button_place_1 = True
    
    save_list_label = "custom_mode_save_list_" + str(custom_color_number)
    save_list = [custom_green, custom_red, custom_blue, custom_brightness, custome_button_place_1]
    print(type(save_list))
    pickle.dump(save_list, open("valteu_lights_gui_saves.dat", "wb"))

    custom_mode_button_1 = tk.Button(color_frame, text="custom", width=5, height=3, bg="white", command=lambda: custom_mode(green=custom_green, red=custom_red, blue=custom_blue, brightness=custom_brightness))
    custom_mode_button_1.pack()
    custom_mode_button_1.place(relx=0.05, rely=0.6)

    create_custom_mode_1 = tk.Button(color_frame, text="edit", width=1, height=1, fg="white", bg="#263D42", command=lambda: create_custom_color_window(custom_color_number=1))
    create_custom_mode_1.pack()
    create_custom_mode_1.place(relx=0.05, rely=0.6)

    return custome_button_place_1

def create_custom_color_window(custom_color_number):
    global entry_green, entry_red, entry_blue, custom_brightness_slider

    custom_window = tk.Toplevel(color_frame, width=int(WIDTH/3), height=int(HEIGHT/3))
    entry_green = Entry(custom_window, width=3)
    entry_green.pack()
    entry_green.place(relx=0.25, rely=0.1)
    entry_red = Entry(custom_window, width=3)
    entry_red.pack()
    entry_red.place(relx=0.25, rely=0.175)
    entry_blue = Entry(custom_window, width=3)
    entry_blue.pack()
    entry_blue.place(relx=0.25, rely=0.25)

    custom_brightness_slider = Scale(custom_window, from_=1, to=100, length=400, orient=HORIZONTAL)
    custom_brightness_slider.pack()
    custom_brightness_slider.place(relx=0.3, rely=0.1)
    custom_brightness_slider. set(75)

    Static_color = tk.Button(custom_window, text="Preview", width=5, height=3, fg="white", bg="#263D42", command=static_color)
    Static_color.pack()
    Static_color.place(relx=0.05, rely=0.1)

    Save_color = tk.Button(custom_window, text="Save", width=5, height=3, fg="white", bg="#263D42",command=lambda: save_custom_color(custom_color_number))
    Save_color.pack()
    Save_color.place(relx=0.85, rely=0.8)

def static_color():
    green_i = entry_green.get()
    red_i = entry_red.get()
    blue_i = entry_blue.get()
    brightness_i = int(brightness_slider.get() * 0.9)
    data_to_arduino(mode=1, green=green_i, red=red_i, blue=blue_i, num_led=12, brightness=brightness_i)

def brightness_controller(_):
    current_mode = mode
    current_green = green
    currnet_red = red
    current_blue = blue
    data_to_arduino(mode=current_mode, green=current_green, red=currnet_red, blue=current_blue, num_led=num_led, brightness=int(brightness_slider.get() * 0.9))

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

brightness_slider = Scale(color_frame, from_=1, to=100, length=400, orient=HORIZONTAL)
brightness_slider.pack()
brightness_slider.place(relx=0.3, rely=0.8)
brightness_slider. set(75)

headline = tk.Label(root, text="Valteu lights", width=15, height=1, bg="#9e0025",  borderwidth=3)
headline.config(font=("Arial", 44), state=DISABLED, anchor=CENTER, highlightbackground = "red", highlightcolor= "red", fg="white")
headline.pack()

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

two_color_fade = tk.Button(color_frame, text="2 Color fade", width=5, height=3, fg="white", bg="#263D42", command=two_color_fade_command)
two_color_fade.pack()
two_color_fade.place(relx=0.875, rely=0.3)

Rainbow_fade = tk.Button(color_frame, text="Rb Fade", width=5, height=3, fg="white", bg="#263D42", command=rainbow_fade_command)
Rainbow_fade.pack()
Rainbow_fade.place(relx=0.925, rely=0.3)

Juggle = tk.Button(color_frame, text="Juggle", width=5, height=3, fg="white", bg="#263D42", command=juggle_command)
Juggle.pack()
Juggle.place(relx=0.925, rely=0.6)

FireButton = tk.Button(color_frame, text="Fire", width=5, height=3, fg="white", bg="#263D42", command=fire_command)
FireButton.pack()
FireButton.place(relx=0.875, rely=0.6)

BeatButton = tk.Button(color_frame, text="Beat", width=5, height=3, fg="white", bg="#263D42", command=beat_command)
BeatButton.pack()
BeatButton.place(relx=0.8, rely=0.6)

if custome_button_place_1 == False:
    create_custom_mode_1 = tk.Button(color_frame, text="custom", width=5, height=3, fg="white", bg="#263D42", command=lambda: create_custom_color_window(custom_color_number=1))
    create_custom_mode_1.pack()
    create_custom_mode_1.place(relx=0.05, rely=0.6)
else:
    custom_mode_button_1 = tk.Button(color_frame, text="custom", width=5, height=3, bg="white", command=lambda: custom_mode(green=custom_green, red=custom_red, blue=custom_blue, brightness=custom_brightness))
    custom_mode_button_1.pack()
    custom_mode_button_1.place(relx=0.05, rely=0.6)

    create_custom_mode_1 = tk.Button(color_frame, text="edit", width=1, height=1, fg="white", bg="#263D42", command=lambda: create_custom_color_window(custom_color_number=1))
    create_custom_mode_1.pack()
    create_custom_mode_1.place(relx=0.05, rely=0.6)

root.mainloop()
