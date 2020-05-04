import array

"""value = array.array("i",[1,2,3,4,-1,4])

print(value.buffer_info())
print(value.typecode)
value.reverse()
print(value)
print(value[2])
for x in value:
    print(x)

value.append(2)#add value
print(value)
value.pop(2) #remove value
print(value)
value.insert(4,2)#value inserting (index,value)
print(value)

new_array = value.__copy__()#array copy
print(new_array)

new2_array = array(value.typecode)
print(new2_array)

i=0
while i < len(value):
    print(value[0])
    i+=1"""


#Array value to the user

"""arr = array.array('i',[])

number = int(input("how many values to be added "))

for i in range(0,number):
    value = int(input("enter the value"))
    arr.append(value)

x = int(input("enter the value you want to serch"))
k=0
for y in arr:
    if x==y:
        print("found")
        print(arr.index(y))#index of serch number is printed
        break
    k+=1
else:
    print("not found")"""

arr = array.array("i", [1,2,-3,4,5,5])
print(arr)
arr.append(12)
print(arr)
arr.insert(0,33)
print(arr)
arr.pop(2)
print(arr)
arr.remove(-3)
print(arr)
arr.reverse()
print(arr)
print(arr.index(5))
print(arr.buffer_info())



