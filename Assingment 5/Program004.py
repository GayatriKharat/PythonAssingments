'''
Q4. Predict the Output:
    
    ba = bytearray ([65, 66, 67])
    ba[0] = 97
    print(ba)

    why is this allowed?
'''
ba = bytearray ([65, 66, 67])
ba[0] = 97
print(ba)

#Explaination : This is allowed beacuse bytearray is mutable, so it's elements can be modified after creation.

