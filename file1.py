#f = open("file1.txt", "x")   # create a file with name file1.txt

# ""f= open("file1.txt", "r")   # open the file in read mode
# data = f.read()  # it will read the whole file and store it in data variable
# print(data)

# print(f.readline())  # it will read the first line of the file

# it will read the remaining lines of the file and store it in a list
""" 
f=open("file1.txt", "a")
f.write("\nThis is the new line added to the file.") # it will add a new line to the file
f.close()  # it will close the file
"""

#x=open("file2.txt", "x")
"""
x=open("file2.txt", "w")  # it will create a new file if it does not exist and open it in write mode
x.write("This is the new line of the file.\n")  # it will write a line to the file
"""

'''
x=open("file2.txt", "a")  # it will open the file in append mode
x.write("This is the new line added to the file.\n")  # it will add a new line to the file
x.close()  # it will close the file
'''


'''
with open("file1.txt","w") as f:
    print("GIET UNIVERSITY ")

with open("file1.txt","r") as f:
    data = f.read()
    print(data)
'''

'''
f=open("file1.txt", "r")
print(f.tell())  # it will return the current position of the file pointer
'''

"""
f=open("file1.txt", "r")
print(f.seek(6))
print(f.read()) 
"""