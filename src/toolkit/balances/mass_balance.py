def run_mass_balance_menu():
    while True:
        print_mass_balance_menu()
        choice = input("Enter your choice: ").strip().lower()
        if choice == "0" or choice == "back":
            print("Returning to Main Menu...")
            break
        elif choice == "1" or choice == "single-stream balance":
            handle_single_stream_balance()
        elif choice == "2" or choice == "multi-stream balance":
            handle_multi_stream_balance()
        elif choice == "3" or choice == "reaction stoichiometry balance":
            handle_reaction_stoichiometry_balance()
        elif choice == "4" or choice == "component mass fractions":
            handle_component_mass_fractions()
        elif choice == "5" or choice == "mixture mass flow calculations":
            handle_mixture_mass_flow_calculations()
        else:
            print("Invalid choice. Please try again.")

def print_mass_balance_menu():
        print("\n=== Mass Balance ===")
        print("0. Back")
        print("1. Single-stream balance")
        print("2. Multi-stream balance")
        print("3. Reaction stoichiometry balance")
        print("4. Component mass fractions")
        print("5. Mixture mass flow calculations")
        print()

def handle_single_stream_balance():
    print("Single-stream balance Coming Soon")

def handle_multi_stream_balance():
    print("Multi-stream balance Coming Soon")

def handle_reaction_stoichiometry_balance():
    print("Reaction stoichiometry balance Coming Soon")

def handle_component_mass_fractions():
    print("Component mass fractions Coming Soon")

def handle_mixture_mass_flow_calculations():
    print("Mixture mass flow calculations Coming Soon")