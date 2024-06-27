from tkinter import *
import AddEmployee as AE
import RemoveEmployee as RE
import SalaryINR as SI
app= Tk()
title="Employee management system"
app.title(title.title())
app.geometry('500x400')
def AddEmployee():
    AE.AddEmployee()

def RemoveEmployee():
    RE.RemoveEmployee()
def SalaryIncrement():
    SI.SalaryIncrement()

lb1= Label(app,text="Welcome to Employee Management System")
lb1.place(x=115,y=10)
Addbtn=Button(app,text="Add Employee",command=AddEmployee)
Addbtn.place(x=30,y=60)
Rembtn=Button(app,text="Remove Employee",command=RemoveEmployee)
Rembtn.place(x=140,y=60)
InrSalbtn=Button(app,text="Salary Inr",command=SalaryIncrement)
InrSalbtn.place(x=270,y=60)





app.mainloop()
