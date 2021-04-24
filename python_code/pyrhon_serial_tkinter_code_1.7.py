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
custom_button_place_1 = False
custom_button_place_2 = False
custom_button_place_3 = False
custom_button_place_4 = False
custom_button_place_5 = False
custom_button_place_6 = False
custom_button_place_7 = False
custom_button_place_8 = False
custom_button_place_9 = False

device_button_place_1 = False

save_list = [[0] , [0], [0], [0], [0], [0], [0], [0], [0]]

os.system("clear")

if path.exists("valteu_lights_gui_saves.dat") == True:
    saved_data = pickle.load(open("valteu_lights_gui_saves.dat", "rb"))
    print(saved_data)
    first_row = saved_data[0]
    if len(first_row) > 1:
        custom_green_1 = first_row[0]
        custom_red_1 = first_row[1]
        custom_blue_1 = first_row[2]
        custom_brightness_1 = first_row[3]
        custom_button_place_1 = first_row[4]


    second_row = saved_data[1]
    if len(second_row) > 1:
        custom_green_2 = second_row[0]
        custom_red_2 = second_row[1]
        custom_blue_2 = second_row[2]
        custom_brightness_2 = second_row[3]
        custom_button_place_2 = second_row[4]
    
    third_row =saved_data[2]
    if len(third_row) > 1:
        custom_green_3 = third_row[0]
        custom_red_3 = third_row[1]
        custom_blue_3 = third_row[2]
        custom_brightness_3 = third_row[3]
        custom_button_place_3 = third_row[4]

    fourth_row = saved_data[3]
    if len(fourth_row) > 1:
        custom_green_4 = fourth_row[0]
        custom_red_4 = fourth_row[1]
        custom_blue_4 = fourth_row[2]
        custom_brightness_4 = fourth_row[3]
        custom_button_place_4 = fourth_row[4]

    fifth_row = saved_data[4]
    if len(fifth_row) > 1:
        custom_green_5 = fifth_row[0]
        custom_red_5 = fifth_row[1]
        custom_blue_5 = fifth_row[2]
        custom_brightness_5 = fifth_row[3]
        custom_button_place_5 = fifth_row[4]

    sixth_row = saved_data[5]
    if len(sixth_row) > 1:
        custom_green_6 = sixth_row[0]
        custom_red_6 = sixth_row[1]
        custom_blue_6 = sixth_row[2]
        custom_brightness_6 = sixth_row[3]
        custom_button_place_6 = sixth_row[4]

    seventh_row = saved_data[6]
    if len(seventh_row) > 1:
        custom_green_7 = seventh_row[0]
        custom_red_7 = seventh_row[1]
        custom_blue_7 = seventh_row[2]
        custom_brightness_7 = seventh_row[3]
        custom_button_place_7 = seventh_row[4]

    eighth_row = saved_data[7]
    if len(eighth_row) > 1:
        custom_green_8 = eighth_row[0]
        custom_red_8 = eighth_row[1]
        custom_blue_8 = eighth_row[2]
        custom_brightness_8 = eighth_row[3]
        custom_button_place_8 = eighth_row[4]

    ninth_row = saved_data[8]
    if len(ninth_row) > 1:
        custom_green_9 = ninth_row[0]
        custom_red_9 = ninth_row[1]
        custom_blue_9 = ninth_row[2]
        custom_brightness_9 = ninth_row[3]
        custom_button_place_9 = ninth_row[4]

    if len(saved_data) > 9:
        device_row = saved_data[9]
        # if len(device_row[0]) > 1:
            # device_button_place_1 = True
            # device_1 = device_row[0]

else:
    first_entry = [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0]] 
    pickle.dump(first_entry, open("valteu_lights_gui_saves.dat", "wb"))

root = Tk()

root.geometry(str(WIDTH) + 'x' + str(HEIGHT))

ArduinoSerial = serial.Serial('/dev/ttyUSB0',9600, timeout=1)
print(ArduinoSerial.name)
time.sleep(2)

