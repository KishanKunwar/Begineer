#prime number

#number = int(input("enter the number"))

"""for i in range(2,number):

    if number % i==0:
        print("its not prime")
        break



else:
    print("it is a prime number")"""

#time calculation and another method function and return
"""import time

t = time.time()

def isPrime(number):
     if number <=1:
         print("number shoule be greater than 1")

     else:

         for i in range(2,number):

             if number %2==0:
                 return False
             break

         else:
             return True


print(isPrime(number))

t2= time.time()

print("time taken is ", t2-t)"""

"""import math
def isprime(number):
    if number <=1:
        print("number should be greater than 2")

    elif number%2==0:
        return False

    else:
        maxdivior = math.floor(math.sqrt(number))
        for i in range(3,maxdivior+1):
            if number%2==0:
                return False
                break
        else:
            print("prime")



print(isprime(number))"""



def isPrime(number):
    if number <= 1:
        print("number should be greater than one ")
    else:

        for i in range(2,number):
            if number%2==0:
                print("Not prime")
                break
        else:
            print("Is prime")


#isPrime(number)



