# This is the Python program to ask the user for their name, age, and location,
# and then print a personalized message.

# Asking the user to input their name and storing it in the variable "name"
name = input("Please enter your name: ")

# Asking the user to input their age and storing it in the variable "age"
# The input is treated as a string, so if you need to use it as a number later, you'll need to convert it.
age = input("Please enter your age: ")

# Asking the user to input their location and storing it in the variable "location"
location = input("Please enter your location: ")

# Printing a personalized message using the user's input
# The placeholders {} in the string are replaced by the values of name, age, and location
print(f"Hello {name}, you are {age} years old and live in {location}.")
