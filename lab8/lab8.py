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