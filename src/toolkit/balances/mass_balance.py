from toolkit.balances.core_mass import single_stream_balance, multi_stream_balance, reaction_stoichiometry_balance, mass_fractions, mixture_mass_flow 
from toolkit.utils.input_validation import get_float, check_non_negative, check_positive
from toolkit.utils.formatting import format_label, format_result, format_section, success_message, error_message

def handler_name():
    # Inputs section
    print()
    format_section("Inputs")
    format_label(...)
    format_label(...)

    # Validation
    if not check_non_negative(...):
        error_message()
        return

    # Results section
    print()
    format_section("Results")
    format_result(...)
    success_message()

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
    m_in = get_float("Enter inlet mass flow rate (kg/s): ")
    print()

    format_section("Inputs")
    format_label("Inlet mass flow rate", m_in, "kg/s")
    
    if not check_non_negative(m_in, "Inlet mass flow rate" ):
        error_message()
        return
    
    result = single_stream_balance(m_in)
    print()
    format_section("Results")
    format_result("Single stream balance", result, "kg/s")
    success_message()

def handle_multi_stream_balance():
    print("\nEnter inlet mass flows rate (kg/s), separated by commas: ")
    in_values = input("Inlet streams: ").strip().split(",")
    in_streams = [float(x) for x in in_values]

    print("\nEnter outlet mass flows rate (kg/s), separated by commas: ")
    out_values = input("Outlet streams: ").strip().split(",")
    out_streams = [float(x) for x in out_values]
    print()

    format_section("Inputs")
    format_label("In streams' mass flow rate", in_streams, "")
    format_label("Out streams' mass flow rate", out_streams, "")

    result = multi_stream_balance(in_streams, out_streams)
    print()
    format_section("Results")
    format_result("Net mass balance", result, "kg/s")
    success_message()

def handle_reaction_stoichiometry_balance():
    print("\nEnter species involved, separated by commas: ")
    species = input("Species: ").strip().split(",")
    species_list = [s.strip() for s in species]

    print("\nEnter stoichiometric coefficients for each species, separated by commas: ")
    coeff_values = input("Coefficients: ").strip().split(",")
    coeff_list = [float(x) for x in coeff_values]

    if len(species_list) != len(coeff_list):
        error_message()
        return

    stoich_coeffs = dict(zip(species_list, coeff_list))
    reaction_rates = get_float("Enter reaction rate (mol/s): ")
    print()

    format_section("Inputs")
    format_label("Species", species_list, "")
    format_label("Coefficients", coeff_list, "")
    format_label("Reaction rate", reaction_rates, "mol/s")

    result = reaction_stoichiometry_balance(stoich_coeffs, reaction_rates)
    print()
    format_section("Results")
    print("Rate of consumption/production for each species (mol/s): ")
    for sp, rate in result.items():
        format_result(sp, rate, "mol/s")
    success_message()


def handle_component_mass_fractions():
    print("\nEnter species involved, separated by commas: ")
    species = input("Species: ").strip().split(",")
    species_list = [s.strip() for s in species]

    print("\nEnter masses for each species (kg/s), separated by commas: ")
    mass_values = input("Masses: ").strip().split(",")
    mass_list = [float(x) for x in mass_values]

    if len(species_list) != len(mass_list):
        error_message()
        return

    masses = dict(zip(species_list, mass_list))
    print()

    format_section("Inputs")
    format_label("Species", species_list, "")
    format_label("Mass fo each species", mass_list, "kg/s")

    result = mass_fractions(masses)
    format_section("Results")
    print("Mass fractions for each species: ")
    for sp, fraction in result.items():
        format_result(sp, fraction, "")
    success_message()

def handle_mixture_mass_flow_calculations():
    density = get_float("Enter mixture density (kg/m^3): ")
    volumetric_flow = get_float("Enter volumetric flow rate (m^3/s): ")
    print()

    format_section("Inputs")
    format_label("Mixture density", density, "kg/m^3")
    format_label("Volumetric flow rate", volumetric_flow, "m^3/s")

    if not check_positive(density, "Mixture density" ):
        error_message()
        return
    if not check_non_negative(volumetric_flow, "Volumetric flow rate" ):
        error_message()
        return

    result = mixture_mass_flow(density, volumetric_flow)
    print()
    format_section("Results")
    format_result("Mixture mass flow rate", result, "kg/s")
    success_message()
