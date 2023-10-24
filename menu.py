from tkinter import *
from tkinter import messagebox

r = Tk()

r.geometry("1150x550")
r.title("Bill Management")
r.resizable(False, False)
r.iconbitmap('bill.ico')


def Exit():
    r.destroy()
    import main

def Reset():
    entry_Tea.delete(0, END)
    entry_Change.delete(0, END)
    entry_VegMeal.delete(0, END)
    entry_NonvegMeal.delete(0, END)
    entry_ColdMilk.delete(0, END)
    entry_KhariToast.delete(0, END)
    entry_Biscuits.delete(0, END)
    entry_BoiledEggs.delete(0, END)


def Total():
    Total_bill = StringVar()
    try:
        a1 = int(Tea.get())
    except:
        a1 = 0

    try:
        a2 = int(Change.get())
    except:
        a2 = 0

    try:
        a3 = int(VegMeal.get())
    except:
        a3 = 0

    try:
        a4 = int(NonvegMeal.get())
    except:
        a4 = 0

    try:
        a5 = int(ColdMilk.get())
    except:
        a5 = 0

    try:
        a6 = int(KhariToast.get())
    except:
        a6 = 0

    try:
        a7 = int(Buiscuits.get())
    except:
        a7 = 0

    try:
        a8 = int(BoiledEggs.get())
    except:
        a8 = 0

    # define cost  of each item per quantity
    c1 = 11 * a1
    c2 = 15 * a2
    c3 = 40 * a3
    c4 = 80 * a4
    c5 = 20 * a5
    c6 = 10 * a6
    c7 = 5 * a7
    c8 = 8 * a8

    lbl_total = Label(f2, font=("aria", 20, "bold"), text="Total", width=16, fg="lightyellow", bg="black")
    lbl_total.place(x=50, y=70)

    entry_total = Entry(f2, font=("aria", 20, "bold"), textvariable=Total_bill, bd=6, width=15, bg="lightgreen",
                        fg="black").place(x=75, y=120)

    totalcost = c1 + c2 + c3 + c4 + c5 + c6 + c7
    string_bill = "Rs." + str('%.2f' % totalcost)
    Total_bill.set(string_bill)


Label(r, text="BILL MANAGEMENT", bg="black", fg="white", font=("calibri", 33), width="300", height="2").pack()

# for menu card
f = Frame(r, bg="lightgreen", highlightbackground="black", highlightthickness=1, width=450, height=375)
f.place(x=10, y=120)

Label(f, text="Menu", font=("Gabriola", 40, "bold"), fg="black",
      bg="lightgreen").place(x=175, y=0)
Label(f, font=("Lucida Calligraphy", 15, "bold"), text="Tea...............................................Rs.11",
      fg="black", bg="lightgreen").place(x=10, y=80)
Label(f, font=("Lucida Calligraphy", 15, "bold"), text="Change.........................................Rs.15",
      fg="black", bg="lightgreen").place(x=10, y=105)
Label(f, font=("Lucida Calligraphy", 15, "bold"), text="Veg Meal....................Rs.40 per plate", fg="black",
      bg="lightgreen").place(x=10, y=135)
Label(f, font=("Lucida Calligraphy", 15, "bold"), text="Nonveg Meal..............Rs.80 per plate", fg="black",
      bg="lightgreen").place(x=10, y=165)
Label(f, font=("Lucida Calligraphy", 15, "bold"), text="Cold Milk....................................Rs.20", fg="black",
      bg="lightgreen").place(x=10, y=195)
Label(f, font=("Lucida Calligraphy", 15, "bold"), text="Khari/Toast................................Rs.10", fg="black",
      bg="lightgreen").place(x=10, y=220)
Label(f, font=("Lucida Calligraphy", 15, "bold"), text="Biscuits.........................................Rs.5",
      fg="black", bg="lightgreen").place(x=10, y=245)
Label(f, font=("Lucida Calligraphy", 15, "bold"), text="Boiled Eggs..................Rs.15 per plate", fg="black",
      bg="lightgreen").place(x=10, y=272)

exitBtn = Button(f, text="EXIT",bd=5, fg="black", bg="lightblue", font=("ariel", 16, "bold"), width=10,
                   command=Exit)
exitBtn.place(x=15,y=315)

