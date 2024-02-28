import customtkinter 
import tempfile, base64, zlib
from PIL import Image, ImageTk
import random
import string
import pyperclip
from tkinter import ttk
import tkinter as tk
import os
from pathlib import Path
from CTkMessagebox import CTkMessagebox

number = []
for i in range(1,38):
    number.append(i)

special_characters_list = string.punctuation
letters = string.ascii_lowercase 
letters_upper = string.ascii_uppercase
number = string.digits


ICON = zlib.decompress(base64.b64decode('eJxjYGAEQgEBBiDJwZDBy'
    'sAgxsDAoAHEQCEGBQaIOAg4sDIgACMUj4JRMApGwQgF/ykEAFXxQRc='))

_, ICON_PATH = tempfile.mkstemp()
with open(ICON_PATH, 'wb') as icon_file:
    icon_file.write(ICON)


screen = customtkinter.CTk()
screen.title("Modern RPG")
screen.geometry("370x500")
screen._set_appearance_mode("dark")
screen.resizable(False,False)
screen.iconbitmap(default=ICON_PATH)

slider_value = 7
special_value = "on"
upper_value = "on"
number_value = "on"
chosen_password = ""
def generate_password():
    global chosen_password
    copy_button.configure(text=" Copy  ")
    password_random_generater = []

    if special_value == "on":
        password_random_generater.extend(special_characters_list)
        password_random_generater.extend(letters)
    elif special_value == "off":
        if letters not in password_random_generater:
            password_random_generater.extend(letters)
    if upper_value == "on":
        if letters_upper not in password_random_generater:
            password_random_generater.extend(letters_upper)
        if letters not in password_random_generater:
            password_random_generater.extend(letters)
    elif upper_value == "off":
        if letters not in password_random_generater:
            password_random_generater.extend(letters)
    if number_value == "on":
        if number not in password_random_generater:
            password_random_generater.extend(number)
        if letters not in password_random_generater:
            password_random_generater.extend(letters)
    elif number_value == "off":
        if letters not in password_random_generater:
            password_random_generater.extend(letters)

    chosen_password = ''.join(random.choice(password_random_generater) for _ in range(slider_value))
    if len(chosen_password) >30:
        pswd_edited = chosen_password[:30]
        password_show_label.configure(text=pswd_edited)
    else:
        password_show_label.configure(text=chosen_password)
    
def copy_text_to_clipboard():
    pyperclip.copy(chosen_password)
    copy_button.configure(text="Copied")

font_1 = ("Arial",105)
font_2 = ("Arial", 50,"bold")
font_3 = ("Arial", 20)
font_4 = ("Arial",15,"bold")
font_5 = ("Arial",15)


logo_frame = customtkinter.CTkFrame(screen, width=350,
                               height=160,
                               fg_color="gray16",
                               border_width=2,
                               border_color="gray25",
                               corner_radius=20)
logo_frame.place(x=8,y=8)

monkey_logo = customtkinter.CTkLabel(screen,text="🫣", font=font_1, text_color="#72B3F9",bg_color="gray16")
monkey_logo.place(x=180, y=10)
dont_panic = customtkinter.CTkLabel(screen,text="Don't", font=font_2, text_color="#72B3F9",bg_color="gray16")
dont_panic.place(x=10, y=20)
dont_panic_1 = customtkinter.CTkLabel(screen,text="panic", font=font_2, text_color="#72B3F9",bg_color="gray16")
dont_panic_1.place(x=30, y=70)
dont_panic_1 = customtkinter.CTkLabel(screen,text="i don't look your password ehehe", font=font_3, text_color="#72B3F9",bg_color="gray16")
dont_panic_1.place(x=50, y=130)

show_text_frame= customtkinter.CTkFrame(screen, width=250,
                               height=30,
                               fg_color="white",
                               border_width=2,
                               border_color="gray40",
                               bg_color="gray15",
                               corner_radius=20)
show_text_frame.place(x=20, y=185)

password_show_label = customtkinter.CTkLabel(screen, text="",text_color="black",fg_color="white",height=15)
password_show_label.place(x=35,y=190)

