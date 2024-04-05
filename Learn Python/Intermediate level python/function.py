# def greet(first_name, last_name): # these are perameters
#     print(f"Hello {first_name} {last_name}")
    
# greet("Jamal", "Shah") #these are aurgumets

# two types of functions
# 1- perfome a task
# def greet(name):
#     print(f"Hi {name}")
# greet('jamal')
# # 2- return a value
# def greet(name):
#     return f"Hi {name}"
# result = greet('Shah')
# print(result)
# greet('jamal')

# keyword aurgument
# def increment(number, by):
#     return number + by

# print(increment(2, by=1))

# Optional Parameter
# def increment(number, by=1): # if you want to pass another parameter so use it before the by=1
#     return number + by

# print(increment(2))

# number of auguments

# def multifly(*numbers):
#     total = 1
#     for number in numbers:
#         total *= number
#     return total

# print(multifly(1, 4, 5, 6))

# **args

# def save_user(**user):
#     print(user["name"])
# save_user(id=1, name='shah', age='23')

# fizzbuzz

def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return "FizzBuzz"
    if input % 3 == 0:
        return "Fixx"
    if input % 5 == 0:
        return "Buzz"
    return input
    
    
print(fizz_buzz(15))
        