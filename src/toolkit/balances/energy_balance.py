from toolkit.balances.core_energy import sensible_heat, latent_heat, reaction_enthalpy, cp_constant, heat_exchanger_energy_balance, two_stream_heat_exchanger_balance

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
    mass_flow = float(input("Enter mass flow rate (kg/h): "))
    cp = float(input("Enter specific heat capacity (J/kg•K)"))
    t_in = float(input("Enter inlet temperature (C or K)"))
    t_out = float(input("Enter out;et temperature (C or K)"))

    result = sensible_heat(mass_flow, cp, t_in, t_out)
    print(f"\nSensible heat duty: {result} W")

def handle_latent_heat():
    print("\n=== Latent Heat Calculation ===")
    mass_flow = float(input("Enter mass flow rate (kg/h): "))
    latent_heat_value = float(input("Enter latent heat value (J/kg): "))

    result = latent_heat(mass_flow, latent_heat_value)
    print(f"\nLatent Heat Duty: {result} W")

def handle_reaction_enthalpy():
    print("\n=== Reaction Enthalpy Calculation ===")
    reaction_rate = float(input("Enter reaction rate (mol/h): "))
    delta_h_reaction = float(input("Enter reaction enthalpy ΔH (J/mol): "))

    result = reaction_enthalpy(reaction_rate, delta_h_reaction)
    print(f"\nReaction Enthalpy Duty: {result} W")

def handle_heat_capacity():
    print("\n=== Heat Capacity (Cp) Calculations ===")
    print("1. Constant Cp")
    print("2. Polynomial Cp (Coming Soon)")

    choice = input("Choose Cp model (1 or 2): ").strip()

    if choice == "1":
        cp_value = float(input("Enter constant Cp value (J/kg·K): "))
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

    mass_flow = float(input("Enter mass flow rate (kg/h): "))
    cp = float(input("Enter specific heat capacity Cp (J/kg·K): "))
    t_in = float(input("Enter inlet temperature (°C or K): "))
    t_out = float(input("Enter outlet temperature (°C or K): "))

    result = heat_exchanger_energy_balance(mass_flow, cp, t_in, t_out)

    print(f"\nHeat Exchanger Duty: {result} W")
    print("Note: Positive = heating, Negative = cooling.")

def handle_two_stream_heat_exchanger_balance():
    print("\n=== Two-Stream Heat Exchanger Energy Balance ===")

    print("\n--- Hot Stream ---")
    m_hot = float(input("Enter hot stream mass flow (kg/h): "))
    cp_hot = float(input("Enter hot stream Cp (J/kg·K): "))
    t_hot_in = float(input("Enter hot stream inlet temperature (°C or K): "))
    t_hot_out = float(input("Enter hot stream outlet temperature (°C or K): "))

    print("\n--- Cold Stream ---")
    m_cold = float(input("Enter cold stream mass flow (kg/h): "))
    cp_cold = float(input("Enter cold stream Cp (J/kg·K): "))
    t_cold_in = float(input("Enter cold stream inlet temperature (°C or K): "))
    t_cold_out = float(input("Enter cold stream outlet temperature (°C or K): "))

    q_hot, q_cold, imbalance = two_stream_heat_exchanger_balance(m_hot, cp_hot, t_hot_in, t_hot_out, m_cold, cp_cold, t_cold_in, t_cold_out)
    print("\n--- Results ---")
    print(f"Hot-side duty:  {q_hot} W")
    print(f"Cold-side duty: {q_cold} W")
    print(f"Energy balance (Q_hot + Q_cold): {imbalance} W")

    if abs(imbalance) < 1e-6:
        print("\nEnergy is balanced.")
    else:
        print("\nEnergy balance is NOT balanced.") 
