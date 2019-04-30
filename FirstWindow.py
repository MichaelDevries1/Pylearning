import tkinter as tk

HEIGHT = 400
WIDTH = 600

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
frame = tk.Frame(root, bg='#80c1ff')
button = tk.Button(frame, text="Test Button", bg="grey", fg='black')
label = tk.Label(frame, text='This is a label', bg="orange")
entry = tk.Entry(frame, bg="white")

canvas.pack()
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
button.place(relx=0, rely=0, relwidth=.25, relheight=.25)
label.place(relx=0.25, rely=0, relwidth=.25, relheight=.25)
entry.place(relx=.5, rely=0, relwidth=.5, relheight=.25)

root.mainloop()
