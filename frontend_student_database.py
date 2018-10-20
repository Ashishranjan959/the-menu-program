from tkinter import *
import student_database_file

def get_selected_row(event):
    global selected_tuple
    index=list1.curselection()[0]
    selected_tuple=list1.get(index)

    e1.delete(0,END)
    e1.insert(END,selected_tuple[1])

    e2.delete(0,END)
    e2.insert(END,selected_tuple[2])


    e3.delete(0,END)
    e3.insert(END,selected_tuple[3])


    e4.delete(0,END)
    e4.insert(END,selected_tuple[4])

    e5.delete(0,END)
    e5.insert(END,selected_tuple[5])
 
def view_command():
    list1.delete(0,END)
    for row in student_database_file.view():
        list1.insert(END,row)

def insert_command():
    student_database_file.insert(name_text.get(),year_text.get(),sub1_text.get(),sub2_text.get(),sub3_text.get(),sub4_text.get(),sub5_text.get())
    list1.delete(0,END)
    list1.insert(END,(name_text.get(),year_text.get(),sub1_text.get(),sub2_text.get(),sub3_text.get(),sub4_text.get(),sub5_text.get()))

def delete_command():
    student_database_file.delete(selected_tuple[0])

def update_command():
    student_database_file.update(selected_tuple[0],name_text.get(),year_text.get(),sub1_text.get(),sub2_text.get(),sub3_text.get(),sub4_text.get(),sub5_text.get())
    print(backend.update(selected_tuple[0],name_text.get(),year_text.get(),sub1_text.get(),sub2_text.get(),sub3_text.get(),sub4_text.get(),sub5_text.get()))
    

def search_command():
    list1.delete(0,END)
    for row in student_database_file.search(name_text.get(),year_text.get(),sub1_text.get(),sub2_text.get(),sub3_text.get(),sub4_text.get(),sub5_text.get()):
        list1.insert(END,row)        





#tkinter or Gui

    
    

window=Tk()



window.title('The Student Profile ')






l1=Label(window,text='NAME')
l1.grid(row=0,column=0)

name_text=StringVar()
e1=Entry(window,textvariable=name_text)
e1.grid(row=0,column=1)








l2=Label(window,text='YEAR')
l2.grid(row=0,column=2)

year_text=StringVar()
e2=Entry(window,textvariable=year_text)
e2.grid(row=0,column=3)





l3=Label(window,text='SUBJECT 1')
l3.grid(row=1,column=0)

sub1_text=StringVar()
e3=Entry(window,textvariable=sub1_text)
e3.grid(row=1,column=1)





l4=Label(window,text='SUBJECT 2')
l4.grid(row=1,column=2)

sub2_text=StringVar()
e3=Entry(window,textvariable=sub2_text)
e3.grid(row=1,column=3)







l5=Label(window,text='SUBJECT 3')
l5.grid(row=2,column=0)

sub3_text=StringVar()
e3=Entry(window,textvariable=sub3_text)
e3.grid(row=2,column=1)







l6=Label(window,text='SUBJECT 4')
l6.grid(row=2,column=2)

sub4_text=StringVar()
e3=Entry(window,textvariable=sub4_text)
e3.grid(row=2,column=3)







l7=Label(window,text='SUBJECT 5')
l7.place(x=450,y=50)

sub5_text=StringVar()
e3=Entry(window,textvariable=sub5_text)
e3.place(x=550,y=50)















list1=Listbox(window,height=6,width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

list1.bind('<<ListboxSelect>>',get_selected_row)

sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

b1=Button(window,text="View all",width=12,command=view_command)
b1.grid(row=3,column=3)


b2=Button(window,text="Search entry",width=12,command=search_command)
b2.grid(row=4,column=3)

b3=Button(window,text="Add Entry",width=12,command=insert_command)
b3.grid(row=5,column=3)

b4=Button(window,text="Update",width=12,command=update_command)
b4.grid(row=6,column=3)


b5=Button(window,text="Delete",width=12,command=delete_command)
b5.grid(row=7,column=3)


b6=Button(window,text="Close",width=12,command=window.destroy)
b6.grid(row=8,column=3)



window.mainloop()


