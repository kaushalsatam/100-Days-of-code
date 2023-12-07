# dictionaries in python
# key - value pairs {key : value}

programming_dictionary = {
    "Bug" : "An error in a program that prevents the program from running as expected.",
    "Function" : "A piece of code that you can easily call over and over again.",
    # "Loop" : "The action of doing something over and over again"
}

# # key is always provided as datatype they are mentioned into in the dictionaries
# print(programming_dictionary["Function"])

# adding new items to dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again"
# print(programming_dictionary)

# # empty dictionary
# empty_dictionary = {}

# # wipe an existing dictionary
# # programming_dictionary = {}
# # print(programming_dictionary)

# # Edit an item in a dictionary
# # programming_dictionary["Bug"] = "Newly assigned value"
# # print(programming_dictionary)

# # loop through dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])