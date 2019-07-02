import tkinter
import os
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *


class newnotetaker:
    __root = Tk()

    __windowWidth = 300
    __windowHeight = 300
    __TextArea = Text(__root)
    __MenuBar = Menu(__root)
    __FileMenu = Menu(__MenuBar, tearoff=0)
    __EditMenu = Menu(__MenuBar, tearoff=0)
    __HelpMenu = Menu(__MenuBar, tearoff=0)

    __ScrollBar = Scrollbar(__TextArea)
    __fileName = None

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

        screenWidth = self.__root.winfo_screenwidth()
        screenHeight = self.__root.winfo_screenheight()

        winLocationLeft = (screenWidth / 2) - (self.__windowWidth / 2)
        winLocationTop = (screenHeight / 2) - (self.__windowHeight / 2)

        self.__root.geometry('%dx%d+%d+%d' % (self.__windowWidth,
                                              self.__windowHeight,
                                              winLocationLeft,
                                              winLocationTop))

        self.__root.rowconfigure(0, weight=1)
        self.__root.columnconfigure(0, weight=1)

        self.__TextArea.grid(sticky=N + E + S + W)

        self.__FileMenu.add_command(label="New", command=self.__newFile)
        self.__FileMenu.add_command(label="Open", command=self.__openFile)
        self.__FileMenu.add_command(label="Save", command=self.__saveFile)
        self.__FileMenu.add_separator()
        self.__FileMenu.add_command(label="Exit",
                                    command=self.__quitApplication)
        self.__MenuBar.add_cascade(label="File", menu=self.__FileMenu)

        self.__EditMenu.add_command(label="Cut", command=self.__cut)
        self.__EditMenu.add_command(label="Copy", command=self.__copy)
        self.__EditMenu.add_command(label="Paste", command=self.__paste)
        self.__MenuBar.add_cascade(label="Edit", menu=self.__EditMenu)

        self.__HelpMenu.add_command(label="About Notepad",
                                    command=self.__showAbout)
        self.__MenuBar.add_cascade(label="Help", menu=self.__HelpMenu)
        self.__root.config(menu=self.__MenuBar)
        self.__ScrollBar.pack(side=RIGHT, fill=Y)
        self.__ScrollBar.config(command=self.__TextArea.yview)
        self.__TextArea.config(yscrollcommand=self.__ScrollBar.set)

    def __quitApplication(self):
        self.__root.destroy()

    def __showAbout(self):
        showinfo("Notepad", "This is my first try at creating a word processor!")

    def __openFile(self):
        self.__fileName = askopenfilename(defaultextension=".txt",
                                          filetypes=[("All Files", "*.*"),
                                                     ("Text Documents", "*.txt")])

        if self.__fileName == "":
            self.__fileName = None
        else:
            self.__root.title(os.path.basename(self.__fileName) + " - Notepad")
            self.__TextArea.delete(1.0, END)

            file = open(self.__fileName, "r")
            self.__TextArea.insert(1.0, file.read())
            file.close()

    def __newFile(self):
        self.__root.title("Untitled - Notepad")
        self._file = None
        self.__TextArea.delete(1.0, END)

    def __saveFile(self):
        if self.__fileName is None:
            self.__fileName = asksaveasfilename(initialfile='Untitled.txt',
                                                defaultextension=".txt",
                                                filetypes=[("All Files", "*.*"),
                                                           ("Text Documents",
                                                            "*.txt")])

            if self.__fileName == "":
                self.__fileName = None
            else:
                file = open(self.__fileName, "w")
                file.write(self.__TextArea.get(1.0, END))
                file.close()
                self.__root.title(os.path.basename(self.__fileName) +
                                  " - Notepad")
        else:
            file = open(self.__fileName, "w")
            file.write(self.__TextArea.get(1.0, END))
            file.close()

    def __cut(self):
        self.__TextArea.event_generate("<<Cut>>")

    def __copy(self):
        self.__TextArea.event_generate("<<Copy>>")

    def __paste(self):
        self.__TextArea.event_generate("<<Paste>>")

    def run(self):
        self.__root.mainloop()


notepad = newnotetaker(width=600, height=400)
notepad.run()
