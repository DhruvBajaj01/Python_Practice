n = int(input("enter a number"))

if n%2 !=0 :
    for i in range(1,n+2,2):
        fact = 1
        for j in range(1,i+1):
            fact = fact*j
        print(fact)
if n%2 ==0 :
    for i in range(2,n+2,2):
        fact = 1
        for j in range(2,i+1):
            fact = fact*j
        print(fact)
    
