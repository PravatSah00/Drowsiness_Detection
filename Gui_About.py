import tkinter as tk
from tkinter import Toplevel
import tkinter.font as tkFont
import tkinter.font as tkFont
from PIL import ImageTk, Image

class App:
    def __init__(self, root):
        self.root = root
        #setting title
        root.title("undefined")
        #setting window size
        width=1000
        height=600
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        global image1
        image1 = Image.open(fp=r"DataDir/Image/Mos_effectiive.png")
        image1 = image1.resize([1000, 550])
        image1 = ImageTk.PhotoImage(image=image1, master = root)

        GLabel_181=tk.Label(root, image = image1)
        GLabel_181["bg"] = "#ffffff"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_181["font"] = ft
        GLabel_181["fg"] = "#333333"
        GLabel_181["justify"] = "center"
        GLabel_181["text"] = ""
        GLabel_181.place(x=0,y=0,width=1000,height=600)

        GButton_352=tk.Button(root)
        GButton_352["bg"] = "#009688"
        ft = tkFont.Font(family='Times',size=18)
        GButton_352["font"] = ft
        GButton_352["fg"] = "#ffffff"
        GButton_352["justify"] = "center"
        GButton_352["text"] = "OK"
        GButton_352["relief"] = "flat"
        GButton_352.place(x=430,y=540,width=154,height=45)
        GButton_352["command"] = self.GButton_352_command

    def GButton_352_command(self):
        self.root.destroy()


def main(master):
    root = Toplevel(master = master)
    root.grab_set()
    app = App(root)
