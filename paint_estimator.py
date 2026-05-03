"""
Brock Nebeker
IS 303 - A01

Paint Estimator
This program estimates the gallons of paint needed to paint a room based on the wall's height and total width.

Inputs:
- Room name (string)
- Wall height in feet (int)
- Wall width in feet (int)

Processes:
- Get the number of gallons by multiplying the wall's height and the wall's total width then dividing it by 350 
- Store the number of gallons in a variable labeled gallons

Outputs:
- Print the room name and how many gallons are needed to paint the room
"""
# Inputs
room_name = input("Room Name: ")
wall_height = int(input("Wall Height in Feet: "))
wall_width = int(input("Total Wall Width in Feet: "))

# Processes
gallons = (wall_height * wall_width) / 350

# Outputs
print()
print(f"{room_name} needs {gallons:.2f} gallons of paint.")