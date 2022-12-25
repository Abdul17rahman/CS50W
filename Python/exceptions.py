#This program is going to handle exceptions that may arise from running a program

#Import the sys module for exit status and code
import sys

#this is how a prog can run normally.
# x = int(input("X: "))
# y = int(input("Y: "))

# results = x / y

# print(f"{x} / {y} is {results}")

#We can catch the zero div exception as shown below.
# x = int(input("X: "))
# y = int(input("Y: "))

# try:
#     results = x / y
# except ZeroDivisionError:
#     print("Can not divide by zero")
#     sys.exit(1)


# print(f"{x} / {y} is {results}")

#Catch the value error.
try:
    x = int(input("X: "))
    y = int(input("Y: "))
except ValueError:
    print("invalid input")
    sys.exit(1)

try:
    results = x / y
except ZeroDivisionError:
    print("Can not divide by zero")
    sys.exit(1)


print(f"{x} / {y} is {results}")