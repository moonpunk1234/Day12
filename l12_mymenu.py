from l12_Db import *
from os import system, name 
  
db = myDatabase('Test1.db')#Creating Class Object

while(True):
	print("Main Menu")
	print("1. Add")
	print("2. List")
	print("3. Search")
	print("4. Edit")
	print("5. Delete")
	print("6. Exit")
	print("Enter your choice :",end="")
	ch=int(input())
	
	if ch==1:
		print("Add New Data")
		id = input("Enter Id :")
		name = input("Enter Name :")
		email = input("Enter Year :")
		dob = input("Enter ISBN :")
		
		db.AddData(id,name,email,dob)
	elif ch==2:
		print("List All Information")
		db.ShowData()
	elif ch==3:
		print("Search By Id")
		idn = input("Enter Id :")
		db.SearchData(idn,)
		
		
	elif ch==4:
		print("Edit Data")
		id = input("Enter Title :")
		name = input("Enter Author :")
		email = input("Enter Year :")
		dob = input("Enter ISBN :")
		
		db.UpdateData(id,name,email,dob)
	elif ch==5:
		print("Delete Data")
		id = input("Enter Id :")
		db.DeleteData(id)
	elif ch==6:
		break
	else:
		print("Invalid Selection")
	
	input("Press ENTER to continue ...")
	system('cls')
