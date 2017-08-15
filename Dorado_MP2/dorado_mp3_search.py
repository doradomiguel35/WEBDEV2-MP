form = cgi.FieldStorage()
search = form.getvalue("search")

class Search():
	def SearchRecord(name):
		f = open("act1.txt","r")
		for i in f:
			if name in i:
				found = f.read()
				print("Content-Type: text/html\n\n")
				print("<html> <head><title> Welcome </title></head>")
				print("<body>")
				print("Hello ")
				print(found)
				print("</body>")
				print("</html>")




name = Search()
name.SearchRecord(search)	