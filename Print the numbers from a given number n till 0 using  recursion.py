def print_numbers(n):
    if n >= 0:
        print(n)
        print_numbers(n - 1)

# Input a number to start from
n = int(input("Enter a number: "))

# Call the function to print numbers from n to 0
print_numbers(n)
