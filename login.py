import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mBox
import mysql.connector
import pandas as pd


win = tk.Tk() 	
win.title("Qatar Travels")
win.minsize(300, 200) 

ulab = ttk.Label(win, text="User ID")
ulab.grid(column=0, row=0)

usr = tk.StringVar()
usrw = ttk.Entry(win, width=20, textvariable=usr)
usrw.grid(column=1, row=0)

upas = ttk.Label(win, text="Password")
upas.grid(column=0, row=1)

pas = tk.StringVar()
pasw = ttk.Entry(win, width=20, textvariable=pas, show='*')
pasw.grid(column=1, row=1)

def _msgBox():
     conn = mysql.connector.connect(host='localhost',
                             database='QatarTravels',
                             user='root',
                             password='root',
                             charset='utf8')
     cursor = conn.cursor()
     cursor.execute("SELECT * FROM login where user_id='"+usr.get()+"' and password='"+pas.get()+"'")
     ls = pd.DataFrame(cursor.fetchall())
     if(len(ls.index)>0):
         mBox.showinfo('Congrats!', 'Welcome '+str(ls[0]))
         usr.set('')
         pas.set('')
         win.quit()
         win.destroy()
         import mainwindow
     else:
         mBox.showinfo('Error!', 'Invalid user id or password!')

				
action = ttk.Button(win, text="LOG IN!", command=_msgBox) 
action.grid(column=1, row=3) 

for child in win.winfo_children():
    child.grid_configure(padx=30, pady=30)
    

win.mainloop()


