import tkinter as tk
from tkinter.messagebox import *
from tkinter.filedialog import *
import time
from spellchecker import spellchecker


class NewNoteTaker:
    __root = Tk()

    __windowWidth = 300
    __windowHeight = 300
    __TextArea = Text(__root)
    __MenuBar = Menu(__root)
    __FileMenu = Menu(__MenuBar, tearoff=0)
    __EditMenu = Menu(__MenuBar, tearoff=0)
    __HelpMenu = Menu(__MenuBar, tearoff=0)

    __ScrollBar = Scrollbar(__TextArea)
    __FileName = None
    __Saved = False

    def __init__(self, **kwargs):
        try:
            self.__root.wm_iconbitmap("Notepad.ico")
        except:
            pass

        try:
            self.__windowWidth = kwargs['width']
        except KeyError:
            pass

        try:
            self.__windowHeight = kwargs['height']
        except KeyError:
            pass

        self.__root.title('Untitled - Notepad')

        screenwidth = self.__root.winfo_screenwidth()
        screenheight = self.__root.winfo_screenheight()

        winlocationleft = (screenwidth / 2) - (self.__windowWidth / 2)
        winlocationtop = (screenheight / 2) - (self.__windowHeight / 2)

        self.__root.geometry('%dx%d+%d+%d' % (self.__windowWidth,
                                              self.__windowHeight,
                                              winlocationleft,
                                              winlocationtop))

        self.__root.rowconfigure(0, weight=1)
        self.__root.columnconfigure(0, weight=1)

        self.__TextArea.grid(sticky=N + E + S + W)

        self.__FileMenu.add_command(label="New", command=self.__newfile)
        self.__FileMenu.add_command(label="Open", command=self.__openfile)
        self.__FileMenu.add_command(label="Save", command=self.__savefile)
        self.__FileMenu.add_separator()
        self.__FileMenu.add_command(label="Exit",
                                    command=self.__quitapplication)
        self.__MenuBar.add_cascade(label="File", menu=self.__FileMenu)

        self.__EditMenu.add_command(label="Cut", command=self.__cut)
        self.__EditMenu.add_command(label="Copy", command=self.__copy)
        self.__EditMenu.add_command(label="Paste", command=self.__paste)
        self.__MenuBar.add_cascade(label="Edit", menu=self.__EditMenu)

        self.__HelpMenu.add_command(label="About Notepad",
                                    command=self.__showabout)
        self.__MenuBar.add_cascade(label="Help", menu=self.__HelpMenu)

        self.__root.config(menu=self.__MenuBar)

        self.__ScrollBar.pack(side=RIGHT, fill=Y)
        self.__ScrollBar.config(command=self.__TextArea.yview)

        self.__TextArea.config(yscrollcommand=self.__ScrollBar.set)

    def __quitapplication(self):
        if not self.__Saved:
            self.__savebeforequit()
        #self.__root.destroy()

    def __savebeforequit(self):
        __top = Toplevel(height=75, width=300)
        __top.title("Caution")
        __frame = tk.Frame(__top)
        __frame.place(anchor='n', relx=0, rely=0)

        __caution = tk.Label(__top, text='Are you sure you wish to exit without saving?')
        __yes = tk.Button(__top, text="Yes", command=self.__root.destroy)
        __no = tk.Button(__top, text="No", command=self.__savefile)

        __caution.place(anchor='n' + 'w', relx=.1, rely=.1)
        __yes.place(anchor='n', relx=.3, rely=.5, relwidth=.2)
        __no.place(anchor='n', relx=.7, rely=.5, relwidth=.2)



    def __showabout(self):
        showinfo("Notepad", "This is my first try at creating a word processor!")

    def __openfile(self):
        self.__FileName = askopenfilename(defaultextension=".txt",
                                          filetypes=[("All Files", "*.*"),
                                                     ("Text Documents", "*.txt")])

        if self.__FileName == "":
            self.__FileName = None
        else:
            self.__root.title(os.path.basename(self.__FileName) + " - Notepad")
            self.__TextArea.delete(1.0, END)

            file = open(self.__FileName, "r")
            self.__TextArea.insert(1.0, file.read())
            file.close()
        self.__Saved = False

    def __newfile(self):
        self.__root.title("Untitled - Notepad")
        self.__FileName = None
        self.__Saved = False
        self.__TextArea.delete(1.0, END)

    def __savefile(self):
        if self.__FileName is None:
            self.__FileName = asksaveasfilename(initialfile='Untitled.txt',
                                                defaultextension=".txt",
                                                filetypes=[("All Files", "*.*"),
                                                           ("Text Documents",
                                                            "*.txt")])

            if self.__FileName == "":
                self.__FileName = None
            else:
                file = open(self.__FileName, "w")
                file.write(self.__TextArea.get(1.0, END))
                file.close()
                self.__root.title(os.path.basename(self.__FileName) +
                                  " - Notepad")
        else:
            file = open(self.__FileName, "w")
            file.write(self.__TextArea.get(1.0, END))
            file.close()
        self.__Saved = True

    def __cut(self):
        self.__TextArea.event_generate("<<Cut>>")

    def __copy(self):
        self.__TextArea.event_generate("<<Copy>>")

    def __paste(self):
        self.__TextArea.event_generate("<<Paste>>")

    def run(self):
        self.__root.mainloop()


notepad = NewNoteTaker(width=600, height=400)
notepad.run()
