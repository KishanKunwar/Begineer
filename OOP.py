#inner class
"""class Device:


    def __init__(self,size,type):
        self.size = size
        self.type = type
        #inner class object creation inside the outerclass
        self.mobile = self.Phones("8GB", "48MP", "4500MaH")
        self.mobile2 = self.Phones("6GB", "108MP", "4250MaH")
        self.lap = self.Laptop("8GB", "i5", "256SSD")
        self.lap2 = self.Laptop("6GB", "i7", "1TB")

    def display(self):
         return self.size, self.type

    class Phones:

        def __init__(self, ram, camera, battery):
            self.ram = ram
            self.camera = camera
            self.battery = battery


        def display(self):
            return self.ram,self.camera,self.battery




    class Laptop:

        def __init__(self, ram, processor, storage):
            self.ram = ram
            self.processor = processor
            self.storage = storage

        def display(self):
            return self.ram,self.processor,self.storage


#objection creation of main class
obj = Device(48,"electronics")
print(obj.display())
print()

#inner class method access
print(obj.mobile.display())

print(obj.mobile2.display() )

print()


print(obj.lap.display())
print(obj.lap2.display())

#object creation of inner class outside the class
mobile = Device.Phones("8GB", "48MP", "4500MaH")
print(mobile.display())"""


#Inheritance

#PARENT CLASS

"""class Human:

    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname

    def display(self):
        print(f"HELLO {self.fname} {self.lname}, you are welcome to python tutorial")

class Male:

    def show(self):
        print("show the name ")


#multiple inheritance
class Boy(Human, Male):

    def getname(self):
        print("get the name")

h1 = Human("Kishan", "Kunwar")
h1.display()

b1 = Boy("amrit","gurung")

b1.display()
b1.show()
b1.getname()"""


#Method Resolution Order(MRO)

class A:

    def __init__(self):
        print("A init ")


    def feature1(self):
        print("Feature A1")


class B:

    def __init__(self):

        print("B init")

    def feature1(self):
        print("Feature B1")

#sub cass of both A and B
class C(A,B):
    def __init__(self):
        super().__init__()#since A is in left at (A,B) a init is called
        print("C init")

    def featureC1(self):#since A is in left at (A,B)  feature1 of A is called
        print("Feature C1")


a1 = A()
a1.feature1()

b1= B()
b1.feature1()

c1 = C()
c1.feature1()





#if super class init has 2 parameter and sub class init hasa 3 parameter
"""class A:

    def __init__(self,fname , lname):
        self.fname = fname
        self.lname = lname

    def display(self):
        print(f"{self.fname} , {self.lname}")


class B(A):
    def __init__(self, fname,lname,year):
        super().__init__(fname,lname)       #say that it will only pass 2 parameter to super init 
        self.year = year
    def display(self):
        print(f"{self.fname} , {self.lname} , {self.year}")


a1 = A("Kishan","kunwar")
a1.display()
print()

b1 = B("kaveeta", "karki" ,2020)
b1.display()"""




