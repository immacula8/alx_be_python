FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
# (Celsius * 9/5) + 32 = Fahrenheit
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
# The offset for Fahrenheit and Celsius conversion is the freezing point of water
FREEZING_POINT_OFFSET = 32

def convert_to_celsius(fahrenheit):
    """
    Converts a temperature from Fahrenheit to Celsius.

    Args:
        fahrenheit (float): The temperature in Fahrenheit.

    Returns:
        float: The temperature converted to Celsius.
    """
    # Use the global conversion factor and offset to perform the calculation
    celsius = (fahrenheit - FREEZING_POINT_OFFSET) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    """
    Converts a temperature from Celsius to Fahrenheit.

    Args:
        celsius (float): The temperature in Celsius.

    Returns:
        float: The temperature converted to Fahrenheit.
    """
    # Use the global conversion factor and offset to perform the calculation
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + FREEZING_POINT_OFFSET
    return fahrenheit

def main():
    """
    Main function to handle user interaction and temperature conversion.
    """
    try:
        # Prompt the user to enter a temperature
        temp_input = input("Enter the temperature to convert: ")
        
        # Validate that the temperature input is numeric
        try:
            temperature = float(temp_input)
        except ValueError:
            # Raise a custom error message if input is not a valid number
            raise ValueError("Invalid temperature. Please enter a numeric value.")

        # Prompt the user to specify the unit (C/F)
        unit_input = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        # Perform conversion based on user's unit input
        if unit_input == 'F':
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted_temp}°C")
        elif unit_input == 'C':
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted_temp}°F")
        else:
            # Handle invalid unit input
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

    except ValueError as e:
        # Catch and print the specific ValueError for invalid temperature
        print(f"Error: {e}")
    except Exception as e:
        # Catch any other unexpected errors
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Ensures that main() is called only when the script is executed directly
    main()