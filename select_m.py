import pandas as pd
import tkinter as tk 
from tkinter import ttk
from tkinter import Menu
from tkinter import messagebox as mBox
import mysql.connector
from mysql.connector import Error


win = tk.Tk()
win.minsize(1000,1000)
win.configure(background='white')
win.title("SELECT Members")

utab=ttk.Label(win,text="QATAR TRAVELS",font=("Impact",42),background="white")
utab.grid(column=2,row=1)

 

utab2=ttk.Label(win,text='Member data',font=("Calibri",32),background="white")
utab2.grid(column=2,row=2)


def actBack():
    win.quit()
    win.destroy()
    import mainwindow
    
action = tk.Button(win, text="Back", command= actBack,bg="black",fg='white',relief='flat',font=('Arial',10))  # create button control
action.grid(column=4, row=1)

try:
     
    conn = mysql.connector.connect(host='localhost',database='QATARTRAVELS',user='root',password='root',charset='utf8')
    cursor = conn.cursor()
    cursor.execute("select * from mEMBERS;")
    ls = pd.DataFrame(cursor.fetchall())

    ttk.Label(win, text="    MEMBER ID",background="white",font=("Lucida Bright",20)).grid(column=0, row=3, sticky=tk.W, columnspan=20)
    ttk.Label(win, text="    TOUR ID",background="white",font=("Lucida Bright",20)).grid(column=1, row=3, sticky=tk.W, columnspan=20)
    ttk.Label(win, text="    MEMBER'S NAME",background="white",font=("Lucida Bright",20)).grid(column=2, row=3, sticky=tk.W, columnspan=701)
    ttk.Label(win, text="    AGE",background="white",font=("Lucida Bright",20)).grid(column=3, row=3, sticky=tk.W, columnspan=20)
    ttk.Label(win, text="    GENDER",background="white",font=("Lucida Bright",20)).grid(column=4, row=3, sticky=tk.W, columnspan=25)
    ttk.Label(win, text="    CONTACT",background="white",font=("Lucida Bright",20)).grid(column=5, row=3, sticky=tk.W, columnspan=25)
    ttk.Label(win, text="    PAID/UNPAID",background="white",font=("Lucida Bright",20)).grid(column=6, row=3, sticky=tk.W, columnspan=25)
   
    
    
    for i in range(0, len(ls.index)):
        for j in range(0, len(ls.columns)):
            b = tk.Entry(win,font=("Helvetica",12))
            b.insert(0, ls.iloc[i][j])
            if(j==0):
                b.grid(row=i+4,column=j,padx=16)
                b.configure(state="readonly",width=20)
            elif(j==1):
                b.grid(row=i+4,column=j,padx=16)
                b.configure(state="readonly",width=20)
            elif(j==2):
                b.grid(row=i+4,column=j,padx=16)
                b.configure(state="readonly",width=20)
            elif(j==3):
                
                b.grid(row=i+4,column=j,padx=16)
                b.configure(state="readonly",width=20)
            elif(j==4):
                b.grid(row=i+4,column=j,padx=16)
                b.configure(state="readonly",width=20)
            else:
                b.grid(row=i+4,column=j,padx=16)
                b.configure(state="readonly",width=20)
    conn.commit()
    conn.close()
except Error as e :
    print("Error while connecting to MySQL", e)
finally:
    print("MySQL connection is closed")


for child in win.winfo_children():
    child.grid_configure(padx=5, pady=5)
    
win.mainloop()
