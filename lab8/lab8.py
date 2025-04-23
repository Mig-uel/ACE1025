"""
Miguel Castillo
April 20, 2025
Introduction to Python
"""

# Single Line Comment: This line will not run


print('\n----- Example 2: Strings ----- ')
print("\t Good morning!\nThis is my first Python code!")

print('\n----- Example 2: Data Types ----- ')
print(f"Data Type of 3.56: {type(3.56)}")
print(f"Data Type of -10: {type(-10)}")
print(f"Data Type of 'hello': {type('hello')}")
print(f"Data Type of True: {type(True)}")
print(f"Data Type of False: {type(False)}")
print(f"Data Type of '$': {type('$')}")

print('\n----- Example 3: Variables ----- ')
# declare variable
num1 = 25
num2 = -12
username = "Peter Pan"
num_sum = num1 + num2
is_raining = True

# prompt results
print(f"{username}, the sum of {num1} and {num2} is: {num_sum}")
print(f"Is it raining today? {is_raining}")

print('\n----- Example 4: Assigning Values to Multiple Vars ----- ')
# declare multiple variables
item1, item2, item3 = "apples", 25, False
print(f"Item 1 = {item1}, Item 2 = {item2}, Item 3 = {item3}")

# declare multiple variables with the same value
score1 = score2 = score3 = 88
print(f"Score 1 = {score1}, Score 2 = {score2}, Score 3 = {score3}")

print('\n----- Example 5: Input Function ----- ')
username = input("Enter username: ")
print(f"Your username is: {username}")

lucky_number = input("Enter a lucky number: ")
print(f"Your lucky number is: {lucky_number}")

# double the lucky_number
# TODO: add the other examples

print('\n----- Example 14: Upper and Lower Method ----- ')
username = username.lower()
print(f"Lower: {username}")

username = username.upper()
print(f"Upper: {username}")

print('\n----- Example 15: Replace Method ----- ')
username = username.replace('P', '%')
print(f"Replaced 'P' with '%': {username}")

print('\n----- Example 16: Split Method ----- ')
message = "Introduction to Python Programming! Today we are learning string methods."
print(message)
print(message.split())

print('\n----- Example 17: Find Method ----- ')
# find the letter 'p'
index_of_p = message.find('P')
print(f"The index of letter 'P' is: {index_of_p}")

# find the second letter 'p'
second_p_index = message.find('P', index_of_p+1)
print(f"Next index of letter P is: {second_p_index}")

# find a non-existing letter 'Y'
index_of_y = message.find('Y')
print(f"The index of letter 'Y' is: {index_of_y}")

print('\n----- Example 18: in, not in Statement ----- ')
# check if the word 'we' is in the message string
is_we = 'we' in message
print(f"Is the word 'we' in 'message'? {is_we}")

is_not_today = 'Today' not in message
print(f"Is the word 'Today' not in 'message'? {is_not_today}")

"""
List
Lists are the same as array in other programming languages.
"""
print('\n----- Example 19: List ----- ')
colors = ["orange", "magenta", "olive"]
numbers = [6, 20, -9, 5, -12]
mixed = [True, "Cat", 13, "peter"]
empty_list = []

print(f"Colors List: {colors}")
print(f"Numbers List: {numbers}")
print(f"Mixed List: {mixed}")
print(f"Empty List: {empty_list}")

# list indexes
print(f"Second Color: {colors[1]}")
print(f"First Number: {numbers[0]}")
# print(f"Third Value: {empty_list[2]}") # will not work

# negative indexing (starting from the right of the list)
print(f"Last Color: {colors[-1]}")
print(f"Third Last Number: {numbers[-3]}")

print('\n----- Example 20: +, * Operator on Lists ----- ')
# concatenate the first color with the last color
new_color = colors[0] + colors[-1]
print(f"The new color is: {new_color}")

# concatenate the second color with the third number
# new_word = colors[1] + numbers[2] # data type error int and string

tripled_color = colors[0]*3
print(f"Tripled color with '*': {tripled_color}")

print('\n----- Example 21: in, not in Statement ----- ')
# remove last color
colors.pop()
print(f"Colors list popped: {colors}")

print('\n----- Example 22: Add items to the list ----- ')
# append item to the end of colors list
colors.append("PINK")
print(f"'PINK' appended to the colors list: {colors}")

print('\n----- Example 23: Sorting ----- ')
# sort list
print(f"Sorted colors list: {colors.sort()}")

print('\n----- Example 24: count Method ----- ')
bool_list = [True, True, False]
count_true = bool_list.count(True)
print(f"'True' count in the bool_list: {count_true}")

# count non-existing value
count_red = colors.count('red')
print(f"'red' count in colors list: {count_red}")

print('\n----- Example 25: Length of List ----- ')
length_colors = len(colors)
print(f"Length of colors list is: {length_colors}")

print('\n----- Example 26: index Method ----- ')
# index of color 'olive'
# index_olive = colors.index('olive') # ValueError
# print(f"Index of the color 'olive': {index_olive}") # ValueError