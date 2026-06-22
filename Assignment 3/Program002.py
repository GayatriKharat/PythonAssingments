'''
Q2. Write a Difference between:
    - Function with parameters
    - Function without parameters

Ans - -------------------------------------------------------------------------
       Function with Parameters              Function Without Parameters
      -------------------------------------------------------------------------
      1. Requires external values          1. Does not require any external
        when called.                          Values during execution.

      2. Can perform operations based       2. Performs operations that do not
         on the provided parameters.          depend on any input.

      3. Example:                            3. Example:
         def add(a, b):                        def greet(): 
      ---------------------------------------------------------------------------            
'''
# Function with parameters
def add(a, b):
    return a + b

# Function without parameters
def greet():
    return "Jay Ganesh! Thank You for using my program."

def main():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print("Sum of two numbers is: ", add(num1, num2))
    print(greet())

if __name__ == "__main__":
    main()
