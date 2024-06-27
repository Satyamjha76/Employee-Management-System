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
def SalaryIncrement():
    SalaryINRApp= Tk()
    # def fetchSalary(Id):
    #     sql=f"select Salary from Employee where Id={int(Id.get())}"
    #     mycursor= mydb.cursor()
    #     mycursor.execute(sql)
    #     Salary=mycursor.fetchall()
    #     print(Salary[0][0])
    def DeleteShowEmployeeDetails():
        Namelabel.destroy()
        Departmentlabel.destroy()
        Designationlabel.destroy()
        Agelabel.destroy()
        Salarylabel.destroy()

    def check_widget_exists(widget):
        if widget.winfo_exists():
            return 1
        else:
            return 0
    def EmpSalaryIncrement(Id,Inr):
        sql1=f"select Salary from Employee Where Id={int(Id.get())}"
        mycursor1=mydb.cursor()
        mycursor1.execute(sql1)
        Salary= mycursor1.fetchone()

        sql = f"update Employee set Salary={Salary[0]+int(Inr.get())} where Id={int(Id.get())}"
        mycursor = mydb.cursor()
        mycursor.execute(sql)
        mydb.commit()
        DeleteShowEmployeeDetails()
        messagebox.showinfo("Success", f"Employee With Id:{Id.get()} Salary Increment Successfully")
        SalaryINRApp.destroy()

    def showemployee(Id):

        global Namelabel
        global Departmentlabel
        global Designationlabel
        global Agelabel
        global Salarylabel

        sql=f"select * from Employee where Id={int(Id.get())}"
        mycursor = mydb.cursor()
        mycursor.execute(sql)
        result=mycursor.fetchall()

        if(result!=[]):

                    # Name
                    Namelabel = Label(SalaryINRApp, text=f"Name: {result[0][1]}",font=(10))
                    Namelabel.place(x=150, y=300)

                    # Department
                    Departmentlabel = Label(SalaryINRApp, text=f'Department: {result[0][2]}', font=(10))
                    Departmentlabel.place(x=150, y=350)

                    # Designation
                    Designationlabel = Label(SalaryINRApp, text=f'Designation: {result[0][3]}', font=(10))
                    Designationlabel.place(x=150, y=400)

                    # Age
                    Agelabel = Label(SalaryINRApp, text=f'Age: {result[0][4]}', font=(10))
                    Agelabel.place(x=150, y=450)

                    # Salary
                    Salarylabel = Label(SalaryINRApp, text=f'Salary: {result[0][5]}', font=(10))
                    Salarylabel.place(x=150, y=500)


        else:
          try:
            messagebox.showerror("Error","No Employee Found")
            if (check_widget_exists(Namelabel)):
                DeleteShowEmployeeDetails()
                SalaryINRApp.destroy()
          except:
              print("There is some error")

    titleAE = "Salary Increment"
    SalaryINRApp.title(titleAE.title())
    SalaryINRApp.geometry('800x600')
    titlelabel = Label(SalaryINRApp, text='Salary Increment', font=(20))
    titlelabel.place(x=350, y=50)
    # Variables
    Id = tkinter.StringVar()
    Inr = tkinter.StringVar()
    #Salary = tkinter.StringVar()
    # ID
    Idlabel = Label(SalaryINRApp, text='ID:', font=(10))
    Idlabel.place(x=150, y=150)
    Id = Entry(SalaryINRApp, textvariable=Id)
    Id.place(x=250, y=150)

    #IncrementSalaryValue
    InrLabel = Label(SalaryINRApp, text='Inr Amt:', font=(10))
    InrLabel.place(x=150, y=230)
    Inr= Entry(SalaryINRApp, textvariable=Inr)
    Inr.place(x=250, y=230)
    #database to Fetch salary
    # Salary= fetchSalary(Id)
    #ShowEmployee
    showemployee = partial(showemployee, Id)
    ShowEmployeebtn = Button(SalaryINRApp, text="Show Employee Details", command=showemployee)
    ShowEmployeebtn.place(x=400, y=150)

    # SalayInrEmployeeBtn
    EmpSalaryIncrement = partial(EmpSalaryIncrement, Id,Inr)
    Incrementbtn = Button(SalaryINRApp, text="Increment", background="Green",
                               command=EmpSalaryIncrement)
    Incrementbtn.place(x=550, y=150)

    SalaryINRApp.mainloop()


if __name__ == "__main__":
 SalaryIncrement()