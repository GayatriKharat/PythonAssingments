'''
Q9. Write a program to take user's name and age and display:
    Hello <name>, you will turn <age+1> next year.
'''
print("-----------------------------------------------------------")
print("-------------Let's Guess Your Next Year Age!---------------")
print("-----------------------------------------------------------")

print("Enter Your Name: ")
name = input()

print("Enter Your Age: ")
age = int(input())

next_year_age = age + 1 
print("Hello", name +", You will turn", next_year_age, "next year.")

print("-----------------------------------------------------------")
print("-------------Thank You for Using Our Program!--------------")
print("-----------------------------------------------------------")
