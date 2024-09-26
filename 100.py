import datetime
import time
import sys

# Function to simulate the "Calculating..." flashing effect
def calculating_effect():
    for _ in range(10):  # Run for 10 seconds
        for dots in range(1, 4):  # Add 1, 2, 3 dots repeatedly
            sys.stdout.write("\rCalculating" + "." * dots)  # Overwrite the previous line
            sys.stdout.flush()  # Ensure the output is updated immediately
            time.sleep(1)  # Wait for 1 second

# Get the current year
current_year = datetime.datetime.now().year

# Ask for user's name
name = input("What's your name? ")

# Simulate the delay with flashing effect
calculating_effect()

# Ask for user's age
age = int(input("\nHow old are you? "))  # '\n' to move to the next line after the effect

# Calculate the year the user will turn 100
years_to_100 = 100 - age
year_turn_100 = current_year + years_to_100

# Print a message
print(f"Hello {name}, you will turn 100 years old in the year {year_turn_100}.")
