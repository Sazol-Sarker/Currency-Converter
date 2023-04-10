from currency_converter import CurrencyConverter 
import tkinter as tk 
from tkinter import * 
import googletrans 
import textblob 
from tkinter import ttk,messagebox 

window=tk.Tk()
window.geometry("500x400+450+70")
window.title("Currency Converter")

a=CurrencyConverter()

def clicked():
    amount=int(e1.get())
    cur1=e2.get()
    cur2=e3.get()
    data=a.convert(amount,cur1,cur2)
    data=round(data,2)
    
    #after conversion, result
    l5=tk.Label(text=data)
    
    #after conversion, result unit
    l6=tk.Label(text=cur2)
    



def clear():
    #    e1.delete('1.0', tk.END)
       e1.delete(0,END)
       e2.delete(0,END)
       e3.delete(0,END)

        #after conversion, result
    #    l5=tk.Label(window)
    #    l5.config(text="")
    #    l5.place(x=320 ,y=230)
    #    #after conversion, result unit
    #    l6=tk.Label(window)
    #    l6.config(text="")
    #    l6.place(x=350 ,y=230)
       l5.destroy()
       l6.destroy()




l1=tk.Label(window,text="Currency Converter",font="Times 20 bold")

l2=tk.Label(window,text="Enter Amount:",font="Times 12 ")
e1=tk.Entry(window)

l3=tk.Label(window,text="Enter Currency:",font="Times 12 ")
e2=tk.Entry(window)

l4=tk.Label(window,text="Enter Required Currency:",font="Times 12 ")
l5=tk.Label(window)
l6=tk.Label(window)
e3=tk.Entry(window)

b1=tk.Button(window,text="Convert",command=clicked,font="Times 15 ")
b2=tk.Button(window,text="Clear",command=clear,font="Times 15 ")
b1.pack()
b2.pack()

l1.place(x=120,y=10)
l2.place(x=50,y=80)
e1.place(x=300 ,y=90)
l3.place(x= 50,y=130)
e2.place(x=300 ,y=140)
l4.place(x= 50,y=180)
e3.place(x=300 ,y=190)
b1.place(x=270 ,y=260)
b2.place(x=380 ,y=260)
l5.place(x=320 ,y=230)
l6.place(x=350 ,y=230)
l5.pack()
l6.pack()


window.mainloop()




