#!/usr/bin/env python
# coding: utf-8

# In[17]:


import tkinter as tk
from tkinter import ttk
import sqlite3
 
window = tk.Tk()
window.title('Employee Information-054')
window.geometry('600x600')
 
 
#declaring text variable
EmployeeName=tk.StringVar()
EmployeeID=tk.StringVar()
Address=tk.StringVar()
Mobile=tk.StringVar()
Date=tk.StringVar()
Month=tk.StringVar()
Year=tk.StringVar()
MailID=tk.StringVar()
BasicPay=tk.IntVar()
HA=tk.IntVar()
DA=tk.IntVar()
#database implemenation
def database():
   name = EmployeeName.get()
   Id = EmployeeID.get()
   add = Address.get()
   mob = Mobile.get()
   doj = Date.get() + Month.get() + ',' + Year.get()
   mail = MailID.get()
   salary = BasicPay.get()+HA.get()+DA.get()
  
   conn = sqlite3.connect('Employee.db')
   with conn:
      cursor=conn.cursor()
   cursor.execute('CREATE TABLE IF NOT EXISTS employee (name TEXT, Id TEXT, address TEXT, mob TEXT, doj TEXT, mail TEXT, salary TEXT)')
   cursor.execute('INSERT INTO employee (name , Id, address, mob, doj, mail, salary  ) VALUES(?,?,?,?,?,?,?)',(name , Id, add, mob, doj, mail, salary,))
   conn.commit()
#display database
def display():
    db=sqlite3.connect('Employee.db')
    
    with db:
        cursor=db.cursor()
        my_w = tk.Tk()
        my_w.geometry("1200x1200") 
 
        r_set=cursor.execute('''SELECT * from employee ''');
        i=0  
        for employee in r_set: 
            for j in range(len(employee)):
                e_054 = tk.Entry(my_w, width=10) 
                e_054.grid(row=i, column=j) 
                e_054.insert(tk.END, employee[j])
            i=i+1  
#Employee Name
l1_054 = tk.Label(window ,text = "Employee Name", background = "#695BCA", foreground="white" ).grid(row = 0,column = 0)
e1_054=tk.Entry(window,textvar= EmployeeName).grid(row = 0,column = 10)
#Employee ID
l2_054 = tk.Label(window ,text = "Employee ID", background = "#695BCA", foreground="white" ).grid(row = 1,column = 0)
e2_054=tk.Entry(window,textvar= EmployeeID).grid(row = 1,column = 10)
 
 
#Address
l3_054 = tk.Label(window ,text = "Address", background = "#695BCA", foreground="white").grid(row = 2,column = 0)
e2_054=tk.Entry(window,textvar= Address).grid(row = 2,column = 10)
 
#Phonenumber
l4_054 = tk.Label(window ,text = "Mobile Number ", background = "#695BCA", foreground="white").grid(row = 3,column = 0)
e4_054=tk.Entry(window,textvar=Mobile).grid(row=3,column=10)
#date of joining
l3_054 = tk.Label(window ,text = "Date Of Joining ", background = "#695BCA", foreground="white" ).grid(row = 4,column = 0)
 
D1_054 = ('1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31')
g1_054 = ttk.Combobox(window,width =4, text="day", value=D1,textvar=Date).grid(row=4,column=9)
 
M1_054 =('January','February','March','April','May','June','July','August','September','October','November','December')
g2_054 = ttk.Combobox(window,width =8, text="Month",values=M1,textvar=Month).grid(row=4,column=10)
 
Y1_054=(2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021)
g3_054 = ttk.Combobox(window, width =4,text="Year", value=Y1,textvar=Year).grid(row=4,column=11)
#Mail id
l4_054 = tk.Label(window ,text = "MailID : ", background = "#695BCA", foreground="white").grid(row = 5,column = 0)
e4_054=tk.Entry(window,textvar=MailID).grid(row=5,column=10)
#basic pay
l4_054 = tk.Label(window ,text = "Basic Pay ", background = "#695BCA", foreground="white").grid(row = 6,column = 0)
e4=tk.Entry(window,textvar=BasicPay).grid(row=6,column=10)
#HA 
l4_054 = tk.Label(window ,text = "HA ", background = "#695BCA", foreground="white").grid(row = 7,column = 0)
e4=tk.Entry(window,textvar=HA).grid(row=7,column=10)
#DA
l4_054 = tk.Label(window ,text = "DA ", background = "#695BCA", foreground="white").grid(row = 8,column = 0)
e4_054=tk.Entry(window,textvar=DA).grid(row=8,column=10)
   
# button
B1_054=tk.Button(window,text="SUBMIT",command=database).grid(row=11,column=0)
B2_054=tk.Button(window,text="SHOW DATABASE",command=display).grid(row=11,column=4)
 
window.mainloop()
 


# In[ ]:





# In[ ]:




