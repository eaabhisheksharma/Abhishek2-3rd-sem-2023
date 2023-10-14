num = int(input("Enter a number:"))

if num % 5 == 0 and num % 7 == 0:
    print(f"{num}is a multiple of both 5 and 7.")
else:
    print (f"{num} is not a multiple of both 5 and 7.")