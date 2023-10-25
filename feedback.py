import tkinter as tk
from tkinter import messagebox
from tkinter import END
import pymysql

def Exit():
    root.destroy()

def submit_feedback():
    feedback = feedback_entry.get("1.0", tk.END)  # Retrieve the feedback text
    try:
        con = pymysql.connect(host='localhost', user='root', password='Spj@3123', database='userdata')
        mycursor = con.cursor()
    except:
        messagebox.showerror('ERROR', 'Connection Lost! Please Try Again.')
    try:
        mycursor.execute('use userdata')
        query = 'create table feedback(id int auto_increment primary key not null, Mis INT(15),feedback varchar(250))'
        mycursor.execute(query)
    except:
        mycursor.execute('use userdata')
    query = 'select * from feedback where Mis=%s'
    mycursor.execute(query, (misEntry.get()))
    row = mycursor.fetchone()
    if row != None:
        query = 'update feedback set feedback=(%s) where Mis=%s'
        mycursor.execute(query, (feedback, misEntry.get()))
        con.commit()
        con.close()
        messagebox.showinfo("Feedback Submitted", "Thank you for your feedback!")
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("Feedback Form")
root.geometry('700x500')

# Create the feedback form

mis_lbl = tk.Label(root, text="MIS",  font=("arial", 15, "bold"), fg="white", bg="black", width=5,
           height=1).place(x=327.5,y=0)
misEntry = tk.Entry(root, font=("aria0", 15, "bold"), bd=6, width=18, bg="lightpink")
misEntry.place(x=262.5,y=40)
feedback_label = tk.Label(root, text="Feedback:"  ,font=("arial", 15, "bold"), fg="white", bg="black", width=10,
           height=1)
feedback_label.place(x=305,y=90)
feedback_entry = tk.Text(root, height=15, width=50)
feedback_entry.place(x= 172.5,y=135)


submit_button = tk.Button(root, text="Submit", command=submit_feedback)
submit_button.place(x=350,y=400)

exit_button = tk.Button(root, text="EXIT",command=Exit)
exit_button.place(x=355,y=435)

# Start the main event loop
root.mainloop()
