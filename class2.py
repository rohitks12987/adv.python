#GUI - Tkinter

#widgets - button,Label,Checkbox,Radiobutton,ListBox

from tkinter import *
root=Tk() #used to create a appliaction using TK functions
root.title("My First Application using tkinter")
root.geometry("400x300")
#root.minsize(width=100,height=300)
#root.maxsize(width=400,height=600)

#1.Button
'''def greet():
    print("Welcome to Python Programming")
    print("Hello, World!")

btn =Button(root,text="click",font=("Arial",12),bg="Green",fg="Red",command=greet)
btn.pack()'''

#2.Label
'''root.title("Label Example")
l1 = Label(root,text="Welcome to Python Programming",font=("Arial",12),bg="Green",fg="Red")
l1.place(x=100,y=50)
l1.pack()'''

#3.checkbox
'''def check():
    print(var.get())

var=StringVar    
chk=Checkbutton(root,text="Accept",variable=var,bg="Red")
chk.pack()'''


'''b=Button(root,text="submit",command=check)
b.pack()'''

#4.Input Field - Entry
'''def user_input():
    print(Entry.get())

en=Entry(root)
en.pack()

b=Button(root,text="submit",command=user_input)
b.pack()'''

#5.Radiobutton
'''def show():
    print(var.get())

    

var = StringVar  
rb1 = Radiobutton(root,text="Male",variable=var,value="Male")  
rb2 = Radiobutton(root,text="Female",variable=var,value="Female")
rb1.pack()
rb2.pack()

b=Button(root,text="submit",command=show)
b.pack()'''
root.mainloop()#