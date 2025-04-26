"""
Miguel Castillo
Lab 10: Exercise
April 25, 2025
"""

colors = ['red', 'orange', 'olive', 'magenta', 'green']

user_input = input('Enter a color: ').lower().strip()
isFound = False

for color in colors:
    if user_input == color:
      isFound = True
      print(f"{user_input} is in the list")
      break

if not(isFound):
  print(f"{user_input} IS NOT in the list")