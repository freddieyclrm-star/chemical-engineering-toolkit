from toolkit.balances import mass_balance, energy_balance
from toolkit.constants import engineering_constants, scientific_constants
from toolkit.units import unit_converter
def run_main_menu():
    while True:
        print_main_menu()
        choice = input("Enter your choice: ").strip().lower()
        if choice == "0" or choice == "exit":
            print("Exiting the program.")
            break
        elif choice == "1" or choice == "unit converter":
            handle_unit_converter()
        elif choice == "2" or choice == "scientific constants":
            handle_scientific_constants()
        elif choice == "3" or choice == "engineering constants":
            handle_engineering_constants()
        elif choice == "4" or choice == "mass balance":
            handle_mass_balance()
        elif choice == "5" or choice == "energy balance":
            handle_energy_balance()
        else:
            print("Invalid choice. Please try again.")


def print_main_menu():
        print("\n================================")
        print("Chemical Engineering Toolkit")
        print("Version 0.1.0")
        print("================================")
        print("Please select an option:")
        print("0. Exit")
        print("1. Unit Converter")
        print("2. Scientific Constants")
        print("3. Engineering Constants")
        print("4. Mass Balance")
        print("5. Energy Balance")
        print()
        

def handle_unit_converter():
    unit_converter.run_unit_menu()

def handle_scientific_constants():
    scientific_constants.run_scientific_menu()

def handle_engineering_constants():
    engineering_constants.run_engineering_menu()

def handle_mass_balance():
    mass_balance.run_mass_balance_menu()

def handle_energy_balance():
    energy_balance.run_energy_balance_menu()