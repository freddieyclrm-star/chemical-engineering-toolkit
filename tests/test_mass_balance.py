import pytest

from toolkit.balances.core_mass import (
    mass_fractions,
    mixture_mass_flow,
    multi_stream_balance,
    reaction_stoichiometry_balance,
    single_stream_balance,
)
from toolkit.utils.input_validation import (
    validate_mass_flow,
    validate_numeric,
    validate_stoich_coeff,
    validate_mass_fraction,
    validate_density,
    validate_volumetric_flow,
    validate_non_negative,
)
from toolkit.utils.input_validation import get_float, check_non_negative, check_positive


def test_single_stream() -> None:
    """Test single_stream_balance with positive value."""
    assert single_stream_balance(100) == 100


def test_single_stream_zero() -> None:
    """Test single_stream_balance with zero value."""
    assert single_stream_balance(0) == 0


def test_get_float(monkeypatch: pytest.MonkeyPatch) -> None:
    """Test get_float with invalid input followed by a valid float."""
    responses = iter(["invalid", "3.5"])
    monkeypatch.setattr("builtins.input", lambda prompt: next(responses))
    assert get_float("Enter value: ") == 3.5


def test_check_positive() -> None:
    """Test check_positive with positive and zero values."""
    assert check_positive(2.0, "mass") is True
    # This should fail the positivity check because zero is not a positive value.
    assert check_positive(0, "mass") is False


def test_validate_non_negative() -> None:
    """Test validate_non_negative with zero and negative values."""
    validate_non_negative(0, "mass")
    # This should fail because negative values are not allowed for non-negative checks.
    with pytest.raises(ValueError):
        validate_non_negative(-1, "mass")


def test_check_non_negative() -> None:
    """Test check_non_negative with zero and negative values."""
    assert check_non_negative(0, "mass") is True
    # This should fail the non-negative check because negative values are not allowed.
    assert check_non_negative(-1, "mass") is False


def test_validate_numeric() -> None:
    """Test validate_numeric with numeric and non-numeric values."""
    validate_numeric(10, "mass")
    # This should fail because a string is not a valid numeric value.
    with pytest.raises(TypeError):
        validate_numeric("bad", "mass")


def test_validate_mass_flow() -> None:
    """Test validate_mass_flow with valid and negative values."""
    validate_mass_flow(1.0, "mass flow")
    # This should fail because mass flow cannot be negative.
    with pytest.raises(ValueError):
        validate_mass_flow(-1.0, "mass flow")


def test_validate_density() -> None:
    """Test validate_density with valid and negative values."""
    validate_density(1.2, "density")
    # This should fail because density cannot be negative.
    with pytest.raises(ValueError):
        validate_density(-0.5, "density")


def test_validate_volumetric_flow() -> None:
    """Test validate_volumetric_flow with valid and negative values."""
    validate_volumetric_flow(2.0, "volumetric flow")
    # This should fail because volumetric flow cannot be negative.
    with pytest.raises(ValueError):
        validate_volumetric_flow(-2.0, "volumetric flow")


def test_validate_stoich_coeff() -> None:
    """Test validate_stoich_coeff with valid and invalid coefficient types."""
    validate_stoich_coeff({"A": 1, "B": 2}, "stoich")
    # This should fail because stoichiometric coefficients must be numeric values.
    with pytest.raises(TypeError):
        validate_stoich_coeff({"A": "x"}, "stoich")


def test_validate_mass_fraction() -> None:
    """Test validate_mass_fraction with valid and invalid mass fractions."""
    validate_mass_fraction({"A": 0.2, "B": 0.8}, "mass fraction")
    # This should fail because the mass fractions sum to zero, which is invalid.
    with pytest.raises(ValueError):
        validate_mass_fraction({"A": 0.0, "B": 0.0}, "mass fraction")


def test_regression_single_stream_balance() -> None:
    """Regression test for single_stream_balance."""
    assert single_stream_balance(10.0) == 10.0

    with pytest.raises(ValueError):
        single_stream_balance(-1.0)


def test_regression_multi_stream_balance() -> None:
    """Regression test for multi_stream_balance."""
    assert multi_stream_balance([2.0, 3.0], [4.0, 1.0]) == 0.0

    with pytest.raises(ValueError):
        multi_stream_balance([1.0, -2.0], [0.0, 0.0])


def test_regression_reaction_stoichiometry_balance() -> None:
    """Regression test for reaction_stoichiometry_balance."""
    assert reaction_stoichiometry_balance({"A": -1.0, "B": 1.0}, 2.0) == {
        "A": -2.0,
        "B": 2.0,
    }


def test_regression_mass_fractions() -> None:
    """Regression test for mass_fractions."""
    assert mass_fractions({"A": 2.0, "B": 3.0}) == {"A": 0.4, "B": 0.6}

    with pytest.raises(ValueError):
        mass_fractions({"A": -1.0, "B": 2.0})


def test_regression_mixture_mass_flow() -> None:
    """Regression test for mixture_mass_flow."""
    assert mixture_mass_flow(1000.0, 0.005) == 5.0

    with pytest.raises(ValueError):
        mixture_mass_flow(-1.0, 0.005)
