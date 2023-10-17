# Function to reverse an integer
def reverse_integer(num):
    reversed_num = 0
    while num > 0:
        remainder = num % 10
        reversed_num = reversed_num * 10 + remainder
        num = num // 10
    return reversed_num

# Input an integer
num = int(input("Enter an integer: "))

# Reverse the integer and display it
reversed_num = reverse_integer(num)
print(f"The integer in reverse is: {reversed_num}")