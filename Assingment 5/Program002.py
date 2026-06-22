'''
Q2. Predict the output:

    b = bytes([65, 66, 67])
    print(b)

    explain how numbers are converted internally.

'''

b = bytes([65, 66, 67])
print(b)

'''
Explaination: Output:
b'ABC'

Explanation:
The bytes() function creates a bytes object from the given list of integers.
Each integer must be in the range 0 to 255 and represents an ASCII value.

65 -> 'A'
66 -> 'B'
67 -> 'C'

Internally, Python converts these integer values into their corresponding
ASCII byte representations and stores them as a bytes object.

Therefore, bytes([65, 66, 67]) becomes b'ABC'.

The prefix 'b' indicates that the object is of type bytes.
'''
