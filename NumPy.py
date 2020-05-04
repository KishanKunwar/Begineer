import numpy as np

# 6 ways of creating an array in numpy
"""arr = np.array([1,2,3,4,5,]) #1-D
print(arr)
print(arr.ndim)#dispaly dimesnion of array

c= np.array([[1,2,3,],[4,5,6]]) #2-D array
print(c)
print(c.ndim)

d = np.array([[[1,2,3,],[4,5,6]],[[2,3,4],[4,5,6]]])#3-D array
print(d)
print(d.ndim)

xyz = np.array([1,2,3,4,5],ndmin=5)#dimension set
print(xyz)
print(xyz.ndim)


x = np.linspace(0,10,2)
print(x)

y= np.logspace(0,10,2)
print(y)

z = np.arange(1,10,2)
print(z)

a= np.zeros(5)
print(a)

b = np.ones(10)
print(b)"""


#Fuction in numpy

"""arr = np.array([1,2,3,4,5])
arr = arr+5

arr2 = np.array([2,3,4,5,6])

arr3 = arr + arr2 #Adding two array
print(arr3)

print(np.sin(arr))
print(np.concatenate([arr,arr2]))"""


#multi dimension array

"""d1 = np.array([1,2,3])
print(d1)

d2 = np.array([[1,2,3],
               [4,5,6]])
print(d2)
d12 = d2.flatten()
print(d12)"""

#flattern and reshape
"""d3 = np.array([ [ [1,2,3,8],
                  [4,5,6,8] ],

                [ [1,2,3,6],
                  [4,5,6,6] ] ])

d12= d3.flatten()
print(d12)


arr77 = d12.reshape(2,2,3) #2*2*3
print(arr77)"""

#matrix

m1 = np.matrix('1 2 3 ; 6 4 5 ; 1 5 7')
m2= np.matrix('3 4 5 ; 6 7 8 ;3 4 2')

print(m1+m2)
print(m1-m2)
print(m1*m2)
print(m1/m2)

















