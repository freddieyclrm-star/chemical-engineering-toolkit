def sensible_heat(mass_flow: float, cp: float, t_in: float, t_out: float) -> float:
    """
    Calculate sensible heat duty.

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
    """
    return mass_flow * cp * (t_out - t_in)


def latent_heat(mass_flow: float, latent_heat_value: float) -> float:
    """
    Calculate latent heat duty.

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
    """
    return mass_flow * latent_heat_value


def reaction_enthalpy(reaction_rate: float, delta_h_reaction: float) -> float:
    """
    Calculate heat duty from reaction enthalpy.

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
    """
    return cp_value


def heat_exchanger_energy_balance(
    mass_flow: float, cp: float, t_in: float, t_out: float
) -> float:
    """
    Calculate heat duty in a heat exchanger.

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
    """
    q_hot = m_hot * cp_hot * (t_hot_out - t_hot_in)
    q_cold = m_cold * cp_cold * (t_cold_out - t_cold_in)

    imbalance = q_hot + q_cold  # should be ~0

    return q_hot, q_cold, imbalance
