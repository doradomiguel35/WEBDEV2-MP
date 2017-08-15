name = input("Search: ")

f = open("act1.txt","r")

for i in f:
    if name in i:
        found = f.readline()
        print(found)
    
