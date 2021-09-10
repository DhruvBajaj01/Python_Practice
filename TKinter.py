#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from tkinter import *
from tkinter import messagebox
from tkinter import ttk
root = Tk()
root.geometry("640x480+100+100")
def cmd1():
sub1 = Toplevel(root)
sub1.title("Dep")
sub1.geometry("320x240+125+125")
deposit_lbl=Label(sub1, text="Enter the amount to Deposit", font=
'Helventica 15 bold').grid(row=0,column=0)
deposit_ent=Entry(sub1,width=10).grid(row=0,column=1)
def cmd3():
messagebox.showinfo("Balance", "bal amount")
btn3 = ttk.Button(sub1,text="UPDATE",command =
cmd3).grid(row=1,column=0)
def cmd2():
sub2 = Toplevel(root)
sub2.title("With")
sub2.geometry("320x240+125+125")
with_lbl=Label(sub2, text="Enter the amount to Withdraw", font=
'Helventica 15 bold').grid(row=0,column=0)
with_ent=Entry(sub2,width=10).grid(row=0,column=1)
def cmd4():
messagebox.showinfo("Balance", "bal amount")
btn4 = ttk.Button(sub1,text="UPDATE",command =
cmd4).grid(row=1,column=0)
btn1 = ttk.Button(root ,text="Deposit",command =
cmd1).grid(row=0,column=0)
btn2 = ttk.Button(root ,text="Withdraw",command =
cmd2).grid(row=1,column=0)
root.mainloop()


# In[ ]:


from tkinter import Tk, Label
root=Tk()
def key_pressed(event):
w=Label(root,text="Advanced programming practices Code:
18CSC207J")
w.place(x=70,y=90)
root.bind("<Key>",key_pressed)
root.mainloop()


# In[ ]:





# In[ ]:




