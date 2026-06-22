'''
Q5. Predict the output:

    s = "Python"
    print(id(s))
    s = s + "3"
    print(id(s))

    explain the reason for change / no change in id ().
'''
s = "Python"
print(id(s))
s = s + "3"
print(id(s))

# The output will show two different id values for the variable `s`.
# This is because strings are immutable in Python. 
# When we concatenate strings, a new string object is created, and the variable `s` now references this new object. 
# The original string remains unchanged in memory.