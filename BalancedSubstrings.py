x=int(input())
 
 
while x!=0:
    num=int(input())
    str=input()
    acnt=0
    flag=0
    bcnt=0
    for i in range(0,num-1):
        for j in range(i+1,num):
            if str[i:j+1].count("a")==str[i:j+1].count("b"):
                print(i+1,j+1)
                flag=1
                break
            acnt=0
            bcnt=0
        if flag==1:
            break               
    if flag==0:
        print("-1 -1")
 
 
    x=x-1
    
