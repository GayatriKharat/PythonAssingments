'''
Q6. What is a dictionary in python?
    - key-value pair
    - why keys must be immutable
    - why duplicate keys are not allowed

Answer:
    A dictionary in Python is a built-in data structure that stores data in the form of key-value pairs. Each key is unique and maps to a specific value, allowing for efficient retrieval of data based on the key.

    Keys must be immutable because they need to have a fixed hash value that does not change during their lifetime. 
    
    This allows dictionaries to quickly look up values based on their keys. If keys were mutable, their hash value could change, leading to inconsistencies and making it impossible for the dictionary to reliably retrieve values.

    Duplicate keys are not allowed in a dictionary because each key must be unique to ensure that there is a clear mapping between keys and values.
     
    If duplicate keys were allowed, it would create ambiguity when trying to access values, as the dictionary would not know which value to return for a given key.

'''