"""
Miguel Castillo
April 24, 2025
Lab 9 Exercise
"""
import math

print('******* Grade Average Calculator *******\n')

grade_1 = float(input('Enter grade 1: '))
grade_2 = float(input('Enter grade 2: '))

average = (grade_1 + grade_2) / 2
gpa = None

if 90 <= average <= 100:
  gpa = 'A'
elif 70 <= average <= 89.99:
  gpa = 'B'
elif 60 <= average <= 69.99:
  gpa = 'C'
elif 0 <= average <=59.99:
  gpa = 'FAIL!'
else:
  gpa = 'UNDEFINED!'

print(f"For the average of {average}, your GPA is {gpa}")