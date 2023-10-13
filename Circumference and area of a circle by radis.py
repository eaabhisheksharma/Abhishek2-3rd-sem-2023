import math

# Function to calculate the circumference of a circle
# Circumference {c} = 2*pi*radis 
def calculate_circumference(radius):
    circumference = 2 * math.pi * radius
    return circumference

# Function to calculate the area of a circle
# Area of a circle is Area (A) pi*radius^2
def calculate_area(radius):
    area = math.pi * radius**2
    return area

# Enter the radius of the circle
radius = float(input("Enter the radius of the circle: "))

# Calculate the circumference and area
circumference = calculate_circumference(radius)
area = calculate_area(radius)

print(f"The circumference of the circle is {circumference:.2f} units.")
print(f"The area of the circle is {area:.2f} square units.")
