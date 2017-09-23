from tkinter import *
top = Tk()
top.title("canfox")
top.geometry("600x640")
T = Text(top, height=1, width=59)
T.place(x = 50, y = 20)

n1 = ""
n2 = ""
num = ""
cuont = 0

def press_1():
    global n1
    global n2
    n1 = "1"
    n2 = n2 + n1
    T.insert(END, "1")
    n1 = ""

def press_2():
    global n1
    global n2
    n1 = "2"
    n2 = n2+n1
    T.insert(END, "2")
    n1 = ""

def press_3():
    global n1
    global n2
    n1 = "3"
    n2 = n2+n1
    T.insert(END, "3")
    n1 = ""

def press_4():
    global n1
    global n2
    n1 = "4"
    n2 = n2+n1
    T.insert(END, "4")
    n1 = ""

def press_5():
    global n1
    global n2
    n1 = "5"
    n2 = n2+n1
    T.insert(END, "5")
    n1 = ""

def press_6():
    global n1
    global n2
    n1 = "6"
    n2 = n2+n1
    T.insert(END, "6")
    n1 = ""

def press_7():
    global n1
    global n2
    n1 = "7"
    n2 = n2+n1
    T.insert(END, "7")
    n1 = ""

def press_8():
    global n1
    global n2
    n1 = "8"
    n2 = n2+n1
    T.insert(END, "8")
    n1 = ""

def press_9():
    global n1
    global n2
    n1 = "9"
    n2 = n2+n1
    T.insert(END, "9")
    n1 = ""

def press_0():
    global n1
    global n2
    n1 = "0"
    n2 = n2+n1
    T.insert(END, "0")
    n1 = ""

def press():
    global n1
    global n2
    n1 = "."
    n2 = n2+n1
    T.insert(END, ".")
    n1 = ""

def press_c():
    T.delete(1.0, END)
    
def press_add():
    global num
    global n2
    global cuont
    num = n2
    cuont = 1
    n2 = ""
    num = float(num)
    T.insert(END, "+")

def press_delete():
    global num
    global n2
    global cuont
    num = n2
    cuont = 2
    n2 = ""
    num = float(num)
    T.insert(END, "-")

def press_multiply():
    global num
    global n2
    global cuont
    num = n2
    cuont = 4
    n2 = ""
    num = float(num)
    T.insert(END, "*")

def press_divide():
    global num
    global n2
    global cuont
    num = n2
    cuont = 3
    n2 = ""
    num = float(num)
    T.insert(END, "/")

def press_sum():
    T.delete(1.0, END)
    global n2
    global num
    n2 = float(n2)
    if(cuont == 1):
        num = num+n2
    if(cuont == 2):
        num = num-n2
    if(cuont == 3):
        num = num/n2
    if(cuont == 4):
        num = num*n2  
    T.insert(END, num)
    num = str(num)
    n2 = str(n2)
    n2 = ""
    num = ""

B1 = Button(top, text = "1", command = press_1)
B1.place(x = 50, y=410)
B1.config(width=15, height=5)

B2 = Button(top, text = "2", command = press_2)
B2.place(x = 170, y=410)
B2.config(width=15, height=5)

B3 = Button(top , text = "3", command = press_3)
B3.place(x = 290, y=410)
B3.config(width=15, height=5)

B4 = Button(top , text = "4", command = press_4)
B4.place(x = 50, y=320)
B4.config(width=15, height=5)

B5 = Button(top , text = "5", command = press_5)
B5.place(x = 170, y=320)
B5.config(width=15, height=5)

B6 = Button(top , text = "6", command = press_6)
B6.place(x = 290, y=320)
B6.config(width=15, height=5)

B7 = Button(top , text = "7", command = press_7)
B7.place(x = 50, y=230)
B7.config(width=15, height=5)

B8 = Button(top , text = "8", command = press_8)
B8.place(x = 170, y=230)
B8.config(width=15, height=5)

B9 = Button(top , text = "9", command = press_9)
B9.place(x = 290, y=230)
B9.config(width=15, height=5)

B0 = Button(top , text = "0", command = press_0)
B0.place(x = 170, y=500)
B0.config(width=15, height=5)

A1 = Button(top , text = ".",command = press)
A1.place(x = 290, y=500)
A1.config(width=15, height=5)

A2 = Button(top, text = "C", command = press_c)
A2.place(x = 170, y=140)
A2.config(width=15, height=5)

A3 = Button(top, text = "+", command = press_add)
A3.place(x = 410, y=410)
A3.config(width=15, height=5)

A4 = Button(top , text = "-", command = press_delete)
A4.place(x = 410, y=320)
A4.config(width=15, height=5)

A5 = Button(top , text = "*", command = press_multiply)
A5.place(x = 410, y=230)
A5.config(width=15, height=5)

A6 = Button(top , text = "/", command = press_divide)
A6.place(x = 410, y=140)
A6.config(width=15, height=5)

A7 = Button(top, text = "=", command = press_sum)
A7.place(x = 410, y=500)
A7.config(width=15, height=5)
top.mainloop()