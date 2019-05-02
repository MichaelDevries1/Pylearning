import tkinter as tk

root = tk.Tk()
for i in range(7):
    for j in range(7):
        tk.Label(root, text="R%s/C%s" % (i, j), borderwidth=1).grid(row=i, column=j)
root.mainloop()
