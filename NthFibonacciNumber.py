'''
Given a number n, print the nth Fibonacci Number. Numbering starts from 0.

Example Input
0
Output
0
'''

n = int(input())

if n == 0:
    f3 = 0
else:
    f1 = 0
    f2 = 1
    f3 = 1
    c = 3
    while(c <= n):
        f1 = f2
        f2 = f3
        f3 = f1+ f2
        c+=1
print(f3)
