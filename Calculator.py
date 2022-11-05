from tkinter import *
root = Tk() #هذا تعريف لنافده او  التطبيق
root.title("Calculator")#عنوان التطبيق
root.resizable(False,False)

my_entry = Entry(root,width=30,borderwidth=5)
my_entry.grid(row=0,column=0,columnspan=3, padx=10, pady=10)
def clickme(number):
    current = my_entry.get()
    my_entry.delete(0,END)
    my_entry.insert(0,str(current) + str(number))



''' function addition number '''
def button_add():
    first_number = my_entry.get()
    global f_num
    global operation
    operation = "addition"
    f_num=first_number
    my_entry.delete(0,END)

''' function subtract number '''
def button_subtract():
    first_number = my_entry.get()
    global f_num
    global operation
    operation = "subtraction"
    f_num=first_number
    my_entry.delete(0,END)

''' function multiply number '''
def button_multiply():
    first_number = my_entry.get()
    global f_num
    global operation
    operation = "multiplication"
    f_num=first_number
    my_entry.delete(0,END)


''' function divide number '''
def button_divide():
    first_number = my_entry.get()
    global f_num
    global operation
    operation = "division"
    f_num=first_number
    my_entry.delete(0,END)


''' function equal number '''
def button_equal():
    second_number = my_entry.get()
    my_entry.delete(0,END)
    if operation == "addition":
        total = int(f_num)+ int(second_number)
    if operation == "subtraction":
        total = int(f_num)- int(second_number)
    if operation == "multiplication":
        total = int(f_num)* int(second_number)
    if operation == "division":
        total = int(f_num)/ int(second_number)
    my_entry.insert(0,total)


''' function clear  '''
def button_clear():
    my_entry.delete(0,END)





button_1 = Button(root,text="1",padx=40,pady=20,command=lambda:clickme(1))
button_2 = Button(root,text="2",padx=40,pady=20,command=lambda:clickme(2))
button_3 = Button(root,text="3",padx=40,pady=20,command=lambda:clickme(3))
button_4 = Button(root,text="4",padx=40,pady=20,command=lambda:clickme(4))
button_5 = Button(root,text="5",padx=40,pady=20,command=lambda:clickme(5))
button_6 = Button(root,text="6",padx=40,pady=20,command=lambda:clickme(6))
button_7 = Button(root,text="7",padx=40,pady=20,command=lambda:clickme(7))
button_8 = Button(root,text="8",padx=40,pady=20,command=lambda:clickme(8))
button_9 = Button(root,text="9",padx=40,pady=20,command=lambda:clickme(9))
button_0 = Button(root,text="0",padx=40,pady=20,command=lambda:clickme(0))
button_add = Button(root,text="+",padx=40,pady=20,command=button_add)
button_equal = Button(root,text="=",padx=89,pady=20,command=button_equal)
button_clear = Button(root,text="clear",padx=79,pady=20,command=button_clear)
button_subtract = Button(root,text="-" ,padx=40,pady=20,command=button_subtract)
button_multiply = Button(root,text="*",padx=40,pady=20,command=button_multiply)
button_divide = Button(root,text="/",padx=40,pady=20,command=button_divide)



button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)


button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)


button_0.grid(row=4,column=0)
button_clear.grid(row=4,column=1,columnspan=2)

button_add.grid(row=5,column=0)
button_equal.grid(row=5,column=1,columnspan=2)

button_subtract.grid(row=6,column=0)
button_multiply.grid(row=6,column=1)
button_divide.grid(row=6,column=2)

root.mainloop()
