from tkinter.messagebox import *
from tkinter.filedialog import *


class Command:
    def __savefile(self):
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

    def __quitapplication(self):
        self.__root.destroy()


    def __showabout(self):
        showinfo("Notepad", "This is my first try at creating a word processor!")


    def __openfile(self):
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


    def __newfile(self):
        self.__root.title("Untitled - Notepad")
        self._file = None
        self.__TextArea.delete(1.0, END)