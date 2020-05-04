

#operator overlaoding
"""class Student:

    def __init__(self,m1):
        self.m1 = m1

    def __add__(self, other):
        x = self.m1 + other.m1
        return x

    def __mul__(self, other):
        mul = self.m1*other.m1
        return mul






s1= Student(40)
s2 = Student(55)

s3 = s1 + s2
s4= s1*s2

print(s3) # In backgroud it is Student.__add__(x,y)

print(s4)"""


#method overloading

#Abstract class and abstract method

""""from abc import ABC , abstractmethod

class Animal(ABC):
    @abstractmethod
    def act(self):
        pass

    @abstractmethod
    def abs(self):
        pass

    def display(self):
        print("hello")

class Human(Animal):

    def act(self):
       print("hello world")

    def xyz(self):
        print("namstay")

    def abs(self):
        print("darshan")



h = Human()
h.act()
h.xyz()
h.abs()"""


#iterator

""""nunm = [1,2,3,4,5,2,3,8]

it = iter(nunm)

print(it.__next__())
print(it.__next__())

#for creating own iterator

class TopTen:

    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= 10:
            val = self.num
            self.num +=1
            return val
        else:
            raise StopIteration


x = TopTen()

for i in x:
    print(i)"""


#Generator

"""def get_generator():

    yield 1
    yield 2
    yield 3


print(get_generator())"""

num1 = int(input("enter the first number (numerator) "))
num2= int(input("enter the second number(denomenator) "))
try:
    num3 = num1/num2
    print(num3)
except Exception as e:
    print("denomenator should not be zero",e)
finally:
    print("finally")

print("end")

if num1 <2:
    raise Exception("number should be greater than 2")
print("hello")







