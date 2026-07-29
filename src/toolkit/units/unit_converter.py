from toolkit.units.conversion import Converter
from toolkit.utils.input_validation import get_float, check_non_negative, check_positive
from toolkit.utils.formatting import format_label, format_result, format_section, success_message, error_message

def handler_name():
    # Inputs section
    format_section("Inputs")
    format_label(...)
    format_label(...)

    # Validation
    if not check_non_negative(...):
        error_message()
        return

    # Results section
    format_section("Results")
    format_result(...)
    success_message()

def run_unit_menu():
    while True:
        print_unit_menu()
        choice = input("Enter your choice: ").strip()
        if choice == "0" or choice.lower() == "back":
            print("Returning to Main Menu...")
            break
        elif choice == "1" or choice.lower() == "length":
            handle_length()
        elif choice == "2" or choice.lower() == "mass":
            handle_mass()
        elif choice == "3" or choice.lower() == "temperature":
            handle_temperature()
        elif choice == "4" or choice.lower() == "volume":
            handle_volume()
        elif choice == "5" or choice.lower() == "pressure":
            handle_pressure()
        elif choice == "6" or choice.lower() == "energy":
            handle_energy()
        elif choice == "7" or choice.lower() == "power":
            handle_power()
        elif choice == "8" or choice.lower() == "time":
            handle_time()
        elif choice == "9" or choice.lower() == "speed":
            handle_speed()
        else:
            print("Invalid choice. Please try again.")

def print_unit_menu():
    print("\n=== Unit Converter Menu ===")
    print("Please select a unit conversion option:")
    print("0. Back to Main Menu")
    print("1. Length")
    print("2. Mass")
    print("3. Temperature")
    print("4. Volume")
    print("5. Pressure")
    print("6. Energy")
    print("7. Power")
    print("8. Time")
    print("9. Speed")
    print()

def handle_length():
    value = get_float("Enter the value to convert: ")
    from_unit = input("Enter the unit to convert from: ").strip()
    to_unit = input("Enter the unit to convert to: ").strip()
    print()

    format_section("Inputs")
    format_label("From unit", value, from_unit)
    
    converter = Converter()
    result = converter.convert(value, from_unit, to_unit)
    format_section("Results")
    format_result("Converted", result, to_unit)
    success_message()

def handle_mass():
    value = get_float("Enter the value to convert: ")
    from_unit = input("Enter the unit to convert from: ").strip()
    to_unit = input("Enter the unit to convert to: ").strip()
    print()

    format_section("Inputs")
    format_label("From unit", value, from_unit)

    if not check_non_negative(value, "Mass"):
        error_message()
        return
    
    converter = Converter()
    result = converter.convert(value, from_unit, to_unit)
    format_section("Results")
    format_result("Converted", result, to_unit)
    success_message()

def handle_temperature():
    value = get_float("Enter the value to convert: ")
    from_unit = input("Enter the unit to convert from: ").strip()
    to_unit = input("Enter the unit to convert to: ").strip()
    print()

    format_section("Inputs")
    format_label("From unit", value, from_unit)
    
    converter = Converter()
    result = converter.convert(value, from_unit, to_unit)
    format_section("Results")
    format_result("Converted", result, to_unit)
    success_message()

def handle_volume():
    value = get_float("Enter the value to convert: ")
    from_unit = input("Enter the unit to convert from: ").strip()
    to_unit = input("Enter the unit to convert to: ").strip()
    print()

    format_section("Inputs")
    format_label("From unit", value, from_unit)

    if not check_non_negative(value, "Volume"):
        error_message()
        return
    
    converter = Converter()
    result = converter.convert(value, from_unit, to_unit)
    format_section("Results")
    format_result("Converted", result, to_unit)
    success_message()

def handle_pressure():
    value = get_float("Enter the value to convert: ")
    from_unit = input("Enter the unit to convert from: ").strip()
    to_unit = input("Enter the unit to convert to: ").strip()
    print()

    format_section("Inputs")
    format_label("From unit", value, from_unit)

    if not check_non_negative(value, "Pressure"):
        error_message()
        return
    
    converter = Converter()
    result = converter.convert(value, from_unit, to_unit)
    format_section("Results")
    format_result("Converted", result, to_unit)
    success_message()

def handle_energy():
    value = get_float("Enter the value to convert: ")
    from_unit = input("Enter the unit to convert from: ").strip()
    to_unit = input("Enter the unit to convert to: ").strip()
    print()

    format_section("Inputs")
    format_label("From unit", value, from_unit)

    if not check_non_negative(value, "Energy"):
        error_message()
        return
    
    converter = Converter()
    result = converter.convert(value, from_unit, to_unit)
    format_section("Results")
    format_result("Converted", result, to_unit)
    success_message()

def handle_power():
    value = get_float("Enter the value to convert: ")
    from_unit = input("Enter the unit to convert from: ").strip()
    to_unit = input("Enter the unit to convert to: ").strip()
    print()

    format_section("Inputs")
    format_label("From unit", value, from_unit)

    if not check_non_negative(value, "Power"):
        error_message()
        return

    converter = Converter()
    result = converter.convert(value, from_unit, to_unit)
    format_section("Results")
    format_result("Converted", result, to_unit)
    success_message()

def handle_time():
    value = get_float("Enter the value to convert: ")
    from_unit = input("Enter the unit to convert from: ").strip()
    to_unit = input("Enter the unit to convert to: ").strip()
    print()

    format_section("Inputs")
    format_label("From unit", value, from_unit)

    if not check_non_negative(value, "Time"):
        error_message()
        return
    
    converter = Converter()
    result = converter.convert(value, from_unit, to_unit)
    format_section("Results")
    format_result("Converted", result, to_unit)
    success_message()

def handle_speed():
    value = get_float("Enter the value to convert: ")
    from_unit = input("Enter the unit to convert from: ").strip()
    to_unit = input("Enter the unit to convert to: ").strip()
    print()

    format_section("Inputs")
    format_label("From unit", value, from_unit)
    
    converter = Converter()
    result = converter.convert(value, from_unit, to_unit)
    format_section("Results")
    format_result("Converted", result, to_unit)
    success_message()
