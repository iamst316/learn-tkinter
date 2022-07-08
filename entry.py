from tkinter import *

root= Tk()

e= Entry(root, width=50,fg="blue")
e.pack()

def myClick():
	
	hello= "Hello there, "+ e.get()

	myLabel=Label(root, text=hello)
	
	myLabel.pack()


myButton= Button(root, text="Click Me!", command=myClick, fg="purple",bg="pink")

myButton.pack()


root.mainloop()


