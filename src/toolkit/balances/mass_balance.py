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
    m_in = float(input("Enter inlet mass flow rate (kg/s): "))
    result = single_stream_balance(m_in)
    print(f"Outlet mass flow rate: {result} kg/s")

def handle_multi_stream_balance():
    print("\nEnter inlet mass flows rate (kg/s), separated by commas: ")
    in_values = input("Inlet streams: ").strip().split(",")
    in_streams = [float(x) for x in in_values]

    print("\nEnter outlet mass flows rate (kg/s), separated by commas: ")
    out_values = input("Outlet streams: ").strip().split(",")
    out_streams = [float(x) for x in out_values]

    result = multi_stream_balance(in_streams, out_streams)
    print(f"Net mass balance: {result} kg/s")

def handle_reaction_stoichiometry_balance():
    print("\nEnter species involved, separated by commas: ")
    species = input("Species: ").strip().split(",")
    species_list = [s.strip() for s in species]

    print("\nEnter stoichiometric coefficients for each species, separated by commas: ")
    coeff_values = input("Coefficients: ").strip().split(",")
    coeff_list = [float(x) for x in coeff_values]

    if len(species_list) != len(coeff_list):
        print("Error: Number of species and coefficients must match.")
        return

    stoich_coeffs = dict(zip(species_list, coeff_list))
    reaction_rates = float(input("Enter reaction rate (mol/s): "))
    result = reaction_stoichiometry_balance(stoich_coeffs, reaction_rates)
    print("\nRate of consumption/production for each species (mol/s): ")
    for sp, rate in result.items():
        print(f"{sp}: {rate} mol/s")

def handle_component_mass_fractions():
    print("\nEnter species involved, separated by commas: ")
    species = input("Species: ").strip().split(",")
    species_list = [s.strip() for s in species]

    print("\nEnter masses for each species (kg/s), separated by commas: ")
    mass_values = input("Masses: ").strip().split(",")
    mass_list = [float(x) for x in mass_values]

    if len(species_list) != len(mass_list):
        print("Error: Number of species and masses must match.")
        return

    masses = dict(zip(species_list, mass_list))
    result = mass_fractions(masses)
    print("\nMass fractions for each species: ")
    for sp, fraction in result.items():
        print(f"{sp}: {fraction}")

def handle_mixture_mass_flow_calculations():
    density = float(input("Enter mixture density (kg/m^3): "))
    volumetric_flow = float(input("Enter volumetric flow rate (m^3/s): "))
    result = mixture_mass_flow(density, volumetric_flow)
    print(f"Mixture mass flow rate: {result} kg/s")