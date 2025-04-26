"""
Miguel Castillo
Lab 10: Exercise
April 25, 2025
"""

colors = ['red', 'orange', 'olive', 'magenta', 'green']

while True:
  matches = False
  user_input = input('Enter a color: ').lower().strip()
  
  for color in colors:
    if user_input == color:
      print(f"Your color {user_input} was found!")
      matches = True
      break
  
  if matches:
    break