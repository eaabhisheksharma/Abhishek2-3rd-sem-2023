# Input a list of numbers
numbers = [int(x) for x in input("Enter a list of numbers separated by spaces: ").split()]

# Find and display the odd numbers in the list
odd_numbers = [num for num in numbers if num % 2 != 0]

if len(odd_numbers) > 0:
    print("The odd numbers in the list are:", odd_numbers)
else:
    print("No odd numbers found in the list.")
