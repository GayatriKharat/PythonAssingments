'''
Q8. What is the range data type in python?
    How is it different from a list of numbers?

Answer:
    The range data type in Python is a built-in type that represents an immutable sequence of numbers. 
    It is commonly used for looping a specific number of times in for loops. 
    The range function generates a sequence of numbers based on the specified start, stop, and step(Jump) parameters.

'''

r = range(3, 9, 2)
print(list(r))  
print(type(r))

# The range data type is different from a list of numbers in several ways:
# 1. Immutability: The range object is immutable, meaning that once it is created, it cannot be modified. In contrast, a list of numbers is mutable, allowing for changes to its elements.
# 2. Memory Efficiency: The range object is more memory efficient than a list of numbers 
#    because it generates numbers on-the-fly as needed, rather than storing all the numbers in memory at once. A list of numbers, on the other hand, requires memory to store all its elements.