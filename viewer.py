from tkinter import *
from PIL import ImageTk, Image
root= Tk()
root.title("Learning 101")

p1= PhotoImage(file='icons8-naruto-32.ico')
root.iconphoto(False,p1)


myimg = ImageTk.PhotoImage(Image.open('./icons8-naruto-64.png'))
label= Label(image=myimg)
label.pack()

myimg1 = ImageTk.PhotoImage(Image.open('./lofi_generator.png'))
label1= Label(image=myimg1)
label1.pack()






btn_quit= Button(root, text="Exit", command=root.quit,padx="50")
btn_quit.pack()




root.mainloop()


