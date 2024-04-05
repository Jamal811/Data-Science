# a decorator is a function that takes another function as an aurgument and extends the behavior of this function without explicitly modifying it

# It allows you to add new functionality  to an existing function 

# def start_end_decorator(func):
    
#     def wrapper():
#         print('start')
#         func()
#         print('end')
#     return wrapper

# @start_end_decorator
# def print_name():
#     print('jamal')
    
# print_name()

# def start_end_decorator(func):
    
#     def wrapper(*args, **kwargs):
#         print('start')
#         result = func(*args, **kwargs)
#         print('end')
#         return result
#     return wrapper

# @start_end_decorator
# def add(x):
#     return x + 5
    
# result = add(5)
# print(result)

import functools

# def start_end_decorator(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         print('start')
#         result = func(*args, **kwargs)
#         print('end')
#         return result
#     return wrapper

# @start_end_decorator
# def add(x):
#     return x + 5
    
# print(add.__name__)
# print(help(add))

# def repeat(num_times):
#     def repeat_decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             for _ in range(num_times):
#                 result = func(*args, **kwargs)
#             return result
#         return wrapper
#     return repeat_decorator
    
    

# @repeat(num_times = 4)
# def greet(name):
#     print(f"Hello {name}")

# greet('Jamal')

# Class decorators
class CountCalls:
    
    def __init__(self, func):
        self.func = func
        self.num_calls = 0
    
    def __call__(self, *args, **kwargs):
        self.num_calls += 1 
        print(f"This function is executed {self.num_calls} times")
        return self.func(*args, **kwargs)

@CountCalls
def say_hello():
    print('hello')

say_hello()
say_hello()
say_hello()