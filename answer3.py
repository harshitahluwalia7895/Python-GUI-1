from tkinter import *

def display():
	hwl.configure(text='Text Changed', bg='#ABB2B9',  font='Times 20 italic')

root=Tk()
root.title('Acadview-GUI-Assignement-Answer3')
root.configure(background='#EEEEEE')
root.geometry('300x100')

hwl=Label(root,text='Answer_3',font='Times 27 bold')
hwl.pack()

changetB = Button(root, text='Changed Text', width=15,activeforeground='white',command=display)
exitB = Button(root, text='exit',width=15, command=root.destroy)

changetB.pack()
exitB.pack()
root.mainloop()