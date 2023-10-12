import math

#formula to find the area of the triangle 
def area_of_triangle(a, b, c):
    s = (a + b + c) / 2  # Calculate the semiperimeter
    area = math.sqrt(s * (s - a) * (s - b) * (s - c) )  # Heron's formula
    return area

# Input the lengths of the three sides
a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))
c = float(input("Enter the length of side c: "))

# Check if the input sides form a valid triangle
if a + b > c and a + c > b and b + c > a:
    triangle_area = area_of_triangle(a, b, c)
    print(f"The area of the triangle is {triangle_area:.2f} square units")
else:
    print("Invalid side lengths. They do not form a triangle.")