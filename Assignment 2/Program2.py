'''
Q2. What is the Difference between 
     a = 10
     b = 10

     and

     a = [10]
     b = [10]
'''

a = 10
b = 10
print("a =", a, "and b =", b)
print("ID of a is:", id(a))
print("ID of b is:", id(b))

a = [10]
b = [10]
print("a =", a, "and b =", b) 
print("ID of a is:", id(a))
print("ID of b is:", id(b)) 

'''
In the first case, a and b are assigned the same integer value 10. Since integers are immutable in Python, both a and b point to the same memory location where the value 10 is stored. Therefore, id(a) and id(b) will return the same memory address.

In the second case, a and b are assigned two separate list objects, each containing the value 10. Lists are mutable in Python, so a and b point to different memory locations even though they contain the same value. Therefore, id(a) and id(b) will return different memory addresses.
'''