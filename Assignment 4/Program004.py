'''
Q4. Explain why strings are immutable in python.
    What happens internally when you modify a string varibles?

Ans:
    Strings are immutable in Python because once a string is created, it cannot be changed. 
    This design choice allows for several benefits, including improved performance and security.

    When you modify a string variable, what happens internally is that a new string object is created
    with the modified value, and the variable now references this new string object.
    
    The original string remains unchanged in memory, and if there are no references to it, it may be garbage collected by Python's memory management system.
    This immutability also allows strings to be used as keys in dictionaries and elements in sets, as they are hashable and their hash value remains constant throughout their lifetime. 
'''