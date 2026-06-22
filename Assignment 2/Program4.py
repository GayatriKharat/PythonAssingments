'''
Q4. What is the purpose of getsizeof()?
Why is memory size different for different data types?
'''
from sys import getsizeof


No1 = 11
No2 = 11.11
Str  = "Jay Ganesh"

print("Size of No1 is :", getsizeof(No1))
print("Size of No2 is :", getsizeof(No2))
print("Size of Str is :", getsizeof(Str))

'''
The getsizeof() function in Python is used to return the size of an object in bytes. It provides information about the memory consumption of different data types and objects.
The memory size is different for different data types because each data type has its own internal representation and
    structure. For example, an integer may require less memory than a floating-point number or a string because of the way they are stored in memory. Additionally, the size of an object can also depend on factors such as the length of a string or the number of elements in a list.
'''
