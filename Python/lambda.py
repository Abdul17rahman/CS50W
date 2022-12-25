#Lambda is a way of representing a single line function.

#Create a list of dicts
# people = [
#     {"name":"Abdul", "address":"Buziga"},
#     {"name":"Hadija", "address":"Kitintale"},
#     {"name":"Birungi", "address":"Luzira"}
# ]

# #Try to sort the dict
# people.sort()

# print(people)

#Improve the code as the one above cause a Type error

# people = [
#     {"name":"Abdul", "address":"Buziga"},
#     {"name":"Hadija", "address":"Kitintale"},
#     {"name":"Birungi", "address":"Luzira"}
# ]

# #Create a function that return the key to sort with.
# def f(person):
#     #We are sorting with a key of name
#     return person["name"]

# #We sort the list by adding a key.
# people.sort(key=f)

# print(people)

#Use Lambda to solve the problem, w/c is a func that takes in and returns a single value

people = [
    {"name":"Abdul", "address":"Buziga"},
    {"name":"Hadija", "address":"Kitintale"},
    {"name":"Birungi", "address":"Luzira"}
]


#We sort the list by adding a key and using a lambda function
people.sort(key= lambda person : person["name"])

print(people)
