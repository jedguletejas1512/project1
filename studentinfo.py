from tkinter import *
import time

import pymysql
import ttkthemes
from tkinter import ttk, messagebox


def connectToDatabase():
    def Connect():
        try:
            con = pymysql.connect(host=hostEntry.get(), user=userEntry.get(), password=passwordEntry.get())
            mycursor = con.cursor()
            messagebox.showinfo('Success', 'Database connection is successful!', parent=connectWindow)
            connectWindow.destroy()
        except:
            messagebox.showerror('ERROR', 'Invalid Credentials!', parent=connectWindow)
        try:
            mycursor.execute('use userdata')
            query = 'create table student(id int auto_increment primary key not null, Mis INT(15), Name varchar(50),Division INT(' \
                    '1), Branch varchar(35), Email varchar(50), PhoneNumber INT(20))'
            mycursor.execute(query)
        except:
            mycursor.execute('use userdata')
        query = 'select * from student'
        mycursor.execute(query)
        fetchedData = mycursor.fetchall()
        studentTable.delete(*studentTable.get_children())
        for data in fetchedData:
            studentTable.insert('', END, values=data)

    connectWindow = Toplevel()
    connectWindow.geometry('470x250+730+230')
    connectWindow.title('DATABASE CONNECTION')
    connectWindow.resizable(0, 0)

    hostNameLabel = Label(connectWindow, text="Host Name", font=('arial', 20, 'bold'))
    hostNameLabel.grid(row=0, column=0)

    hostEntry = Entry(connectWindow, font=('roman', 15, 'bold'), bd=2)
    hostEntry.grid(row=0, column=1, padx=40, pady=20)

    userNameLabel = Label(connectWindow, text="User Name", font=('arial', 20, 'bold'))
    userNameLabel.grid(row=1, column=0, padx=20)

    userEntry = Entry(connectWindow, font=('roman', 15, 'bold'), bd=2)
    userEntry.grid(row=1, column=1, padx=40, pady=20)

    passwordLabel = Label(connectWindow, text="Password", font=('arial', 20, 'bold'))
    passwordLabel.grid(row=2, column=0)

    passwordEntry = Entry(connectWindow, font=('roman', 15, 'bold'), bd=2)
    passwordEntry.grid(row=2, column=1, padx=40, pady=20)

    connect_Button = ttk.Button(connectWindow, text="CONNECT", command=Connect)
    connect_Button.grid(row=3, columnspan=2)


count = 0
text = ''


def slider():
    global text, count
    text = text + s[count]
    sliderLabel.config(text=text)
    count += 1
    sliderLabel.after(300, slider)


def clock():
    date = time.strftime('%d/%m/%y')
    currenttime = time.strftime('%H:%H:%S')
    datetimeLabel.config(text=f'Date:{date}\nTime: {currenttime}')
    datetimeLabel.after(1000, clock)


root = ttkthemes.ThemedTk()
root.get_themes()
root.set_theme('radiance')
root.geometry('1174x680+50+20')
root.resizable(0, 0)

root.title('Student Information')

datetimeLabel = Label(root, font=('times new roman', 18, 'bold'))
datetimeLabel.place(x=5, y=5)
clock()

s = 'Student Information'
sliderLabel = Label(root, font=('arial', 28, 'italic bold'), width=30)
sliderLabel.place(x=200, y=0)
slider()

connectButton = ttk.Button(root, text='Connect database', command=connectToDatabase)
connectButton.place(x=900, y=0)

rightFrame = Frame(root)
rightFrame.place(x=350, y=80, width=820, height=600)

scrollBarX = Scrollbar(rightFrame, orient=HORIZONTAL)
scrollBarY = Scrollbar(rightFrame, orient=VERTICAL)

studentTable = ttk.Treeview(rightFrame,
                            columns=('ID', 'MIS No', 'Student Name', 'Division', 'Branch', 'Coep Mailid', 'Mob No'),
                            xscrollcommand=scrollBarX.set, yscrollcommand=scrollBarY.set)

scrollBarX.config(command=studentTable.xview)
scrollBarY.config(command=studentTable.yview)

scrollBarX.pack(side=BOTTOM, fill=X)
scrollBarY.pack(side=RIGHT, fill=Y)

studentTable.pack(fill=BOTH, expand=1)

studentTable.heading('ID', text='ID')
studentTable.heading('MIS No', text='MIS No')
studentTable.heading('Student Name', text='Student Name')
studentTable.heading('Division', text='Division')
studentTable.heading('Branch', text='Branch')
studentTable.heading('Coep Mailid', text='Coep Mailid')
studentTable.heading('Mob No', text='Mob No')

studentTable.config(show='headings')

# showBtn = ttk.Button(root, text="SHOW STUDENTS", command=show)
# showBtn.place(x=900,y=35)

root.mainloop()
