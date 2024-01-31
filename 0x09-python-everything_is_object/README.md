data types in python are objects and the only controlling factore is the concept of mutable and immutable 
#mutable
lists
sets
dictionaries
#immutable
int strings 
tuples 
and so on ....

immutable: when we create two different variables with the same variable they pint to the same object and refer to the same address
a = 5
b = 5
a and b point to the object 5
and """ immutable means unchangeable; cannot change the value with staying in the same address, rather than it overrides the variable to point to another objct.
for instance, if changed a = 8
>>> print(id(a) is id(b))
false ___only b point to 5 while a point to 8___

x = "hi"
y = x
>>> print(id(x) is id(y))
true

x = "hello"
>>> print(x)
hello
>>> print(y)
hi
and difintley, id of x differ y
"""

mutable: creating two mutable objects with the same value gives us two different addresses 
x = [1, 2, 3]
y = [1, 2, 3]
>>> print(id(x) is id(y))
false
z = x
x = [1, 4, 3] ___changeable; can edit the mutable obj within the same obj__
>>> print(z)
[1, 4, 3]

>>>
l1 = [1, 2, 3]
l2 = l1
print(id(l1), id(l2))
l1.append(4)
print(l2)
______
l1 = [1, 2, 3]
l2 = l1
print(id(l1), id(l2))
l1.append(4)
print(l2)
""" append modify in place """"
______
def assign_value(n, v):
    print(id(n), id(v))
    n = v
    print(n)
    print(id(n), id(v))

l1 = [1, 2, 3]
l2 = [4, 5, 6]
print(id(l1), id(l2))
assign_value(l1, l2)
print(id(l1), id(l2))
print(l1)


#output 
3019195275520 3019195273600
3019195275520 3019195273600
[4, 5, 6]
3019195273600 3019195273600
3019195275520 3019195273600
[1, 2, 3]
______

is works for comparison by reference 
== works for comarison by values
