# Function to find the product of a set of real numbers
def product_of_numbers(numbers):
    result = 1  # Initialize the result to 1

    for num in numbers:
        result *= num  # Multiply the current number with the result

    return result

# Input a set of real numbers (as a list)
numbers = [float(x) for x in input("Enter a set of real numbers separated by spaces: ").split()]

# Check if the set is not empty
if numbers:
    product = product_of_numbers(numbers)
    print(f"The product of the numbers is: {product:.2f}")
else:
    print("No numbers provided. Please enter a set of real numbers.")
