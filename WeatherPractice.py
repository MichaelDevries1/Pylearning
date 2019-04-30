import tkinter as tk
from PIL import Image, ImageTk

WHEIGHT = 500
WWIDTH = 600
FONT = 30
TEXTBG = 'white'

root = tk.Tk()
root.title('Weather App')

canvas = tk.Canvas(root, height=WHEIGHT, width=WWIDTH).pack()

image = Image.open('try2.jpg')
background_image = ImageTk.PhotoImage(image)
background_label = tk.Label(root, image=background_image)

textFrame = tk.Frame(root, bg='#80ddd9', bd=2)
textEntry = tk.Entry(textFrame, font=FONT, bg=TEXTBG)
acceptance = tk.Button(textFrame, text='Find', font=FONT)

background_label.place(x=0, y=0, relwidth=1, relheight=1)
textFrame.place(relx=.5, rely=.1, relwidth=.75, relheight=.05, anchor='n')
textEntry.place(relwidth=.65, relheight=1)
acceptance.place(relx=.66, relwidth=.34, relheight=1)

infoDisplay = tk.Frame(root, bg='#80ddd9', bd=2)
label = tk.Label(infoDisplay, bg=TEXTBG)

infoDisplay.place(anchor='n', relx=.5, rely=.2, relwidth=.75, relheight=.7)
label.place(relwidth=1, relheight=1)

root.mainloop()
