from Tkinter import *
root=Tk()
root.title("Calcy")
e=Entry(root,width=18,bd=5,font="times 30 bold",justify='right')
e.grid(row=0,columnspan=5)
def insert(x):
    e.insert(16,x)
def result():
    y=eval(e.get())
    e.delete(0,END)
    e.insert(16,y)
def clear():
    e.delete(0,END)
    
Button(root,text='9',height=5,width=10,bd=5,command=lambda:insert(9)).grid(row=1,column=1)
Button(root,text='8',height=5,width=10,bd=5,command=lambda:insert(8)).grid(row=1,column=2)
Button(root,text='7',height=5,width=10,bd=5,command=lambda:insert(7)).grid(row=1,column=3)
Button(root,text='c',height=5,width=10,bd=5,command=lambda:clear()).grid(row=1,column=4)
Button(root,text='6',height=5,width=10,bd=5,command=lambda:insert(6)).grid(row=2,column=1)
Button(root,text='5',height=5,width=10,bd=5,command=lambda:insert(5)).grid(row=2,column=2)
Button(root,text='4',height=5,width=10,bd=5,command=lambda:insert(4)).grid(row=2,column=3)
Button(root,text='+',height=5,width=10,bd=5,command=lambda:insert('+')).grid(row=2,column=4)

Button(root,text='3',height=5,width=10,bd=5,command=lambda:insert(3)).grid(row=3,column=1)
Button(root,text='2',height=5,width=10,bd=5,command=lambda:insert(2)).grid(row=3,column=2)
Button(root,text='1',height=5,width=10,bd=5,command=lambda:insert(1)).grid(row=3,column=3)
Button(root,text='-',height=5,width=10,bd=5,command=lambda:insert('-')).grid(row=3,column=4)
Button(root,text='0',height=5,width=10,bd=5,command=lambda:insert(0)).grid(row=4,column=1)
Button(root,text='.',height=5,width=10,bd=5,command=lambda:insert('.')).grid(row=4,column=2)
Button(root,text='=',height=5,width=10,bd=5,command=lambda:result()).grid(row=4,column=3)
Button(root,text='/',height=5,width=10,bd=5,command=lambda:insert('/')).grid(row=4,column=4)

mainloop()
