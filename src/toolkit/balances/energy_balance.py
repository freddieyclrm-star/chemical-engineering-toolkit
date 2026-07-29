from toolkit.balances.core_energy import sensible_heat, latent_heat, reaction_enthalpy, cp_constant, heat_exchanger_energy_balance, two_stream_heat_exchanger_balance
from toolkit.utils.input_validation import check_non_negative, get_float, check_positive, check_temperature_direction
from toolkit.utils.formatting import format_result, format_label, format_section, success_message, error_message

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
    mass_flow = get_float("Enter mass flow rate (kg/s): ")
    cp = get_float("Enter specific heat capacity (J/kg•K): ")
    t_in = get_float("Enter inlet temperature (°C): ")
    t_out = get_float("Enter outlet temperature (°C): ")
    print()

    format_section("Inputs")
    format_label("Mass flow rate", mass_flow, "kg/s")
    format_label("Specific heat capacity", cp, "J/kg•K")
    format_label("Inlet temperature", t_in, "°C")
    format_label("Outlet temperature", t_out, "°C")

    if not check_non_negative(mass_flow, "mass flow rate"):
        error_message()
        return

    if not check_positive(cp, "specific heat capacity"):
        error_message()
        return

    result = sensible_heat(mass_flow, cp, t_in, t_out)
    print()
    format_section("Results")
    format_result("Sensible heat duty", result, "W")
    success_message()

def handle_latent_heat():
    print("\n=== Latent Heat Calculation ===")
    mass_flow = get_float("Enter mass flow rate (kg/s): ")
    latent_heat_value = get_float("Enter latent heat value (J/kg): ")
    print()
    
    format_section("Inputs")
    format_label("Mass flow rate", mass_flow, "kg/s")
    format_label("Latent heat value", latent_heat_value, "J/kg")

    if not check_non_negative(mass_flow, "mass flow rate"):
        error_message()
        return
    if not check_non_negative(latent_heat_value, "latent heat value"):
        error_message()
        return
    result = latent_heat(mass_flow, latent_heat_value)
    print()
    format_section("Results")
    format_result("Latent heat duty", result, "W")
    success_message()

def handle_reaction_enthalpy():
    print("\n=== Reaction Enthalpy Calculation ===")
    reaction_rate = get_float("Enter reaction rate (mol/s): ")
    delta_h_reaction = get_float("Enter reaction enthalpy ΔH (J/mol): ")
    print()
    
    format_section("Inputs")
    format_label("Reaction rate", reaction_rate, "mol/s")
    format_label("Reaction enthalpy ΔH", delta_h_reaction, "J/mol")

    result = reaction_enthalpy(reaction_rate, delta_h_reaction)
    print()
    format_section("Results")
    format_result("Reaction enthalpy duty", result, "W")
    success_message()

def handle_heat_capacity():
    print("\n=== Heat Capacity (Cp) Calculations ===")
    print("1. Constant Cp")
    print("2. Polynomial Cp (Coming Soon)")

    choice = input("Choose Cp model (1 or 2): ").strip()

    if choice == "1":
        cp_value = get_float("Enter constant Cp value (J/kg·K): ")
        print()
        
        format_section("Inputs")
        format_label("Constant Cp value", cp_value, "J/kg·K")

        if not check_positive(cp_value, "specific heat capacity"):
            error_message()
            return
        result = cp_constant(cp_value)
        print()
        format_section("Results")
        format_result("Specific heat capacity", result, "J/kg·K")
        success_message()
    elif choice == "2":
        print("\nPolynomial Cp model COMING SOON.")
    else:
        print("Invalid choice.")
        error_message()
        return

def handle_heat_exchanger_energy_balance():
    print("\n=== Heat Exchanger Energy Balance ===")
    print("Calculate heat duty using one stream (hot or cold).")

    mass_flow = get_float("Enter mass flow rate (kg/s): ")
    cp = get_float("Enter specific heat capacity Cp (J/kg·K): ")
    t_in = get_float("Enter inlet temperature (°C): ")
    t_out = get_float("Enter outlet temperature (°C): ")
    print()
    
    format_section("Inputs")
    format_label("Mass flow rate", mass_flow, "kg/s")
    format_label("Specific heat capacity", cp, "J/kg•K")
    format_label("Inlet temperature", t_in, "°C")
    format_label("Outlet temperature", t_out, "°C")

    if not check_non_negative(mass_flow, "mass flow rate"):
        error_message()
        return
    if not check_positive(cp, "specific heat capacity"):
        error_message()
        return
    
    result = heat_exchanger_energy_balance(mass_flow, cp, t_in, t_out)

    print()
    format_section("Results")
    format_result("Heat exchanger balance", result, "W")
    print("Note: Positive = heating, Negative = cooling.")
    success_message()

def handle_two_stream_heat_exchanger_balance():
    print("\n=== Two-Stream Heat Exchanger Energy Balance ===")

    print("\n--- Hot Stream ---")
    m_hot = get_float("Enter hot stream mass flow rate (kg/s): ")
    cp_hot = get_float("Enter hot stream Cp (J/kg·K): ")
    t_hot_in = get_float("Enter hot stream inlet temperature (°C): ")
    t_hot_out = get_float("Enter hot stream outlet temperature (°C): ")
    print()
    
    format_section("Inputs")
    format_label("Mass flow rate", m_hot, "kg/s")
    format_label("Specific heat capacity", cp_hot, "J/kg•K")
    format_label("Inlet temperature", t_hot_in, "°C")
    format_label("Outlet temperature", t_hot_out, "°C")

    print("\n--- Cold Stream ---")
    m_cold = get_float("Enter cold stream mass flow rate (kg/s): ")
    cp_cold = get_float("Enter cold stream Cp (J/kg·K): ")
    t_cold_in = get_float("Enter cold stream inlet temperature (°C): ")
    t_cold_out = get_float("Enter cold stream outlet temperature (°C): ")
    print()
    
    format_section("Inputs")
    format_label("Mass flow rate", m_cold, "kg/s")
    format_label("Specific heat capacity", cp_cold, "J/kg•K")
    format_label("Inlet temperature", t_cold_in, "°C")
    format_label("Outlet temperature", t_cold_out, "°C")

    if not check_non_negative(m_hot, "hot stream mass flow rate"):
        error_message()
        return
    if not check_non_negative(m_cold, "cold stream mass flow rate"):
        error_message()
        return
    if not check_positive(cp_hot, "hot stream specific heat capacity"):
        error_message()
        return
    if not check_positive(cp_cold, "cold stream specific heat capacity"):
        error_message()
        return
    if not check_temperature_direction(t_hot_in, t_hot_out, "hot"):
        error_message()
        return
    if not check_temperature_direction(t_cold_in, t_cold_out, "cold"):
        error_message()
        return
    q_hot, q_cold, imbalance = two_stream_heat_exchanger_balance(m_hot, cp_hot, t_hot_in, t_hot_out, m_cold, cp_cold, t_cold_in, t_cold_out)
    print()
    format_section("Results")
    format_result("Hot-side duty", q_hot, "W")
    format_result("Cold-side duty", q_cold, "W")
    format_result("Energy balance", imbalance, "W")
    success_message(

    )
    if abs(imbalance) < 1e-6:
        print("\nEnergy is balanced.")
    else:
        print("\nEnergy balance is NOT balanced.") 
