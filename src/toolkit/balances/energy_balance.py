def run_energy_balance_menu():
    while True:
        print_energy_balance_menu()
        choice = input("Enter your choice: ").strip().lower()
        if choice == "0" or choice == "back":
            print("Returning to Main Menu...")
            break
        elif choice == "1" or choice == "sensible heat calculation":
            handle_sensible_heat_calculation()
        elif choice == "2" or choice == "latent heat calculation":
            handle_latent_heat_calculation()
        elif choice == "3" or choice == "reaction enthalpy":
            handle_reaction_enthalpy()
        elif choice == "4" or choice == "heat capacity (cp) calculations":
            handle_heat_capacity_calculations()
        elif choice == "5" or choice == "heat exchanger energy balance":
            handle_heat_exchanger_energy_balance()
        else:
            print("Invalid choice. Please try again.")

def print_energy_balance_menu():
    print("\n=== Energy Balance ===")
    print("0. Back")
    print("1. Sensible Heat Calculation")
    print("2. Latent Heat Calculation")
    print("3. Reaction Enthalpy")
    print("4. Heat Capacity (Cp) Calculations")
    print("5. Heat Exchanger Energy Balance")
    print()

def handle_sensible_heat_calculation():
    print("Sensible Heat Calculation Coming Soon")

def handle_latent_heat_calculation():
    print("Latent Heat Calculation Coming Soon")

def handle_reaction_enthalpy():
    print("Reaction Enthalpy Coming Soon")

def handle_heat_capacity_calculations():
    print("Heat Capacity (Cp) Calculations Coming Soon")

def handle_heat_exchanger_energy_balance():
    print("Heat Exchanger Energy Balance Coming Soon")