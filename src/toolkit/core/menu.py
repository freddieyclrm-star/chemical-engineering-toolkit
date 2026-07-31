from toolkit.balances import mass_balance, energy_balance
from toolkit.constants import engineering_constants, scientific_constants
from toolkit.units import unit_converter
from toolkit.utils.formatting import invalid_choice, clear_screen, spacer, safe_run


def run_main_menu() -> None:
    """Run the main menu loop for the Chemical Engineering Toolkit.

    Displays the main menu, reads user input, and invokes the selected menu
    handler until the user chooses to exit.
    """
    while True:
        print_main_menu()
        choice = input("Enter your choice: ").strip().lower()
        if choice == "0" or choice == "exit":
            print("Exiting the program.")
            break
        elif choice == "1" or choice == "unit converter":
            safe_run(handle_unit_converter)
        elif choice == "2" or choice == "scientific constants":
            safe_run(handle_scientific_constants)
        elif choice == "3" or choice == "engineering constants":
            safe_run(handle_engineering_constants)
        elif choice == "4" or choice == "mass balance":
            safe_run(handle_mass_balance)
        elif choice == "5" or choice == "energy balance":
            safe_run(handle_energy_balance)
        else:
            invalid_choice()


def print_main_menu() -> None:
    """Print the main menu options to the console."""
    print("\n================================")
    print("Chemical Engineering Toolkit")
    print("Version 0.1.1")
    print("================================")
    print("Please select an option:")
    print("0. Exit")
    print("1. Unit Converter")
    print("2. Scientific Constants")
    print("3. Engineering Constants")
    print("4. Mass Balance")
    print("5. Energy Balance")
    spacer(1)


def handle_unit_converter() -> None:
    """Handle the unit converter menu selection."""
    clear_screen()
    unit_converter.run_unit_menu()


def handle_scientific_constants() -> None:
    """Handle the scientific constants menu selection."""
    clear_screen()
    scientific_constants.run_scientific_menu()


def handle_engineering_constants() -> None:
    """Handle the engineering constants menu selection."""
    clear_screen()
    engineering_constants.run_engineering_menu()


def handle_mass_balance() -> None:
    """Handle the mass balance menu selection."""
    clear_screen()
    mass_balance.run_mass_balance_menu()


def handle_energy_balance() -> None:
    """Handle the energy balance menu selection."""
    clear_screen()
    energy_balance.run_energy_balance_menu()
