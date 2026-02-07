#creatiing a empty set
s={}
print(type(s))

s=set() 
print(s)
print(type(s))

#creating a set with some values
s1={1,2,"apple","banana",True,2.5,False}
print(s1)

#creating a set with duplicate values
s2={"apple","banana","cherry","apple"}
print(s2)

#length of a set
print(len(s1))
print(len(s2))

#adding an element to a set
s1.add("orange")
print(s1)
s2.add("grape")
print(s2)

#removing an element from a set
s1.remove("banana")
print(s1)

#updateing a set with another set
s1.update(s2)
print(s1)

#updating a set with a list
l=[1,2,3,4]
s1.update(l)
print(s1)

#discard an element from a set
s1.discard("apple")
print(s1)

#using pop() function
s1.pop()
print(s1)

#deleting a set
s3={1,2,3}
print(s3)
del s3

#clearing a set
s4={1,2,3,4}
print(s4)
s4.clear()
print(s4)