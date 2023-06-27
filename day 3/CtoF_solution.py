"""
Celsius to Fahrenheit Temperature Converter

Write a program that converts Celsius temperatures to Fahrenheit temperatures. The formula is as follows:
  F = (9/5)C + 32
The program should ask the user to enter a temperature in Celsius, then display the temperature converted to Fahrenheit.
"""
num = 3
c = input("Enter degree in celsius: ")
c = float(c)
f = (9/5) * c + 32
print(f"Degree in fahrenheit is {f} degree")