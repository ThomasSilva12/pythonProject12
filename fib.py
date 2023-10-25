### Thomas Silva
### ENGR 103 project 4b.

def fib(num):
    if num <= 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fib(num - 1) + fib(num - 2)


### This section of the code tests the function
print(fib(1))  # Output: 1
print(fib(3))  # Output: 2
print(fib(20)) # Output: 55
