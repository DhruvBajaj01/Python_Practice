# Sum of Digits
# Example1 -> 123 => 1 + 2 + 3 = 6
# Example2 -> 5678 => 5 + 6 + 7 + 8 = 26

n = input("NUMBER : ")
s = 0
for i in n:
    s += int(i)
print("SUM OF DIGITS : ", s)
