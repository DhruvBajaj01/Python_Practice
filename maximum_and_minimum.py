print("Enter the values in the tuple with a space.")
t = input()
a = tuple(int(x) for x in t.split())
#view this tuple
print(a)
# initializing K
K = 2
 
# Maximum and Minimum K elements in Tuple
# Using sorted() + loop
res = []
a = list(sorted(a))
 
for idx, val in enumerate(a):
    if idx < K or idx >= len(a) - K:
        res.append(val)
res = tuple(res)
 
# printing result
print("The extracted values : " + str(res))