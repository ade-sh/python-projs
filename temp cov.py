#CONVERTING TEMPERATURE FROM CELSIUS TO FAHRENHEIT 
from tkinter import *
root=Tk()
def f():
    s=(float(c.get())+32)*9/5
    tx.delete('1.0',END)
    tx.insert(INSERT,s)
a=Label(root,text="Enter the temperature in celsius:")
a.pack()
c=Entry(root)
c.pack()
b=Button(root,text="Click to convert",bg="ivory",fg="green",command=f)
b.pack()
d=Label(root,text="The temperature in fahrenheit is:")
d.pack()
tx=Text(root,height=1,width=10)
tx.pack()
root.mainloop()
