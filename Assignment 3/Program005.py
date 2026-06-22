'''
Q5. What is the Diffrence between:
    print()
    return

    Explain with example.
'''
# The difference between print() and return is as follows:
# print() displays output on the screen but does not send a value back to the caller.
# return sends a value back to the caller and ends the function execution.

def print_example():
    print("This is a print statement.")

def return_example():
    return "This is a return statement."

def main():
    print_example() 
    result = return_example() 
    print(result)
    
if __name__ == "__main__":
    main()