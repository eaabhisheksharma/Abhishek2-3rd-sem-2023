# Input a list of numbers
numbers = [int(x) for x in input("Enter a list of numbers separated by spaces: ").split()]

# Input the number to insert
number_to_insert = int(input("Enter the number to insert: "))

# Input the position where you want to insert the number
position = int(input("Enter the position to insert the number: "))

# Check if the position is valid
if 0 <= position <= len(numbers):
    numbers.insert(position, number_to_insert)
    print(f"The number {number_to_insert} has been inserted at position {position}.")
    print("Updated list:", numbers)
else:
    print("Invalid position. Please enter a position within the range [0, length of the list].")
