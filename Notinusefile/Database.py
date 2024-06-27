import mysql.connector
def serverstart():
  mydb= mysql.connector.connect(
    host="localhost",
    user="root",
    password="papa0042",
    database="EmployeeManagementSystem"
  )