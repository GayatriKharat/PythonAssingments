'''
Q8. Explain why the following code works without declaration:
    
    x = 10
    compare this with C or java.
'''

def main():
    x = 100
    print(x)

if __name__ == "__main__":
    main()

'''
Output: 100
Reason: In Python, variables are dynamically typed, which means we do not need to declare the type of a variable before using it. 
The type is inferred at runtime based on the value assigned to the variable. 
In contrast, languages like C or Java require explicit declaration of the variable type before it can be used.
Example in C:
int x = 100; // Declaration and initialization of an integer variable.
'''