copy_button = customtkinter.CTkButton(master=screen,
                                 width=30,
                                 height=30,
                                 border_color="light blue",
                                 border_width=2,
                                 corner_radius=20,
                                 fg_color="#72B3F9",
                                 bg_color="gray15",
                                 text=" Copy  ",
                                 text_color="white",
                                 hover_color="light blue",
                                 font=font_4,
                                 command=copy_text_to_clipboard)

copy_button.place(x=280,y=185)


slider_frame = customtkinter.CTkFrame(screen, width=200,
                               height=60,
                               fg_color="gray20",
                               border_width=2,
                               border_color="gray40",
                               bg_color="gray15",
                               corner_radius=15)

slider_frame.place(x= 12, y=245)

current_value = customtkinter.DoubleVar(value=7)
old_slider_value=0

s = ttk.Style()
s.theme_use('clam')
s.configure("green.Horizontal.TProgressbar", foreground='green', background='green')
strong_password = ttk.Progressbar(screen, orient='vertical', mode='determinate',length=225,value=64,style="green.Horizontal.TProgressbar")
strong_password.place(x=290, y=310)

def get_current_value():
    global slider_value,old_slider_value,strong_password
    old_value = old_slider_value
    slider_value = int('{: .0f}'.format(current_value.get()))
    old_slider_value = slider_value
    if slider_value > old_value:
        slider_value_math = slider_value-old_value  
        slider_value_math *= 1
        strong_password['value'] += slider_value_math
        if strong_password["value"]<40:
            s.configure("red.Horizontal.TProgressbar", foreground='red', background='red')
            strong_password.configure(style="red.Horizontal.TProgressbar")
        elif 70 > strong_password["value"] > 40 :
            s.configure("yellow.Horizontal.TProgressbar", foreground='yellow', background='yellow')
            strong_password.configure(style="yellow.Horizontal.TProgressbar")
        elif  strong_password["value"] >= 70:
            s.configure("green.Horizontal.TProgressbar", foreground='green', background='green')
            strong_password.configure(style="green.Horizontal.TProgressbar")
        
    elif slider_value < old_value:
        old_value_math = old_value - slider_value   
        old_value_math*=1
        strong_password['value'] -= old_value_math
        if strong_password["value"]<40:
            s.configure("red.Horizontal.TProgressbar", foreground='red', background='red')
            strong_password.configure(style="red.Horizontal.TProgressbar")
        elif 70 > strong_password["value"] > 40 :
            s.configure("yellow.Horizontal.TProgressbar", foreground='yellow', background='yellow')
            strong_password.configure(style="yellow.Horizontal.TProgressbar")
        elif  strong_password["value"] >= 70:
            s.configure("green.Horizontal.TProgressbar", foreground='green', background='green')
            strong_password.configure(style="green.Horizontal.TProgressbar")      
    else:
        pass

    return '{: .0f}'.format(current_value.get())


def slider_changed(event):
    value_of_slider.configure(text=f"length of password:{get_current_value()}")

password_length_scroll = customtkinter.CTkSlider(screen, from_=7, to=36,variable=current_value,command=slider_changed,width=180,bg_color="gray20")
password_length_scroll.place(x=20,y=250)
password_length = get_current_value()
print(password_length)

value_of_slider = customtkinter.CTkLabel(screen,text=f"length of password:{get_current_value()}",font=font_4,bg_color="gray20")
value_of_slider.place(x=25,y=270)

switch_frame = customtkinter.CTkFrame(screen, width=200,
                               height=110,
                               fg_color="gray20",
                               border_width=2,
                               border_color="gray40",
                               bg_color="gray15",
                               corner_radius=15)

switch_frame.place(x=10,y=320)

captial_and_special_label = customtkinter.CTkLabel(screen,text="----------------------------------", bg_color="gray20",text_color="gray40")
captial_and_special_label.place(x=40,y=344)

captial_and_number_label = customtkinter.CTkLabel(screen,text="----------------------------------", bg_color="gray20",text_color="gray40")
captial_and_number_label.place(x=40,y=378)

