def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius *9/5) + 32
    return fahrenheit
celsius = float(input("Enter temperature in degree Celsius:"))
fahrenheit = celsius_to_fahrenheit(celsius)
print(f"{celsius} degree celsius in equal to {fahrenheit} degree Fahrenheit.")