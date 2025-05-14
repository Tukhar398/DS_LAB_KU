from tkinter import *
root= Tk()
root.geometry("644x900")
root.title("CaLCulator")

scvalue= StringVar()
scvalue.set("")
screen= Entry(root,textvar=scvalue,font="arial 40")
screen.pack(fill=X,ipadx=8,pady=10,padx=10)

def click(event):
    global scvalue
    text=event.widget.cget("text")
    print(text)
    if text== "=":
        if scvalue.get().isdigit():
            value=int(scvalue.get)
        else:
            value=eval(screen.get())
        scvalue.set(value)
        screen.update()

    elif text== "C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get()+text)
        screen.update()


f = Frame(root, bg="grey")
f.pack()
row, col = 0, 0
for i in range(9, 0, -1):
    b = Button(f, text=str(i), padx=28, pady=17, font="lucida 35 bold")
    b.grid(row=row, column=col)
    b.bind("<Button-1>", click)
    col += 1
    if col == 3:
        col = 0
        row += 1

f= Frame(root,bg="grey")
b=Button(f,text="+",padx=27,pady=17,font="lucida 35 bold")
b.pack(side="left")
b.bind("<Button-1>", click)

b=Button(f,text="0",padx=28,pady=17,font="lucida 35 bold")
b.pack(side="left")
b.bind("<Button-1>", click)

b=Button(f,text="-",padx=30,pady=17,font="lucida 35 bold")
b.pack(side="left")
b.bind("<Button-1>", click)
f.pack()



f= Frame(root,bg="grey")
b=Button(f,text="*",padx=17,pady=17,font="lucida 35 bold")
b.pack(side="left")
b.bind("<Button-1>", click)

b=Button(f,text="/",padx=17,pady=17,font="lucida 35 bold")
b.pack(side="left")
b.bind("<Button-1>", click)

b=Button(f,text="=",padx=17,pady=17,font="lucida 35 bold")
b.pack(side="left")
b.bind("<Button-1>", click)

b=Button(f,text="C",padx=17,pady=17,font="lucida 35 bold")
b.pack(side="left")
b.bind("<Button-1>", click)

f.pack()

root.mainloop()