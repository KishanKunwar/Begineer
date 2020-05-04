
#Febonacci Sequence

"""n = int(input("enter the number "))

x = 0
y = 1

def fibo(n):
    global x, y
    for i in range(n):
        z = x+y
        print(z)
        x=y
        y=z


fibo(n)"""


#Factoraial

"""number = int(input("enter the number you want factoraial"))

x=1
def fac(number):
    global x
    for i in range(2,number+1):
        x = i*x


    print(x)

fac(number)"""

#Recursion
"""import sys

sys.setrecursionlimit(50)

i = 0

def greet():
    global i
    i+=1
    print(i)
    print("hello")
    greet()

greet()"""

#Recursion for factorial
"""import sys

n= int(input("enter the number to do factoraila"))


def fac(n):
    if n==0:
        return 1
    result = n*fac(n-1)
    return result




print(fac(n))"""

# lambda

"""def square(n):
    return n*n

print(square(12))

# INSTED OF ABOVE WE CAN WRITE

f =lambda n : n*n 
print(f(5))"""


# Filter

#def is_even(n):
    #return n%2==0

"""number = [1,2,4,5,7,3,4,2,9]

even = list(filter(lambda n : n%2==0 ,number))
print(even)"""

#Double

#def to_double(n):
   # return n*2
"""double = list(map(lambda n : n*2,number))
print(double)"""


#Reduce
"""from functools import reduce
#def sum(x,y):
    #return x+y
sum = reduce(lambda x,y:x+y,number)
print(sum)"""


#Decorators

def div(x,y):
    return x/y



def smart_div(function):

    def inner(x,y):
        if x <y:
            x,y =y,x
            return function(x,y)
    return inner


xyz = smart_div(div)
print(xyz(2,4))





