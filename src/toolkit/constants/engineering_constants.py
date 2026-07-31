from toolkit.utils.formatting import clear_screen, invalid_choice


def print_engineering_menu() -> None:
    """Print the engineering constants menu options.

    Assumptions:
    - Menu display is formatted for standard console output.
    - All constants are at standard conditions (STP).
    """
    print("\n=== Engineering Constants ===")
    print("0. Back")
    print("1. Atmospheric Pressure")
    print("2. Specific Heat Capacity")
    print("3. Density of Water")
    print("4. Density of Air")
    print()


def run_engineering_menu() -> None:
    """Run the interactive engineering constants menu loop."""
    while True:
        print_engineering_menu()
        choice = input("Enter your choice: ").strip().lower()
        if choice == "0" or choice == "back":
            print("Returning to Main Menu...")
            break
        elif choice == "1" or choice == "atmospheric pressure":
            handle_atmospheric_pressure()
        elif choice == "2" or choice == "specific heat capacity":
            handle_specific_heat_capacity()
        elif choice == "3" or choice == "density of water":
            handle_density_of_water()
        elif choice == "4" or choice == "density of air":
            handle_density_of_air()
        else:
            invalid_choice()


def handle_atmospheric_pressure() -> None:
    """Print the standard atmospheric pressure constant.

    Assumptions:
    - Standard atmospheric pressure at sea level (101,325 Pa).
    - Temperature = 15°C, relative humidity = 0%.

    References:
    - NIST Standard Reference Database: standard atmospheric pressure at sea level.
    """
    clear_screen()
    print("Atmospheric Pressure: 101,325 Pa")


def handle_specific_heat_capacity() -> None:
    """Print the specific heat capacity of water constant.

    Assumptions:
    - Value applies to liquid water at 25°C.
    - Pressure = 1 atm.

    References:
    - IAPWS / CRC Handbook of Chemistry and Physics: specific heat capacity of liquid water.
    """
    clear_screen()
    print("Specific Heat Capacity of Water: 4.184 J/g°C")


def handle_density_of_water() -> None:
    """Print the density of water constant.

    Assumptions:
    - Liquid water at 4°C (maximum density).
    - Pure water with no dissolved solids.
    - Pressure = 1 atm.

    References:
    - IUPAC / CRC Handbook of Chemistry and Physics: density of pure water at 4°C.
    """
    clear_screen()
    print("Density of Water: 1,000 kg/m³")


def handle_density_of_air() -> None:
    """Print the density of air constant.

    Assumptions:
    - Dry air at sea level conditions.
    - Temperature = 15°C, pressure = 101,325 Pa.
    - Standard air composition (78% N2, 21% O2, 1% Ar and others).

    References:
    - ICAO standard atmosphere: density of dry air at sea level.
    """
    clear_screen()
    print("Density of Air: 1.225 kg/m³")
