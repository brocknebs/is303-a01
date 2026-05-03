"""
Brock Nebeker
IS 303 - A01

BMI Calculator
This program is used to calculate the user's BMI based on their height and weight.

Inputs:
- Name (string)
- Height in inches (int)
- Weight in pounds (int)

Processes:
- Get BMI by dividing weight by height squared all times by 703
- Store BMI in a variable labeled bmi

Outputs:
- Print the name, height, weight, and BMI in a formatted message
"""
# Inputs
name = input("What is your name?: ")
height = int(input("What is your height in inches?: "))
weight = int(input("What is your weight in pounds?: "))

# Processes
bmi = (weight / (height * height)) * 703

# Outputs
print()
print(f"Name: {name}")
print(f"Height: {height} inches")
print(f"Weight: {weight} lbs")
print(f"BMI: {bmi:.2f}")