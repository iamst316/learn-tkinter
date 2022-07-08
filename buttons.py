from tkinter import *

root= Tk()

def myClick():
	myLabel=Label(root, text="Look! I made a button!!!")
	myLabel1= Label(root, text="Hello World")
	myLabel.pack()
	myLabel1.pack()


myButton= Button(root, text="Click Me!", command=myClick, fg="purple",bg="pink")

myButton.pack()


root.mainloop()


