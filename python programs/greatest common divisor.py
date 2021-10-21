''' hello this code is in the form of a module type file ie only functions
the input is to be of the form int and int only for the first two types of functions
the program returns the greatest common divisor also known as the highest common factor
this is a common problem from middle school maths that is automated using python 
this program uses three different methods
method one is gcd_rec which uses a recursive function 
method two is gcd which uses a while loop instead of a recursive function
method three is gcd which is a function overloaded version and takes a numeric list as input and finds the gcd for the entire list
'''


"""
kindly note that any input being zero will instantly return zero back to the function call 
this is done so that the code doesnt enter any sort of unnecessary loops or terminate due to division by zero error
"""
def gcd_rec(a,b):
	a,b=max(a,b),min(a,b)
	if b==0:
		return 0
	if a%b==0:
        return b
    else :
        return gcd_rec(b,a%b)

def gcd(a,b):
	a,b=max(a,b),min(a,b)
	if b==0:
		return 0
	while a%b!=0:
		a,b=b,a%b
	return b


def gcd(l):
    l.sort()
    n=len(l)
    gcd=l[0]
	if gcd==0:
		return 0
    for i in range(n-1):
        div=l[i+1]
        while div%gcd!=0:
            div,gcd=gcd,div%gcd
        else:
            for j in l:
                if j%gcd!=0:
                    continue
    return gcd