data = [0, 0, 0, 0, 0, 0]

print(ArduinoSerial.readline())

def data_to_arduino(mode, green, red, blue, num_led, brightness):
    x = 1
    current_strip = str(saved_data[9][0][0])
    print(current_strip)
    while x == 1:
        data[0] = int(mode)
        data[1] = int(green)
        data[2] = int(red)
        data[3] = int(blue)
        data[4] = int(current_strip)
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
    brightness = int(brightness_slider.get())
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

    if custom_color_number == 1:
        custom_button_place_1 = True
    
        save_column = [custom_green, custom_red, custom_blue, custom_brightness, custom_button_place_1]
        saved_data[0] = save_column


        custom_mode_button_1 = tk.Button(color_frame, text="custom", width=5, height=3, bg="white", command=lambda: custom_mode(green=custom_green, red=custom_red, blue=custom_blue, brightness=custom_brightness))
        custom_mode_button_1.pack()
        custom_mode_button_1.place(relx=0.05 + (0.075 * custom_color_number-1), rely=0.6)

        create_custom_mode_1 = tk.Button(color_frame, text="edit", width=1, height=1, fg="white", bg="#263D42", command=lambda: create_custom_color_window(custom_color_number=1))
        create_custom_mode_1.pack()
        create_custom_mode_1.place(relx=0.05 + (0.075 * custom_color_number-1), rely=0.6)


    elif custom_color_number == 2:
        custom_button_place_2 = True
    
        save_column = [custom_green, custom_red, custom_blue, custom_brightness, custom_button_place_2]
        saved_data[1] = save_column

        custom_mode_button_2 = tk.Button(color_frame, text="custom", width=5, height=3, bg="white", command=lambda: custom_mode(green=custom_green, red=custom_red, blue=custom_blue, brightness=custom_brightness))
        custom_mode_button_2.pack()
        custom_mode_button_2.place(relx=0.05 + (0.075 * custom_color_number-1), rely=0.6)

        create_custom_mode_2 = tk.Button(color_frame, text="edit", width=1, height=1, fg="white", bg="#263D42", command=lambda: create_custom_color_window(custom_color_number=2))
        create_custom_mode_2.pack()
        create_custom_mode_2.place(relx=0.05 + (0.075 * custom_color_number-1), rely=0.6)


    elif custom_color_number == 3:
        custom_button_place_3 = True
    
        save_column = [custom_green, custom_red, custom_blue, custom_brightness, custom_button_place_3]
        saved_data[2] = save_column

        custom_mode_button_3 = tk.Button(color_frame, text="custom", width=5, height=3, bg="white", command=lambda: custom_mode(green=custom_green, red=custom_red, blue=custom_blue, brightness=custom_brightness))
        custom_mode_button_3.pack()
        custom_mode_button_3.place(relx=0.05 + (0.075 * custom_color_number-1), rely=0.6)

        create_custom_mode_3 = tk.Button(color_frame, text="edit", width=1, height=1, fg="white", bg="#263D42", command=lambda: create_custom_color_window(custom_color_number=3))
        create_custom_mode_3.pack()
        create_custom_mode_3.place(relx=0.05 + (0.075 * custom_color_number-1), rely=0.6)


    elif custom_color_number == 4:
        custom_button_place_4 = True
    
        save_column = [custom_green, custom_red, custom_blue, custom_brightness, custom_button_place_4]
        saved_data[3] = save_column

        custom_mode_button_4 = tk.Button(color_frame, text="custom", width=5, height=3, bg="white", command=lambda: custom_mode(green=custom_green, red=custom_red, blue=custom_blue, brightness=custom_brightness))
        custom_mode_button_4.pack()
        custom_mode_button_4.place(relx=0.05 + (0.075 * custom_color_number-1), rely=0.6)

        create_custom_mode_4 = tk.Button(color_frame, text="edit", width=1, height=1, fg="white", bg="#263D42", command=lambda: create_custom_color_window(custom_color_number=4))
        create_custom_mode_4.pack()
        create_custom_mode_4.place(relx=0.05 + (0.075 * custom_color_number-1), rely=0.6)


    elif custom_color_number == 5:
        custom_button_place_5 = True
    
        save_column = [custom_green, custom_red, custom_blue, custom_brightness, custom_button_place_5]
        saved_data[4] = save_column

        custom_mode_button_5 = tk.Button(color_frame, text="custom", width=5, height=3, bg="white", command=lambda: custom_mode(green=custom_green, red=custom_red, blue=custom_blue, brightness=custom_brightness))
        custom_mode_button_5.pack()
        custom_mode_button_5.place(relx=0.05 + (0.075 * custom_color_number-1), rely=0.6)

        create_custom_mode_5 = tk.Button(color_frame, text="edit", width=1, height=1, fg="white", bg="#263D42", command=lambda: create_custom_color_window(custom_color_number=5))
        create_custom_mode_5.pack()
        create_custom_mode_5.place(relx=0.05 + (0.075 * custom_color_number-1), rely=0.6)


    elif custom_color_number == 6:
        custom_button_place_6 = True
    
        save_column = [custom_green, custom_red, custom_blue, custom_brightness, custom_button_place_6]
        saved_data[5] = save_column

        custom_mode_button_6 = tk.Button(color_frame, text="custom", width=5, height=3, bg="white", command=lambda: custom_mode(green=custom_green, red=custom_red, blue=custom_blue, brightness=custom_brightness))
        custom_mode_button_6.pack()
        custom_mode_button_6.place(relx=0.05 + (0.075 * custom_color_number-1), rely=0.6)

        create_custom_mode_6 = tk.Button(color_frame, text="edit", width=1, height=1, fg="white", bg="#263D42", command=lambda: create_custom_color_window(custom_color_number=6))
        create_custom_mode_6.pack()
        create_custom_mode_6.place(relx=0.05 + (0.075 * custom_color_number-1), rely=0.6)


    elif custom_color_number == 7:
        custom_button_place_7 = True
    
        save_column = [custom_green, custom_red, custom_blue, custom_brightness, custom_button_place_7]
        saved_data[6] = save_column

        custom_mode_button_7 = tk.Button(color_frame, text="custom", width=5, height=3, bg="white", command=lambda: custom_mode(green=custom_green, red=custom_red, blue=custom_blue, brightness=custom_brightness))
        custom_mode_button_7.pack()
        custom_mode_button_7.place(relx=0.05 + (0.075 * custom_color_number-1), rely=0.6)

        create_custom_mode_7 = tk.Button(color_frame, text="edit", width=1, height=1, fg="white", bg="#263D42", command=lambda: create_custom_color_window(custom_color_number=7))
        create_custom_mode_7.pack()
        create_custom_mode_7.place(relx=0.05 + (0.075 * custom_color_number-1), rely=0.6)


    elif custom_color_number == 8:
        custom_button_place_8 = True
    
        save_column = [custom_green, custom_red, custom_blue, custom_brightness, custom_button_place_8]
        saved_data[7] = save_column

        custom_mode_button_8 = tk.Button(color_frame, text="custom", width=5, height=3, bg="white", command=lambda: custom_mode(green=custom_green, red=custom_red, blue=custom_blue, brightness=custom_brightness))
        custom_mode_button_8.pack()
        custom_mode_button_8.place(relx=0.05 + (0.075 * custom_color_number-1), rely=0.6)

        create_custom_mode_8 = tk.Button(color_frame, text="edit", width=1, height=1, fg="white", bg="#263D42", command=lambda: create_custom_color_window(custom_color_number=8))
        create_custom_mode_8.pack()
        create_custom_mode_8.place(relx=0.05 + (0.075 * custom_color_number-1), rely=0.6)


    elif custom_color_number == 9:
        custom_button_place_9 = True
    
        save_column = [custom_green, custom_red, custom_blue, custom_brightness, custom_button_place_9]
        saved_data[8] = save_column

        custom_mode_button_9 = tk.Button(color_frame, text="custom", width=5, height=3, bg="white", command=lambda: custom_mode(green=custom_green, red=custom_red, blue=custom_blue, brightness=custom_brightness))
        custom_mode_button_9.pack()
        custom_mode_button_9.place(relx=0.05 + (0.075 * custom_color_number-1), rely=0.6)

        create_custom_mode_9 = tk.Button(color_frame, text="edit", width=1, height=1, fg="white", bg="#263D42", command=lambda: create_custom_color_window(custom_color_number=9))
        create_custom_mode_9.pack()
        create_custom_mode_9.place(relx=0.05 + (0.075 * custom_color_number-1), rely=0.6)

    pickle.dump(saved_data, open("valteu_lights_gui_saves.dat", "wb"))

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

