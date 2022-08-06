"""
Check if a queue can be sorted into another queue using a stack

"""

"""
Input : Queue[] = { 5, 1, 2, 3, 4 } 
Output : Yes 
Pop the first element of the given Queue i.e 5. 
Push 5 into the stack. 
Now, pop all the elements of the given Queue and push them to 
second Queue. 
Now, pop element 5 in the stack and push it to the second Queue. 
  
Input : Queue[] = { 5, 1, 2, 6, 3, 4 } 
Output : No 
Push 5 to stack. 
Pop 1, 2 from given Queue and push it to another Queue. 
Pop 6 from given Queue and push to stack. 
Pop 3, 4 from given Queue and push to second Queue. 
Now, from using any of above operation, we cannot push 5 
into the second Queue because it is below the 6 in the stack. 


"""