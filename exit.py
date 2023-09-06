# from distutils import command
from tkinter import*
from PIL import Image,ImageTk # pip install pillow
class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Registration Form")
        self.root.geometry("1350x700+0+0")
        self.root.bg=ImageTk.PhotoImage(file="images\b2.jpg")
root=Tk()
obj=Register(root)
root.mainloop()