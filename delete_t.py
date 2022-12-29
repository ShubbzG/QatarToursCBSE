import tkinter as tk 
from tkinter import ttk
from tkinter import Menu
from tkinter import messagebox as mBox
import mysql.connector
import pandas as pd

win = tk.Tk()
win.configure(background="white")
win.title("UPDATE TOURS")

utab=ttk.Label(win,text="Qatar Travels",fon=("Impact",42),background="white")
utab.grid(column=0,row=0,padx=110,columnspan=2)


utab2=ttk.Label(win,text='Update Tour Details',font=("Calibri",30),background="white")
utab2.grid(column=0,row=1,columnspan=2,padx=30)



lmid = ttk.Label(win, text="Member  ID : ",background="white",font=("Calibri",20))
lmid.grid(column=0, row=2, sticky=tk.W,padx=10,pady=20)

mid = tk.IntVar()
tmid = ttk.Entry(win, width=20, textvariable=mid,font=("Helvetica",15))
tmid.grid(column=1, row=2)

def getData():
    conn = mysql.connector.connect(host='localhost',database='QatarTravels',user='root',password='root',charset='utf8')
    cursor = conn.cursor()
    cursor.execute("select * from tours where tour_id="+str(iid.get()))
    ls = pd.DataFrame(cursor.fetchall())
    if(len(ls.index>0)):
       iid.set(ls.loc[0,0])
       s.set(ls.loc[0,1])
       sdate.set(ls.loc[0,2])
       adate.set(ls.loc[0,3])
       a.set(ls.loc[0,4])
       d.set(ls.loc[0,5])
    else:
        mBox.showinfo('Error', 'Not found')

bk = tk.Button(win, text="GET Details", command=getData,bg="black",fg="white",relief="flat",font=('Arial',10)) 
bk.grid(column=2, row=2)


lid = ttk.Label(win, text="Tour  ID : ",background="white",font=("Calibri",20))
lid.grid(column=0, row=2, sticky=tk.W,padx=10,pady=20)

iid = tk.IntVar()
tid = ttk.Entry(win, width=20, textvariable=iid,font=("Helvetica",15))
tid.grid(column=1, row=2)
#iid.set((ls[0][0])+1)

ls = ttk.Label(win, text="No. of Members ",background="white",font=("Calibri",20))
ls.grid(column=0, row=3, sticky=tk.W,padx=10,pady=20)

s= tk.IntVar()
ts = ttk.Entry(win, width=20, textvariable=s,font=("Helvetica",15))
ts.grid(column=1, row=3)


lsdate = ttk.Label(win, text="Departure : ",background="white",font=("Calibri",20))
lsdate.grid(column=0, row=4, sticky=tk.W,padx=10,pady=20)

sdate= tk.StringVar()
tsdate = ttk.Entry(win, width=20, textvariable=sdate, font=("Helvetica",15))
tsdate.grid(column=1, row=4)

ladate = ttk.Label(win, text="Arrival : ",background="white",font=("Calibri",20))
ladate.grid(column=0, row=5, sticky=tk.W,padx=10,pady=20)

adate = tk.StringVar()
tadate = ttk.Entry(win, width=20, textvariable=adate,font=("Helvetica",15))
tadate.grid(column=1, row=5)


la = ttk.Label(win, text="Amount : ",background="white",font=("Calibri",20))
la.grid(column=0, row=6, sticky=tk.W,padx=10,pady=20)

a= tk.IntVar()
ta = ttk.Entry(win, width=20, textvariable=a,font=("Helvetica",15))
ta.grid(column=1, row=6)

ld = ttk.Label(win, text="Destination : ",background="white",font=("Calibri",20))
ld.grid(column=0, row=7, sticky=tk.W,padx=10,pady=20)

d= tk.StringVar()
td = ttk.Entry(win, width=20, textvariable=d,font=("Helvetica",15))
td.grid(column=1, row=7)


def _msgBox():
     conn = mysql.connector.connect(host='localhost',database='QatarTravels',user='root',password='root',charset='utf8')
     cursor = conn.cursor()
     row = cursor.execute("delete from tours  where tour_id="+str(iid.get()))
     if(cursor.rowcount>0):   # help to ensure that something changed/added into table
         mBox.showinfo('Done','Deleted!')
         iid.set('')
         s.set('')
         sdate.set('')
         adate.set('')
         a.set('')
         d.set('')
         
         conn.commit()
         
        
     else:
         mBox.showinfo('Error','Not Deleted!')
    

submit = tk.Button(win, text="DELETE", command=_msgBox,bg="black",fg="white",relief="flat",font=('Arial',10)) 
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
