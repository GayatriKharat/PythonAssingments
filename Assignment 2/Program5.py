'''
Q15. Predict Output
    a = 10
    b = 10
    print(id(a) == id(b))
'''
a = 10
b = 10
print(id(a) == id(b))

'''
OUTPUT:

True
In this case, the output is True because both a and b are assigned the same integer value 10. Since integers are immutable in Python, both a and b point to the same memory location where the value 10 is stored. Therefore, id(a) and id(b) will return the same memory address, making the expression id(a) == id(b) evaluate to True.
'''