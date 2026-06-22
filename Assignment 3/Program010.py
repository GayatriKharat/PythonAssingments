'''
Q10. Explain how Python manages memory automatically.
     Why does the program not need to explicitly allocate or free memory?
'''
'''
Answer:
Python manages memory automatically through a built-in garbage collector that handles memory allocation and deallocation. 
When objects are created in Python, memory is allocated for them automatically. 
The garbage collector keeps track of the number of references to each object. When an object is no longer referenced (i.e., there are no more references to it), the garbage collector automatically frees the memory occupied by that object.
This automatic memory management means that programmers do not need to explicitly allocate or free memory, reducing the risk of memory leaks and other memory-related issues. 
The garbage collector runs periodically to clean up unused objects, ensuring efficient memory usage without requiring manual intervention from the programmer.    
'''