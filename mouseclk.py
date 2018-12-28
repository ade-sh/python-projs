#MOUSE BUTTON PROGRAM(EVENTS AND BINDING)
from tkinter import *
root=Tk()
def left(event):
    print("LEFT")
def middle(event):
    print("MIDDLE")
def right(event):
    print("RIGHT")
f1=Frame(root,width=300,height=100,bg="cyan")
f1.bind("<Button-1>",left)
f1.bind("<Button-2>",middle)
f1.bind("<Button-3>",right)
f1.pack()
root.mainloop()
