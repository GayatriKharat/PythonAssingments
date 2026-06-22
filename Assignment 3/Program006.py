'''
Q6. Write a Program to display:
    - Data Type 
    - Memory Address 
    - Size in bytes
    of a variable enterd by user.
'''
import sys

def main():
    user_input = eval(input("Enter a variable: "))

    print("Data Type: ", type(user_input))
    print("Memory Address: ", id(user_input))       
    print("Size in bytes: ", sys.getsizeof(user_input)) 
    
if __name__ == "__main__":
    main()