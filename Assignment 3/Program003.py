'''
Q3.Predict the Output:
    
def fun():
    x = 10
    print(x)

fun()
print(x)

Explain the reason.
'''

def fun():
    x = 10
    print(x)

fun()
print(x)

'''
Output: 10
10  
NameError: name 'x' is not defined

Reason: The variable 'x' is defined inside the function 'fun()', which means it has a local scope.
        When we call 'fun()', it prints the value of 'x' which is 10.
        However, when we try to print 'x' outside the function, it results in a NameError because 'x' is not defined in the global scope.
'''