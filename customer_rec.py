#!/usr/bin/env python
# coding: utf-8

# In[ ]:


n=1
while n <= 5:
    print("Customer ", n)
    customerID = int(input("Enter Customer ID "))
    customerName = input("Enter Customer Name ")
    units = int(input("Enter Units Consumed "))
    date = input("Enter Date of Payment ")
    amountPaid = input("Amount Paid (YES/NO) ")
    print("---------------------")
    print("Bill Id : BCus_00", n)
    print("Customer ID :", customerID)
    print("Customer Name :", customerName)
    print("Units consumed :", units)
  
    if amountPaid == 'YES' or 'yes':
        print("Amount Paid : YES")
        print("Date of Payment :", date)
    else:
        print("Amount Paid : NO")
    print("---------------------")
    n += 1

