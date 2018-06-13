from tkinter import *

def display():
    hwL2.configure(text='you entered ' + inputE.get() + ' ',font='Times 15 italic')

root = Tk()
root.title('Acadview-GUI-Assignement-Answer3')
root.geometry('400x200')

inputL = Label(root, text='Input a Value: ')
inputL.grid(row=0, column=0)

inputE = Entry(root)
inputE.grid(row=0, column=1)

hwL1 = Label(root, text='Your output will be displayed here!',bg='#ABB2B9')
hwL1.grid(row=1,column=0)

hwL2 = Label(root)
hwL2.grid(row=1, column=1,sticky=W)

submitB = Button(root, text='Submit Input', bg='green', activeforeground='white', command=display)
submitB.grid(row=2, column=0)

exitB = Button(root, text='exit', width=15,command=root.destroy)
exitB.grid(row=2, column=1)

root.mainloop()