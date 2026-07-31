from toolkit.balances.core_mass import (
    single_stream_balance,
    multi_stream_balance,
    reaction_stoichiometry_balance,
    mass_fractions,
    mixture_mass_flow,
)
from toolkit.utils.input_validation import get_float, check_non_negative, check_positive
from toolkit.utils.formatting import (
    format_label,
    format_result,
    format_section,
    success_message,
    error_message,
    clear_screen,
    invalid_choice,
    spacer,
    safe_run,
)


def handler_name() -> None:
    """Placeholder handler function.

    This function is a placeholder present in the original file. It prints an
    inputs section, performs a non-negative check on a value and prints a
    results section. The implementation here mirrors the original placeholder
    behavior (no real values are processed).
    """
    # Inputs section
    spacer(1)
    format_section("Inputs")
    format_label(...)
    format_label(...)

    # Validation
    if not check_non_negative(...):
        error_message()
        return

    # Results section
    spacer(1)
    format_section("Results")
    format_result(...)
    success_message()


def run_mass_balance_menu() -> None:
    """Display and process the mass balance menu.

    Repeatedly shows the mass balance menu options, prompts the user for a
    selection, and dispatches the chosen handler. The loop continues until the
    user chooses to return to the main menu.
    """
    while True:
        print_mass_balance_menu()
        choice = input("Enter your choice: ").strip().lower()
        if choice == "0" or choice == "back":
            print("Returning to Main Menu...")
            break
        elif choice == "1" or choice == "single-stream balance":
            safe_run(handle_single_stream_balance)
        elif choice == "2" or choice == "multi-stream balance":
            safe_run(handle_multi_stream_balance)
        elif choice == "3" or choice == "reaction stoichiometry balance":
            safe_run(handle_reaction_stoichiometry_balance)
        elif choice == "4" or choice == "component mass fractions":
            safe_run(handle_component_mass_fractions)
        elif choice == "5" or choice == "mixture mass flow calculations":
            safe_run(handle_mixture_mass_flow_calculations)
        else:
            invalid_choice()


def print_mass_balance_menu() -> None:
    """Print the mass balance menu options.

    Displays the available mass balance operations and the option to go back to
    the main menu.
    """
    print("\n=== Mass Balance ===")
    print("0. Back")
    print("1. Single-stream balance")
    print("2. Multi-stream balance")
    print("3. Reaction stoichiometry balance")
    print("4. Component mass fractions")
    print("5. Mixture mass flow calculations")
    spacer(1)


def handle_single_stream_balance() -> None:
    """Handle single-stream mass balance input, validation and output.

    Prompts the user for an inlet mass flow rate, validates it and prints the
    computed single stream balance result.
    """
    clear_screen()
    m_in = get_float("Enter inlet mass flow rate (kg/s): ")
    spacer(1)

    format_section("Inputs")
    format_label("Inlet mass flow rate", m_in, "kg/s")

    if not check_non_negative(m_in, "Inlet mass flow rate"):
        error_message()
        return
    try:
        result = single_stream_balance(m_in)
    except Exception as exc:
        print("\nAn error occurred during calculation:")
        print(f"→ {exc}")

    spacer(1)
    format_section("Results")
    format_result("Single stream balance", result, "kg/s")
    success_message()


def handle_multi_stream_balance() -> None:
    """Handle multi-stream mass balance input and output.

    Prompts the user for inlet and outlet stream mass flows and prints the
    net mass balance.
    """
    clear_screen()
    print("\nEnter inlet mass flows rate (kg/s), separated by commas: ")
    in_values = input("Inlet streams: ").strip().split(",")
    in_streams = [float(x) for x in in_values]

    print("\nEnter outlet mass flows rate (kg/s), separated by commas: ")
    out_values = input("Outlet streams: ").strip().split(",")
    out_streams = [float(x) for x in out_values]
    spacer(1)

    format_section("Inputs")
    format_label("In streams' mass flow rate", in_streams, "")
    format_label("Out streams' mass flow rate", out_streams, "")

    if not check_non_negative(in_streams, "Inlet mass flow rate"):
        error_message()
        return
    if not check_non_negative(out_streams, "Outlet mass flow rate"):
        error_message()
        return

    try:
        result = multi_stream_balance(in_streams, out_streams)
    except Exception as exc:
        print("\nAn error occurred during calculation:")
        print(f"→ {exc}")

    spacer(1)
    format_section("Results")
    format_result("Net mass balance", result, "kg/s")
    success_message()


def handle_reaction_stoichiometry_balance() -> None:
    """Handle reaction stoichiometry balance calculations.

    Prompts for species names and stoichiometric coefficients, reaction rate
    and prints the rate of consumption/production for each species.
    """
    clear_screen()
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
    spacer(1)

    format_section("Inputs")
    format_label("Species", species_list, "")
    format_label("Coefficients", coeff_list, "")
    format_label("Reaction rate", reaction_rates, "mol/s")
    try:
        result = reaction_stoichiometry_balance(stoich_coeffs, reaction_rates)
    except Exception as exc:
        print("\nAn error occurred during calculation:")
        print(f"→ {exc}")

    spacer(1)
    format_section("Results")
    print("Rate of consumption/production for each species (mol/s): ")
    for sp, rate in result.items():
        format_result(sp, rate, "mol/s")
    success_message()


def handle_component_mass_fractions() -> None:
    """Compute and display component mass fractions.

    Prompts for species and their masses, validates input lengths and prints
    mass fractions for each species.
    """
    clear_screen()
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
    spacer(1)

    format_section("Inputs")
    format_label("Species", species_list, "")
    format_label("Mass fo each species", mass_list, "kg/s")
    try:
        result = mass_fractions(masses)
    except Exception as exc:
        print("\nAn error occurred during calculation:")
        print(f"→ {exc}")

    format_section("Results")
    print("Mass fractions for each species: ")
    for sp, fraction in result.items():
        format_result(sp, fraction, "")
    success_message()


def handle_mixture_mass_flow_calculations() -> None:
    """Calculate mixture mass flow from density and volumetric flow.

    Prompts for mixture density and volumetric flow, validates them and
    prints the resulting mixture mass flow rate.
    """
    clear_screen()
    density = get_float("Enter mixture density (kg/m^3): ")
    volumetric_flow = get_float("Enter volumetric flow rate (m^3/s): ")
    spacer(1)

    format_section("Inputs")
    format_label("Mixture density", density, "kg/m^3")
    format_label("Volumetric flow rate", volumetric_flow, "m^3/s")

    if not check_positive(density, "Mixture density"):
        error_message()
        return
    if not check_non_negative(volumetric_flow, "Volumetric flow rate"):
        error_message()
        return
    try:
        result = mixture_mass_flow(density, volumetric_flow)
    except Exception as exc:
        print("\nAn error occurred during calculation:")
        print(f"→ {exc}")

    spacer(1)
    format_section("Results")
    format_result("Mixture mass flow rate", result, "kg/s")
    success_message()
