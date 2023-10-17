import math

# Function to calculate the geometric mean
def geometric_mean(numbers):
    product = 1
    n = len(numbers)

    for num in numbers:
        product *= num

    geometric_mean = math.pow(product, 1/n)
    return geometric_mean

# Input the number of values and the values themselves
n = int(input("Enter the number of values: "))
values = []

for i in range(n):
    value = float(input(f"Enter value {i+1}: "))
    values.append(value)

# Calculate the geometric mean and display it
if n > 0:
    result = geometric_mean(values)
    print(f"The geometric mean is: {result:.2f}")
else:
    print("No values provided. Please enter at least one value.")
