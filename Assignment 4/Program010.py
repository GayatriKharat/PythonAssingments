'''
Q10. What isthe Difference between:
     range(1, 10)
     range(1, 10, 2)

     Explain the parameters.

'''
r1 = range(1, 10)
r2 = range(1, 10, 2)

print(r1)
print(list(r1))

print(r2)
print(list(r2))

'''
Explaination: In r1 Starting point is 1 and End point is 10 we have not given Step(Jump) hence it will by default choose step as 1 and give the output as:
              range(1, 10)
              [1, 2, 3, 4, 5, 6, 7, 8, 9]

              In r2 we have provided all the parameters hence it will jump for 2 and will give the output as:
              range(1, 10, 2)
              [1, 3, 5, 7, 9]  
'''