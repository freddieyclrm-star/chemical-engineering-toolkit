def print_scientific_menu():
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

def run_scientific_menu():
    while True:
        print_scientific_menu()
        choice = input("Enter your choice: ").strip()
        if choice == "0" or choice.lower() == "back":
            break
        elif choice == "1" or choice.lower() == "speed of light":
            handle_speed_of_light()
        elif choice == "2" or choice.lower() == "planck constant":
            handle_planck_constant()
        elif choice == "3" or choice.lower() == "boltzmann constant":
            handle_boltzmann_constant()
        elif choice == "4" or choice.lower() == "newton's gravitational constant":
            handle_newtons_gravitational_constant()
        elif choice == "5" or choice.lower() == "stefan-boltzmann constant":
            handle_stefan_boltzmann_constant()
        elif choice == "6" or choice.lower() == "elementary charge":
            handle_elementary_charge()
        elif choice == "7" or choice.lower() == "mass of electron":
            handle_mass_of_electron()
        elif choice == "8" or choice.lower() == "mass of proton":
            handle_mass_of_proton()
        elif choice == "9" or choice.lower() == "mass of neutron":
            handle_mass_of_neutron()
        elif choice == "10" or choice.lower() == "avogadro's constant":
            handle_avogadros_constant()
        elif choice == "11" or choice.lower() == "molar gas constant":
            handle_molar_gas_constant()
        else:
            print("Invalid choice. Please try again.")

def handle_speed_of_light():
    print("Speed of Light: 299,792,458 m/s")

def handle_planck_constant():
    print("Planck Constant: 6.62607015 × 10^-34 J·s")

def handle_boltzmann_constant():
    print("Boltzmann Constant: 1.380649 × 10^-23 J/K")

def handle_newtons_gravitational_constant():
    print("Newton's Gravitational Constant: 6.6743015 × 10^-11 m^3/(kg·s^2)")

def handle_stefan_boltzmann_constant():
    print("Stefan-Boltzmann Constant: 5.670374419 × 10^-8 W/(m^2·K^4)")

def handle_elementary_charge():
    print("Elementary Charge: 1.602176634 × 10^-19 C")

def handle_mass_of_electron():
    print("Mass of Electron: 9.109383713928 × 10^-31 kg")

def handle_mass_of_proton():
    print("Mass of Proton: 1.6726219259552 × 10^-27 kg")

def handle_mass_of_neutron():
    print("Mass of Neutron: 1.6749275005685 × 10^-27 kg")

def handle_avogadros_constant():
    print("Avogadro's Constant: 6.02214076 × 10^23 mol^-1")

def handle_molar_gas_constant():
    print("Molar Gas Constant: 8.31446261815324 J/(mol·K)")