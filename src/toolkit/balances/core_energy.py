def sensible_heat(mass_flow: float, cp: float, t_in: float, t_out: float) -> float:
    """
    Calculate sensible heat duty.

    Q = m * Cp * (T_out - T_in)

    Parameters
    ----------
    mass_flow : float
        Mass flow rate (kg/s).
    cp : float
        Specific heat capacity (kJ/kg·K).
    t_in : float
        Inlet temperature.
    t_out : float
        Outlet temperature.

    Returns
    -------
    float
        Heat duty (kW).
    """
    return mass_flow * cp * (t_out - t_in)

def latent_heat(mass_flow: float, latent_heat_value: float) -> float:
    """Q = m * latent heat"""
    return mass_flow * latent_heat_value

def reaction_enthalpy(reaction_rate: float, delta_h_reaction: float) -> float:
    """Q = reaction rate * delta H reaction"""
    return reaction_rate * delta_h_reaction

def cp_constant(cp_value: float) -> float:
    return cp_value

def heat_exchanger_energy_balance(mass_flow: float, cp: float, t_in: float, t_out: float) -> float:
    """Q = m * Cp * (T_out - T_in)"""
    return mass_flow * cp * (t_out - t_in)

def two_stream_heat_exchanger_balance(
    m_hot: float, cp_hot: float, t_hot_in: float, t_hot_out: float,
    m_cold: float, cp_cold: float, t_cold_in: float, t_cold_out: float
) -> tuple[float, float, float]:
    """
    Computes hot-side and cold-side duties and checks energy balance.
    Q = m * Cp * (T_out - T_in)
    Returns (Q_hot, Q_cold, imbalance)
    """
    q_hot = m_hot * cp_hot * (t_hot_out - t_hot_in)
    q_cold = m_cold * cp_cold * (t_cold_out - t_cold_in)

    imbalance = q_hot + q_cold  # should be ~0

    return q_hot, q_cold, imbalance