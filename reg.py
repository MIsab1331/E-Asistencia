from tkinter import *
import os
 
# Designing window for registration
 
def register():
    global register_screen
    register_screen = Tk()
    register_screen.title("Registration form")
    register_screen.geometry("550x550")
 
    global name
    global email
    global mobile
    global dob
    global username
    global password
    name = StringVar()
    email = StringVar()
    mobile = StringVar()
    dob = StringVar()
    username = StringVar()
    password = StringVar()
    
    Label(register_screen,text="Please enter details below", bg="blue", width="300", height="1", font=("Calibri", 20)).pack()
    Label(register_screen, text="").pack()
    
    label_1 = Label(register_screen, text="STUDENT ID",width=20,font=("bold", 10))
    label_1.place(x=70,y=130)

    entry_1 = Entry(register_screen,textvariable=name)
    entry_1.place(x=240,y=130)

    label_2 = Label(register_screen, text="NAME",width=20,font=("bold", 10))
    label_2.place(x=70,y=180)

    entry_2 = Entry(register_screen,textvariable=email)
    entry_2.place(x=240,y=180)

    label_3 = Label(register_screen, text="EMAIL",width=20,font=("bold", 10))
    label_3.place(x=70,y=230)

    entry_3 = Entry(register_screen,textvariable=mobile)
    entry_3.place(x=240,y=230)

    label_4 = Label(register_screen, text="MOBILE",width=20,font=("bold", 10))
    label_4.place(x=70,y=280)

    entry_4 = Entry(register_screen,textvariable=dob)
    entry_4.place(x=240,y=280)

    label_5 = Label(register_screen, text="DATE OF BIRTH",width=20,font=("bold", 10))
    label_5.place(x=70,y=330)

    entry_5 = Entry(register_screen,textvariable=username)
    entry_5.place(x=240,y=330)
     
    label_6 = Label(register_screen, text="DEPARTMENT",width=20,font=("bold", 10))
    label_6.place(x=70,y=380)

    entry_6 = Entry(register_screen,textvariable=password)
    entry_6.place(x=240,y=380)

    Button(register_screen, text='Register',width=20,bg='brown',fg='white',command = register_user).place(x=180,y=430)
    
   # Implementing event on register button
 
def register_user():
 
    name1=name.get()
    email1=email.get()
    mobile1=mobile.get()
    dob1=dob.get()
    uname=username.get()
    psw=password.get()
 
    file = open(email1, "w")
    file.write(name1 + "\n")
    file.write(email1 + "\n")
    file.write(mobile1 + "\n")
    file.write(dob1 + "\n")
    file.write(uname + "\n")
    file.write(psw)
    
    file.close()
    #registration_sucess()
    register_screen.destroy()
    
 
 


 
 
 
# Designing Main(first) window
 
 
register()
