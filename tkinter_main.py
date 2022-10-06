from struct import pack
import tkinter as tk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox as mBox
from mysql.connector import Error


window = tk.Tk()
window.title('Qatar Tours')

frame = tk.Frame(window)
# PACK GRID AND PLACE ARE GEOMETRY COMMs
frame.pack()

# Customer info frame
customer_info_frame = tk.LabelFrame(frame,text='Customer Details')
customer_info_frame.grid(row=0,column=0,padx= 10,pady = 5)

#Widgets for cusomter info (labels and entry)

First_Name_Label = tk.Label(customer_info_frame, text="First Name")
First_Name_Label.grid(row=0,column=0,padx= 10,pady = 5)

Last_Name_Label = tk.Label(customer_info_frame,text='Last Name')
Last_Name_Label.grid(row=0,column=2,padx= 10,pady = 5)

First_Name_Entry = tk.Entry(customer_info_frame)
First_Name_Entry.grid(row=1,column=0,padx= 10,pady = 5)

Last_Name_Entry = tk.Entry(customer_info_frame)
Last_Name_Entry.grid(row=1,column=2,padx= 10,pady = 5)

package = tk.Label(customer_info_frame,text='SELECT PACKAGE')
package_combobox = ttk.Combobox(customer_info_frame,values=['World Tour/6M','World Tour/1Y','Any Country 1M'])
package.grid(row=0,column=4,padx= 10,pady = 5)
package_combobox.grid(row=1,column=4,padx= 10,pady = 5)

age_label = tk.Label(customer_info_frame,text='No. of people ( includes adult and children)')
age_spinbox = tk.Spinbox(customer_info_frame,from_=1,to=10)
age_label.grid(row=2,padx= 10,pady = 5)
age_spinbox.grid(row=2,column = 2,padx= 10,pady = 5)


# Frame 2 
#terms of service and check button
CourseFrame = tk.LabelFrame(frame,text='Finalization')
CourseFrame.grid(row=1,column=0)

terms = tk.Label(CourseFrame,text='I AGREE TO TERMS AND CONDITIONS ( REQUIRED)')
terms_checkbox = tk.Checkbutton(CourseFrame,text='I agree to Terms and Conditions')
terms_info = tk.Label(CourseFrame,text='for any further inquires please contact us on "QatarTours@gmail.com"')

terms.grid(row=1,column=0)
terms_checkbox.grid(row=2,column=0)
terms_info.grid(row=3,column=0)

#Yaha par password aur database tera kar lena aur execute jaisi table bana de
def _msgBox():
    try:
     
     conn = mysql.connector.connect(host='localhost',database='project',user='root',password='123456')
     cursor = conn.cursor()
     row = cursor.execute("insert into qatar_tours(First_Name, Last_Name, Select_Package, No_of_People) values('"+First_Name_Entry.get()+"', '"+Last_Name_Entry.get()+"','"+package_combobox.get()+"','"+age_spinbox.get()+"')")
     print(cursor.rowcount)
    
     if(cursor.rowcount>0):
         mBox.showinfo('Congrats!')
         
     else:
         print('Not Done!')
    except Error as e :
     print("Error while connecting to MySQL", e)
    finally:
        print("MySQL connection is closed")
        conn.commit()



action = ttk.Button(CourseFrame, text="Confirm!",command=_msgBox) 
action.grid(row=4,column=0)
window.mainloop()


#Itna hi karna hai kya









