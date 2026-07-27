def sensible_heat(mass_flow, cp, t_in, t_out):
    """Q = m * Cp * (T_out - T_in)"""
    return mass_flow * cp * (t_out - t_in)

def latent_heat(mass_flow, latent_heat_value):
    """Q = m * latent heat"""
    return mass_flow * latent_heat_value

def reaction_enthalpy(reaction_rate, delta_h_reaction):
    """Q = reaction rate * delta H reaction"""
    return reaction_rate * delta_h_reaction

def cp_constant(cp_value):
    return cp_value

def heat_exchanger_energy_balance(mass_flow, cp, t_in, t_out):
    """Q = m * Cp * (T_out - T_in)"""
    return mass_flow * cp * (t_out - t_in)

def two_stream_heat_exchanger_balance(
    m_hot, cp_hot, t_hot_in, t_hot_out,
    m_cold, cp_cold, t_cold_in, t_cold_out
):
    """
    Computes hot-side and cold-side duties and checks energy balance.
    Q = m * Cp * (T_out - T_in)
    Returns (Q_hot, Q_cold, imbalance)
    """
    q_hot = m_hot * cp_hot * (t_hot_out - t_hot_in)
    q_cold = m_cold * cp_cold * (t_cold_out - t_cold_in)

    imbalance = q_hot + q_cold  # should be ~0

    return q_hot, q_cold, imbalance