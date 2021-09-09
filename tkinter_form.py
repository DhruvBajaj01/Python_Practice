#!/usr/bin/env python
# coding: utf-8

# In[ ]:


tkFileDialog.askopenfilename(initialdir = “/”,title = “Select file”,filetypes = ((“file_type”,”*.extension”),(“all files”,”*.*”)))


# In[ ]:


# Python program to create 
# a file explorer in Tkinter
  
# import all components
# from the tkinter library
from tkinter import *
  
# import filedialog module
from tkinter import filedialog
  
# Function for opening the 
# file explorer window
def browseFiles():
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("Text files",
                                                        "*.txt*"),
                                                       ("all files",
                                                        "*.*")))
      
    # Change label contents
    label_file_explorer.configure(text="File Opened: "+filename)
      
      
                                                                                                  
# Create the root window
window = Tk()
  
# Set window title
window.title('File Explorer')
  
# Set window size
window.geometry("500x500")
  
#Set window background color
window.config(background = "white")
  
# Create a File Explorer label
label_file_explorer = Label(window, 
                            text = "File Explorer using Tkinter",
                            width = 100, height = 4, 
                            fg = "blue")
  
      
button_explore = Button(window, 
                        text = "Browse Files",
                        command = browseFiles) 
  
button_exit = Button(window, 
                     text = "Exit",
                     command = exit) 
  
# Grid method is chosen for placing
# the widgets at respective positions 
# in a table like structure by
# specifying rows and columns
label_file_explorer.grid(column = 1, row = 1)
  
button_explore.grid(column = 1, row = 2)
  
button_exit.grid(column = 1,row = 3)
  
# Let the window wait for any events
window.mainloop()


# In[ ]:


from Tkinter import *

master = Tk()
Label(master, text="First Name").grid(row=0)
Label(master, text="Last Name").grid(row=1)

e1 = Entry(master)
e2 = Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

mainloop( )


# In[ ]:


hi


# In[ ]:


int=int(input(" enter"))
print(int)


# In[ ]:




