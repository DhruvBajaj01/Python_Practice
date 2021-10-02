s = input("Enter any string: ")
#take input from user
x = s.split()
#use split method to split at whitespaces
x.reverse()
#reverse all the elements of the string 
print(' '.join(x))
#concatenate them into a string