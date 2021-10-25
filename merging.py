n1=int(input())
l1=[int(x) for x in input().split()]
n2=int(input())
l2=[int(x) for x in input().split()]
l=l1+l2
l.sort()
print(*l)
