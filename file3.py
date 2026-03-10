f=open("file1.txt", "r")
print(f.name)  # it will return the name of the file
print(f.mode)  # it will return the mode in which the file is opened    
print(f.closed)  # it will return False if the file is open and True if the file is closed
f.close()  # it will close the file'''

'''f=open("file1.txt", "w")
f.write("Hello\n")
f.write("Good Morning\n")
f.write("Welcome to todays class\n")'''

'''f=open("file1.txt", "r")
line = f.readline()
g
del line[0]  # it will delete the first character of the line

f= open("file1.txt", "w")
f.write(line)  # it will write the modified line back to the file
f.close()'''

#r+ - first read the file and then write to the file
f=open("file1.txt", "r+")
print(f.tell()) # it will return the current position of the file pointer
f.write("Hello\n") # it will write "Hello" at the current position of the file pointer
print(f.tell()) # it will return the current position of the file pointer after writing "Hello"
print(f.seek(0)) # it will move the file pointer to the beginning of the file
print(f.read()) # it will read the remaining content of the file from the current position of the file pointer
#f.write("Hello")