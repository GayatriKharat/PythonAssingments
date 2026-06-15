'''
Q3. What does the id() function return?
Is the value returned by id() same for two variables holding the same value?
'''
a = 10
b = 10      

print("ID of a is:", id(a))
print("ID of b is:", id (b))

'''
In Python, the id() function returns the identity of an object, which is a unique integer that represents the memory address where the object is stored.
In the case of immutable objects like integers, Python optimizes memory usage by reusing the same memory location for identical values. Therefore, when we assign the value 10 to both a and b, they point to the same memory location, and id(a) and id(b) will return the same value.
However, for mutable objects like lists, each variable will point to a different memory location even if they contain the same values. In such cases, id() will return different values for each variable.
'''