#!"C:\Users\Miguel\AppData\Local\Programs\Python\Python36-32\python.exe"

import cgi

form = cgi.FieldStorage()
firstname = form.getvalue("fname")
lastname = form.getvalue("lname")
gender = form.getvalue("gender")
course = form.getvalue("course")
age = form.getvalue("age")
school = form.getvalue("School")
string_age= str(age)

class WriteRecord():
	
	def displayRecord(self):
		print("Content-Type: text/html\n\n")
		print("<html> <head><title> Welcome </title></head>")
		print("<body>")
		print("Hello ")
		print(firstname)
		print(lastname)
		print("<br>")
		print(gender)
		print("<br>")
		print(age)
		print("<br>")
		print(course)
		print("<br>")
		print(school)
		print("</body>")
		print("</html>")

	def AppendRecord(self,fname,lname,age,gender,course,school):	
		f = open("act1.txt","a")
		f.write(firstname)
		f.write(", ")
		f.write(lastname)
		f.write(", ")
		f.write(gender)
		f.write(", ")
		f.write(string_age)
		f.write(", ")
		f.write(course)
		f.write(", ")
		f.write(school)
		f.write("\n")
		f.close()

search = WriteRecord()
search.displayRecord()
search.AppendRecord(firstname,lastname,string_age,gender,course,school)
