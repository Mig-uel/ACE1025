"""
Miguel Castillo
Lab 11: Dictionary, Functions, Classes
April 27, 2025
"""

print("----- Example 1: Python Dictionary")

# create a dictionary
car = {"brand": "Ford", "model": "Mustang", "year": 1964}

# print a complete dictionary
print(car)

# access items in a dictionary we use ["KEY_NAME"]
print(f"The year of the car is: {car['year']}")

# update the value of the key
car["year"] = 1980
print(f"The year of the car was updated to: {car['year']}")

# add key:value pair
car["color"] = "red"
print(car)

print("\n----- Example 2: Loop Through Each Key in Dict.")
for key in car:
    print(key)

print("\n----- Example 3: Loop Through Each Value in Dict.")
for key in car:
    print(car[key])

print("\n----- Example 4: Loop Through Each Pair in Dict.")
for key in car:
    print(f"{key}: {car[key]}")

print("\n----- Example 5: Check If Key is Present in Dict.")
check = "owner" in car
print(f"The key 'owner' is in car?: {check}")

print("\n----- Example 6: Python Dictionary Application")

# given the following list, create a dict. that will count
# the number of times that a word appears in the string
# the dict. will organize the words as the keys, and the number
# of occurrence of the word as the value of the key

phrase = "to be or not to be"
phrase_split = phrase.strip().split()
phrase_map = {}

for word in phrase_split:
    if word in phrase_map:
        phrase_map[word] += 1
    else:
        phrase_map[word] = 1

print("Results of the Phrase Dictionary:")
for key in phrase_map:
    print(f"'{key}' appears {phrase_map[key]} times")

print("\n----- Example 7: Function (no returning values)")


# defining a function
def greeting():
    print("Welcome to Functions!")


# run function 'greeting'
greeting()
