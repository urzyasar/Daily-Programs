#fibonacci using generator funtion
def fibonacci(n):
    a,b=0,1
    while n>0:
        yield a
        a,b=b,a+b
        n-=1
for num in fibonacci(5):
    print(num)
    
 """   
Function with yeild keyword in it is Generator funtion.
If you print the return value of that funtion , you can find the iterator object.
Only difference is , it having no return keyword.
However, it will process one by one value and pause and return it.

Watched video: telusko
Geeks site:https://www.geeksforgeeks.org/python-yield-keyword/
"""
    
