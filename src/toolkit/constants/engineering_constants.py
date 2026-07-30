def print_engineering_menu() -> None:
    """Print the engineering constants menu options."""
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
            print("Invalid choice. Please try again.")


def handle_atmospheric_pressure() -> None:
    """Print the standard atmospheric pressure constant."""
    print("Atmospheric Pressure: 101,325 Pa")


def handle_specific_heat_capacity() -> None:
    """Print the specific heat capacity of water constant."""
    print("Specific Heat Capacity of Water: 4.184 J/g°C")


def handle_density_of_water() -> None:
    """Print the density of water constant."""
    print("Density of Water: 1,000 kg/m³")


def handle_density_of_air() -> None:
    """Print the density of air constant."""
    print("Density of Air: 1.225 kg/m³")