def add_device():
    global entry_device_number, entry_device_len_led
    add_device_window = tk.Toplevel(device_frame, width=int(WIDTH/3), height=int(HEIGHT/3))
    entry_device_number = Entry(add_device_window, width=3)
    entry_device_number.pack()
    entry_device_number.place(relx=0.25, rely=0.1)

    entry_device_len_led = Entry(add_device_window, width=3)
    entry_device_len_led.pack()
    entry_device_len_led.place(relx=0.25, rely=0.3)

    Save_device = tk.Button(add_device_window, text="Save", width=5, height=3, fg="white", bg="#263D42",command=save_device)
    Save_device.pack()
    Save_device.place(relx=0.85, rely=0.8)

def save_device():
    device_num = entry_device_number.get()
    device_led_len = entry_device_len_led.get()
    device = [[device_num, device_led_len]]
    if not saved_data:
        if len(saved_data) < 10:
            saved_data.append(device)
        else:
            saved_data[9] = device
        print(saved_data)

    device_button_place_1 = True
    pickle.dump(saved_data, open("valteu_lights_gui_saves.dat", "wb"))

def edit_device():
    global entry_device_number

    edit_device_window = tk.Toplevel(device_frame, width=int(WIDTH/3), height=int(HEIGHT/3))
    entry_device_number = Entry(edit_device_window, width=3)
    entry_device_number.pack()
    entry_device_number.place(relx=0.25, rely=0.1)

