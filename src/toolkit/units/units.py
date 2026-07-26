from toolkit.units.conversion import *

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
    print("\n Please select a unit conversion option:")
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
    print("Length Conversion Coming Soon")

def handle_mass():
    print("Mass Conversion Coming Soon")

def handle_temperature():
    print("Temperature Conversion Coming Soon")

def handle_volume():
    print("Volume Conversion Coming Soon")

def handle_pressure():
    print("Pressure Conversion Coming Soon")

def handle_energy():
    print("Energy Conversion Coming Soon")

def handle_power():
    print("Power Conversion Coming Soon")

def handle_time():
    print("Time Conversion Coming Soon")

def handle_speed():
    print("Speed Conversion Coming Soon")

