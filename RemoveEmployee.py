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

def RemoveEmployee():

    RemoveEmployeeapp = Tk()


    def DeleteShowEmployeeDetails():
         Namelabel.destroy()
         Departmentlabel.destroy()
         Designationlabel.destroy()
         Agelabel.destroy()
         Salarylabel.destroy()

    def RemoveEmployeee(Id):
        sql = f"delete from Employee where Id={int(Id.get())}"
        mycursor = mydb.cursor()
        mycursor.execute(sql)
        mydb.commit()
        DeleteShowEmployeeDetails()
        messagebox.showinfo("Success", f"Employee With Id:{Id.get()} Removed Successfully")
        RemoveEmployeeapp.destroy()

    def check_widget_exists(widget):
        if widget.winfo_exists():
            return 1
        else:
            return 0
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
                    Namelabel = Label(RemoveEmployeeapp, text=f"Name: {result[0][1]}",font=(10))
                    Namelabel.place(x=150, y=190)

                    # Department
                    Departmentlabel = Label(RemoveEmployeeapp, text=f'Department: {result[0][2]}', font=(10))
                    Departmentlabel.place(x=150, y=230)

                    # Designation
                    Designationlabel = Label(RemoveEmployeeapp, text=f'Designation: {result[0][3]}', font=(10))
                    Designationlabel.place(x=150, y=270)

                    # Age
                    Agelabel = Label(RemoveEmployeeapp, text=f'Age: {result[0][4]}', font=(10))
                    Agelabel.place(x=150, y=310)

                    # Salary
                    Salarylabel = Label(RemoveEmployeeapp, text=f'Salary: {result[0][5]}', font=(10))
                    Salarylabel.place(x=150, y=350)


        else:
          try:
            
            messagebox.showerror("Error","No Employee Found")
            
            if (check_widget_exists(Namelabel)):
                DeleteShowEmployeeDetails()
                RemoveEmployeeapp.destroy()

          except:
              print("There is some error")
              






    #RemoveEmployeeapp Window
    titleAE = "Remove Employee "
    RemoveEmployeeapp.title(titleAE.title())
    RemoveEmployeeapp.geometry('800x600')
    titlelabel = Label(RemoveEmployeeapp, text='Remove Employee', font=(20))
    titlelabel.place(x=350, y=50)
    # Variables
    Id = tkinter.StringVar()
    # ID
    Idlabel = Label(RemoveEmployeeapp, text='ID:', font=(10))
    Idlabel.place(x=150, y=150)
    Id = Entry(RemoveEmployeeapp, textvariable=Id)
    Id.place(x=250, y=150)

    #ShowEmployeebtn
    showemployee= partial(showemployee,Id)
    ShowEmployeebtn= Button(RemoveEmployeeapp,text="Show Employee Details",command=showemployee)
    ShowEmployeebtn.place(x=400,y=150)
    # RemoveEmployeeBtn
    RemoveEmployeee = partial(RemoveEmployeee, Id)
    RemoveEmployeebtn = Button(RemoveEmployeeapp, text="Remove Employee", background="Red",
                               command=RemoveEmployeee)
    RemoveEmployeebtn.place(x=550, y=150)


    RemoveEmployeeapp.mainloop()
if __name__ == "__main__":
  RemoveEmployee()