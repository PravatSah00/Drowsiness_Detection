from tkinter import *
from tkinter import messagebox
import tkinter as tk
import tkinter.font as tkFont
from PIL import ImageTk, Image

import Gui_Login
import Gui_About
import Main

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

        # Background Label:
        GLabel_855=tk.Label(root)
        GLabel_855["bg"] = "#7d6bf2"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_855["font"] = ft
        GLabel_855["fg"] = "#333333"
        GLabel_855["justify"] = "center"
        GLabel_855["text"] = ""
        GLabel_855.place(x=0,y=0,width=1000,height=623)


        # Loading first image for left side:
        global image1
        image1 = Image.open(fp=r"DataDir/Image/imageForKinter_best.png")
        image1 = ImageTk.PhotoImage(image=image1, master = root)
        GLabel_79=tk.Label(root, image = image1)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_79["font"] = ft
        GLabel_79["bg"] = "#ffffff"
        GLabel_79["justify"] = "center"
        GLabel_79["text"] = ""
        GLabel_79.place(x=0,y=80,width=595,height=540)

        # Loading second image for right side:
        global image2
        image2 = Image.open(fp=r"DataDir/Image/dashboard_small.png")
        image2 = image2.resize([510, 530])
        image2 = ImageTk.PhotoImage(image=image2, master = root)
        GLabel_425=tk.Label(root, image=image2)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_425["font"] = ft
        GLabel_425["bg"] = "#ffffff"
        GLabel_425["justify"] = "center"
        GLabel_425["text"] = ""
        GLabel_425.place(x=600,y=80,width=414,height=537)

        # Login button
        GButton_232=tk.Button(root)
        GButton_232["bg"] = "#f22e62"
        ft = tkFont.Font(family='Times',size=20)
        GButton_232["font"] = ft
        GButton_232["fg"] = "#ffffff"
        GButton_232["justify"] = "center"
        GButton_232["text"] = "LOGIN"
        GButton_232["relief"] = "flat"
        GButton_232.place(x=200,y=20,width=164,height=38)
        GButton_232["command"] = self.GButton_232_command

        # Detection button
        GButton_151=tk.Button(root)
        GButton_151["bg"] = "#f22e62"
        ft = tkFont.Font(family='Times',size=20)
        GButton_151["font"] = ft
        GButton_151["fg"] = "#ffffff"
        GButton_151["justify"] = "center"
        GButton_151["text"] = "DETECTION"
        GButton_151["relief"] = "flat"
        GButton_151.place(x=420,y=20,width=164,height=38)
        GButton_151["command"] = self.GButton_151_command

        # About Us button
        GButton_543=tk.Button(root)
        GButton_543["bg"] = "#f22e62"
        ft = tkFont.Font(family='Times',size=20)
        GButton_543["font"] = ft
        GButton_543["fg"] = "#ffffff"
        GButton_543["justify"] = "center"
        GButton_543["text"] = "ABOUT US"
        GButton_543["relief"] = "flat"
        GButton_543.place(x=635,y=20,width=164,height=38)
        GButton_543["command"] = self.GButton_543_command

    # Login Command
    def GButton_232_command(self):
        Gui_Login.main(self.root)


    # Detection Command
    def GButton_151_command(self):
        state = True

        user_number = open(r"DataDir/UserData/user_number.ff","r")
        if not user_number:
            print("Error!!! Unable to open file")
        if user_number.read() == "":
            state = False
        user_number.close()

        if state:
            Main.main()
        else:
            messagebox.showinfo("info", " Login first for Detection")

    # About Us command
    def GButton_543_command(self):
        Gui_About.main(self.root)


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
