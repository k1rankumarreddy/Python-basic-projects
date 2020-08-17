from tkinter import *

val = ""
k = Tk()
k.geometry("237x225")
k.title("Calculator")

def press(value):
    global val
    val = val+value
    eq.set(val)

def equal():
    global val
    try:
        if('^' in val):
            val=val.replace("^","**")
        eq.set(str(eval(val)))
        val=""
    except:
        eq.set("You entered Invalid syntax")
        val=""

def clear():
    global val
    eq.set("")
    val=""

def b_space():
    global val
    val = val[:len(val)-1]
    eq.set(val)
eq=StringVar()
Entry(k,textvariable=eq).grid(columnspan=4,ipadx=50)
eq.set("Here enter any expression")
Button(k, text='1',fg="white",bg="black",command=lambda : press('1'),height=2,width=7).grid(row=2,column=0)
Button(k, text='2',fg="white",bg="black",command=lambda : press('2'),height=2,width=7).grid(row=2,column=1)
Button(k, text='3',fg="white",bg="black",command=lambda : press('3'),height=2,width=7).grid(row=2,column=2)
Button(k, text='4',fg="white",bg="black",command=lambda : press('4'),height=2,width=7).grid(row=3,column=0)
Button(k, text='5',fg="white",bg="black",command=lambda : press('5'),height=2,width=7).grid(row=3,column=1)
Button(k, text='6',fg="white",bg="black",command=lambda : press('6'),height=2,width=7).grid(row=3,column=2)
Button(k, text='7',fg="white",bg="black",command=lambda : press('7'),height=2,width=7).grid(row=4,column=0)
Button(k, text='8',fg="white",bg="black",command=lambda : press('8'),height=2,width=7).grid(row=4,column=1)
Button(k, text='9',fg="white",bg="black",command=lambda : press('9'),height=2,width=7).grid(row=4,column=2)
Button(k, text='0',fg="white",bg="black",command=lambda : press('0'),height=2,width=7).grid(row=5,column=1)
Button(k, text='+',fg="white",bg="black",command=lambda : press('+'),height=2,width=7).grid(row=2,column=3)
Button(k, text='-',fg="white",bg="black",command=lambda : press('-'),height=2,width=7).grid(row=3,column=3)
Button(k, text='*',fg="white",bg="black",command=lambda : press('*'),height=2,width=7).grid(row=4,column=3)
Button(k, text='=',fg="white",bg="black",command=equal,height=2,width=7).grid(row=6,column=3)
Button(k, text='/',fg="white",bg="black",command=lambda : press('/'),height=2,width=7).grid(row=6,column=2)
Button(k, text='%',fg="white",bg="black",command=lambda : press('%'),height=2,width=7).grid(row=6,column=0)
Button(k, text='^',fg="white",bg="black",command=lambda : press('^'),height=2,width=7).grid(row=6,column=1)
Button(k, text='.',fg="white",bg="black",command=lambda : press('.'),height=2,width=7).grid(row=5,column=0)
Button(k, text='Clear',fg="white",bg="black",command=clear,height=2,width=7).grid(row=5,column=2)
Button(k, text='b-space',fg="white",bg="black",command=b_space,height=2,width=7).grid(row=5,column=3)

k.mainloop()
