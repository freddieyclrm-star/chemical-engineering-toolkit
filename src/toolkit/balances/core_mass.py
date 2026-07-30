def single_stream_balance(m_in: float) -> float:
    """Return the outlet mass for a single-stream mass balance.

    Parameters
    ----------
    m_in : float
        Mass entering the system (kg or consistent units).

    Assumptions
    -----------------------
    Assumes a steady-state single-stream balance with no accumulation and no
    generation or consumption of mass within the control volume.

    Returns
    -------
    float
        Mass leaving the system (equal to m_in for a steady single-stream balance).

    References
    ----------
    Single-stream mass conservation: m_in = m_out. See Cengel, Y. A., &
    Boles, M. A. (2015). Thermodynamics: An Engineering Approach, or Bird, R. B.,
    Stewart, W. E., & Lightfoot, E. N. (2002). Transport Phenomena.
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

    Assumptions
    -----------------------
    Assumes the balance is evaluated over the same control volume and time basis.

    Returns
    -------
    float
        Net mass accumulation: sum(in_streams) - sum(out_streams). Positive means net inflow.

    References
    ----------
    Net mass balance for multiple streams: sum(m_in) - sum(m_out). See Cengel,
    Y. A., & Boles, M. A. (2015). Thermodynamics: An Engineering Approach, or
    Felder, R. M., & Rousseau, R. W. (2005). Elementary Principles of Chemical
    Processes.
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

    Assumptions
    -----------------------
    Assumes the reaction rate applies uniformly to all species in the balance.

    Returns
    -------
    dict[str, float]
        Dictionary mapping species to their production (positive) or consumption (negative) rates.

    References
    ----------
    Uses stoichiometric relation r_i = nu_i * R, where nu_i are stoichiometric
    coefficients and R is the reaction rate. See Fogler, H. S. (2016).
    Elements of Chemical Reaction Engineering.
    """
    return {species: nu * reaction_rates for species, nu in stoich_coeffs.items()}


def mass_fractions(masses: dict[str, float]) -> dict[str, float]:
    """Compute mass fractions for components in a mixture.

    Parameters
    ----------
    masses : dict[str, float]
        Mapping of species to their mass flow rates.

    Assumptions
    -----------------------
    Assumes the supplied masses represent a single mixture at the same state.

    Returns
    -------
    dict[str, float]
        Mapping of species to mass fraction (mass / total mass).

    Raises
    ------
    ValueError
        If the total mass is zero.

    References
    ----------
    Mass fraction definition: w_i = m_i / sum(m_i). See Bird et al., Transport Phenomena (2002).
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

    Assumptions
    -----------------------
    Assumes the fluid density is uniform over the cross-section and that the
    volumetric flow rate is measured at the same conditions as the density.

    Returns
    -------
    float
        Mass flow rate (kg/s).

    References
    ----------
    Mass flow via density and volumetric flow: m_dot = rho * Q. See Cengel, Y. A., &
    Boles, M. A. (2015). Thermodynamics: An Engineering Approach, or standard
    transport texts such as Bird et al. (2002).
    """
    return density * volumetric_flow
