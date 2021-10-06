def recur_factorial(n):  
   if n == 0:  
       return 1
   else:  
       return n*recur_factorial(n-1)  
# take input from the user  
num = int(input("Enter a number: "))  
# check is the number is negative  
if num < 0:  
   print("Sorry, factorial does not exist for negative numbers")  
else:  
   print("The factorial of",num,"is",recur_factorial(num))  