def current_device(num_device):
    current_num_led = saved_data[9][num_device -1][1]
    current_num_led_strip = saved_data[9][num_device -1]
    return current_num_led, current_num_led_strip

def choose_device():
    global entry_device_number, entry_device_len_led
    choose_device_window = tk.Toplevel(device_frame, width=int(WIDTH/3), height=int(HEIGHT/3))
    entry_device_number = Entry(choose_device_window, width=3)
    entry_device_number.pack()
    entry_device_number.place(relx=0.25, rely=0.1)
    Save_device = tk.Button(choose_device_window, text="Save", width=5, height=3, fg="white", bg="#263D42",command=save_chosen_device)
    Save_device.pack()
    Save_device.place(relx=0.85, rely=0.8)


def save_chosen_device():
    saved_data[9] = entry_device_number.get()
    pickle.dump(saved_data, open("valteu_lights_gui_saves.dat", "wb"))

def select_device():
    devicename = device_listbox.get(ANCHOR)
    if device_list[0] == devicename:
        device_num = 0
        device_led_len = 12
        device = [[device_num, device_led_len]]
        if len(saved_data) < 10:
            saved_data.append(device)
        else:
            saved_data[9] = device
        print(device)
        pickle.dump(saved_data, open("valteu_lights_gui_saves.dat", "wb"))
    elif device_list[1] == devicename:
        device_2_exists = True
        device_num = 1
        device_led_len = 12
        device = [[device_num, device_led_len]]
        if len(saved_data) < 10:
            saved_data.append(device)
        else:
            saved_data[9] = device
        print(device)
        pickle.dump(saved_data, open("valteu_lights_gui_saves.dat", "wb"))
    elif device_list[2] == devicename:
        device_3_exists = True
        device_num = 2
        device_led_len = 12
        device = [[device_num, device_led_len]]
        if len(saved_data) < 10:
            saved_data.append(device)
        else:
            saved_data[9] = device
        print(device)
        pickle.dump(saved_data, open("valteu_lights_gui_saves.dat", "wb"))

    pickle.dump(saved_data, open("valteu_lights_gui_saves.dat", "wb"))


