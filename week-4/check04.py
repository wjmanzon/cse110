# a program to convert from Fahrenheit to Celsius

fahrenheit = float(input("What is  the temperature in Fahrenheit? "))

celcius = (fahrenheit - 32) * (5/9)

print(f"The temperature in Celsius is {celcius:.1f}")