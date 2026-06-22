'''
Q3. Predict the output:
    lst = [10, 20, 30]
    tpl = (10, 20, 30)

    lst[0] = 100
    tpl[0] = 100
    which line wil raise an error and why?
'''
lst = [10, 20, 30]
tpl = (10, 20, 30)

lst[0] = 100
tpl[0] = 100  # Error

# The line `tpl[0] = 100` will raise an error because tuples are immutable in Python, meaning that their elements cannot be changed after they have been created. 
# In contrast, lists are mutable, allowing for modification of their elements. 
# Therefore, while `lst[0] = 100` will successfully change the first element of the list to 100, attempting to change the first element of the tuple will result in a TypeError.