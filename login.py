from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import numpy as np
import pandas as pd
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


def main():
    win=Tk()
    app=login_window(win)
    win.mainloop()
    
    


class login_window:
    def __init__(self,root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")
        
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\SHIVAM\Desktop\Mini-project\images\bgp.jpeg")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)
        
        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)
        
        img1=Image.open(r"C:\Users\SHIVAM\Desktop\Mini-project\images\pngwing.com.png")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="black",borderwidth="0")
        lblimg1.place(x=730,y=175,width=100,height=100)
        
        get_str=Label(frame,text="LOGIN",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=125,y=100)
        
        username=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=70,y=155)
        
        self.txtuser=ttk.Entry(frame,text="Username",font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)
        
        password=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        password.place(x=70,y=225)
        
        self.txtpass=ttk.Entry(frame,text="Password",font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=250,width=270)
        
        img2=Image.open(r"C:\Users\SHIVAM\Desktop\Mini-project\images\user.png")
        img2=img2.resize((25,25),Image.ANTIALIAS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg1=Label(image=self.photoimage2,bg="black",borderwidth="0")
        lblimg1.place(x=650,y=323,width=25,height=25)
        
        img3=Image.open(r"C:\Users\SHIVAM\Desktop\Mini-project\images\padlock.png")
        img3=img3.resize((25,25),Image.ANTIALIAS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg1=Label(image=self.photoimage3,bg="black",borderwidth="0")
        lblimg1.place(x=650,y=395,width=25,height=25)
        
        loginbtn=Button(frame,command=self.login,text="Login",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="blue",activeforeground="white",activebackground="blue")
        loginbtn.place(x=110,y=300,width=120,height=35)
        
        registerbtn=Button(frame,text="New User Register",command=self.register_window,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=15,y=350,width=160)
        
        fpbtn=Button(frame,text="forget Password",font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        fpbtn.place(x=10,y=370,width=160)
       
    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)
           
    
    
     
    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="" :
            messagebox.showerror("Error","All fields are required")
        else :
            conn=mysql.connector.connect(host="localhost",user="root",password="Shivam@12",database="sys")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(self.txtuser.get(),self.txtpass.get()))
            row=my_cursor.fetchone()
            if row==None :
                messagebox.showerror("Error","Invalid username or password")
            else :
                open_main=messagebox.askyesno("yesno","Access only Admin")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=main_page(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()
            
            
class Register:
    def __init__(self,root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")
        
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()
        self.var_check=IntVar()
        
        
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\SHIVAM\Desktop\Mini-project\images\bgp.jpeg")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)
        
        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=100,width=800,height=550)
        
        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="darkgreen",bg="white")
        register_lbl.place(x=20,y=20)
        
        self.txt_fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),fg="black",bg="white")
        self.txt_fname.place(x=50,y=100)
        
        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        fname_entry.place(x=50,y=130,width=250)
        
        lname=Label(frame,text="Last Name",font=("times new roman",15,"bold"),fg="black",bg="white")
        lname.place(x=370,y=100)
        
        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15,"bold"))
        self.txt_lname.place(x=370,y=130,width=250)
        
        contact=Label(frame,text="Contact",font=("times new roman",15,"bold"),fg="black",bg="white")
        contact.place(x=50,y=170)
        
        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15,"bold"))
        self.txt_contact.place(x=50,y=200,width=250)
        
        email=Label(frame,text="Email",font=("times new roman",15,"bold"),fg="black",bg="white")
        email.place(x=370,y=170)
        
        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15,"bold"))
        self.txt_email.place(x=370,y=200,width=250)
        
        security_Q=Label(frame,text="Security Question",font=("times new roman",15,"bold"),fg="black",bg="white")
        security_Q.place(x=50,y=240)
        
        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security_Q["values"]=("Select","Your Birth Place","Your Best Friend","Your Pet Name")
        self.combo_security_Q.place(x=50,y=270,width=250)
        self.combo_security_Q.current(0)
        
        
        security_A=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),fg="black",bg="white")
        security_A.place(x=370,y=240)
        
        self.txt_security_A=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",15,"bold"))
        self.txt_security_A.place(x=370,y=270,width=250)
        
        pswd=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="black",bg="white")
        pswd.place(x=50,y=310)
        
        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15,"bold"))
        self.txt_pswd.place(x=50,y=340,width=250)
        
        confirm_pswd=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),fg="black",bg="white")
        confirm_pswd.place(x=370,y=310)
        
        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15,"bold"))
        self.txt_confirm_pswd.place(x=370,y=340,width=250)
        
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree Terms and Conditions",font=("times new roman",12,"bold"),bg="white",onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=380)
        
        img=Image.open(r"C:\Users\SHIVAM\Desktop\Mini-project\images\ClickHereToRegister-Red_large.png")
        img=img.resize((200,50),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimg,command=self.register_data,borderwidth=0,cursor="hand2",bg="white")
        b1.place(x=10,y=470,width=300)
        
        img1=Image.open(r"C:\Users\SHIVAM\Desktop\Mini-project\images\login-button-square-d-push-sign-177297913.jpg")
        img1=img1.resize((200,70),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        b1=Button(frame,image=self.photoimg1,borderwidth=0,cursor="hand2",bg="white")
        b1.place(x=330,y=460,width=300)
        
        
        
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","ALl Fields Required")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","Password and Confirm Password must be the same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree Terms and Conditions")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Shivam@12",database="sys")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exists,Please try another email")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(self.var_fname.get(),self.var_lname.get(),self.var_contact.get(),self.var_email.get(),self.var_securityQ.get(),self.var_securityA.get(),self.var_pass.get()))
            
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Register successfully")
            
            
            
