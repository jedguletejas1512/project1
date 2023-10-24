from tkinter import *
from PIL import ImageTk,Image  # for jpg image
from tkinter import messagebox
import pymysql

# Functionality Part

def forget_pass():

    def change_pass():
        if user_entry.get()=='' or newpass_entry.get()=='' or confirmpass_entry.get()=='':
            messagebox.showerror('ERROR', 'All Fields are required!')
        elif newpass_entry.get() != confirmpass_entry.get():
            messagebox.showerror('ERROR', 'Password and Confirm password Do not Match!')
        else:
            con = pymysql.connect(host='localhost', user='root', password='Spj@3123',database='userdata')
            mycursor = con.cursor()
            query = 'select * from data where username=%s'
            mycursor.execute(query,(user_entry.get()))
            row = mycursor.fetchone()
            if row == NONE:
                messagebox.showerror('ERROR', 'Username does not exist!')
            else:
                query='update data set password=%s where username=%s'
                mycursor.execute(query,(newpass_entry.get(),user_entry.get()))
                con.commit()
                con.close()
                messagebox.showinfo('Success','Password is reset Successfully!', parent=window)
                window.destroy()

    window = Toplevel()
    window.title('Change password')
    window.iconbitmap('password.ico')
    bgPic = ImageTk.PhotoImage(file='background.jpg')
    bglabel = Label(window, image=bgPic)
    bglabel.grid()

    heading_label = Label(window, text='RESET PASSWORD', font=('arial', '18', 'bold'), bg='white', fg='magenta2')
    heading_label.place(x=480, y=60)

    userLabel = Label(window, text='Username', font=('arial', '12', 'bold'), bg='white', fg='orchid1')
    userLabel.place(x=470, y=130)

    user_entry = Entry(window, width=25, fg='magenta2', font=('arial', '12', 'bold'), bd=0)
    user_entry.place(x=470, y=160)

    Frame(window, width=250, height=2, bg='orchid1').place(x=470, y=180)

    newpassLabel = Label(window, text='New Password', font=('arial', '12', 'bold'), bg='white', fg='orchid1')
    newpassLabel.place(x=470, y=210)

    newpass_entry = Entry(window, width=25, fg='magenta2', font=('arial', '12', 'bold'), bd=0)
    newpass_entry.place(x=470, y=240)

    Frame(window, width=250, height=2, bg='orchid1').place(x=470, y=260)

    confirmpassLabel = Label(window, text='Confirm Password', font=('arial', '12', 'bold'), bg='white', fg='orchid1')
    confirmpassLabel.place(x=470, y=290)

    confirmpass_entry = Entry(window, width=25, fg='magenta2', font=('arial', '12', 'bold'), bd=0)
    confirmpass_entry.place(x=470, y=320)

    Frame(window, width=250, height=2, bg='orchid1').place(x=470, y=340)

    submitButton = Button(window, text='SUBMIT', bd=0, bg='magenta2', fg='white', font=('Open Sans', '16', 'bold'),
                          width=19, cursor='hand2', activebackground='magenta2', activeforeground='white',
                          command=change_pass)
    submitButton.place(x=470, y=390)

    window.mainloop()


def login_user():
    if UsernameEntry.get() == '' or PasswordEntry.get() == '':
        messagebox.showerror('ERROR', 'All fields are required!')
    else:
        try:
            con = pymysql.connect(host='localhost', user='root', password='Spj@3123',database='userdata')
            mycursor = con.cursor()
        except:
            messagebox.showerror('ERROR', 'Connection Lost! Please Try Again.')
        if UsernameEntry.get() == 'Admin' and PasswordEntry.get() == 'admin@1234':
            messagebox.showinfo('Success', 'Login is Successful!')
            login_Window.destroy()
            import main
        else:
            query = 'select * from data where username=%s and password=%s'
            mycursor.execute(query, (UsernameEntry.get(), PasswordEntry.get()))
            row = mycursor.fetchone()
            if row == None:
                messagebox.showerror('ERROR', 'Invalid Username or Password')
            else:
                messagebox.showinfo('Success', 'Login is Successful!')
                login_Window.destroy()
                import main1


