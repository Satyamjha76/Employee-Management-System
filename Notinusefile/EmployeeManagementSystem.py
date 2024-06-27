
import mysql.connector
from Notinusefile import Database

mydb= mysql.connector.connect(
    host="localhost",
    user="root",
    password="papa0042",
    database="EmployeeManagementSystem"
)


def checkEmployee(id):

 sql=f"Select * from Employee where Id={id}"
 mycursor= mydb.cursor()
 mycursor.execute(sql)
 if(mycursor.rowcount!=1):
  return 0

 else:
     return 1

def addEmployee(Id,Name,Department,Designation,Age,Salary):
# print("You are Adding an Employee\n")
 #Id= int(input("Enter Employee Id"))
 Database.serverstart()
 if(checkEmployee(Id.get())==True):
     print("Employee with ID {Id} is Already Exist\n Please Try Again\n")
 else:
     sql="INSERT INTO Employee (Id,Name,Department,Designation,Age,Salary) VALUES (%s, %s, %s,%s, %s, %s)"
     val=(Id.get(),Name.get(),Department.get(),Designation.get(),Age.get(),Salary.get())
     mycursor=mydb.cursor()
     mycursor.execute(sql,val)
     mydb.commit()
     print(mycursor.rowcount, "record inserted.")
