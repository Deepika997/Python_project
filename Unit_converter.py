def convert_length(value, from_unit, to_unit):
    length_units = {
        "meters": 1,
        "kilometers": 0.001,
        "centimeters": 100,
        "millimeters": 1000,
        "miles": 0.000621371,
        "yards": 1.09361,
        "feet": 3.28084,
        "inches": 39.3701
    }
    
    if from_unit in length_units and to_unit in length_units:
        converted_value = value * (length_units[to_unit] / length_units[from_unit])
        return converted_value
    else:
        return None

def convert_weight(value, from_unit, to_unit):
    weight_units = {
        "kilograms": 1,
        "grams": 1000,
        "milligrams": 1000000,
        "pounds": 2.20462,
        "ounces": 35.274
    }
    
    if from_unit in weight_units and to_unit in weight_units:
        converted_value = value * (weight_units[to_unit] / weight_units[from_unit])
        return converted_value
    else:
        return None

def convert_temperature(value, from_unit, to_unit):
    if from_unit == "celsius":
        if to_unit == "fahrenheit":
            return (value * 9/5) + 32
        elif to_unit == "kelvin":
            return value + 273.15
    elif from_unit == "fahrenheit":
        if to_unit == "celsius":
            return (value - 32) * 5/9
        elif to_unit == "kelvin":
            return (value - 32) * 5/9 + 273.15
    elif from_unit == "kelvin":
        if to_unit == "celsius":
            return value - 273.15
        elif to_unit == "fahrenheit":
            return (value - 273.15) * 9/5 + 32
    
    return None

def main():
    while True:
        print("\nUnit Converter")
        print("1. Convert Length")
        print("2. Convert Weight")
        print("3. Convert Temperature")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            value = float(input("Enter the value: "))
            from_unit = input("Enter the from unit (meters, kilometers, centimeters, millimeters, miles, yards, feet, inches): ").lower()
            to_unit = input("Enter the to unit (meters, kilometers, centimeters, millimeters, miles, yards, feet, inches): ").lower()
            result = convert_length(value, from_unit, to_unit)
            if result is not None:
                print(f"{value} {from_unit} is equal to {result} {to_unit}.")
            else:
                print("Invalid units entered.")
        
        elif choice == '2':
            value = float(input("Enter the value: "))
            from_unit = input("Enter the from unit (kilograms, grams, milligrams, pounds, ounces): ").lower()
            to_unit = input("Enter the to unit (kilograms, grams, milligrams, pounds, ounces): ").lower()
            result = convert_weight(value, from_unit, to_unit)
            if result is not None:
                print(f"{value} {from_unit} is equal to {result} {to_unit}.")
            else:
                print("Invalid units entered.")
        
        elif choice == '3':
            value = float(input("Enter the value: "))
            from_unit = input("Enter the from unit (celsius, fahrenheit, kelvin): ").lower()
            to_unit = input("Enter the to unit (celsius, fahrenheit, kelvin): ").lower()
            result = convert_temperature(value, from_unit, to_unit)
            if result is not None:
                print(f"{value} {from_unit} is equal to {result} {to_unit}.")
            else:
                print("Invalid units entered.")
        
        elif choice == '4':
            print("Exiting the converter. Goodbye!")
            break
        
        else:
            print("Invalid choice, please select again.")

if __name__ == "__main__":
    main()
