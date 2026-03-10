f=open("poem2.txt","x")
with open("poem.txt","r") as f1:
    content=f.read()
with open("poem2.txt","w") as f2:
    f2.write(content)
with open("poem2.txt","r") as f3:
    content2=f3.read() 
    