def get_special_characters():
    global special_value
    special_value=special_characters_var.get()
    if special_value == "on":
        strong_password['value'] += 20
        if strong_password["value"]<40:
            s.configure("red.Horizontal.TProgressbar", foreground='red', background='red')
            strong_password.configure(style="red.Horizontal.TProgressbar")
        elif 70 > strong_password["value"] > 40 :
            s.configure("yellow.Horizontal.TProgressbar", foreground='yellow', background='yellow')
            strong_password.configure(style="yellow.Horizontal.TProgressbar")
        elif  strong_password["value"] >= 70:
            s.configure("green.Horizontal.TProgressbar", foreground='green', background='green')
            strong_password.configure(style="green.Horizontal.TProgressbar")
    else:
        strong_password['value'] -= 20
        if strong_password["value"]<40:
            s.configure("red.Horizontal.TProgressbar", foreground='red', background='red')
            strong_password.configure(style="red.Horizontal.TProgressbar")
        elif 70 > strong_password["value"] > 40 :
            s.configure("yellow.Horizontal.TProgressbar", foreground='yellow', background='yellow')
            strong_password.configure(style="yellow.Horizontal.TProgressbar")
        elif  strong_password["value"] >= 70:
            s.configure("green.Horizontal.TProgressbar", foreground='green', background='green')
            strong_password.configure(style="green.Horizontal.TProgressbar")


special_characters_var = customtkinter.StringVar(value="on")

special_characters = customtkinter.CTkSwitch(screen ,text="Special characters",variable=special_characters_var, onvalue="on", offvalue="off",command=get_special_characters,font=font_4,bg_color="gray20")
special_characters.place(x=20,y=330)


def get_upper_characters():
    global upper_value
    upper_value = upper_charascters_var.get()
    if upper_value == "on":
        strong_password['value'] += 20
        if strong_password["value"]<40:
            s.configure("red.Horizontal.TProgressbar", foreground='red', background='red')
            strong_password.configure(style="red.Horizontal.TProgressbar")
        elif 70 > strong_password["value"] > 40 :
            s.configure("yellow.Horizontal.TProgressbar", foreground='yellow', background='yellow')
            strong_password.configure(style="yellow.Horizontal.TProgressbar")
        elif  strong_password["value"] >= 70:
            s.configure("green.Horizontal.TProgressbar", foreground='green', background='green')
            strong_password.configure(style="green.Horizontal.TProgressbar")
    else:
        strong_password['value'] -= 20
        if strong_password["value"]<40:
            s.configure("red.Horizontal.TProgressbar", foreground='red', background='red')
            strong_password.configure(style="red.Horizontal.TProgressbar")
        elif 70 > strong_password["value"] > 40 :
            s.configure("yellow.Horizontal.TProgressbar", foreground='yellow', background='yellow')
            strong_password.configure(style="yellow.Horizontal.TProgressbar")
        elif  strong_password["value"] >= 70:
            s.configure("green.Horizontal.TProgressbar", foreground='green', background='green')
            strong_password.configure(style="green.Horizontal.TProgressbar")

upper_charascters_var = customtkinter.StringVar(value="on")

upper_charascters = customtkinter.CTkSwitch(screen ,text="Capital letters",variable=upper_charascters_var, onvalue="on", offvalue="off",command=get_upper_characters,font=font_4,width=5,bg_color="gray20")
upper_charascters.place(x=20,y=365)


def get_number_characters():
    global number_value 
    number_value = number_charascters_var.get()
    if number_value == "on":
        strong_password['value'] += 20
        if strong_password["value"]<40:
            s.configure("red.Horizontal.TProgressbar", foreground='red', background='red')
            strong_password.configure(style="red.Horizontal.TProgressbar")
        elif 70 > strong_password["value"] > 40 :
            s.configure("yellow.Horizontal.TProgressbar", foreground='yellow', background='yellow')
            strong_password.configure(style="yellow.Horizontal.TProgressbar")
        elif  strong_password["value"] >= 70:
            s.configure("green.Horizontal.TProgressbar", foreground='green', background='green')
            strong_password.configure(style="green.Horizontal.TProgressbar")
    else:
        strong_password['value'] -= 20
        if strong_password["value"]<40:
            s.configure("red.Horizontal.TProgressbar", foreground='red', background='red')
            strong_password.configure(style="red.Horizontal.TProgressbar")
        elif 70 > strong_password["value"] > 40 :
            s.configure("yellow.Horizontal.TProgressbar", foreground='yellow', background='yellow')
            strong_password.configure(style="yellow.Horizontal.TProgressbar")
        elif  strong_password["value"] >= 70:
            s.configure("green.Horizontal.TProgressbar", foreground='green', background='green')
            strong_password.configure(style="green.Horizontal.TProgressbar")

