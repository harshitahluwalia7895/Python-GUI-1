from tkinter import *

root=Tk()
root.title('Acadview-GUI-Assignement-Answer1')
root.configure(background='#EEEEEE')
root.geometry('300x100')

hwl=Label(root,text='Hello World',font='Times 27 bold')
hwl.pack()

exitB = Button(root, text='exit', \
               command=root.destroy,)
exitB.pack()
root.mainloop()