def run_main_menu():
    while True:
        print_main_menu()
        choice = input("Enter your choice: ").strip()
        if choice == "0" or choice.lower() == "exit":
            break
        elif choice == "1" or choice.lower() == "unit converter":
            handle_unit_converter()
        elif choice == "2" or choice.lower() == "scientific constants":
            handle_scientific_constants()
        elif choice == "3" or choice.lower() == "engineering constants":
            handle_engineering_constants()
        elif choice == "4" or choice.lower() == "mass balance":
            handle_mass_balance()
        elif choice == "5" or choice.lower() == "energy balance":
            handle_energy_balance()
        else:
            print("Invalid choice. Please try again.")


def print_main_menu():
        print("\nPlease select an option:")
        print("0. Exit")
        print("1. Unit Converter")
        print("2. Scientific Constants")
        print("3. Engineering Constants")
        print("4. Mass Balance")
        print("5. Energy Balance")
        

def handle_unit_converter():
    print("Unit Converter Coming Soon")

def handle_scientific_constants():
    print("Scientific Constants Coming Soon")

def handle_engineering_constants():
    print("Engineering Constants Coming Soon")

def handle_mass_balance():
    print("Mass Balance Coming Soon")

def handle_energy_balance():
    print("Energy Balance Coming Soon")