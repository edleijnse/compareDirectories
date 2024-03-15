import pyqrcode
import png
from pyqrcode import QRCode
from tkinter import *


# Function to generate QR Code
def generate_qrcode():

    # String which represents the QR code
    s = entry_text.get()

    # Generate QR code
    url = pyqrcode.create(s)

    # Create and save the svg file naming "myqr.svg"
    url.svg("myqr.svg", scale=8)

    # Create and save the png file naming "myqr.png"
    url.png('myqr.png', scale=6)


# Creating tkinter window
win = Tk()
win.title("QR Code Generator")

# Adding widgets
label = Label(win, text="Enter text to generate QR Code")
label.pack()
entry_text = Entry(win)
entry_text.pack()
button = Button(win, text="Generate", command=generate_qrcode)
button.pack()

win.mainloop()
