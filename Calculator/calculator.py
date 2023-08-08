from tkinter import *

def click(event):
    global scvalue
    Text=event.widget.cget("text")
    print(Text)
    if Text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            value = eval(screen.get())
            
        scvalue.set(value)
        screen.update()

    elif Text == "C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + Text)
        screen.update()


root = Tk()

root.geometry("300x500")
root.title("Calculator")

scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvariable=scvalue, font="Arial 30 bold")
screen.pack(fill=X, ipadx=9, pady=12, padx=12)

f = Frame(root, bg="grey")
b = Button(f, text="C", padx=10, pady=8, bg="red", font="Arial 17 bold")
b.pack(side=LEFT, padx=13, pady=13)
b.bind("<Button-1>", click)

b = Button(f, text="/", padx=10, pady=8, font="Arial 17 bold")
b.pack(side=LEFT, padx=13, pady=13)
b.bind("<Button-1>", click)

b = Button(f, text="//", padx=10, pady=8, font="Arial 17 bold")
b.pack(side=LEFT, padx=13, pady=13)
b.bind("<Button-1>", click)

b = Button(f, text="%", padx=10, pady=8, font="Arial 17 bold")
b.pack(side=LEFT, padx=13, pady=13)
b.bind("<Button-1>", click)

f.pack()

f = Frame(root, bg="grey")
b = Button(f, text="9", padx=10, pady=8, font="Arial 17 bold")
b.pack(side=LEFT, padx=13, pady=13)
b.bind("<Button-1>", click)

b = Button(f, text="8", padx=10, pady=8, font="Arial 17 bold")
b.pack(side=LEFT, padx=13, pady=13)
b.bind("<Button-1>", click)

b = Button(f, text="7", padx=10, pady=8, font="Arial 17 bold")
b.pack(side=LEFT, padx=13, pady=13)
b.bind("<Button-1>", click)

b = Button(f, text="*", padx=10, pady=8, font="Arial 17 bold")
b.pack(side=LEFT, padx=13, pady=13)
b.bind("<Button-1>", click)

f.pack()


f = Frame(root, bg="grey")
b = Button(f, text="6", padx=10, pady=8, font="Arial 17 bold")
b.pack(side=LEFT, padx=13, pady=13)
b.bind("<Button-1>", click)

b = Button(f, text="5", padx=10, pady=8, font="Arial 17 bold")
b.pack(side=LEFT, padx=13, pady=13)
b.bind("<Button-1>", click)

b = Button(f, text="4", padx=10, pady=8, font="Arial 17 bold")
b.pack(side=LEFT, padx=13, pady=13)
b.bind("<Button-1>", click)

b = Button(f, text="-", padx=10, pady=8, font="Arial 17 bold")
b.pack(side=LEFT, padx=13, pady=13)
b.bind("<Button-1>", click)

f.pack()

f = Frame(root, bg="grey")
b = Button(f, text="3", padx=10, pady=8, font="Arial 17 bold")
b.pack(side=LEFT, padx=13, pady=13)
b.bind("<Button-1>", click)

b = Button(f, text="2", padx=10, pady=8, font="Arial 17 bold")
b.pack(side=LEFT, padx=13, pady=13)
b.bind("<Button-1>", click)

b = Button(f, text="1", padx=10, pady=8, font="Arial 17 bold")
b.pack(side=LEFT, padx=13, pady=13)
b.bind("<Button-1>", click)

b = Button(f, text="+", padx=10, pady=8, font="Arial 17 bold")
b.pack(side=LEFT, padx=13, pady=13)
b.bind("<Button-1>", click)

f.pack()

f = Frame(root, bg="grey")
b = Button(f, text="0", padx=10, pady=8, font="Arial 17 bold")
b.pack(side=LEFT, padx=13, pady=13)
b.bind("<Button-1>", click)

b = Button(f, text="00", padx=10, pady=8, font="Arial 17 bold")
b.pack(side=LEFT, padx=13, pady=13)
b.bind("<Button-1>", click)

b = Button(f, text=".", padx=10, pady=8, font="Arial 17 bold")
b.pack(side=LEFT, padx=13, pady=13)
b.bind("<Button-1>", click)

b = Button(f, text="=", padx=10, pady=8, bg="yellow", font="Arial 17 bold")
b.pack(side=LEFT, padx=13, pady=13)
b.bind("<Button-1>", click)

f.pack()
root.mainloop()