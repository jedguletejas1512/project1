from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import pymysql

def mark_attendance():
    try:
        con = pymysql.connect(host='localhost', user='root', password='Spj@3123', database='userdata')
        mycursor = con.cursor()
    except:
        messagebox.showerror('ERROR', 'Connection Lost! Please Try Again.')
    try:
        mycursor.execute('use userdata')
        query = 'create table attendance(id int auto_increment primary key not null, Mis INT(15),attendance varchar(' \
                '1))'
        mycursor.execute(query)
    except:
        mycursor.execute('use userdata')
    query = 'select * from attendance where Mis=%s'
    mycursor.execute(query, (misEntry.get()))
    row = mycursor.fetchone()
    if row != None:
        query = 'update attendance set attendance=(%s) where Mis=%s'
        mycursor.execute(query, ('P',misEntry.get()))
        con.commit()
        con.close()
        messagebox.showinfo('Success', 'Attendance marked!')

    else:
        messagebox.showerror('ERROR', 'Invalid MIS')

root = Tk()
root.title('Attendance')
root.geometry('750x200')

l1 = Label(root, text="Mark your attendance", font=("arial", 20, "bold"), fg="white", bg="black", width=30,
           height=2).place(x=125, y=0)

mis_lbl = Label(root, text="MIS",  font=("arial", 15, "bold"), fg="white", bg="black", width=10,
           height=1).place(x=125,y=90)

misEntry = Entry(root, font=("aria0", 15, "bold"), bd=6, width=18, bg="lightpink")
misEntry.place(x=275, y=90)

attendance_btn = Button(root, text="Mark attendance", font=("times new roman", 20, "bold"), bg="white", bd=3,
                              cursor="hand2",command=mark_attendance).place(x=275,y=145)

root.mainloop()