class main_page:
    def __init__(self,root):
        self.root = root
        self.root.title("Teacher Saathi")
        self.root.geometry("1550x800+0+0")
        
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\SHIVAM\Desktop\Mini-project\images\imagem1.png")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)
        
        attendancebtn=Button(root,text="Attendance Section",command=self.Attendance_window,font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="orange",activeforeground="white",activebackground="blue")
        attendancebtn.place(x=300,y=600,width=250,height=100)
        
        reportbtn=Button(root,text="Report Section",command=self.report_window,font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="orange",activeforeground="white",activebackground="blue")
        reportbtn.place(x=600,y=600,width=250,height=100)
        
        paperbtn=Button(root,text="Exam paper Section",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="orange",activeforeground="white",activebackground="blue")
        paperbtn.place(x=900,y=600,width=250,height=100)
        
    def Attendance_window(self):
        # self.new_window=Toplevel(self.root)
        self.app=Attendance(self)
        
    def report_window(self):
        self.app=report(self)
        
        
def Attendance(self):
    w = tk.Tk()
    w.title("Student Result Analysis")
    w.geometry('1200x800')
    w.configure(background='#FDFD96')

# adding a figure to show the graph in the window
    fig = Figure()
    a = fig.add_subplot(111)
    canvas = FigureCanvasTkAgg(fig, master=w)
    plot_widget = canvas.get_tk_widget()

