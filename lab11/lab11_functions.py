"""
Miguel Castillo
Lab 11: Functions
April 27, 2025
"""

# import 'math' module
import math

print("----- Function 1 (no args or return) -----")


# defining a function
def greeting():
    print("Welcome to Functions!")


print("\n----- Function 2 (args) -----")


def print_username(username: str):
    print(f"Welcome to Functions, {username}!")


print("\n----- Function 3 (default args) -----")


def user_country(username="John Doe", country="Unknown"):
    print(f"{username} is living in {country}")


print("\n----- Function 4 (args and return value) -----")


def product(n1: int, n2: int):
    return n1 * n2


print("\n----- Function 5 (boolean function) -----")


def multiple3(n=0):
    if n % 3 == 0 and not (n == 0):
        return True
    else:
        return False


print("\n----- Function 6 (function composition) -----")


# define a function to collect, validate, and return a number between 1 and 9
def collect_number():
    n = float(input("Enter a number between 1 and 9 (inclusive): "))

    while not (n >= 1) or not (n <= 9):
        n = float(input("(Try again) Enter a number between 1 and 9 (inclusive): "))
    return n


# define a function to sum all numbers up to a specific range and returns the sum of those numbers
def sum_numbers(amount: int = 0):
    sum = 0
    for i in range(amount):
        sum += collect_number()
    return sum


# define a function to print results
def print_results(totalSum):
    print(f"Sum of all numbers is: {totalSum}")


# define a function to calculate and return the area of a circle
def area_circle(r: float):
    area = math.pow(r, 2) * math.pi
    return round(area, 2)


# function to print area result
def print_area(area, radius=0):
    print(f"The area of a circle with radius of {radius} is: {area}")


# function to return the ratio of two numbers (hours)
def hour_ratio(hour: int):
    hours_in_day = 24
    try:
        return hours_in_day / hour
    except ZeroDivisionError:
        print("---- ZERO DIVISION ERROR ----")
        print("There was an error in the division.")
        return 0
    except (TypeError, ValueError):
        print("---- TYPE AND VALUE ERROR ----")
        print("Number was not provided.")
        return 0
    finally:
        print("Process completed")
