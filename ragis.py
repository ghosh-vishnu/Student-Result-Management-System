from tkinter import*
from PIL import ImageTk
from tkinter import messagebox
#  self.root.resizable(False,False)
class registration:
    def __init__(self,root):
        self.root=root
        self.root.title("Registration Form")
        self.root.geometry('400x400')
#=================================Label========================================
        Label( self.root,text='Registration Form',font='ariel 20 bold',background='red',fg='white').pack(fill='both')

        Label( self.root,text='Name',font='15').place(x=40,y=75)
        Label( self.root,text='Phone No',font='15').place(x=40,y=155)
        Label( self.root,text='Age',font='15').place(x=40,y=115)
        Label( self.root,text='Email ID',font='15').place(x=40,y=195)
            #==================================Entry============================================
        self.Name_info=StringVar()
        self.age_info=StringVar()
        self.phone_info=StringVar()
        self.email_info=StringVar()
        self.name_entry=Entry( self.root,font='10',bd=4,textvariable=self.Name_info)
        self.name_entry.place(x=140,y=75)
        self.age_entry=Entry( self.root,font='10',bd=4,textvariable=self.age_info)
        self.age_entry.place(x=140,y=115)

        self.phone_entry=Entry( self.root,font='10',bd=4,textvariable=self.phone_info)
        self.phone_entry.place(x=140,y=155)

        self.email_entry=Entry( self.root,font='10',bd=4,textvariable=self.email_info)
        self.email_entry.place(x=140,y=195)

        #=============================Button=============================
        Button( self.root,text="Register",font='20',command=self.register).place(x=185,y=255)
        Button( self.root,text="Clear",font='20',command=self.clear).place(x=345,y=365)
    def register(self):
        name=self.Name_info.get()
        age=self.age_info.get()
        phone=self.phone_info.get()
        email=self.email_info.get()
        if name=="":
            messagebox.showerror("Error","Please Enter Your Name")
        elif age=="":
            messagebox.showerror("Error","Please Enter Your Age")
        elif phone=="":
            messagebox.showerror("Error","Please Enter Your Phone Number")
        elif email=="":
            messagebox.showerror("Error","Please Enter Your Email ID")
        else:
            Label( self.root,text="Registration Sucessfull",font='20',fg='green').place(x=135,y=285)

        with open(name+'.text',mode='w')as f:
            f.write("Name: "+name+"\n")
            f.write("Age: "+age+"\n")
            f.write("Phone: "+phone+"\n")
            f.write("Email ID: "+email+"\n")

    def clear(self):
        self.name_entry.delete(0,END)
        self.age_entry.delete(0,END)
        self.phone_entry.delete(0,END)
        self.email_entry.delete(0,END)
if __name__=="__main__":
    root=Tk()
    obj=registration(root)
    root.mainloop()