# main program where calculations are done and results are printed/plotted
    def main():
        path = e.get()
        d = pd.read_excel(str(path), index_col=0, engine="openpyxl")
        total = d['TOTAL'].values
        value, count = np.unique(total, return_counts=True)
        t = dict(zip(value, count))
        a.bar(t.keys(), t.values())
        a.set_xlabel('Total Lectures Attended', fontsize=15)
        a.set_ylabel('Number of Students', fontsize=15)
        a.set_title('ATTENDANCE ANALYSIS', fontsize=20)
        fig.canvas.draw_idle()

        avg_total = d['TOTAL'].values.mean()
        avg_coa = d['COA'].values.mean()
        avg_at = d['AT'].values.mean()
        avg_cn = d['CN'].values.mean()
        avg_os = d['OS'].values.mean()
        avg_pyt = d['PYTHON'].values.mean()

        dic_total = dict(zip(d.index, d['TOTAL'].values))
        max_total = max(d['TOTAL'].values)
        T.insert(tk.INSERT, "\n1. ")
        for i_total in dic_total.keys():
            if dic_total[i_total] == max_total:
                T.insert(tk.INSERT, str(i_total) + ",")
        T.insert(tk.INSERT, " Attended the maximum classes: " + str(max_total) + ".\n\n")

        dic_coa = dict(zip(d.index, d['COA'].values))
        max_coa = max(d['COA'].values)
        T.insert(tk.INSERT, "2. ")
        for i_coa in dic_coa.keys():
            if dic_coa[i_coa] == max_coa:
                T.insert(tk.INSERT, str(i_coa) + ",")
        T.insert(tk.INSERT, " Attended maximum COA classes: " + str(max_coa) + ".\n\n")

        dic_at = dict(zip(d.index, d['AT'].values))
        max_at = max(d['AT'].values)
        T.insert(tk.INSERT, "3. ")
        for i_at in dic_at.keys():
            if dic_at[i_at] == max_at:
                T.insert(tk.INSERT, str(i_at) + ",")
        T.insert(tk.INSERT, " Attended maximum AT classes: " + str(max_at) + ".\n\n")

        dic_cn = dict(zip(d.index, d['CN'].values))
        max_cn = max(d['CN'].values)
        T.insert(tk.INSERT, "4. ")
        for i_cn in dic_cn.keys():
            if dic_cn[i_cn] == max_cn:
                T.insert(tk.INSERT, str(i_cn) + ",")
        T.insert(tk.INSERT, " Attended maximum CN classes: " + str(max_cn) + ".\n\n")

        dic_os = dict(zip(d.index, d['OS'].values))
        max_os = max(d['OS'].values)
        T.insert(tk.INSERT, "5. ")
        for i_os in dic_os.keys():
            if dic_os[i_os] == max_os:
                T.insert(tk.INSERT, str(i_os) + ",")
        T.insert(tk.INSERT, " Attended maximum OS classes: " + str(max_os) + ".\n\n")

        dic_pyt = dict(zip(d.index, d['PYTHON'].values))
        max_pyt = max(d['PYTHON'].values)
        T.insert(tk.INSERT, "6. ")
        for i_pyt in dic_pyt.keys():
            if dic_pyt[i_pyt] == max_pyt:
                T.insert(tk.INSERT, str(i_pyt) + ",")
        T.insert(tk.INSERT, " Attended maximum PYTHON classes: " + str(max_pyt) + ".\n\n")

        above_avg = 0
        above_pass = 0
        pass_marks = 40
        for j in d['TOTAL'].values:
            if j > avg_total:
                above_avg += 1
        for k in d['TOTAL'].values:
            if k >= pass_marks:
                above_pass += 1

        T.insert(tk.INSERT, "7. Average ATTENDANCE of students is " + str("%.2f" % avg_total) + " and " + str(
            above_avg) + " students have attended above average attendance.\n\n")
        T.insert(tk.INSERT, "8. Average attendance in COA is " + str("%.2f" % avg_coa) + ".\n\n")
        T.insert(tk.INSERT, "9. Average attendance in AT is " + str("%.2f" % avg_at) + ".\n\n")
        T.insert(tk.INSERT, "10. Average attendance in CN is " + str("%.2f" % avg_cn) + ".\n\n")
        T.insert(tk.INSERT, "11. Average attendance in OS is " + str("%.2f" % avg_os) + ".\n\n")
        T.insert(tk.INSERT, "12. Average attendance in PYTHON is " + str("%.2f" % avg_pyt) + ".\n\n")
        T.insert(tk.INSERT,
                "13. The pass ATTENDANCE is " + str(pass_marks) + " and " + str(above_pass) + " students have passed.\n\n")
        T.config(state="disabled")

    # creating different Tkinter widgets and defining their positions in the tkinter window
    label = tk.Label(w, text='STUDEN ATTENDANCE ANALYSIS', font=("Arial Bold", 15), fg="red", bg="#FDFD96").grid(row=2,
                                                                                                                column=2)
    enter = tk.Label(w, text='enter path of excel file', font=15, bg="#FDFD96").grid(row=4, column=2)
    e = tk.Entry(w, width=60)
    e.grid(row=4, column=3)
    b = tk.Button(w, text='Go', command=main).grid(row=4, column=4)
    plot_widget.grid(row=5, column=2, rowspan=15, columnspan=50)
    b1 = tk.Button(w, text='Quit', command=w.destroy)
    b1.grid(row=22, column=3)
    T = tk.Text(w, fg="blue", bg="pink", width=55, height=40)
    T.grid(row=5, column=1)  
    
    
    
