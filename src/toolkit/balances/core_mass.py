def single_stream_balance(m_in: float)->float:
    """m_in = m_out"""
    return m_in

def multi_stream_balance(in_streams: list, out_streams: list)-> float:
    """total mass= sum(in) - sum(out)"""
    total_in = sum(in_streams)
    total_out = sum(out_streams)
    return total_in - total_out

def reaction_stoichiometry_balance(stoich_coeffs:dict[str, float], reaction_rates:float)-> dict[str, float]:
    """mass [i] = nu[i] * reaction_rate"""
    return {species: nu * reaction_rates for species, nu in stoich_coeffs.items()}

def mass_fractions(masses:dict[str, float] )-> dict[str, float]:
    """mass fraction [i] = mass[i] / total_mass"""
    total_mass = sum(masses.values())
    return {species: m / total_mass for species, m in masses.items()}

def mixture_mass_flow(density: float, volumetric_flow: float)-> float:
    """mass flow = density * volumetric flow"""
    return density * volumetric_flow