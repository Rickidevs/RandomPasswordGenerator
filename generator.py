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
screen.geometry("370x450")
screen._set_appearance_mode("dark")
screen.resizable(False,False)
screen.iconbitmap(default=ICON_PATH)

font_1 = ("Arial",105)
font_2 = ("Arial", 50,"bold")
font_3 = ("Arial", 20)
font_4 = ("Arial",15,"bold")

logo_frame = customtkinter.CTkFrame(screen, width=350,
                               height=160,
                               fg_color="gray20",
                               border_width=2,
                               border_color="gray25",
                               corner_radius=20)
logo_frame.place(x=8,y=8)

monkey_logo = customtkinter.CTkLabel(screen,text="🫣", font=font_1, text_color="#72B3F9",bg_color="gray20")
monkey_logo.place(x=180, y=10)
dont_panic = customtkinter.CTkLabel(screen,text="Don't", font=font_2, text_color="#72B3F9",bg_color="gray20")
dont_panic.place(x=10, y=20)
dont_panic_1 = customtkinter.CTkLabel(screen,text="panic", font=font_2, text_color="#72B3F9",bg_color="gray20")
dont_panic_1.place(x=30, y=70)
dont_panic_1 = customtkinter.CTkLabel(screen,text="i don't look your password ehehe", font=font_3, text_color="#72B3F9",bg_color="gray20")
dont_panic_1.place(x=50, y=130)

show_text_label = customtkinter.CTkFrame(screen, width=250,
                               height=30,
                               fg_color="white",
                               border_width=2,
                               border_color="gray40",
                               bg_color="gray15",
                               corner_radius=20)
show_text_label.place(x=20, y=180)

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
copy_button.place(x=280,y=180)

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
password_button.place(x=20,y=250)

screen.mainloop()