'''
Q1. What is bytes in python?
    Why are they immutable?

Answer:
    - bytes is a Data Type in the Python mostly used in file handling and networking.

    - bytes are the immutable beacuse they are designed to represent fixed, raw binary data (like files or network streams). 
      Once created, their underlying memory allocation cannot be altered.

    - One advantage of having an immutable bytes type is that code objects can use these. 
      It also makes it possible to efficiently create hash tables using bytes for keys; 
      this may be useful when parsing protocols like HTTP or SMTP which are based on bytes representing text.
'''