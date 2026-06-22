'''
Q4. Write a Functoin that does not return anything but prints a message.
    Explain the default return value of such a function.
'''
# Function that does not return anything but prints a message

def add(a, b):
    print("Sum of two numbers is: ", a + b)

def main():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    add(num1, num2) 

if __name__ == "__main__":
    main()

# Default return value of such a function is None, which means it does not return any value.

'''
Output: Sum of two numbers is:  15 
'''