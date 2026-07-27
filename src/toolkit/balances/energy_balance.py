from toolkit.balances.core_energy import sensible_heat, latent_heat, reaction_enthalpy, cp_constant, heat_exchanger_energy_balance, two_stream_heat_exchanger_balance
from toolkit.utils.input_validation import check_non_negative
def get_Float(x):
    while True:
        try:
            user_input = float(input(x))
            return user_input
        except ValueError:
            print("Number expected, try again")


def run_energy_balance_menu():
    while True:
        print_energy_balance_menu()
        choice = input("Enter your choice: ").strip().lower()
        if choice == "0" or choice == "back":
            print("Returning to Main Menu...")
            break
        elif choice == "1" or choice == "sensible heat calculation":
            handle_sensible_heat()
        elif choice == "2" or choice == "latent heat calculation":
            handle_latent_heat()
        elif choice == "3" or choice == "reaction enthalpy":
            handle_reaction_enthalpy()
        elif choice == "4" or choice == "heat capacity (cp) calculations":
            handle_heat_capacity()
        elif choice == "5" or choice == "heat exchanger energy balance":
            handle_heat_exchanger_energy_balance()
        elif choice == "6" or choice == "two streams heat exchanger balance":
            handle_two_stream_heat_exchanger_balance()
        else:
            print("Invalid choice. Please try again.")

def print_energy_balance_menu():
    print("\n=== Energy Balance ===")
    print("0. Back")
    print("1. Sensible Heat Calculation")
    print("2. Latent Heat Calculation")
    print("3. Reaction Enthalpy")
    print("4. Heat Capacity (Cp) Calculations")
    print("5. Heat Exchanger Energy Balance")
    print("6. Two Streams Heat Exchanger Balance")
    print()

def handle_sensible_heat():
    print("\n=== Sensible Heat Calculation ===")
    mass_flow = get_Float("Enter mass flow rate (kg/s): ")
    cp = get_Float("Enter specific heat capacity (J/kg•K): ")
    t_in = get_Float("Enter inlet temperature (°C): ")
    t_out = get_Float("Enter outlet temperature (°C): ")

    if mass_flow <= 0:
        print("Mass flow rate must be positive")
        return

    if cp <= 0:
        print("specific heat capacity must be positive")
        return

    result = sensible_heat(mass_flow, cp, t_in, t_out)
    print(f"\nSensible heat duty: {result} W")

def handle_latent_heat():
    print("\n=== Latent Heat Calculation ===")
    mass_flow = get_Float("Enter mass flow rate (kg/s): ")
    latent_heat_value = get_Float("Enter latent heat value (J/kg): ")

    if mass_flow <= 0:
        print("Mass flow rate must be positive")
        return
    if latent_heat_value <= 0:
        print("Latent heat value must be positive")
        return
    result = latent_heat(mass_flow, latent_heat_value)
    print(f"\nLatent Heat Duty: {result} W")

def handle_reaction_enthalpy():
    print("\n=== Reaction Enthalpy Calculation ===")
    reaction_rate = get_Float("Enter reaction rate (mol/s): ")
    delta_h_reaction = get_Float("Enter reaction enthalpy ΔH (J/mol): ")

    result = reaction_enthalpy(reaction_rate, delta_h_reaction)
    print(f"\nReaction Enthalpy Duty: {result} W")

def handle_heat_capacity():
    print("\n=== Heat Capacity (Cp) Calculations ===")
    print("1. Constant Cp")
    print("2. Polynomial Cp (Coming Soon)")

    choice = input("Choose Cp model (1 or 2): ").strip()

    if choice == "1":
        cp_value = get_Float("Enter constant Cp value (J/kg·K): ")

        if cp_value <= 0:
            print("Specific heat capacity must be positive")
            return
        result = cp_constant(cp_value)
        print(f"\nCp: {result}")
    elif choice == "2":
        print("\nPolynomial Cp model COMING SOON.")
    else:
        print("Invalid choice.")
        return

def handle_heat_exchanger_energy_balance():
    print("\n=== Heat Exchanger Energy Balance ===")
    print("Calculate heat duty using one stream (hot or cold).")

    mass_flow = get_Float("Enter mass flow rate (kg/s): ")
    cp = get_Float("Enter specific heat capacity Cp (J/kg·K): ")
    t_in = get_Float("Enter inlet temperature (°C): ")
    t_out = get_Float("Enter outlet temperature (°C): ")

    if mass_flow <= 0:
        print("Mass flow rate must be positive")
        return
    if cp <= 0:
        print("specific heat capacity must be positive")
        return
    result = heat_exchanger_energy_balance(mass_flow, cp, t_in, t_out)

    print(f"\nHeat Exchanger Duty: {result} W")
    print("Note: Positive = heating, Negative = cooling.")

def handle_two_stream_heat_exchanger_balance():
    print("\n=== Two-Stream Heat Exchanger Energy Balance ===")

    print("\n--- Hot Stream ---")
    m_hot = get_Float("Enter hot stream mass flow rate (kg/s): ")
    cp_hot = get_Float("Enter hot stream Cp (J/kg·K): ")
    t_hot_in = get_Float("Enter hot stream inlet temperature (°C): ")
    t_hot_out = get_Float("Enter hot stream outlet temperature (°C): ")

    print("\n--- Cold Stream ---")
    m_cold = get_Float("Enter cold stream mass flow rate (kg/s): ")
    cp_cold = get_Float("Enter cold stream Cp (J/kg·K): ")
    t_cold_in = get_Float("Enter cold stream inlet temperature (°C): ")
    t_cold_out = get_Float("Enter cold stream outlet temperature (°C): ")

    if m_hot <= 0 or m_cold <= 0:
        print("Mass flow rate must be positive")
        return
    if cp_hot <= 0 or cp_cold <= 0:
        print("specific heat capacity must be positive")
        return
    if t_hot_in < t_hot_out:
        print("Hot stream should cool down")
        return
    if t_cold_in > t_cold_out:
        print("Cold stream sould heat up")
        return
    q_hot, q_cold, imbalance = two_stream_heat_exchanger_balance(m_hot, cp_hot, t_hot_in, t_hot_out, m_cold, cp_cold, t_cold_in, t_cold_out)
    print("\n--- Results ---")
    print(f"Hot-side duty:  {q_hot} W")
    print(f"Cold-side duty: {q_cold} W")
    print(f"Energy balance (Q_hot + Q_cold): {imbalance} W")

    if abs(imbalance) < 1e-6:
        print("\nEnergy is balanced.")
    else:
        print("\nEnergy balance is NOT balanced.") 
