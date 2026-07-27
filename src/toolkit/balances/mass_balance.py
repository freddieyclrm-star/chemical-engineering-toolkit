from toolkit.balances.core_mass import single_stream_balance, multi_stream_balance, reaction_stoichiometry_balance, mass_fractions, mixture_mass_flow 

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
    m_in = float(input("Enter inlet mass flow (kg/s): "))
    result = single_stream_balance(m_in)
    print(f"Outlet mass flow: {result} kg/s")

def handle_multi_stream_balance():
    print("\nEnter inlet mass flows (kg/s) separated by commas: ")
    in_values = input("Inlet streams: ").strip().split(",")
    in_streams = [float(x) for x in in_values]

    print("\nEnter outlet mass flows (kg/s) separated by commas: ")
    out_values = input("Outlet streams: ").strip().split(",")
    out_streams = [float(x) for x in out_values]

    result = multi_stream_balance(in_streams, out_streams)
    print(f"Net mass balance: {result} kg/s")

def handle_reaction_stoichiometry_balance():
    print("Reaction stoichiometry balance Coming Soon")

def handle_component_mass_fractions():
    print("Component mass fractions Coming Soon")

def handle_mixture_mass_flow_calculations():
    print("Mixture mass flow calculations Coming Soon")