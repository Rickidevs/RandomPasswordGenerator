import customtkinter 
import tempfile, base64, zlib
from PIL import Image, ImageTk


# for remove tk iconbit
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

show_text_label = customtkinter.CTkFrame(screen, width=250,
                               height=30,
                               fg_color="white",
                               border_width=2,
                               border_color="gray40",
                               bg_color="gray15",
                               corner_radius=20)
show_text_label.place(x=20, y=185)

copy_button = customtkinter.CTkButton(master=screen,
                                 width=20,
                                 height=30,
                                 border_color="light blue",
                                 border_width=2,
                                 corner_radius=20,
                                 fg_color="#72B3F9",
                                 bg_color="gray15",
                                 text="copy",
                                 text_color="white",
                                 hover_color="light blue",
                                 font=font_4
                                 )

copy_button.place(x=280,y=185)


slider_frame = customtkinter.CTkFrame(screen, width=200,
                               height=60,
                               fg_color="gray20",
                               border_width=2,
                               border_color="gray40",
                               bg_color="gray15",
                               corner_radius=15)

slider_frame.place(x= 12, y=245)

current_value = customtkinter.DoubleVar()

def get_current_value():
    return '{: .0f}'.format(current_value.get())

def slider_changed(event):
    value_of_slider.configure(text=f"length of password:{get_current_value()}")

password_length_scroll = customtkinter.CTkSlider(screen, from_=7, to=36,variable=current_value,command=slider_changed,width=180,bg_color="gray20")
password_length_scroll.place(x=20,y=250)
password_length = get_current_value()
print(password_length)

value_of_slider = customtkinter.CTkLabel(screen,text=f"length of password:{get_current_value()}",font=font_4,bg_color="gray20")
value_of_slider.place(x=25,y=270)

switch_label = customtkinter.CTkFrame(screen, width=200,
                               height=110,
                               fg_color="gray20",
                               border_width=2,
                               border_color="gray40",
                               bg_color="gray15",
                               corner_radius=15)

switch_label.place(x=10,y=320)

def get_special_characters():
    return print(special_characters_var.get())

special_characters_var = customtkinter.StringVar(value="on")

special_characters = customtkinter.CTkSwitch(screen ,text="Special characters",variable=special_characters_var, onvalue="on", offvalue="off",command=get_special_characters,font=font_4,bg_color="gray20")
special_characters.place(x=20,y=330)


def get_upper_characters():
    return print(upper_charascters_var.get())

upper_charascters_var = customtkinter.StringVar(value="on")

upper_charascters = customtkinter.CTkSwitch(screen ,text="Capital letters",variable=upper_charascters_var, onvalue="on", offvalue="off",command=get_upper_characters,font=font_4,width=5,bg_color="gray20")
upper_charascters.place(x=20,y=365)


def get_number_characters():
    return print(number_charascters_var.get())

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
                                 font=font_4)

password_button.place(x=20,y=450)

screen.mainloop()