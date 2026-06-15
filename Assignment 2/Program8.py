'''
Q8. Predict the output:
    x = input("Enter a number: ")
    print(type(x))
    Explain the reason.
'''
x = input("Enter a number: ")
print(type(x))

'''
OUTPUT:
<class 'str'>
The reason for this output is that the input() function in Python always returns a string. When you use input(), it captures everything the user types and treats it as text, regardless of whether it looks like a number or not. Therefore, even if you enter a number, it will be stored as a string, and the type of x will be <class 'str'>.
'''

