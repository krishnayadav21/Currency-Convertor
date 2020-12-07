import tkinter as tk
import requests #pip install requests
from tkinter import *
from tkinter import ttk

#function 
def convert():
    from_=select1.get()
    to_=select2.get()
    a=x.get()
    b=y.get()
    res=requests.get(f'https://api.exchangeratesapi.io/latest?base={from_}&symbols={to_}')
    data=res.json()
    exchange_rate=data['rates'][to_]
    amount=float(a)
    result=amount*exchange_rate
    result=format(result,'.4f')
    y.set(result)
        
window=tk.Tk()
window.title("Currency Convertor")
window.geometry("300x290")
x=IntVar()
y=IntVar()
select1=StringVar()
select1.set("INR")
select2=StringVar()
select2.set("USD")

label1=tk.Label(window,text="Curruncey Convertor ",font=("Arial",20,"bold"))
label1.grid(row=0,columnspan=2,padx=5,pady=5)
#entry box
entry1=tk.Entry(window,textvariable=x,width=30)
entry1.grid(row=2,column=0)
entry2=tk.Entry(window,textvariable=y,width=30)
entry2.grid(row=3,column=0)

combo1=ttk.Combobox(window,width=10,textvariable=select1)
combo1['values']=('CAD','HKD','ISK','PHP','DKK','HUF','CZK','GBP','RON','SEK','IDR','INR','BRL','RUB','HRK','JPY',
'THB','CHF','EUR','MYR','BGN','TRY','CNY','NOK','NZD','ZAR','USD','MXN','SGD','AUD','ILS','KRW','PLN')
combo1.grid(row=2,column=1,pady=10)

combo2=ttk.Combobox(window,width=10,textvariable=select2)
combo2['values']=('CAD','HKD','ISK','PHP','DKK','HUF','CZK','GBP','RON','SEK','IDR','INR','BRL','RUB','HRK','JPY',
'THB','CHF','EUR','MYR','BGN','TRY','CNY','NOK','NZD','ZAR','USD','MXN','SGD','AUD','ILS','KRW','PLN')
combo2.grid(row=3,column=1,pady=10)

button=tk.Button(window,command=convert,text="Convert",font=("Arial",10,"bold"),bg="light blue")
button.grid(row=6,columnspan=2)
window.mainloop()
