
f = open("ABC","r")
"""print(f.readline(),end="")
print(f.readline(),end="")
print(f.readline(),end="")"""

#we can print from for loop as well

for i in f:
    print(i)

#to write in file
x = open("xyz","w")
x.write("   ")#this will replace the current lines in that file os in order to not remove we can use append "a"

ab = open("xyz","a")
ab.write("    ")


cz = open("newfile","x") #this will creat new file , if file already exits it show an error



