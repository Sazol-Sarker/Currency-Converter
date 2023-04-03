from currency_converter import CurrencyConverter 
import tkinter as tk 

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
    
    l5=tk.Label(window,text=data)
    l5.place(x=320 ,y=230)
    l6=tk.Label(window,text=cur2)
    l6.place(x=350 ,y=230)

l1=tk.Label(window,text="Currency Converter",font="Times 20 bold")

l2=tk.Label(window,text="Enter Amount:",font="Times 12 ")
e1=tk.Entry(window)

l3=tk.Label(window,text="Enter Currency:",font="Times 12 ")
e2=tk.Entry(window)

l4=tk.Label(window,text="Enter Required Currency:",font="Times 12 ")
e3=tk.Entry(window)

b1=tk.Button(window,text="click",command=clicked,font="Times 15 ")


l1.place(x=120,y=10)
l2.place(x=50,y=80)
e1.place(x=300 ,y=90)
l3.place(x= 50,y=130)
e2.place(x=300 ,y=140)
l4.place(x= 50,y=180)
e3.place(x=300 ,y=190)
b1.place(x=328 ,y=260)



window.mainloop()