image1 = Image.open("//home//valteu//programming//lights//light_gui_images//background_gui.png")
test = ImageTk.PhotoImage(image1)


label1 = tk.Label(image=test)
label1.image = test

label1.place(x=-1, y=-1)

profile_frame = tk.Frame(root, bg="#9e0025")
profile_frame.place(relwidth=0.25, relheight=0.7, relx=0.05, rely=0.2)

profile_frame_headline = tk.Label(profile_frame, text="Profiles", height=1, width=int(WIDTH*0.3), padx=55, pady=2, bg="#9e0025", fg="white",  borderwidth=3)
profile_frame_headline.config(font=("Arial", 24), state=DISABLED, anchor=CENTER, highlightbackground = "red", highlightcolor= "red", fg="white")
profile_frame_headline.pack()

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
headline.place(relx=0.36, rely=0.05)

device_frame = tk.Frame(root, bg="#9e0025")
device_frame.place(relwidth=0.6, relheight=0.39, relx=0.35, rely=0.2)

device_listbox = Listbox(device_frame)
device_listbox.pack(pady = 0.4)

device_list = ["Device 1", "Device 2", "Device 3"]
for item in device_list:
    device_listbox.insert(END, item)

SelectDevice = tk.Button(device_frame, text="Select", width=5, height=1, bg="gold", fg="black", command=select_device)
SelectDevice.pack()
SelectDevice.place(relx=0.5, rely=0.15)

AddDevice_1 = tk.Button(device_frame, text="Add", width=5, height=1, bg="gold", fg="black", command=add_device)
AddDevice_1.pack()
AddDevice_1.place(relx=0.0125, rely=0.15)

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

if custom_button_place_1 == False:
    create_custom_mode_1 = tk.Button(color_frame, text="custom", width=5, height=3, fg="white", bg="#263D42", command=lambda: create_custom_color_window(custom_color_number=1))
    create_custom_mode_1.pack()
    create_custom_mode_1.place(relx=0.05, rely=0.6)
else:
    custom_mode_button_1 = tk.Button(color_frame, text="custom", width=5, height=3, bg="white", command=lambda: custom_mode(green=custom_green_1, red=custom_red_1, blue=custom_blue_1, brightness=custom_brightness_1))
    custom_mode_button_1.pack()
    custom_mode_button_1.place(relx=0.05, rely=0.6)

    edit_custom_mode_1 = tk.Button(color_frame, text="edit", width=1, height=1, fg="white", bg="#263D42", command=lambda: create_custom_color_window(custom_color_number=1))
    edit_custom_mode_1.pack()
    edit_custom_mode_1.place(relx=0.05, rely=0.6)

if custom_button_place_2 == False:
    create_custom_mode_2 = tk.Button(color_frame, text="custom", width=5, height=3, fg="white", bg="#263D42", command=lambda: create_custom_color_window(custom_color_number=2))
    create_custom_mode_2.pack()
    create_custom_mode_2.place(relx=0.125, rely=0.6)
else:
    custom_mode_button_2 = tk.Button(color_frame, text="custom", width=5, height=3, bg="white", command=lambda: custom_mode(green=custom_green_2, red=custom_red_2, blue=custom_blue_2, brightness=custom_brightness_2))
    custom_mode_button_2.pack()
    custom_mode_button_2.place(relx=0.125, rely=0.6)

    edit_custom_mode_2 = tk.Button(color_frame, text="edit", width=1, height=1, fg="white", bg="#263D42", command=lambda: create_custom_color_window(custom_color_number=2))
    edit_custom_mode_2.pack()
    edit_custom_mode_2.place(relx=0.125, rely=0.6)

