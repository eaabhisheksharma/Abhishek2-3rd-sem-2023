def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

N = int(input("Enter a value for N: "))

print(f"Prime numbers from 1 to {N}:")
for i in range(2, N + 1):
    if is_prime(i):
        print(i, end=" ")
