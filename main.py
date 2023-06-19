# For NotePad

# Library
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

# Code part
def new_file():
    global file
    root.title("NewFile-NotePad")
    file = None
    TextArea.delete(1.0, END)

def openfile():
    global file
    file = askopenfilename(defaultextension=".txt",
                           filetypes=[("All Types", "*.*"),
                                      ("Text Document", "*.txt")]
                           )
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + "-NotePad")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()

def savefile():
    global file
    if file is None:
        file = asksaveasfilename(initialfile="NewFile.txt", defaultextension=".txt",
                                 filetypes=[("All Types", "*.*"),
                                            ("Text Document", "*.txt")]
                                 )

        if file == "":
            file = None
        else:
            # Save new file
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()
            root.title(os.path.basename(file) + "-NotePad")

    else:
        # Save a file
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()

def copy():
    TextArea.event_generate("<<Copy>>")

def cut():
    TextArea.event_generate("<<Cut>>")

def paste():
    TextArea.event_generate("<<Paste>>")

def about():
    showinfo("NotePad", "NotePad By Sandesh Paudel")

def quitApp():
    root.destroy()

if __name__ == '__main__':
    root = Tk()
    root.title("NewFile-NotePad")
    root.geometry('800x600')

    TextArea = Text(root, font="sans-serif 16")
    file = None
    TextArea.pack(expand=True, fill=BOTH)

    MenuBar = Menu(root)

    # For File Menu
    FileMenu = Menu(MenuBar, tearoff=0)
    FileMenu.add_command(label="New", command=new_file)
    FileMenu.add_command(label="Open", command=openfile)
    FileMenu.add_command(label="Save", command=savefile)
    FileMenu.add_separator()
    FileMenu.add_command(label="Exit", command=quitApp)
    MenuBar.add_cascade(label="File", menu=FileMenu)

    # For Edit Menu
    EditMenu = Menu(MenuBar, tearoff=0)
    EditMenu.add_command(label="Copy", command=copy)
    EditMenu.add_command(label="Cut", command=cut)
    EditMenu.add_command(label="Paste", command=paste)
    MenuBar.add_cascade(label="Edit", menu=EditMenu)

    # For About/Help Menu
    Help_AboutMenu = Menu(MenuBar, tearoff=0)
    Help_AboutMenu.add_command(label="About NotePad", command=about)
    MenuBar.add_cascade(label="Help", menu=Help_AboutMenu)

    root.config(menu=MenuBar)

    SCROLL = Scrollbar(TextArea)
    SCROLL.pack(side=RIGHT, fill=Y)
    SCROLL.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=SCROLL.set)

    # For running the application
    root.mainloop()
