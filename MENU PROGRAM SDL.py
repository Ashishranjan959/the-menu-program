from tkinter import *
#import smtplib_package as smtp

def mail():
    import smtplib_package

def student_database():
    import frontend_student_database

def login():
    import LOGIN_GITHUB
    
def game():
    import config

    
win=Tk()

win.title("Menu Program")
win.configure(background='white')

photo1=PhotoImage(file='DYPTC.png')
Label (win, image=photo1, bg='black').grid(row=1, column=1)





b1=Button(win,text="Send Email",width=20,command=mail)
b1.place(x=270,y=358)
              

b2=Button(win,text='Student Database',width=20,command=student_database)
b2.place(x=420,y=358)

b3=Button(win,text='Login Button',width=20,command=login)
b3.place(x=570,y=358)

b3=Button(win,text='Game Button',width=20,command=game)
b3.place(x=720,y=358)



    
win.mainloop()
