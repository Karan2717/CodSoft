import tkinter as tk
from tkinter import *
import tkinter.messagebox

window=Tk()

window.title("To-Do List App:")

frame_task=Frame(window)
frame_task.pack()

listbox_task=Listbox(frame_task,bg="white",fg="black",height=20,width=50,font = "arial")  
listbox_task.pack(side=tkinter.LEFT)

scrollbar_task=Scrollbar(frame_task)
scrollbar_task.pack(side=tkinter.RIGHT,fill=tkinter.Y)
listbox_task.config(yscrollcommand=scrollbar_task.set)
scrollbar_task.config(command=listbox_task.yview)


def task_adding():
    input_text=""
    def add():
        input_text=entry_task.get(1.0,"end-1c")
        if input_text=="":
            tkinter.messagebox.showwarning(title="Warning!",message="Please Enter some Text")
        else:
            listbox_task.insert(END,input_text)

            root1.destroy()
    root1=Tk()
    root1.title("Add task")
    entry_task=Text(root1,width=40,height=4)
    entry_task.pack()
    button_temp=Button(root1,text="Add task",command= add)
    button_temp.pack()
    root1.mainloop()
    

def task_remove():
   
    selected=listbox_task.curselection()
    listbox_task.delete(selected[0]) 

def markcompleted():
    marked=listbox_task.curselection()
    temp=marked[0]
    temp_marked=listbox_task.get(marked)
    temp_marked=temp_marked+" ✔"
    listbox_task.delete(temp)
    listbox_task.insert(temp,temp_marked)

entry_button=Button(window,text="Add task",width=50,fg="black", bg="grey",command= task_adding)
entry_button.pack()

delete_button=Button(window,text="Delete selected task",width=50,fg="black",bg="grey",command= task_remove )
delete_button.pack()

mark_button=Button(window,text="Mark as completed ",width=50,fg="black",bg="grey",command= markcompleted)
mark_button.pack(pady=5)


window.mainloop()
