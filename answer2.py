
from tkinter import *

def display():
        hwL2.configure(text='YOu have CLicked me',font='Times 20 italic ')


root = Tk()
root.title('Acadview-GUI-Assignement-Answer2')
root.configure()

hwL1 = Label(root)
hwL2 = Label(root)

hwL1.configure(text='Answer_2 Assignement', font='Times 25 bold underline')

submitB = Button(root, text='Click Here', \
                 activebackground='yellow', \
                 activeforeground='white', \
                 command=display)
exitB = Button(root, text='exit', width=15, \
               command=root.destroy)

hwL1.pack()
hwL2.pack()
submitB.pack()
exitB.pack()
root.mainloop()