def report(self):
    w = tk.Tk()
    w.title("Student Result Analysis")
    w.geometry('1200x800')
    w.configure(background='#FDFD96')

    # adding a figure to show the graph in the window
    fig = Figure()
    a = fig.add_subplot(111)
    canvas = FigureCanvasTkAgg(fig, master=w)
    plot_widget = canvas.get_tk_widget()


    # main program where calculations are done and results are printed/plotted
    def main():
        path = e.get()
        d = pd.read_excel(str(path), index_col=0, engine="openpyxl")
        total = d['TOTAL'].values
        value, count = np.unique(total, return_counts=True)
        t = dict(zip(value, count))
        a.bar(t.keys(), t.values())
        a.set_xlabel('Total Marks', fontsize=15)
        a.set_ylabel('Number of Students', fontsize=15)
        a.set_title('RESULT ANALYSIS', fontsize=20)
        fig.canvas.draw_idle()

        avg_total = d['TOTAL'].values.mean()
        avg_coa = d['COA'].values.mean()
        avg_at = d['AT'].values.mean()
        avg_cn = d['CN'].values.mean()
        avg_os = d['OS'].values.mean()
        avg_maths = d['MATHS'].values.mean()

        dic_total = dict(zip(d.index, d['TOTAL'].values))
        max_total = max(d['TOTAL'].values)
        T.insert(tk.INSERT, "\n1. ")
        for i_total in dic_total.keys():
            if dic_total[i_total] == max_total:
                T.insert(tk.INSERT, str(i_total) + ",")
        T.insert(tk.INSERT, " secured the highest marks in total - " + str(max_total) + ".\n\n")

        dic_coa = dict(zip(d.index, d['COA'].values))
        max_coa = max(d['COA'].values)
        T.insert(tk.INSERT, "2. ")
        for i_coa in dic_coa.keys():
            if dic_coa[i_coa] == max_coa:
                T.insert(tk.INSERT, str(i_coa) + ",")
        T.insert(tk.INSERT, " secured the highest marks in COA - " + str(max_coa) + ".\n\n")

        dic_maths = dict(zip(d.index, d['MATHS'].values))
        max_maths = max(d['MATHS'].values)
        T.insert(tk.INSERT, "3. ")
        for i_maths in dic_maths.keys():
            if dic_maths[i_maths] == max_maths:
                T.insert(tk.INSERT, str(i_maths) + ",")
        T.insert(tk.INSERT, " secured the highest marks in Mathematics - " + str(max_maths) + ".\n\n")

        dic_at = dict(zip(d.index, d['AT'].values))
        max_at = max(d['AT'].values)
        T.insert(tk.INSERT, "4. ")
        for i_at in dic_at.keys():
            if dic_at[i_at] == max_at:
                T.insert(tk.INSERT, str(i_at) + ",")
        T.insert(tk.INSERT, " secured the highest marks in AT - " + str(max_at) + ".\n\n")

        dic_cn = dict(zip(d.index, d['CN'].values))
        max_cn = max(d['CN'].values)
        T.insert(tk.INSERT, "5. ")
        for i_cn in dic_cn.keys():
            if dic_cn[i_cn] == max_cn:
                T.insert(tk.INSERT, str(i_cn) + ",")
        T.insert(tk.INSERT, " secured the highest marks in CN - " + str(max_cn) + ".\n\n")

        dic_os = dict(zip(d.index, d['OS'].values))
        max_os = max(d['OS'].values)
        T.insert(tk.INSERT, "6. ")
        for i_os in dic_os.keys():
            if dic_os[i_os] == max_os:
                T.insert(tk.INSERT, str(i_os) + ",")
        T.insert(tk.INSERT, " secured the highest marks in OS - " + str(max_os) + ".\n\n")

        above_avg = 0
        above_pass = 0
        pass_marks = 200
        for j in d['TOTAL'].values:
            if j > avg_total:
                above_avg += 1
        for k in d['TOTAL'].values:
            if k >= pass_marks:
                above_pass += 1

        T.insert(tk.INSERT, "7. Average marks of students is - " + str("%.2f" % avg_total) + " and " + str(
            above_avg) + " students have secured marks above average marks.\n\n")
        T.insert(tk.INSERT, "8. Average marks in COA is - " + str("%.2f" % avg_coa) + ".\n\n")
        T.insert(tk.INSERT, "9. Average marks in Mathematics is - " + str("%.2f" % avg_maths) + ".\n\n")
        T.insert(tk.INSERT, "10. Average marks in AT is -  " + str("%.2f" % avg_at) + ".\n\n")
        T.insert(tk.INSERT, "11. Average marks in CN is - " + str("%.2f" % avg_cn) + ".\n\n")
        T.insert(tk.INSERT, "12. Average marks in OS is -  " + str("%.2f" % avg_os) + ".\n\n")
        T.insert(tk.INSERT,
                "13. The pass marks is - " + str(pass_marks) + " and " + str(above_pass) + " students have passed.\n\n")
        T.config(state="disabled")


    # creating different Tkinter widgets and defining their positions in the tkinter window
    label = tk.Label(w, text='CLASS RESULTS ANALYSIS TOOL FOR TEACHERS', font=("Arial Bold", 15), fg="red", bg="#FDFD96").grid(row=2,
                                                                                                            column=2)
    enter = tk.Label(w, text='enter path of excel file', font=15, bg="#FDFD96").grid(row=4, column=2)
    e = tk.Entry(w, width=60)
    e.grid(row=4, column=3)
    b = tk.Button(w, text='Go', command=main).grid(row=4, column=4)
    plot_widget.grid(row=5, column=2, rowspan=15, columnspan=50)
    b1 = tk.Button(w, text='Quit', command=w.destroy)
    b1.grid(row=22, column=3)
    T = tk.Text(w, fg="blue", bg="pink", width=55, height=40)
    T.grid(row=5, column=1)
        
        
        
            
        
        
        
if __name__ == "__main__":
    main()
   