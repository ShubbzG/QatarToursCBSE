import tkinter as tk 
from tkinter import ttk
from tkinter import Menu
from tkinter import messagebox as mBox
import mysql.connector
import pandas as pd

win = tk.Tk()
win.configure(background="white")
win.title("UPDATE MEMBER")

utab=ttk.Label(win,text="Qatar Travels",fon=("Impact",42),background="white")
utab.grid(column=0,row=0,padx=110,columnspan=2)


utab2=ttk.Label(win,text='Enter Memeber Details',font=("Calibri",30),background="white")
utab2.grid(column=0,row=1,columnspan=2,padx=30)



lmid = ttk.Label(win, text="Member  ID : ",background="white",font=("Calibri",20))
lmid.grid(column=0, row=2, sticky=tk.W,padx=10,pady=20)

mid = tk.IntVar()
tmid = ttk.Entry(win, width=20, textvariable=mid,font=("Helvetica",15))
tmid.grid(column=1, row=2)

def getData():
    conn = mysql.connector.connect(host='localhost',database='QatarTravels',user='root',password='root',charset='utf8')
    cursor = conn.cursor()
    cursor.execute("select * from members where member_id="+str(mid.get()))
    ls = pd.DataFrame(cursor.fetchall())
    if(len(ls.index>0)):
       tid.set(ls.loc[0,1])
       name.set(ls.loc[0,2])
       age.set(ls.loc[0,3])
       gen.set(ls.loc[0,4])
       ph.set(ls.loc[0,5])
       vst.set(ls.loc[0,6])
    else:
        mBox.showinfo('Error', 'Not found')

bk = tk.Button(win, text="GET Details", command=getData,bg="black",fg="white",relief="flat",font=('Arial',10)) 
bk.grid(column=2, row=2)


ltid = ttk.Label(win, text="Tour  ID : ",background="white",font=("Calibri",20))
ltid.grid(column=0, row=3, sticky=tk.W,padx=10,pady=10)

tid = tk.IntVar()
ttid = ttk.Entry(win, width=20, textvariable=tid,font=("Helvetica",15))
ttid.grid(column=1, row=3)


lname = ttk.Label(win, text="Member's Name : ",background="white",font=("Calibri",20))
lname.grid(column=0, row=4, sticky=tk.W,padx=10,pady=10)

name= tk.StringVar()
tname = ttk.Entry(win, width=20, textvariable=name, font=("Helvetica",15))
tname.grid(column=1, row=4)

lage = ttk.Label(win, text="Age : ",background="white",font=("Calibri",20))
lage.grid(column=0, row=5, sticky=tk.W,padx=10,pady=10)

age = tk.IntVar()
tage = ttk.Entry(win, width=20, textvariable=age,font=("Helvetica",15))
tage.grid(column=1, row=5)


lgen = ttk.Label(win, text="Gender : ",background="white",font=("Calibri",20))
lgen.grid(column=0, row=6, sticky=tk.W,padx=10,pady=10)

gen= tk.StringVar()
tgen = ttk.Entry(win, width=20, textvariable=gen,font=("Helvetica",15))
tgen.grid(column=1, row=6)

lph = ttk.Label(win, text="Phone : ",background="white",font=("Calibri",20))
lph.grid(column=0, row=7, sticky=tk.W,padx=10,pady=10)

ph= tk.StringVar()
tph = ttk.Entry(win, width=20, textvariable=ph,font=("Helvetica",15))
tph.grid(column=1, row=7)					


lst = ttk.Label(win, text="Paid/Unpaid : ",background="white",font=("Calibri",20))
lst.grid(column=0, row=8,sticky=tk.W,padx=10,pady=10)

vst = tk.StringVar() 									
tvst = ttk.Entry(win, width=20, textvariable=vst,font=("Helvetica",15))
tvst.grid(column=1, row=8)



def _msgBox():
     conn = mysql.connector.connect(host='localhost',database='QatarTravels',user='root',password='root',charset='utf8')
     cursor = conn.cursor()
     row = cursor.execute("update members set tour_id="+str(tid.get())+", name='"+name.get()+"', age="+str(age.get())+", gender='"+gen.get()+"', phone_no="+ph.get()+", paid='"+vst.get()+"' where member_id="+str(mid.get()))
     if(cursor.rowcount>0):   # help to ensure that something changed/added into table
         mBox.showinfo('Added!')
         mid.set('')
         tid.set('')
         name.set('')
         age.set('')
         gen.set('')
         ph.set('')
         
         conn.commit()
     else:
         print('Not Done!')
    

submit = tk.Button(win, text="UPDATE", command=_msgBox,bg="black",fg="white",relief="flat",font=('Arial',10)) 
submit.grid(column=0, row=9,pady=40,sticky=tk.W,padx=10)


def back():
         win.quit()
         win.destroy()
         import mainwindow
         
bk = tk.Button(win, text="BACK", command=back,bg="black",fg="white",relief="flat",font=('Arial',10)) 
bk.grid(column=1, row=9,pady=40,sticky=tk.W,columnspan=2)



def neta():
    a=amt.get()-disc.get()
    net.set(a)

def det():
    import delete_order_details_2
    



'''
bk = tk.Button(win, text="DELETE", command=det,bg="black",fg="white",relief="flat",font=('Arial',10)) 
bk.grid(column=1, row=7,sticky=tk.E)
'''
win.mainloop()
