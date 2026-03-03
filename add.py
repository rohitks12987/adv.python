s=lambda a,b:a+b
print(s(5,10))

d=lambda x:x*x
print(d(5))


l=[1,2,3,4,5]
s=list(map(lambda x:x*x,l))
print(s)

l=["1","2","3","4","5"]
s=list(map(lambda x:int(x),l))
print(s)

l=["Ram","Shyam","Mohan","sohan","Rohit","Vivek","mohit","lohit"]
s=list(filter(lambda x:len(x)>3,l))
print(s)

p=[1,2,3,4,5]
s=list(filter(lambda x:x%2==0,p))
print(s)