from WordProcessor.ToolBar import Command
from tkinter.filedialog import *


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

        self.__FileMenu.add_command(label="New", command=Command.__newfile)
        self.__FileMenu.add_command(label="Open", command=Command.__openfile)
        self.__FileMenu.add_command(label="Save", command=Command.__savefile)
        self.__FileMenu.add_separator()
        self.__FileMenu.add_command(label="Exit",
                                    command=Command.__quitapplication)
        self.__MenuBar.add_cascade(label="File", menu=Command.__FileMenu)

        self.__EditMenu.add_command(label="Cut", command=Command.__cut)
        self.__EditMenu.add_command(label="Copy", command=Command.__copy)
        self.__EditMenu.add_command(label="Paste", command=Command.__paste)
        self.__MenuBar.add_cascade(label="Edit", menu=Command.__EditMenu)

        self.__HelpMenu.add_command(label="About Notepad",
                                    command=Command.__showabout)
        self.__MenuBar.add_cascade(label="Help", menu=Command.__HelpMenu)
        self.__root.config(menu=Command.__MenuBar)
        self.__ScrollBar.pack(side=RIGHT, fill=Y)
        self.__ScrollBar.config(command=Command.__TextArea.yview)
        self.__TextArea.config(yscrollcommand=Command.__ScrollBar.set)

    def run(self):
        self.__root.mainloop()


notepad = NewNoteTaker(width=600, height=400)
notepad.run()
