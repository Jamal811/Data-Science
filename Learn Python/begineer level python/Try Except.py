# try:
#     # asnwerr = 10/0
#     number = int(input("Enter a number: "))
#     print(number)
# except:
#     print("invalid input")
    
# try:
#     asnwerr = 10/0
# except ZeroDivisionError:
#     print("Divided by zero error")
    
# try:
#     asnwerr = 10/0
# except ZeroDivisionError as error:
#     print(error)

try:
    number = int(input("Enter a number: "))
    print(number)
except ValueError:
    print("invalid input")