'''
Q9. What is the difference between:

    x = 10
    x = "Ten"
Is it allowed? Why?
'''
def main():
    x = 10
    print("Value of x:", x)
    print("Type of x:", type(x))

    x = "Ten"
    print("Value of x:", x)
    print("Type of x:", type(x))

if __name__ == "__main__":
    main()

'''
Output:
Value of x: 10
Type of x: <class 'int'>

Value of x: Ten
Type of x: <class 'str'>

Explanation: In Python, variables are dynamically typed, which means that the type of a variable can change during the execution of a program. 
             In the example above, the variable 'x' is first assigned an integer value (10), and later it is reassigned a string value ("Ten"). 
             This is allowed in Python because the language does not require explicit type declarations, allowing for flexibility in variable usage.

'''