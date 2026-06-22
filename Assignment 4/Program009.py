'''
Q9. Predict the Output:
    r = range(5)
    print(r)
    print(list(r))

'''
r = range(5)
print(r)        
print(list(r))

'''
Explaination: range requires at least one parameter in above example we have given '5' .
             so for remaining 2 parameters it will take default values as '0' for Start and '1' for Step(Jump)
             Will print output as :
             range(0, 5)
             [0, 1, 2, 3, 4]
'''