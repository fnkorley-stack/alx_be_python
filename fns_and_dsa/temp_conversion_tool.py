# File: temp_conversion_tool.py
# Directory: fns_and_dsa
# Repo: alx_be_python

# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5


def convert_to_celsius(fahrenheit: float) -> float:
    """Convert Fahrenheit to Celsius using the global factor."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius: float) -> float:
    """Convert Celsius to Fahrenheit using the global factor."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


if __name__ == "__main__":
    # Ask for temperature input
    temp_input = input("Enter the temperature to convert: ").strip()

    # Validate numeric input
    try:
        temperature = float(temp_input)
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")
        exit(1)  # Stop the program safely

    # Ask for unit input
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if unit == "C":
        result = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {result}°F")
    elif unit == "F":
        result = convert_to_celsius(temperature)
        print(f"{temperature}°F is {result}°C")
    else:
        print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
