import tkinter as tk
from PIL import ImageTk, Image

FONT = 30
IMAGE_NAME = 'landscape.jpeg'


def button_click():
    print("Button Clicked!!!")


root = tk.Tk()
root.title('Weather App')
root.geometry('600x500')
root.config(bg='black')

# Background
bg_image = Image.open(IMAGE_NAME).resize((600, 500))
bg_photo = ImageTk.PhotoImage(bg_image)
bg_label = tk.Label(root, image=bg_photo)
bg_label.place(relwidth=1, relheight=1)

# City find box
input_frame = tk.Frame(root, bd=5, bg='#80c1ff')
city_input = tk.Entry(input_frame, font=FONT)
find_button = tk.Button(input_frame, text='Find', font=FONT, command=button_click)

input_frame.place(anchor='n', relx=.5, rely=.1, relwidth=.75, relheight=.07)
city_input.place(relwidth=.65, relheight=1)
find_button.place(relx=.7, relwidth=.3, relheight=1)

# Results box
lower_frame = tk.Frame(root, bd=5, bg='#80c1ff')
result_label = tk.Label(lower_frame)

lower_frame.place(anchor='n', relx=.5, rely=.22, relwidth=.75, relheight=.7)
result_label.place(relwidth=1, relheight=1)

root.mainloop()
