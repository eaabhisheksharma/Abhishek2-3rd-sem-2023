num = int(input("Enter an integer: "))

digit_sum = 0

while num > 0:
    digit = num % 10  
    digit_sum += digit 
    num = num // 10  

print(f"The sum of the digits is: {digit_sum}")