if custom_button_place_3 == False:
    create_custom_mode_3 = tk.Button(color_frame, text="custom", width=5, height=3, fg="white", bg="#263D42", command=lambda: create_custom_color_window(custom_color_number=3))
    create_custom_mode_3.pack()
    create_custom_mode_3.place(relx=0.2, rely=0.6)
else:
    custom_mode_button_3 = tk.Button(color_frame, text="custom", width=5, height=3, bg="white", command=lambda: custom_mode(green=custom_green_3, red=custom_red_3, blue=custom_blue_3, brightness=custom_brightness_3))
    custom_mode_button_3.pack()
    custom_mode_button_3.place(relx=0.2, rely=0.6)

    edit_custom_mode_3 = tk.Button(color_frame, text="edit", width=1, height=1, fg="white", bg="#263D42", command=lambda: create_custom_color_window(custom_color_number=3))
    edit_custom_mode_3.pack()
    edit_custom_mode_3.place(relx=0.2, rely=0.6)

if custom_button_place_4 == False:
    create_custom_mode_4 = tk.Button(color_frame, text="custom", width=5, height=3, fg="white", bg="#263D42", command=lambda: create_custom_color_window(custom_color_number=4))
    create_custom_mode_4.pack()
    create_custom_mode_4.place(relx=0.275, rely=0.6)
else:
    custom_mode_button_4 = tk.Button(color_frame, text="custom", width=5, height=3, bg="white", command=lambda: custom_mode(green=custom_green_4, red=custom_red_4, blue=custom_blue_4, brightness=custom_brightness_4))
    custom_mode_button_4.pack()
    custom_mode_button_4.place(relx=0.275, rely=0.6)

    edit_custom_mode_4 = tk.Button(color_frame, text="edit", width=1, height=1, fg="white", bg="#263D42", command=lambda: create_custom_color_window(custom_color_number=4))
    edit_custom_mode_4.pack()
    edit_custom_mode_4.place(relx=0.275, rely=0.6)

if custom_button_place_5 == False:
    create_custom_mode_5 = tk.Button(color_frame, text="custom", width=5, height=3, fg="white", bg="#263D42", command=lambda: create_custom_color_window(custom_color_number=5))
    create_custom_mode_5.pack()
    create_custom_mode_5.place(relx=0.35, rely=0.6)
else:
    custom_mode_button_5 = tk.Button(color_frame, text="custom", width=5, height=3, bg="white", command=lambda: custom_mode(green=custom_green_5, red=custom_red_5, blue=custom_blue_5, brightness=custom_brightness_5))
    custom_mode_button_5.pack()
    custom_mode_button_5.place(relx=0.35, rely=0.6)

    edit_custom_mode_5 = tk.Button(color_frame, text="edit", width=1, height=1, fg="white", bg="#263D42", command=lambda: create_custom_color_window(custom_color_number=5))
    edit_custom_mode_5.pack()
    edit_custom_mode_5.place(relx=0.35, rely=0.6)

if custom_button_place_6 == False:
    create_custom_mode_6 = tk.Button(color_frame, text="custom", width=5, height=3, fg="white", bg="#263D42", command=lambda: create_custom_color_window(custom_color_number=6))
    create_custom_mode_6.pack()
    create_custom_mode_6.place(relx=0.425, rely=0.6)
else:
    custom_mode_button_6 = tk.Button(color_frame, text="custom", width=5, height=3, bg="white", command=lambda: custom_mode(green=custom_green_6, red=custom_red_6, blue=custom_blue_6, brightness=custom_brightness_6))
    custom_mode_button_6.pack()
    custom_mode_button_6.place(relx=0.425, rely=0.6)

    edit_custom_mode_6 = tk.Button(color_frame, text="edit", width=1, height=1, fg="white", bg="#263D42", command=lambda: create_custom_color_window(custom_color_number=6))
    edit_custom_mode_6.pack()
    edit_custom_mode_6.place(relx=0.425, rely=0.6)

