def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Input N (the term you want to find)
N = int(input("Enter the term (N) in the Fibonacci series: "))

if N < 0:
    print("Invalid input. Please enter a non-negative integer.")
else:
    result = fibonacci(N)
    print(f"The {N}th term in the Fibonacci series is: {result}")
