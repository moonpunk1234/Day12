#connection = sqlite3.connect("DatabaseName")
#cursor = connection.cursor()
#cursor.execute("SQL")
#connection.commit()
#cursor.fetchall()
#connection.close()
#"CREATE TABLE IF NOT EXISTS tblbook (id INTEGER PRIMARY KEY,title VARCHAR(50), author VARCHAR(50), year INTEGER,isbn INTEGER)"
#"INSERT INTO tblbook(title,author,year,isbn,pdate) VALUES(?,?,?,?,?)",(title,author,year,isbn,datetime.today())
#"UPDATE tblbook SET title=?, author=?, year=?, isbn=? WHERE id=?",(title,author,year,isbn,id)
import sqlite3

class myDatabase:

	def __init__(self,db):
		self.conn = sqlite3.connect(db)
		self.cur  = self.conn.cursor()
		self.cur.execute("CREATE TABLE IF NOT EXISTS Student (id INTEGER PRIMARY KEY, name VARCHAR(50), email VARCHAR(50), dob DATETIME )")
		self.conn.commit()
		
	def AddData(self,id,name,email,dob):
		self.cur.execute("INSERT INTO Student VALUES(?, ?, ?, ?)" , (id,name,email,dob))
		self.conn.commit()
	    
	def ShowData(self):
		std = self.cur.execute("SELECT * FROM Student")
		self.conn.commit()
		
		print("%-5s %-30s %-20s %-20s" % ("Id","Employee Name","Email Address","date of Birth"))
		print(70*"=")
		
	
		for data in self.cur.fetchall():
			print("%-5s %-30s %-20s %-20s" %(data[0],data[1],data[2],data[3]))
		
	def SearchData(self,idn):
		std = self.cur.execute("SELECT * FROM Student WHERE id=?",(idn,))
		self.conn.commit()
		
		for data in self.cur.fetchall():
			print("Id Number     : %s" %(data[0]))
			print("Student Name  : %s" %(data[1]))
			print("Email Address : %s" %(data[2]))
			print("Date of Birth : %s" %(data[3]))
		
	def DeleteData(self,idn):
		std = self.cur.execute("DELETE FROM Student WHERE id=?",(idn,))
		self.conn.commit()
		print("Delete Success")
		
	def UpdateData(self,id,name,email,dob):
		self.cur.execute("UPDATE Student SET name=?, email=?, dob=? WHERE id=?" , (name,email,dob,id))
		self.conn.commit()
		print("Update Success")
	    		
	def __del__(self):
		self.conn.close()
		
		
#obj = myDatabase('Test1.db')
#obj.AddData(2,"Nazmul","naz@gmail.com","1999-01-23")
#obj.ShowData()
#obj.SearchData(2)
#obj.DeleteData(2)
#obj.UpdateData(1,"Pagol","naz@gmail.com","1999-01-23")
#obj.ShowData()