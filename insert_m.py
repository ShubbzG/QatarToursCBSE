import tkinter as tk 
from tkinter import ttk
from tkinter import Menu
from tkinter import messagebox as mBox
import mysql.connector
import pandas as pd

win = tk.Tk()
win.configure(background="white")
win.title("INSERT MEMBERS")

utab=ttk.Label(win,text="Qatar Travels",fon=("Impact",42),background="white")
utab.grid(column=0,row=0,padx=110,columnspan=2)


utab2=ttk.Label(win,text='Enter Tour Details',font=("Calibri",30),background="white")
utab2.grid(column=0,row=1,columnspan=2,padx=30)


conn = mysql.connector.connect(host='localhost',database='QatarTravels',user='root',password='root',charset='utf8')
cursor = conn.cursor()
cursor.execute("select max(member_id) from members")
ls = pd.DataFrame(cursor.fetchall())



lmid = ttk.Label(win, text="Member  ID : ",background="white",font=("Calibri",20))
lmid.grid(column=0, row=2, sticky=tk.W,padx=10,pady=10)

mid = tk.IntVar()
tmid = ttk.Entry(win, width=20, textvariable=mid,font=("Helvetica",15))
tmid.grid(column=1, row=2)
mid.set(ls[0][0])

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
s = tk.Radiobutton(win, text='Paid', variable=vst, value='Y') 
s.grid(column=1, row=8, sticky=tk.W) 						
ns=tk.Radiobutton(win, text='Unpaid', variable=vst, value='N') 
ns.grid(column=2, row=8, sticky=tk.W)



def _msgBox():
     conn = mysql.connector.connect(host='localhost',database='QatarTravels',user='root',password='root',charset='utf8')
     cursor = conn.cursor()
     row = cursor.execute("insert into members values("+str(mid.get())+", "+str(tid.get())+", '"+name.get()+"', "+str(age.get())+", '"+gen.get()+"', "+ph.get()+", '"+vst.get()+"');")
     if(cursor.rowcount>0):   # help to ensure that something changed/added into table
         mBox.showinfo('Done','Added!')
         mid.set('')
         tid.set('')
         name.set('')
         age.set('')
         gen.set('')
         ph.set('')
         
         conn.commit()
     else:
         mBox.showinfo('Error','Not Added!')
    

submit = tk.Button(win, text="INSERT", command=_msgBox,bg="black",fg="white",relief="flat",font=('Arial',10)) 
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
bk = tk.Button(win, text="GET", command=neta,bg="black",fg="white",relief="flat",font=('Arial',10)) 
bk.grid(column=2, row=6)
'''
'''
bk = tk.Button(win, text="DELETE", command=det,bg="black",fg="white",relief="flat",font=('Arial',10)) 
bk.grid(column=1, row=7,sticky=tk.E)
'''
win.mainloop()
