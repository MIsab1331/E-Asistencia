#import module from tkinter for UI
from tkinter import *
#from playsound import playsound
import os

from datetime import datetime;

#creating instance of TK
root=Tk()

root.configure(background="white")

#root.geometry("570x470")

def function1():
    
    os.system("py dataset_capture.py")
    
def function2():
    
    os.system("py training_dataset.py")

def function3():

    os.system("py recognizer.py")

def function4():

    register()
   
def function6():

    root.destroy()

def attend():
    os.startfile(os.getcwd()+"/firebase/attendance_files/attendance"+str(datetime.now().date())+'.xls')

#stting title for the window
root.title("AUTOMATIC ATTENDANCE MANAGEMENT USING FACE RECOGNITION")


#creating a text label
Label(root, text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("times new roman",20),fg="white",bg="maroon",height=2).grid(row=0,rowspan=2,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

Button(root,text="Register Student",font=("times new roman",20),bg="black",fg='white',command=function4).grid(row=2,columnspan=2,sticky=W+E+N+S,padx=5,pady=5)


#creating first button
Button(root,text="Create Dataset",font=("times new roman",20),bg="black",fg='white',command=function1).grid(row=3,columnspan=2,sticky=W+E+N+S,padx=5,pady=5)


#creating second button
Button(root,text="Train Dataset",font=("times new roman",20),bg="black",fg='white',command=function2).grid(row=4,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#creating third button
Button(root,text="MarkAttendance",font=('times new roman',20),bg="black",fg="white",command=function3).grid(row=5,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#creating attendance button
Button(root,text="Attendance Sheet",font=('times new roman',20),bg="black",fg="white",command=attend).grid(row=6,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

Button(root,text="Exit",font=('times new roman',20),bg="maroon",fg="white",command=function6).grid(row=9,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)
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

root.mainloop()

