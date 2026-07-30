def sensible_heat(mass_flow: float, cp: float, t_in: float, t_out: float) -> float:
    """
    Calculate sensible heat duty.

    Equation: Sensible Heat Duty
    Q = m * Cp * (T_out - T_in)

    Parameters
    ----------
    mass_flow : float
        Mass flow rate (kg/s).
    cp : float
        Specific heat capacity (J/kg·K).
    t_in : float
        Inlet temperature (°C).
    t_out : float
        Outlet temperature (°C).

    Returns
    -------
    float
        Heat duty (W).

    References
    ----------
    - Heat transfer fundamentals: Q = m * Cp * ΔT
    - Smith, Van Ness, Abbott (2005). Introduction to Chemical Engineering Thermodynamics

    Assumptions
    -----------
    - Specific heat capacity is constant over the temperature range.
    - Pressure effects on heat capacity are negligible.
    - No phase change occurs.
    """
    return mass_flow * cp * (t_out - t_in)


def latent_heat(mass_flow: float, latent_heat_value: float) -> float:
    """
    Calculate latent heat duty.

    Equation: Latent Heat Duty
    Q = m * latent heat

    Parameters
    ----------
    mass_flow : float
        Mass flow rate (kg/s).
    latent_heat_value : float
        Latent heat of vaporization or condensation (J/kg).

    Returns
    -------
    float
        Heat duty (W).

    References
    ----------
    - Latent heat transfer: Q = m * λ
    - Smith, Van Ness, Abbott (2005). Introduction to Chemical Engineering Thermodynamics

    Assumptions
    -----------
    - Phase change occurs at constant temperature.
    - Latent heat value is constant at the operating conditions.
    - All mass undergoing phase change.
    """
    return mass_flow * latent_heat_value


def reaction_enthalpy(reaction_rate: float, delta_h_reaction: float) -> float:
    """
    Calculate heat duty from reaction enthalpy.

    Equation: Reaction Enthalpy Heat Duty
    Q = reaction rate * delta H reaction

    Parameters
    ----------
    reaction_rate : float
        Reaction rate (mol/s).
    delta_h_reaction : float
        Heat of reaction (J/mol).

    Returns
    -------
    float
        Heat duty (W).

    References
    ----------
    - Reaction heat: Q = r * ΔH_rxn
    - Smith, Van Ness, Abbott (2005). Introduction to Chemical Engineering Thermodynamics

    Assumptions
    -----------
    - Reaction goes to completion at specified rate.
    - Heat of reaction is constant over the operating range.
    """
    return reaction_rate * delta_h_reaction


def cp_constant(cp_value: float) -> float:
    """
    Return constant specific heat capacity value.

    Parameters
    ----------
    cp_value : float
        Specific heat capacity (J/kg·K).

    Returns
    -------
    float
        Specific heat capacity (J/kg·K).

    Assumptions
    -----------
    - Specific heat capacity does not vary with temperature or pressure.
    - Value provided is applicable for the operating range.
    """
    return cp_value


def heat_exchanger_energy_balance(
    mass_flow: float, cp: float, t_in: float, t_out: float
) -> float:
    """
    Calculate heat duty in a heat exchanger.

    Equation: Heat Exchanger Energy Balance
    Q = m * Cp * (T_out - T_in)

    Parameters
    ----------
    mass_flow : float
        Mass flow rate (kg/s).
    cp : float
        Specific heat capacity (J/kg·K).
    t_in : float
        Inlet temperature (°C).
    t_out : float
        Outlet temperature (°C).

    Returns
    -------
    float
        Heat duty (W).

    References
    ----------
    - Energy balance equation: Q = m * Cp * (T_out - T_in)
    - Smith, Van Ness, Abbott (2005). Introduction to Chemical Engineering Thermodynamics

    Assumptions
    -----------
    - Specific heat capacity is constant over the temperature range.
    - Steady-state operation.
    - No phase change occurs during heat exchange.
    - Kinetic and potential energy changes are negligible.
    """
    return mass_flow * cp * (t_out - t_in)


def two_stream_heat_exchanger_balance(
    m_hot: float,
    cp_hot: float,
    t_hot_in: float,
    t_hot_out: float,
    m_cold: float,
    cp_cold: float,
    t_cold_in: float,
    t_cold_out: float,
) -> tuple[float, float, float]:
    """
    Calculate heat duties and energy balance for a two-stream heat exchanger.

    Equation: Two-Stream Heat Exchanger Balance
    Q_hot = m_hot * Cp_hot * (T_hot_out - T_hot_in)
    Q_cold = m_cold * Cp_cold * (T_cold_out - T_cold_in)
    Imbalance = Q_hot + Q_cold (should be ~0 for perfect balance)

    Computes the duty on the hot and cold sides using Q = m * Cp * (T_out - T_in)
    and returns the imbalance (sum of duties, which should be ~0 for perfect balance).

    Parameters
    ----------
    m_hot : float
        Hot stream mass flow rate (kg/s).
    cp_hot : float
        Hot stream specific heat capacity (J/kg·K).
    t_hot_in : float
        Hot stream inlet temperature (°C).
    t_hot_out : float
        Hot stream outlet temperature (°C).
    m_cold : float
        Cold stream mass flow rate (kg/s).
    cp_cold : float
        Cold stream specific heat capacity (J/kg·K).
    t_cold_in : float
        Cold stream inlet temperature (°C).
    t_cold_out : float
        Cold stream outlet temperature (°C).

    Returns
    -------
    tuple[float, float, float]
        Q_hot : Heat duty on hot side (W).
        Q_cold : Heat duty on cold side (W).
        imbalance : Energy balance check (W), should be ~0.

    References
    ----------
    - Energy balance: Q_hot + Q_cold = 0 (ideal case)
    - Q = m * Cp * ΔT for each stream
    - Smith, Van Ness, Abbott (2005). Introduction to Chemical Engineering Thermodynamics

    Assumptions
    -----------
    - Specific heat capacities are constant for each stream.
    - Steady-state operation.
    - No phase change occurs in either stream.
    - Negligible heat loss to surroundings.
    """
    q_hot = m_hot * cp_hot * (t_hot_out - t_hot_in)
    q_cold = m_cold * cp_cold * (t_cold_out - t_cold_in)

    imbalance = q_hot + q_cold  # should be ~0

    return q_hot, q_cold, imbalance
