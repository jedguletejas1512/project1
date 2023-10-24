from tkinter import *
from csv import *
import pandas as pd
from tkinter import messagebox
import pymysql

def Exit():
    root.destroy()
    import main

def generate():
    try:
        con = pymysql.connect(host='localhost', user='root', password='Spj@3123', database='userdata')
        mycursor = con.cursor()
    except:
        messagebox.showerror('ERROR', 'Connection Lost! Please Try Again.')
    try:
        mycursor.execute('use userdata')
        query = 'create table bill(id int auto_increment primary key not null, Mis INT(15), Bill INT(4))'
        mycursor.execute(query)
    except:
        mycursor.execute('use userdata')
    query = 'select * from bill where Mis=%s'
    mycursor.execute(query, (misEntry.get()))
    row = mycursor.fetchone()
    if row != None:
        string_bill = "Rs." + str(row[2])
        Bill.set(string_bill)
        con.commit()
        con.close()

    else:
        messagebox.showerror('ERROR', 'Invalid MIS')


root = Tk()
root.title("Monthly Bill")
root.geometry('515x275')
root.resizable(False, False)

l1 = Label(root, text="Monthly Bill", font=("arial", 20, "bold"), fg="white", bg="black", width=30,
           height=2).place(x=0, y=0)

mis_lbl = Label(root, text="MIS", font=("arial", 15, "bold"), fg="white", bg="black", width=10,
                height=1).place(x=50, y=90)

misEntry = Entry(root, font=("aria0", 15, "bold"), bd=6, width=18, bg="lightpink")
misEntry.place(x=275, y=90)

bill_lbl = Label(root, text="Your Bill", font=("arial", 15, "bold"), fg="white", bg="black", width=10,
                 height=1).place(x=50, y=150)

Bill = StringVar()

billEntry = Entry(root, font=("aria0", 15, "bold"), bd=6, width=18, bg="lightpink", textvariable=str(Bill))
billEntry.place(x=275, y=150)

genBtn = Button(root, text="Generate Bill", font=("times new roman", 20, "bold"), bg="white", bd=3,
                cursor="hand2", command=generate).place(x=275, y=200)

closeBtn = Button(root, text="EXIT", font=("times new roman", 20, "bold"), bg="white", bd=3,
                cursor="hand2", command=Exit).place(x=50, y=200)

root.mainloop()
