def single_stream_balance(m_in: float) -> float:
    """Return the outlet mass for a single-stream mass balance.

    Parameters
    ----------
    m_in : float
        Mass entering the system (kg or consistent units).

    Returns
    -------
    float
        Mass leaving the system (equal to m_in for a steady single-stream balance).
    """
    return m_in


def multi_stream_balance(in_streams: list, out_streams: list) -> float:
    """Compute net mass accumulation for a system with multiple inlet and outlet streams.

    Parameters
    ----------
    in_streams : list
        List of inlet mass flow rates (floats).
    out_streams : list
        List of outlet mass flow rates (floats).

    Returns
    -------
    float
        Net mass accumulation: sum(in_streams) - sum(out_streams). Positive means net inflow.
    """
    total_in = sum(in_streams)
    total_out = sum(out_streams)
    return total_in - total_out


def reaction_stoichiometry_balance(
    stoich_coeffs: dict[str, float], reaction_rates: float
) -> dict[str, float]:
    """Calculate species production/consumption rates from stoichiometric coefficients.

    Parameters
    ----------
    stoich_coeffs : dict[str, float]
        Stoichiometric coefficients (nu) for each species. Conventions: positive for
        products, negative for reactants.
    reaction_rates : float
        Overall reaction rate (mol/s).

    Returns
    -------
    dict[str, float]
        Dictionary mapping species to their production (positive) or consumption (negative) rates.
    """
    return {species: nu * reaction_rates for species, nu in stoich_coeffs.items()}


def mass_fractions(masses: dict[str, float]) -> dict[str, float]:
    """Compute mass fractions for components in a mixture.

    Parameters
    ----------
    masses : dict[str, float]
        Mapping of species to their mass flow rates.

    Returns
    -------
    dict[str, float]
        Mapping of species to mass fraction (mass / total mass).

    Raises
    ------
    ValueError
        If the total mass is zero.
    """
    total_mass = sum(masses.values())
    if total_mass == 0:
        raise ValueError("Total mass must be non-zero to compute mass fractions")
    return {species: m / total_mass for species, m in masses.items()}


def mixture_mass_flow(density: float, volumetric_flow: float) -> float:
    """Calculate mass flow from density and volumetric flow.

    Parameters
    ----------
    density : float
        Fluid density (kg/m^3).
    volumetric_flow : float
        Volumetric flow rate (m^3/s).

    Returns
    -------
    float
        Mass flow rate (kg/s).
    """
    return density * volumetric_flow
