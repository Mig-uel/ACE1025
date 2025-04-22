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
