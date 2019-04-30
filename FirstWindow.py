import tkinter as tk

HEIGHT = 400
WIDTH = 600

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
frame = tk.Frame(root, bg='#80c1ff')
button = tk.Button(frame, text="Test Button", bg="red", fg='blue')
label = tk.Label(frame, text='This is a label')
entry = tk.Entry(frame, bg="white")

canvas.pack()
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
button.grid(row=0, column=0)
label.place(relx=0.2, rely=0.3)
entry.grid(row=1, column=0)

root.mainloop()
