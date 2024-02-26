from customtkinter import CTk
from tkinter import *
import tempfile, base64, zlib


# for remove tk iconbit
ICON = zlib.decompress(base64.b64decode('eJxjYGAEQgEBBiDJwZDBy'
    'sAgxsDAoAHEQCEGBQaIOAg4sDIgACMUj4JRMApGwQgF/ykEAFXxQRc='))

_, ICON_PATH = tempfile.mkstemp()
with open(ICON_PATH, 'wb') as icon_file:
    icon_file.write(ICON)


screen = CTk()
screen.title("Modern RPG")
screen.geometry("350x400")
screen._set_appearance_mode("dark")
screen.resizable(False,False)
screen.iconbitmap(default=ICON_PATH)


screen.mainloop()