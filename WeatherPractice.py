import tkinter as tk

WHEIGHT = 500
WWIDTH = 400

root = tk.Tk()

canvas = tk.Canvas(root, height=WHEIGHT, width=WWIDTH).pack()

textFrame = tk.Frame(root, bg='blue')
textEntry = tk.Entry(textFrame, font=12)
acceptance = tk.Button(textFrame, text='Find')

textFrame.place(relx=.5, rely=.1, relwidth=.75, relheight=.05, anchor='n')
textEntry.place(relwidth=.65, relheight=1)
acceptance.place(relx=.65, relwidth=.35, relheight=1)

root.mainloop()
