'''
Q1. What is the difference between List and Tuple in python ?
    Explain in terms of:
    - Mutability
    - Memory 
    - Performance
    - Use Cases
Ans:
    |------------------------------------------------------------------------------|
    | Aspect       | List                          | Tuple                         |
    |--------------|-------------------------------|-------------------------------|
    | Mutability   | Mutable (can be modified)     | Immutable (cannot be modified)|
    |------------------------------------------------------------------------------|
    | Memory       | Uses more memory due to       | Uses less memory due to       |    
    |              | dynamic resizing and overhead | fixed size and less overhead  |
    |------------------------------------------------------------------------------|
    | Performance  | Slower due to mutability      | Faster due to immutability    |
    |------------------------------------------------------------------------------|
    | Use Cases    | Suitable for collections      | Suitable for fixed collections|
    |              |  that may need to be modified | that should not change        |
    |------------------------------------------------------------------------------|
    
    - Lists are ideal for scenarios where you need to add, remove, or modify elements frequently, such as in data processing or when working with collections of items that may change.
    - Tuples are ideal for scenarios where you want to ensure that the data remains constant,
        such as in cases where you want to use the data as keys in a dictionary or when you want to return multiple values from a function without allowing modification.

'''
