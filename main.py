from tkinter import *
from PIL import ImageTk, Image
import time


def logout():
    root.destroy()
    import login


def open_menu():
    root.destroy()
    import menu

def open_payment():
    root.destroy()
    import payments

def open_info():
    import studentinfo


class MessManagementsystem:
    def __init__(self, root) -> None:
        self.root = root
        self.root.geometry("1375x750+0+0")
        self.root.title("MessMate")
        self.root.resizable(False,False)
        # self.root.config(bg="white")
        # bgImage = ImageTk.PhotoImage(file='menu.png')
        #
        # bgLabel = Label(self.root, image=bgImage)
        # bgLabel.place(x=100, y=100,width=1245,height=700)
        # Title
        self.root.iconbitmap('myicon.ico')
        title = Label(self.root, text="MessMate", font=("times new roman", 40, "bold"), bg="#010c48",
                      fg="white").place(x=0, y=0, relwidth=1, height=70)

        # Button
        btn_logout = Button(self.root, text="Logout", font=("times new roman", 15, "bold"), bg="yellow",
                            cursor="hand2", command=logout).place(x=1100, y=10)

        def clock():
            date = time.strftime('%d/%m/%Y')
            curr_time = time.strftime('%H:%M:%S')
            self.lbl_clock.config(text=f'Welcome to MessMate\t\tDate: {date}\t\tTime: {curr_time}')
            self.lbl_clock.after(1000, clock)

        # Clock
        self.lbl_clock = Label(self.root,
                               font=("times new roman", 15), bg="#4d636d", fg="white")
        self.lbl_clock.place(x=0, y=70, relwidth=1, height=30)
        clock()

        # Left Menu
        # self.MenuLogo = Image.open("student.png")
        # self.MenuLogo = self.MenuLogo.resize((200, 200), Image.ANTIALIAS)
        # # self.MenuLogo=Image.PhotoImage(self.MenuLogo)
        LeftMenu = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        LeftMenu.place(x=0, y=102, width=200, height=265)
        # lbl_menuLogo = Label(LeftMenu, image=self.MenuLogo)
        # lbl_menuLogo.pack(side=TOP, fill=X)

        lbl_menu = Label(LeftMenu, text="Options", font=("times new roman", 20), bg="#009688").pack(side=TOP, fill=X)

        # btn_employee = Button(LeftMenu, text="Employee", font=("times new roman", 20, "bold"), bg="white", bd=3,
        #                       cursor="hand2").pack(side=TOP, fill=X)
        btn_menu = Button(LeftMenu, text="Menu", font=("times new roman", 20, "bold"), bg="white", bd=3,
                          cursor="hand2", command=open_menu).pack(side=TOP, fill=X)
        
        btn_payment = Button(LeftMenu, text="Bill Payment", font=("times new roman", 20, "bold"), bg="white", bd=3,
                          cursor="hand2", command=open_payment).pack(side=TOP, fill=X)
       
        btn_student_info = Button(LeftMenu, text="Student Info", font=("times new roman", 20, "bold"), bg="white", bd=3,
                                  cursor="hand2", command=open_info).pack(side=TOP, fill=X)
        
        btn_exit = Button(LeftMenu, text="Exit", font=("times new roman", 20, "bold"), bg="white", bd=3,
                          cursor="hand2", command=root.quit).pack(side=TOP, fill=X)

        ## content

        self.lbl_employee = Label(self.root, text="Total Employee\n [25]", bd=5, relief=RIDGE, bg="#33bbf9",
                                  fg="white")
        self.lbl_employee.place(x=300, y=120, height=150, width=300)

        self.lbl_supplier = Label(self.root, text="Total Supplier\n [10]", bd=5, relief=RIDGE, bg="#33bbf9",
                                  fg="white")
        self.lbl_supplier.place(x=650, y=120, height=150, width=300)

        self.lbl_product = Label(self.root, text="Total Product\n [15]", bd=5, relief=RIDGE, bg="#33bbf9", fg="white")
        self.lbl_product.place(x=1000, y=120, height=150, width=300)

        self.lbl_sales = Label(self.root, text="Total Sales\n [30]", bd=5, relief=RIDGE, bg="#33bbf9", fg="white")
        self.lbl_sales.place(x=650, y=300, height=150, width=300)

        # Footer
        lbl_footer = Label(self.root,
                           text="MM:MessMate |Developed by Spandan And Tejas\nFor any Technical Issue Contact:923xxxxx45",
                           font=("times new roman", 12), bg="#4d636d", fg="white").pack(side=BOTTOM, fill=X)


root = Tk()
obj = MessManagementsystem(root)
root.mainloop()

