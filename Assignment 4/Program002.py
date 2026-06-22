'''
Q2. Why are tuples faster than List ?
    In which real-world scenario would you prefer a tuple over a list ?

Answer:
      
    Tuples are faster than lists in Python due to their immutability. Since tuples cannot be modified after creation, they have a smaller memory footprint and less overhead compared to lists, 
    which are mutable and require additional memory for dynamic resizing and management of elements. This makes tuple operations generally faster than list operations.

    Real-world scenarios where you would prefer a tuple over a list include:
    - When we need to store a collection of items that should not change, such as coordinates (x, y) or RGB color values.
    - When we want to use the collection as keys in a dictionary, since tuples are hashable while lists are not.
    - When returning multiple values from a function where the returned values should remain constant and not be modified by the caller.
'''
