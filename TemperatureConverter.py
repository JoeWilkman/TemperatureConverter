# Temperature Converter
# Convert temperature from Celsius to Fahrenheit and vice versa

def celsius_to_fahrenheit(celsius):
    """Convert temperature from celsius to Fahrenheit"""
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    """Convert temperature from Fahrenheit to Celsius"""
    celsius = (fahrenheit -32) * 5/9
    return celsius


#Ask user for temperature input and choice of conversion
temperature = float(input("Please enter the temperature you would like converted: "))
conversion = input("Convert to (F)ahrenheit or (C)elsius?: ")

if conversion.lower() == "f":
    #Convert Celsius to Fahrenheit
    result = celsius_to_fahrenheit(temperature)
    print(f"{temperature}°C is equal to {result}°F.")
elif conversion.lower() == "c":
    #Convert Fahrenheit to Celsius
    result = fahrenheit_to_celsius(temperature)
    print(f"{temperature}°F is equal to {result}°C.")
else:
    #Invalid choice of conversion
    print("Invalid choice of conversion.")