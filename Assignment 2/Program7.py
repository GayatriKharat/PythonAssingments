'''
Q7. Why does the input()function always return a string?
How can you convert it to another data type?
'''
print("Enter a number:")
a = input()

print("Type of a is before Typecasting(input()):", type(a))
a = int(a)
print("Type of a is after Typecasting(int(input()):", type(a))


'''
The input() function in Python always returns a string because it is designed to read user input as text. When you use input(), it captures everything the user types and treats it as a string, regardless of whether it looks like a number or not.
To convert the input to another data type, you can use typecasting functions. For example, if you want to convert the input to an integer, you can use the int() function. If you want to convert it to a floating-point number, you can use the float() function. Here's how you can do it:

# Convert input to an integer
a = int(input("Enter a number: "))
print("Value of a is:", a)  
print("Type of a is:", type(a)) 

In this example, the input is first captured as a string, and then it is converted to the desired data type using the appropriate typecasting function.
'''