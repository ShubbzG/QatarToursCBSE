import tkinter as tk 
from tkinter import ttk
from tkinter import Menu
from tkinter import messagebox as mBox

win = tk.Tk()
win.title("Qatar Travels Portal") 

#win.iconbitmap(r'pz.ico')

win.geometry("533x405")
'''
win.configure(background='light grey')
bg=tk.PhotoImage(file='banner.png')
x1=tk.Label(image=bg)
x1.grid(column=0, row=0,columnspan=2)
'''
def veg():
    import vegmenu

def nveg():
    import nvegmenu

def modmenu():
    win.quit()
    win.destroy()
    import modmenu

def norder():
    win.quit()
    win.destroy()
    import norder

def ordhst():
    win.quit()
    win.destroy()
    import ordhst

def todord():
    win.quit()
    win.destroy()
    import todord

select1 = ttk.Button(win, text="Select", command=veg) 
select1.grid(column=0, row=1)

nveg = ttk.Button(win, text="Non Veg Menu", command=nveg) 
nveg.grid(column=1, row=1)

modmenu = ttk.Button(win, text="Modify Menu", command=modmenu) 
modmenu.grid(column=0, row=2)

norder = ttk.Button(win, text="Place New Order", command=norder) 
norder.grid(column=1, row=2)

todord = ttk.Button(win, text="Today's Orders", command=ordhst) 
todord.grid(column=0, row=3)

ordhst = ttk.Button(win, text="Order History", command=ordhst) 
ordhst.grid(column=1, row=3)

for child in win.winfo_children():
    child.grid_configure(padx=10, pady=20)
