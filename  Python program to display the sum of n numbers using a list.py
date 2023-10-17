# Input the number of values (n)
n = int(input("Enter the number of values: "))

# An empty list to store the numbers
numbers = []

# Input 'n' numbers and store them in the list
for i in range(n):
    value = float(input(f"Enter value {i + 1}: "))
    numbers.append(value)

# Calculate the sum of the numbers using the sum() function
total = sum(numbers)

# Display the sum
print(f"The sum of the {n} numbers is: {total}")