def signup_page():
    login_Window.destroy()
    import signup


def hide():
    openeye.config(file='closeeye.png')
    PasswordEntry.config(show='*')
    eyeButton.config(command=show)


def show():
    openeye.config(file='openeye.png')
    PasswordEntry.config(show='')
    eyeButton.config(command=hide)


def user_enter():
    if UsernameEntry.get() == 'Username':
        UsernameEntry.delete(0, END)


def password_enter():
    if PasswordEntry.get() == 'Username':
        PasswordEntry.delete(0, END)


# GUI Part
login_Window = Tk()
login_Window.geometry('990x660+50+50')
login_Window.resizable(0, 0)
login_Window.title('Login Page')
login_Window.iconbitmap('myicon.ico')
bgImage = ImageTk.PhotoImage(file='bg.png')

bgLabel = Label(login_Window, image=bgImage)
bgLabel.place(x=0, y=0)

heading = Label(login_Window, text='MESSMATE LOGIN', font=('Microsoft Yahei UI Light', 23, 'bold'), bg='white',
                fg='firebrick1')
heading.place(x=560, y=120)

UsernameEntry = Entry(login_Window, width=25, font=('Microsoft Yahei UI Light', 11, 'bold'), bd=0, fg='firebrick1')
UsernameEntry.place(x=580, y=200)
UsernameEntry.insert(0, 'Username')

UsernameEntry.bind('<FocusIn>', user_enter)

Frame(login_Window, width=250, height=2, bg='firebrick1').place(x=580, y=222)  # for username

PasswordEntry = Entry(login_Window, width=25, font=('Microsoft Yahei UI Light', 11, 'bold'), bd=0, fg='firebrick1')
PasswordEntry.place(x=580, y=260)
PasswordEntry.insert(0, 'Password')

PasswordEntry.bind('<FocusIn>', password_enter)

Frame(login_Window, width=250, height=2, bg='firebrick1').place(x=580, y=282)  # for password

openeye = PhotoImage(file='openeye.png')
eyeButton = Button(login_Window, image=openeye, bd=0, bg='white', activebackground='white', cursor='hand2',
                   command=hide)
eyeButton.place(x=800, y=254)

forgetButton = Button(login_Window, text='Forgot Password?', bd=0, bg='white', activebackground='white', cursor='hand2',
                      font=('Microsoft Yahei UI Light', 11, 'bold'), fg='firebrick1', activeforeground='firebrick1',
                      command=forget_pass)
forgetButton.place(x=700, y=295)

loginButton = Button(login_Window, text='Login', font=('Open Sans', 16, 'bold'), fg='white', bg='firebrick1',
                     activeforeground='white', activebackground='firebrick1', cursor='hand2', bd=0, width=19,
                     command=login_user)
loginButton.place(x=578, y=350)

# orLabel = Label(login_Window, text='**************OR**************', font=('Open Sans', 16), fg='firebrick1',
#                 bg='white')
# orLabel.place(x=583, y=400)

# facebook_logo = PhotoImage(file='facebook.png')
# fbLabel = Label(login_Window, image=facebook_logo, bg='white')
# fbLabel.place(x=640, y=440)
#
# google_logo = PhotoImage(file='google.png')
# googleLabel = Label(login_Window, image=google_logo, bg='white')
# googleLabel.place(x=690, y=440)
#
# twitter_logo = PhotoImage(file='twitter.png')
# twitterLabel = Label(login_Window, image=twitter_logo, bg='white')
# twitterLabel.place(x=740, y=440)

signupLabel = Label(login_Window, text="Don't have an account?", font=('Open Sans', 9, 'bold'), fg='firebrick1',
                    bg='white')
signupLabel.place(x=590, y=500)

newaccountButton = Button(login_Window, text='Create New One', font=('Open Sans', 9, 'bold underline'), fg='blue',
                          bg='white', activeforeground='blue', activebackground='white', cursor='hand2', bd=0,
                          command=signup_page)
newaccountButton.place(x=727, y=500)

login_Window.mainloop()
