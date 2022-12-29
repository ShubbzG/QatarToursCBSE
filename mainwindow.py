import tkinter as tk 
from tkinter import ttk
from tkinter import Menu
from tkinter import messagebox as mBox
import mysql.connector
import pandas as pd

win = tk.Tk()
win.title("Qatar Travels Portal") 
win.geometry("1200x600")
win.maxsize(1200,600)

#win.configure(background=BackG)
#x1=tk.Label(image=bg)
#x1.grid(column=0, row=0,columnspan=2)
utab=ttk.Label(win,text="QATAR TRAVELS",font=("Impact",42),background="white")
utab.grid(column=4,row=1)

def SelectMenu():
    import select_m


def Update():
    win.quit()
    win.destroy()
    import update_m

def delete():
    win.quit()
    win.destroy()
    import delete_m

def Insert():
    win.quit()
    win.destroy()
    import insert_m

def TourUpdate():
    win.quit()
    win.destroy()
    import update_t

def TourDelete():
    win.quit()
    win.destroy()
    import delete_t

def Toursadd():
    win.quit()
    win.destroy()
    import insert_t
    
def TourSelect():
    win.quit()
    win.destroy()
    import select_t






LMembers=ttk.Label(win,text="Member info",font=("Impact",42),background="white")
LMembers.grid(column=1,row=3)


deletei = tk.PhotoImage(file='Delete_m.png')
deletem = ttk.Button(win, image=deletei, command=delete) 
deletem.grid(column=0, row=8)

infom=tk.PhotoImage(file='info_m.png')
Info = ttk.Button(win, image=infom, command=SelectMenu) 
Info.grid(column=1, row=8)

updatem = tk.PhotoImage(file='update_m.png')
modmenu = ttk.Button(win, image=updatem, command=Update) 
modmenu.grid(column=0, row=11)

addm=tk.PhotoImage(file='add_m.png')
AddM = ttk.Button(win, image=addm, command=Insert) 
AddM.grid(column=1, row=11)

LToursInfo=ttk.Label(win,text="Tour info",font=("Impact",42),background="white")
LToursInfo.grid(column=7,row=3)

Tour_I = tk.PhotoImage(file='Tour_I.png')
ToursInfoB = ttk.Button(win,image=Tour_I,command = TourSelect)
ToursInfoB.grid(column = 7,row = 8)

UpdateTours = ttk.Button(win,image=updatem,command = TourUpdate)
UpdateTours.grid(column = 7,row = 11)

DeleteTours = ttk.Button(win,image = deletei,command = TourDelete)
DeleteTours.grid(column = 6, row = 8)

ToursAdd = ttk.Button(win,image=addm, command = Toursadd)
ToursAdd.grid(column =6, row =11) 

def backup():
    conn = mysql.connector.connect(host='localhost',database='QATARTRAVELS',user='root',password='root',charset='utf8')
    cursor = conn.cursor()
    cursor.execute("select * from TOURS")
    ls = pd.DataFrame(cursor.fetchall())
    ls.to_csv('tours.csv')
    cursor.execute("select * from members")
    ls = pd.DataFrame(cursor.fetchall())
    ls.to_csv('members.csv')
    
BackupB = ttk.Button(win,text = 'Backup',command = backup)
BackupB.grid(column = 7 , row = 15)

def quitwindow():
    win.quit()
    win.destroy()
    import login


LogOutB = ttk.Button(win,text = 'Log Out', command = quitwindow)
LogOutB.grid(column = 6,row = 15)










BackG = tk.PhotoImage(file='QATAR LOGO FINAL.png')


for child in win.winfo_children():
    child.grid_configure(padx=10, pady=20)
