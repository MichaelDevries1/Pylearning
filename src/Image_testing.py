import tkinter as tk

from PIL import Image, ImageTk

root = tk.Tk()
root.title("Title")
root.geometry("600x500")
root.configure(background="black")

image = Image.open("landscape.jpeg").resize((600, 500))
bg_image = ImageTk.PhotoImage(image)
bg_label = tk.Label(root, image=bg_image)

bg_label.place(relheight=1, relwidth=1)

root.mainloop()
