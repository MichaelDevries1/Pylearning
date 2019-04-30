import tkinter as tk

WHEIGHT = 500
WWIDTH = 400

root = tk.Tk()

canvas = tk.Canvas(root, height=WHEIGHT, width=WWIDTH).pack()

textFrame = tk.Frame(canvas, bg='blue').place(relx=.2, rely=.2, relwidth=.5, height=20)
cityEntry = tk.Entry(textFrame, bg='white').place(relwidth=.95, relheight=.95)

root.mainloop()
