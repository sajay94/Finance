import tkinter as tk
import pickle
import tkinter.messagebox
window = tk.Tk()
window.title('Your main page')
window.geometry('450x300')
var1 = tk.StringVar()
l = tk.Label(window, bg='yellow', width=16, textvariable=var1)
l.pack()
var1.set('Stock at hand')


def print_selection():
    value = lb.get(lb.curselection())

    var1.set(value)


b1 = tk.Button(window, text='print selection', width=15,
               height=2, command=print_selection)
b1.pack()
var2 = tk.StringVar()
var2.set(('stock a', 'stock b', 'stock c', 'stock d'))
lb = tk.Listbox(window, listvariable=var2)
# list_items=[1,2,3,4]
# for item in list_items:
#   lb.insert('end',item)
lb.insert(1, 'stock e')
lb.insert(2, 'stock f')
lb.insert(3, 'stock g')
lb.insert(4, 'stock h')
lb.pack()

"""""
var5 = tk.StringVar()
tem = tk.Label(window, bg='yellow', width=16, textvariable=var5)
var5.set("wait for your decision")
"""
var5 = tk.StringVar()
l = tk.Label(window, bg='yellow', width=100, textvariable=var5)
l.pack()
var5.set('wait for your selection')
def buy_command():
    var5.set("I press the buy button. I need to increase something in list. And my account balance will decrease")


buybutton = tk.Button(window, text='buybutton', width=15, height=2, command=buy_command)
buybutton.pack()

window.mainloop()