number_charascters_var = customtkinter.StringVar(value="on")

number_charascters = customtkinter.CTkSwitch(screen ,text="Number characters",variable=number_charascters_var, onvalue="on", offvalue="off",command=get_number_characters,font=font_4,width=5,bg_color="gray20")
number_charascters.place(x=20,y=395)


password_button = customtkinter.CTkButton(master=screen,
                                 width=50,
                                 height=30,
                                 border_color="light blue",
                                 border_width=2,
                                 corner_radius=20,
                                 fg_color="#72B3F9",
                                 bg_color="gray15",
                                 text="Generate password",
                                 text_color="white",
                                 hover_color="light blue",
                                 font=font_4,
                                 command=generate_password)

password_button.place(x=20,y=450)


def encyption_screen():

    escreen_frame =customtkinter.CTkFrame(screen, width=380,
                               height=280,
                               fg_color="gray14",
                               bg_color="gray14",
                               corner_radius=0)
    escreen_frame.place(x=0,y=230)
    tabview = customtkinter.CTkTabview(master=escreen_frame)

    tabview.add("Cryption")  # add tab at the end
    tabview.add("Decrption")  # add tab at the end
    tabview.set("Cryption")  # set currently visible tab

    def generate_cryption():
        name_passwrod = name_of_password.get()
        password_cryption = password_for_ctyption.get()
        note_password = note_for_password.get()
        if name_passwrod == "":
            name_of_password.configure(border_color="red",placeholder_text="Name of password")
        elif password_cryption == "":
            password_for_ctyption.configure(border_color="red",placeholder_text="Password for decryption")
        
        elif len(chosen_password) == 0 :
             CTkMessagebox(title="Warning!",icon="warning", message="Generate The Password", option_1="OK",width=400,height=150, font=font_4,button_color="#72B3F9",title_color="#72B3F9",button_hover_color="light blue",sound="ON", button_width= 10)
        else:
            def key_encode(key,clear):
                enc = []
                for i in range(len(clear)):
                    key_c = key[i % len(key)]
                    enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
                    enc.append(enc_c)
                return base64.urlsafe_b64encode("".join(enc).encode()).decode()
            
            password_encypted = key_encode(password_cryption,chosen_password)

            try:

                path_to_download = os.path.join(Path.home(), 'Desktop')
                with open(f"{path_to_download}/mysecret.txt", "a") as data_file:
                    data_file.write(f'\n--------\nFor: {name_passwrod}\nDescription: {note_password}\nPassword: {password_encypted}\n--------\n')
            except FileNotFoundError:
                with open(f"{path_to_download}/mysecret.txt", "w") as data_file:
                    data_file.write(f'\n{password_encypted}')
            
            save_cryption.configure(text="Saved!")
            name_of_password.delete(0,"end")
            password_for_ctyption.delete(0,"end")
            note_for_password.delete(0,"end")

    def decode(key, enc):
        dec = []
        enc = base64.urlsafe_b64decode(enc).decode()
        for i in range(len(enc)):
            key_c = key[i % len(key)]
            dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
            dec.append(dec_c)
        return "".join(dec)


    name_of_password =  customtkinter.CTkEntry(tabview.tab("Cryption"),placeholder_text="Name of password",corner_radius=15,width=250,height=30,font=font_5)
    name_of_password.place(x=17,y=15)
    password_for_ctyption =  customtkinter.CTkEntry(tabview.tab("Cryption"),placeholder_text="Password for decryption",corner_radius=15,width=250,height=30,font=font_5)
    password_for_ctyption.place(x=17,y=55)
    note_for_password =  customtkinter.CTkEntry(tabview.tab("Cryption"),placeholder_text="Note for password (optional)",corner_radius=15,width=250,height=30,font=font_5)
    note_for_password.place(x=17,y=95)
    save_cryption = customtkinter.CTkButton(tabview.tab("Cryption"),
                                 width=50,
                                 height=30,
                                 border_color="light blue",
                                 border_width=2,
                                 corner_radius=13,
                                 fg_color="#72B3F9",
                                 bg_color="gray17",
                                 text="Save",
                                 text_color="white",
                                 hover_color="light blue",
                                 font=font_4,
                                 command=generate_cryption)
    save_cryption.place(x=60,y=150)

    def destroy_frame():
         escreen_frame.destroy()

    back_button =customtkinter.CTkButton(tabview.tab("Cryption"),width=50,
                                 height=30,
                                 border_color="light blue",
                                 border_width=2,
                                 corner_radius=13,
                                 fg_color="#72B3F9",
                                 bg_color="gray17",
                                 text="Back",
                                 text_color="white",
                                 hover_color="light blue",
                                 font=font_4,
                                 command=destroy_frame)
    back_button.place(x=150,y=150)

    encryption_text = customtkinter.CTkEntry(tabview.tab("Decrption"),placeholder_text="Enter encrypted text",corner_radius=15,width=250,height=30,font=font_5)
    encryption_text.place(x=17,y=15)
    encryption_password = customtkinter.CTkEntry(tabview.tab("Decrption"),placeholder_text="Enter Password",corner_radius=15,width=250,height=30,font=font_5)
    encryption_password.place(x=17,y=55)

    def copy_text_to_clipboard_password():
        try:
            pyperclip.copy(decode_password)
            copy_password_in_frame.configure(text="Copied")
        except:
            troll_message = "OOOO Meeeen"
            pyperclip.copy(troll_message)
            copy_password_in_frame.configure(text="Copied")

    def decode_function():
        global decode_password
        enc_text = encryption_text.get()
        enc_password = encryption_password.get()
        if enc_text == "":
            encryption_text.configure(border_color="red")
        elif enc_password == "":
            encryption_password.configure(border_color="red")
        else:
            decode_show_label=customtkinter.CTkLabel(tabview.tab("Decrption"), text="*************",text_color="black",fg_color="white",height=15)
            try:
                 decode_password = decode(enc_password,enc_text)
                 decode_show_label.place(x=30,y=105)
            except:
                decode_show_label.place(x=30,y=105)
            

    show_password_frame = customtkinter.CTkFrame(tabview.tab("Decrption"), width=170,
                               height=30,
                               fg_color="white",
                               border_width=2,
                               border_color="gray40",
                               bg_color="gray15",
                               corner_radius=20)
    show_password_frame.place(x=17,y=95)

    copy_password_in_frame = customtkinter.CTkButton(tabview.tab("Decrption"),width=50,
                                 height=30,
                                 border_color="light blue",
                                 border_width=2,
                                 corner_radius=13,
                                 fg_color="#72B3F9",
                                 bg_color="gray17",
                                 text="Copy",
                                 text_color="white",
                                 hover_color="light blue",
                                 font=font_4,
                                 command=copy_text_to_clipboard_password)
    
    copy_password_in_frame.place(x=200,y=95)

    back_button =customtkinter.CTkButton(tabview.tab("Decrption"),width=50,
                                 height=30,
                                 border_color="light blue",
                                 border_width=2,
                                 corner_radius=13,
                                 fg_color="#72B3F9",
                                 bg_color="gray17",
                                 text="Back",
                                 text_color="white",
                                 hover_color="light blue",
                                 font=font_4,
                                 command=destroy_frame)
    back_button.place(x=200,y=150)

    decode_cryption = customtkinter.CTkButton(tabview.tab("Decrption"),
                                 width=50,
                                 height=30,
                                 border_color="light blue",
                                 border_width=2,
                                 corner_radius=13,
                                 fg_color="#72B3F9",
                                 bg_color="gray17",
                                 text="Decode",
                                 text_color="white",
                                 hover_color="light blue",
                                 font=font_4,
                                 command=decode_function)
    decode_cryption.place(x=60,y=150)

    tabview.place(x=35,y=0)
    
encyption_button = customtkinter.CTkButton(master=screen,
                                 width=50,
                                 height=30,
                                 border_color="light blue",
                                 border_width=2,
                                 corner_radius=20,
                                 fg_color="#72B3F9",
                                 bg_color="gray15",
                                 text="Cryption",
                                 text_color="white",
                                 hover_color="light blue",
                                 font=font_4,
                                 command=encyption_screen)

encyption_button.place(x=260,y=250)



screen.mainloop()