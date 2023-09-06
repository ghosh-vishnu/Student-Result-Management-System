from tkinter import*
from PIL import ImageTk
from tkinter import messagebox
from dashboard import RMS
from ragis import registration

class Login_system:
    def __init__(self,root):
        self.root=root
        # self.root.resizable(False,False)
        self.root.title("Login System ")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg='#FCFCFC')
        # self.bg_image=ImageTk.PhotoImage(file="img_log\login.jpg")
        # self.bg1_=Label(self.root,image=self.bg_image).place(x=50,y=0,relwidth=1,relheight=1)
        footer = Label(self.root, text="SRMS-STUDENT RESULT MANAGEMENT SYSTEM\nContact Us For Any Technical Issue: 7061468001",font=("goudy old",12),bg="#033054",fg="white").pack(side=BOTTOM,fill=X)

#==============================Images=====================================================================
        self.login=ImageTk.PhotoImage(file="img_log\log.png")
        self.lbl_login=Label(self.root,image=self.login,bd=0).place(x=200,y=50)
#==============================Login Frame=====================================================================
        self.username=StringVar()
        self.password=StringVar() 
        Login_frame1=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        Login_frame1.place(x=690,y=120,width=350,height=460)
        title=Label(Login_frame1,text="LOGIN SYSTEM",font=("Elephant",25,"bold"),bg="white").place(x=0,y=30,relwidth=1)
        lbl_user=Label(Login_frame1,text="User Name",font=("Andalus",15),bg="white",fg="#767171").place(x=50,y=100)
        text=Label(Entry(Login_frame1,textvariable=self.username,font=("times new roman",15),bg="#ECECEC").place(x=50,y=140,width=250))
        
        lbl_pass=Label(Login_frame1,text="Password",font=("Andalus",15),bg="white",fg="#767171").place(x=50,y=180)
        text=Label(Entry(Login_frame1,textvariable=self.password,show="*",font=("times new roman",15),bg="#ECECEC").place(x=50,y=220,width=250))

        log_btn=Button(Login_frame1,command=self.log,text="LOG IN",font=("Arial Rounded MT Bold",15),bg="#00CDCD",cursor="hand2").place(x=50,y=300,width=250,height=35)
        hr=Label(Login_frame1,bg="lightgrey").place(x=50,y=370,width=240,height=2)
        or_=Label(Login_frame1,text="OR",bg="white",fg="lightgrey",font=("times new roman",15,"bold")).place(x=150,y=355)

        fg_pass=Button(Login_frame1,text="Forget Password?",font=("times new roman",13),bg="white",activebackground="lightgrey",activeforeground="blue",fg="blue",bd=0).place(x=100,y=390)

        #=========================================Frame2========================================
        Login_frame2=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        Login_frame2.place(x=690,y=610,width=350,height=60) 
        reg_lbl=Label(Login_frame2,text="Don't have an account?",font=("times new roman",15),bg="white").place(x=30,y=15)
        btn_singup=Button(Login_frame2,command=self.signip,text="Sign Up?",font=("times new roman",13,"bold"),bg="white",activebackground="lightgrey",activeforeground="blue",fg="blue",bd=0).place(x=240,y=15)

    def log(self):
        if self.username.get()=="" or self.password.get()=="":
            messagebox.showerror("Error","All fields are required")
        elif self.username.get()!="Deepak" or self.password.get()!="Deepak":
            messagebox.showerror("Error","Invalid User Name and Password\nTry again with correct credentials")
        else:
            messagebox.showinfo("Information",f"Welcome{self.username.get()}")
            self.new_win=Toplevel(self.root)
            self.new_obj=RMS(self.new_win)


#=====================================Animation Image==============================================================
    def animate(self):
        self.im=self.im1
        self.im1=self.im2
        self.im2=self.im3
        self.im3=self.im4
        self.im4=self.im
        self.lbl.config(image=self.im)
        self.lbl.after(2000,self.animate)

        self.im1=ImageTk.PhotoImage(file="img_log\img1.jpg")
        self.im2=ImageTk.PhotoImage(file="img_log\img2.jpg")
        self.im3=ImageTk.PhotoImage(file="img_log\img3.jpg")
        self.im4=ImageTk.PhotoImage(file="img_log\img4.jpg")

        self.lbl_change=Label(self.root,bg="white")
        self.lbl_change.place(x=397,y=173,width=215,height=373)
        self.animate
    def signip(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=registration(self.new_win)
if __name__=="__main__":
    root=Tk() 
    obj=Login_system(root)
    root.mainloop()
    