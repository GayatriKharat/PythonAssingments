'''
Q1. What is a user defined Function ?
Ans - The user Defined function is the Function which is craated by Programmer using def.
      Which is used to perform a specific task. It is used to break the program into smaller and modular chunks. 
      It helps in code reusability and makes the program more organized and manageable.
'''
'''
Write a function to accept two numbers and return their multiplication. 
'''

def Multiplication():  #User Defiend Function
    No1 = int(input("Enter first number: "))
    No2 = int(input("Enter second number: "))
    Result = No1 * No2
    return Result
    
def main(): #Main Function
    print("Multiplication of two numbers is: ", Multiplication())

if __name__ == "__main__": #Entry point of the program (Starter)
    main()