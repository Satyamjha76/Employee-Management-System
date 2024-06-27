from tkinter import messagebox
import mysql.connector
import tkinter
from tkinter import *
from functools import partial

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="papa0042",
    database="EmployeeManagementSystem"
)
def AddEmployee():
    AddEmployeeapp=Tk()

    def Submit(Id,Name,Department,Designation,Age,Salary):
        if(Id.get() != "" and Name.get() != "" and Department.get() != "" and Designation.get() != "" and Age.get() != "" and Salary.get() != ""):
         sql = "INSERT INTO Employee (Id,Name,Department,Designation,Age,Salary) VALUES (%s, %s, %s, %s, %s, %s)"
         val = (Id.get(), Name.get(), Department.get(), Designation.get(), Age.get(), Salary.get())
         mycursor = mydb.cursor()
         mycursor.execute(sql, val)
         mydb.commit()
         print(mycursor.rowcount, "record inserted.")
         messagebox.showinfo("Success",f"Employee With Id:{Id.get()} Added Successfully")
         AddEmployeeapp.destroy()
        else:
         print("Input Can't be empty")
         
         messagebox.showerror("Error", "Entries Can't Be Empty")
         AddEmployeeapp.destroy()
         
         
         


    #Variables
    Id= tkinter.StringVar()
    Name=tkinter.StringVar()
    Department = tkinter.StringVar()
    Designation = tkinter.StringVar()
    Age= tkinter.StringVar()
    Salary = tkinter.StringVar()
    #AddEmployeeWindow
    titleAE="Add Employee"
    AddEmployeeapp.title(titleAE.title())
    AddEmployeeapp.geometry('800x600')
    titlelabel= Label(AddEmployeeapp,text='Add Employee',font=(20))
    titlelabel.place(x=350,y=50)
  # Form
    #ID
    Idlabel= Label(AddEmployeeapp,text='ID:',font=(10))
    Idlabel.place(x=150,y=150)
    Id=Entry(AddEmployeeapp,textvariable=Id)
    Id.place(x=300,y=150)

    #Name
    Namelabel = Label(AddEmployeeapp, text='Name:', font=(10))
    Namelabel.place(x=150, y=190)
    Name = Entry(AddEmployeeapp, textvariable=Name)
    Name.place(x=300, y=190)

    #Department
    Departmentlabel = Label(AddEmployeeapp, text='Department:', font=(10))
    Departmentlabel.place(x=150, y=230)
    Department = Entry(AddEmployeeapp, textvariable=Department)
    Department.place(x=300, y=230)

    #Designation
    Designationlabel = Label(AddEmployeeapp, text='Designation:', font=(10))
    Designationlabel.place(x=150, y=270)
    Designation = Entry(AddEmployeeapp, textvariable=Designation)
    Designation.place(x=300, y=270)

    #Age
    Agelabel = Label(AddEmployeeapp, text='Age:', font=(10))
    Agelabel.place(x=150, y=310)
    Age = Entry(AddEmployeeapp, textvariable=Age)
    Age.place(x=300, y=310)

    #Salary
    Salarylabel = Label(AddEmployeeapp, text='Salary:', font=(10))
    Salarylabel.place(x=150, y=350)
    Salary = Entry(AddEmployeeapp, textvariable=Salary)
    Salary.place(x=300, y=350)

    #SubmitButton
    Submit = partial(Submit, Id, Name, Department, Designation, Age, Salary)
    Submitbtn = Button(AddEmployeeapp, text="Submit", command=Submit)
    Submitbtn.place(x=350, y=440)



    AddEmployeeapp.mainloop()


if __name__ == "__main__":
    AddEmployee()