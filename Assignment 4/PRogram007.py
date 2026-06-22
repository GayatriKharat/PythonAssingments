'''
Q7. Predict the ouput:
    
    d = {1: "one", 1: "ONE", 2: "Two"}
    print(d)

'''

d = {1: "one", 1: "ONE", 2: "Two"}
print(d)

# The output will be: {1: 'ONE', 2: 'Two'}
# This is because in a dictionary, keys must be unique.
# When the dictionary is created, the second occurrence of the key `1` with the value `"ONE"` will overwrite the first occurrence of the key `1` with the value `"one"`.
# As a result, the final dictionary will only contain the last value associated with the key `1`, which is `"ONE"`, and the key `2` with the value `"Two"` will remain unchanged.