if custom_button_place_7 == False:
    create_custom_mode_7 = tk.Button(color_frame, text="custom", width=5, height=3, fg="white", bg="#263D42", command=lambda: create_custom_color_window(custom_color_number=7))
    create_custom_mode_7.pack()
    create_custom_mode_7.place(relx=0.5, rely=0.6)
else:
    custom_mode_button_7 = tk.Button(color_frame, text="custom", width=5, height=3, bg="white", command=lambda: custom_mode(green=custom_green_7, red=custom_red_7, blue=custom_blue_7, brightness=custom_brightness_7))
    custom_mode_button_7.pack()
    custom_mode_button_7.place(relx=0.5, rely=0.6)

    edit_custom_mode_7 = tk.Button(color_frame, text="edit", width=1, height=1, fg="white", bg="#263D42", command=lambda: create_custom_color_window(custom_color_number=7))
    edit_custom_mode_7.pack()
    edit_custom_mode_7.place(relx=0.5, rely=0.6)

if custom_button_place_8 == False:
    create_custom_mode_8 = tk.Button(color_frame, text="custom", width=5, height=3, fg="white", bg="#263D42", command=lambda: create_custom_color_window(custom_color_number=8))
    create_custom_mode_8.pack()
    create_custom_mode_8.place(relx=0.575, rely=0.6)
else:
    custom_mode_button_8 = tk.Button(color_frame, text="custom", width=5, height=3, bg="white", command=lambda: custom_mode(green=custom_green_8, red=custom_red_8, blue=custom_blue_8, brightness=custom_brightness_8))
    custom_mode_button_8.pack()
    custom_mode_button_8.place(relx=0.575, rely=0.6)

    edit_custom_mode_8 = tk.Button(color_frame, text="edit", width=1, height=1, fg="white", bg="#263D42", command=lambda: create_custom_color_window(custom_color_number=8))
    edit_custom_mode_8.pack()
    edit_custom_mode_8.place(relx=0.575, rely=0.6)

if custom_button_place_9 == False:
    create_custom_mode_9 = tk.Button(color_frame, text="custom", width=5, height=3, fg="white", bg="#263D42", command=lambda: create_custom_color_window(custom_color_number=9))
    create_custom_mode_9.pack()
    create_custom_mode_9.place(relx=0.65, rely=0.6)
else:
    custom_mode_button_9 = tk.Button(color_frame, text="custom", width=5, height=3, bg="white", command=lambda: custom_mode(green=custom_green_9, red=custom_red_9, blue=custom_blue_9, brightness=custom_brightness_9))
    custom_mode_button_9.pack()
    custom_mode_button_9.place(relx=0.65, rely=0.6)

    edit_custom_mode_9 = tk.Button(color_frame, text="edit", width=1, height=1, fg="white", bg="#263D42", command=lambda: create_custom_color_window(custom_color_number=9))
    edit_custom_mode_9.pack()
    edit_custom_mode_9.place(relx=0.65, rely=0.6)

# if device_button_place_1 == False:
AddDevice_1 = tk.Button(device_frame, text="Add", width=5, height=1, bg="gold", fg="black", command=choose_device)
AddDevice_1.pack()
AddDevice_1.place(relx=0.0125, rely=0.15)
# else:
#     Device_1 = tk.Button(device_frame, text="Device 1", width=5, height=3, bg="white", command=lambda: current_device(num_device=1))
#     Device_1.pack()
#     Device_1.place(relx=0.0125, rely=0.15)

#     edit_device_1 = tk.Button(device_frame, text="edit", width=1, height=1, fg="white", bg="#263D42", command=edit_device)
#     edit_device_1.pack()
#     edit_device_1.place(relx=0.0125, rely=0.15)


root.mainloop()
