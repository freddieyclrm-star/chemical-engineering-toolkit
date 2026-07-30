def print_scientific_menu() -> None:
    """Print the scientific constants menu to stdout.

    This function displays the list of available scientific constants
    and their corresponding menu numbers. It does not return a value.
    """
    print("\n=== Scientific Constants ===")
    print("0. Back")
    print("1. Speed of Light")
    print("2. Planck Constant")
    print("3. Boltzmann Constant")
    print("4. Newton's Gravitational Constant")
    print("5. Stefan-Boltzmann Constant")
    print("6. Elementary Charge")
    print("7. Mass of Electron")
    print("8. Mass of Proton")
    print("9. Mass of Neutron")
    print("10. Avogadro's Constant")
    print("11. Molar Gas Constant")
    print()


def run_scientific_menu() -> None:
    """Run the interactive scientific constants menu loop.

    Continues to prompt the user for choices until they select '0' or
    type 'back'. Calls the appropriate handler for each selection.
    """
    while True:
        print_scientific_menu()
        choice = input("Enter your choice: ").strip().lower()
        if choice == "0" or choice == "back":
            print("Returning to Main Menu...")
            break
        elif choice == "1" or choice == "speed of light":
            handle_speed_of_light()
        elif choice == "2" or choice == "planck constant":
            handle_planck_constant()
        elif choice == "3" or choice == "boltzmann constant":
            handle_boltzmann_constant()
        elif choice == "4" or choice == "newton's gravitational constant":
            handle_newtons_gravitational_constant()
        elif choice == "5" or choice == "stefan-boltzmann constant":
            handle_stefan_boltzmann_constant()
        elif choice == "6" or choice == "elementary charge":
            handle_elementary_charge()
        elif choice == "7" or choice == "mass of electron":
            handle_mass_of_electron()
        elif choice == "8" or choice == "mass of proton":
            handle_mass_of_proton()
        elif choice == "9" or choice == "mass of neutron":
            handle_mass_of_neutron()
        elif choice == "10" or choice == "avogadro's constant":
            handle_avogadros_constant()
        elif choice == "11" or choice == "molar gas constant":
            handle_molar_gas_constant()
        else:
            print("Invalid choice. Please try again.")


def handle_speed_of_light() -> None:
    """Display the value of the speed of light (m/s)."""
    print("Speed of Light: 299,792,458 m/s")


def handle_planck_constant() -> None:
    """Display the value of Planck's constant (J·s)."""
    print("Planck Constant: 6.62607015 × 10^-34 J·s")


def handle_boltzmann_constant() -> None:
    """Display the value of the Boltzmann constant (J/K)."""
    print("Boltzmann Constant: 1.380649 × 10^-23 J/K")


def handle_newtons_gravitational_constant() -> None:
    """Display Newton's gravitational constant (m^3/(kg·s^2))."""
    print("Newton's Gravitational Constant: 6.6743015 × 10^-11 m^3/(kg·s^2)")


def handle_stefan_boltzmann_constant() -> None:
    """Display the Stefan-Boltzmann constant (W/(m^2·K^4))."""
    print("Stefan-Boltzmann Constant: 5.670374419 × 10^-8 W/(m^2·K^4)")


def handle_elementary_charge() -> None:
    """Display the elementary charge (C)."""
    print("Elementary Charge: 1.602176634 × 10^-19 C")


def handle_mass_of_electron() -> None:
    """Display the mass of an electron (kg)."""
    print("Mass of Electron: 9.109383713928 × 10^-31 kg")


def handle_mass_of_proton() -> None:
    """Display the mass of a proton (kg)."""
    print("Mass of Proton: 1.6726219259552 × 10^-27 kg")


def handle_mass_of_neutron() -> None:
    """Display the mass of a neutron (kg)."""
    print("Mass of Neutron: 1.6749275005685 × 10^-27 kg")


def handle_avogadros_constant() -> None:
    """Display Avogadro's constant (mol^-1)."""
    print("Avogadro's Constant: 6.02214076 × 10^23 mol^-1")


def handle_molar_gas_constant() -> None:
    """Display the molar gas constant R (J/(mol·K))."""
    print("Molar Gas Constant: 8.31446261815324 J/(mol·K)")
