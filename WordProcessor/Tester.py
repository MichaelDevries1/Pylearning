import tkinter as tk


def answeryes():
    print('yes')


def answerno():
    print('no')


top = tk.Toplevel(width=300, height=50)
top.title("Caution")

warning = tk.Label(top, text="Do you want to save before you exit?")
yes = tk.Button(top, text="Yes", command=answeryes)
no = tk.Button(top, text="No", command=answerno)

warning.place(anchor='n', relx=.5, rely=.5)
yes.place(anchor='center', relx=.3, rely=.7, relwidth=.2)
no.place(anchor='center', relx=.7, rely=.7, relwidth=.2)

top.mainloop()
