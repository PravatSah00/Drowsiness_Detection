from tkinter import *
from tkinter.ttk import *
import tkinter as tk
import tkinter.font as tkFont
from PIL import ImageTk, Image

def isPhoneNo(str):
    if(len(str) != 10):
        return False
    for ch in str:
        if(ch < "0" or ch > "9"):
            return False
    return True

class FileHandaler:
    def __init__(self) -> None:
        # Get the prev user name:
        user_name = open(r"DataDir/UserData/user_name.ff","r")
        if not user_name:
            print("Error!!! Unable to open file")
        self.prev_user_name = user_name.read()
        user_name.close()

    def write_data(self, user_name, phone_number):
        # Open user_name.ff and user_number.ff:
        user_name_file = open(r"DataDir/UserData/user_name.ff","w")
        user_number_file = open(r"DataDir/UserData/user_number.ff","w")

        if not user_name_file or not user_number_file:
            print("Error!!! Unable to open file")
            return
        
        if user_name == "":
            user_name = self.prev_user_name
        
        user_name_file.write(user_name)
        user_number_file.write(phone_number)

        user_name_file.close()
        user_number_file.close()


class App:
    def __init__(self, root):
        self.warning = "! Phone Number Is Incorrect "
        self.root = root
        self.file_handaler = FileHandaler()

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
    
        GLabel_807=tk.Label(root)
        GLabel_807["bg"] = "#606ded"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_807["font"] = ft
        GLabel_807["fg"] = "#333333"
        GLabel_807["justify"] = "center"
        GLabel_807["text"] = ""
        GLabel_807.place(x=0,y=0,width=1000,height=600)
        
        #first image
        global image2
        image2 = Image.open(fp=r"DataDir/Image/imageForKinter1.png")
        image2 = image2.resize([450, 550])
        image2 = ImageTk.PhotoImage(image=image2, master = root)
        GLabel_649=tk.Label(root, image = image2)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_649["font"] = ft
        GLabel_649["fg"] = "#333333"
        GLabel_649["bg"] = "#606ded"
        GLabel_649["justify"] = "center"
        GLabel_649["text"] = ""
        GLabel_649.place(x=0,y=0,width=500,height=600)
        
        
        #2nd images
        global image1
        image1 = Image.open(fp=r"DataDir/Image/dashboard_second_copy.png")
        image1 = image1.resize([450, 550])
        image1 = ImageTk.PhotoImage(image=image1, master = root)
        GLabel_239=tk.Label(root, image = image1)
        GLabel_239["bg"] = "#ffffff"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_239["font"] = ft
        GLabel_239["fg"] = "#333333"
        GLabel_239["justify"] = "center"
        GLabel_239["text"] = ""
        GLabel_239.place(x=500,y=0,width=500,height=600)
        
        #First entry
        GLineEdit_697=tk.Entry(root)
        GLineEdit_697["borderwidth"] = "0px"
        ft = tkFont.Font(family='Consolas',size=20)
        GLineEdit_697["font"] = ft
        GLineEdit_697["fg"] = "#333333"
        GLineEdit_697["justify"] = "left"
        GLineEdit_697["text"] = ""
        GLineEdit_697.place(x=70,y=250,width=280,height=39)
        self.name = GLineEdit_697


        #2nd entry
        GLineEdit_569=tk.Entry(root)
        GLineEdit_569["borderwidth"] = "0px"
        ft = tkFont.Font(family='Consolas',size=20)
        GLineEdit_569["font"] = ft
        GLineEdit_569["fg"] = "#333333"
        GLineEdit_569["justify"] = "left"
        GLineEdit_569["text"] = ""
        GLineEdit_569.place(x=70,y=340,width=280,height=39)
        self.phone = GLineEdit_569


        #lets go button
        GButton_188=tk.Button(root)
        GButton_188["bg"] = "#F24162"
        ft = tkFont.Font(family='Consolas',size=20, weight="bold")
        GButton_188["font"] = ft
        GButton_188["fg"] = "#ffffff"
        GButton_188["borderwidth"] = "0px"
        GButton_188["justify"] = "center"
        GButton_188["text"] = "NEXT"
        GButton_188.place(x=110,y=420,width=197,height=49)
        GButton_188["command"] = self.GButton_188_command

        # Warning Label:
        GLabel_878=tk.Label(root)
        ft = tkFont.Font(family='Consolas ',size=10, weight="bold")
        GLabel_878["font"] = ft
        GLabel_878["fg"] = "#FFCC2F"
        GLabel_878["bg"] = "#606ded"
        GLabel_878["justify"] = "left"
        GLabel_878["text"] = ""
        GLabel_878.place(x=65,y=390,width=195,height=10)
        self.warn = GLabel_878

    #NEXT BUTTON FUNCTION⚠ 
    def GButton_188_command(self):
        user_name = self.name.get()
        phone_number = self.phone.get()

        if(isPhoneNo(phone_number)):
            self.warn["text"] = ""
            self.file_handaler.write_data(
                user_name = user_name,
                phone_number = phone_number
            )
            self.root.destroy()
        else:
            self.warn["text"] = self.warning
            self.name.delete(0, END)
            self.phone.delete(0, END)

def main(master):
    root = Toplevel(master = master)
    root.grab_set()
    app = App(root)