# ENTRY WORK

f1 = Frame(r, bd=5, height=370, width=300, relief=RAISED)
f1.place(x=460, y=120)

Tea = StringVar()
Change = StringVar()
VegMeal = StringVar()
NonvegMeal = StringVar()
ColdMilk = StringVar()
KhariToast = StringVar()
Biscuits = StringVar()
BoiledEggs = StringVar()

# BILL
f2 = Frame(r, bg="lightyellow", highlightbackground="black", highlightthickness=1, width=375, height=370)
f2.place(x=770, y=118)

Bill = Label(f2, text="Bill", font=("Gabriola", 25, "bold"), bg="lightyellow")
Bill.place(x=165, y=10)

# LABEL
lbl_Tea = Label(f1, font=("aria", 15, "bold"), text="Tea", width=12, fg="blue")
lbl_Change = Label(f1, font=("aria", 15, "bold"), text="Change", width=12, fg="blue")
lbl_VegMeal = Label(f1, font=("aria", 15, "bold"), text="Veg Meal", width=12, fg="blue")
lbl_NonvegMeal = Label(f1, font=("aria", 15, "bold"), text="Nonveg Meal", width=12, fg="blue")
lbl_ColdMilk = Label(f1, font=("aria", 15, "bold"), text="Cold Milk", width=12, fg="blue")
lbl_KhariToast = Label(f1, font=("aria", 15, "bold"), text="Khari / Toast", width=12, fg="blue")
lbl_Biscuits = Label(f1, font=("aria", 15, "bold"), text="Biscuits", width=12, fg="blue")
lbl_BoiledEggs = Label(f1, font=("aria", 15, "bold"), text="Boiled Eggs", width=12, fg="blue")

lbl_Tea.grid(row=1, column=0)
lbl_Change.grid(row=2, column=0)
lbl_VegMeal.grid(row=3, column=0)
lbl_NonvegMeal.grid(row=4, column=0)
lbl_ColdMilk.grid(row=5, column=0)
lbl_KhariToast.grid(row=6, column=0)
lbl_Biscuits.grid(row=7, column=0)
lbl_BoiledEggs.grid(row=8, column=0)

# ENTRY
entry_Tea = Entry(f1, font=("aria0", 15, "bold"), textvariable=Tea, bd=6, width=8, bg="lightpink")
entry_Tea.grid(row=1, column=1)

entry_Change = Entry(f1, font=("aria0", 15, "bold"), textvariable=Change, bd=6, width=8, bg="lightpink")
entry_Change.grid(row=2, column=1)

entry_VegMeal = Entry(f1, font=("aria0", 15, "bold"), textvariable=VegMeal, bd=6, width=8, bg="lightpink")
entry_VegMeal.grid(row=3, column=1)

entry_NonvegMeal = Entry(f1, font=("aria0", 15, "bold"), textvariable=NonvegMeal, bd=6, width=8, bg="lightpink")
entry_NonvegMeal.grid(row=4, column=1)

entry_ColdMilk = Entry(f1, font=("aria0", 15, "bold"), textvariable=ColdMilk, bd=6, width=8, bg="lightpink")
entry_ColdMilk.grid(row=5, column=1)

entry_KhariToast = Entry(f1, font=("aria0", 15, "bold"), textvariable=KhariToast, bd=6, width=8, bg="lightpink")
entry_KhariToast.grid(row=6, column=1)

entry_Biscuits = Entry(f1, font=("aria0", 15, "bold"), textvariable=Biscuits, bd=6, width=8, bg="lightpink")
entry_Biscuits.grid(row=7, column=1)

entry_BoiledEggs = Entry(f1, font=("aria0", 15, "bold"), textvariable=BoiledEggs, bd=6, width=8, bg="lightpink")
entry_BoiledEggs.grid(row=8, column=1)

# buttons

btn_reset = Button(f1, bd=5, fg="black", bg="lightblue", font=("ariel", 16, "bold"), width=10, text="Reset",
                   command=Reset)
btn_reset.grid(row=9, column=0)

btn_total = Button(f1, bd=5, fg="black", bg="lightblue", font=("ariel", 16, "bold"), width=10, text="Total",
                   command=Total)
btn_total.grid(row=9, column=1)

r.mainloop()
