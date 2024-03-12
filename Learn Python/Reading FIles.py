# employee_file = open("read.txt", "r")
# print(employee_file.readable())
# employee_file.close()

# employee_file = open("read.txt", "w")
# print(employee_file.readable())
# employee_file.close()

# employee_file = open("read.txt", "r")
# print(employee_file.read())
# employee_file.close()

# employee_file = open("read.txt", "r")
# print(employee_file.readline())
# print(employee_file.readline())
# print(employee_file.readline())
# employee_file.close()

# employee_file = open("read.txt", "r")
# print(employee_file.readlines())
# employee_file.close()

# employee_file = open("read.txt", "r")
# print(employee_file.readlines()[2])
# employee_file.close()

employee_file = open("read.txt", "r")
for employee in employee_file.readlines():
    print(employee)
employee_file.close()


