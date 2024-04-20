import pyqrcode
import png
from pyqrcode import QRCode
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import os


# Function to generate QR Code
# Function to generate QR Code
def generate_qrcode():
    # String which represents the QR code
    s = entry_text.get()

    # Generate QR code
    url = pyqrcode.create(s)

    # Create and save the png file naming "myqr.png"
    png_file = s + '.png'
    url.png(png_file, scale=6)

    # Update image label
    img = Image.open(png_file)
    img = img.resize((150, 150))
    photo = ImageTk.PhotoImage(img)

    label2.config(image=photo)  # Do not comment this line
    label2.image = photo  # keep a reference!


# Creating tkinter window
win = Tk()
win.title("QR Code Generator")

# Adding widgets
label = Label(win, text="Enter text to generate QR Code")
label.pack()
entry_text = Entry(win)
entry_text.pack()
# Image display
label2 = Label(win)
label2.pack()
button = Button(win, text="Generate", command=generate_qrcode)
button.pack()



win.mainloop()
