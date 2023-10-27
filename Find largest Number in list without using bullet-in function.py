# Input a list of numbers
numbers = [int(x) for x in input("Enter a list of numbers separated by spaces: ").split()]

# Initialize a variable to store the largest number
largest = None

# Iterate through the list to find the largest number
for num in numbers:
    if largest is None or num > largest:
        largest = num

if largest is not None:
    print("The largest number in the list is:", largest)
else:
    print("The list is empty.")
