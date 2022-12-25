#Import the square fundtion from function file.

#One way to do it
# from functions import Square

# for i in range(10):
#     print(f"The Square of {i} is {Square(i)}")

#Another way

import functions

for i in range(10):
    print(f"The Square of {i} is {functions.Square(i)}")
