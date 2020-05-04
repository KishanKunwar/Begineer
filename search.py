# Linear Search

"""n = int(input("enter how many number should be in the list "))


this_list =[]
for i in range(n):
    x= int(input(f"enter the {i+1} number in the list "))
    this_list.append(x)

print(this_list)
this_list.sort()
print(this_list)

search = int(input("enter the number to be search in the list "))


def is_found():
    y=1
    for a in this_list:
        if a == search:
            print(f"found at {y}")
            break

        y=y+1
    else:
        print("not found")

is_found()

# Binary search
low_index = 0
upper_index = n-1

low_bound = this_list[0]
upper_bound = this_list[n-1]

mid_index = int((low_index + upper_index)/2)



for i in range(n):

    if this_list[mid_index]==search:
        print(f"found at {mid_index}")
        break
    else:
        if search > this_list[mid_index]:
            low_bound = this_list[mid_index]
            low_index = mid_index
            upper_index = n-1

        else:
            upper_bound = this_list[mid_index]
            low_index =0
            upper_index = mid_index

        mid_index = int((upper_index+low_index)/2)

else:
    print("number not found")"""



# Bubble sort -> sorting

number = [5,3,8,6,7,2]

"""n = len(number)
print(n)

for i in range(n-1):

    for x in range(n-1):
        if number[x] > number[x+1]:
            number[x], number[x+1] = number[x+1], number[x]

        print(number)

    n-=1"""


# Selection sort


for i in range(len(number)):

    # Find the minimum element in remaining
    # unsorted array
    min_idx = i
    for j in range(i + 1, len(number)):
        if number[min_idx] > number[j]:
            min_idx = j

            # Swap the found minimum element with
    # the first element
    number[i], number[min_idx] = number[min_idx], number[i]

# Driver code to test above
print("Sorted array")
for i in range(len(number)):
    print("%d" % number[i]),


print(number)













