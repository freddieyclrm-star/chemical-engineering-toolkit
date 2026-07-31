import pytest

from toolkit.balances.core_energy import (
    sensible_heat,
    latent_heat,
    reaction_enthalpy,
    cp_constant,
    heat_exchanger_energy_balance,
    two_stream_heat_exchanger_balance,
)
from toolkit.utils.input_validation import (
    check_positive,
    validate_temperature_direction,
    check_non_negative,
    validate_numeric,
    validate_non_negative,
    assert_temperature_range,
    validate_mass_flow,
    validate_cp,
    check_temperature_direction,
)


def test_sensible_heat() -> None:
    """Verify sensible_heat calculation for a positive temperature change."""
    # Fails if sensible_heat does not compute the expected heat for a positive temperature change.
    result = sensible_heat(mass_flow=10, cp=4184, t_in=10, t_out=30)
    assert result == 836800


def test_zero_temperature_change() -> None:
    """Verify sensible_heat calculation for no temperature change."""
    # Fails if sensible_heat returns a non-zero result when the temperature change is zero.
    assert sensible_heat(10, 4184, 10, 10) == 0


def test_check_positive_returns_false_for_non_positive(
    capsys: pytest.CaptureFixture[str],
) -> None:
    """Verify check_positive rejects non-positive values."""
    # Fails if check_positive accepts a non-positive value or omits the expected message.
    assert check_positive(-2, "flow rate") is False


def test_check_temperature_direction_accepts_hot_stream_direction() -> None:
    """Verify check_temperature_direction accepts a hot stream with cooling."""
    # Fails if a hot stream that cools down is incorrectly rejected.
    assert check_temperature_direction(80, 40, "hot") is True


def test_check_non_negative_accepts_non_negative_sequence() -> None:
    """Verify check_non_negative accepts a non-negative list."""
    # Fails if non-negative values are incorrectly rejected by check_non_negative.
    assert check_non_negative([1, 2, 3], "temperature") is True


def test_validate_numeric_rejects_non_numeric_value() -> None:
    """Verify validate_numeric raises for non-numeric input."""
    # Fails if non-numeric input is accepted instead of raising TypeError.
    with pytest.raises(TypeError):
        validate_numeric("abc", "temperature")


def test_validate_non_negative_rejects_negative_value() -> None:
    """Verify validate_non_negative raises for negative input."""
    # Fails if negative values are allowed through validate_non_negative.
    with pytest.raises(ValueError):
        validate_non_negative(-1, "mass flow")


def test_validate_temperature_direction_rejects_invalid_hot_stream() -> None:
    """Verify validate_temperature_direction rejects a hot stream that heats up."""
    # Fails if a hot stream that heats up is incorrectly accepted.
    with pytest.raises(ValueError):
        validate_temperature_direction(20, 30, "hot")


def test_assert_temperature_range_rejects_below_absolute_zero() -> None:
    """Verify assert_temperature_range rejects temperatures below absolute zero."""
    # Fails if temperatures below absolute zero are not rejected.
    with pytest.raises(AssertionError):
        assert_temperature_range(-300, "temperature")


def test_validate_mass_flow_rejects_negative_value() -> None:
    """Verify validate_mass_flow rejects negative mass flow values."""
    # Fails if negative mass flow is not rejected by validate_mass_flow.
    with pytest.raises(ValueError):
        validate_mass_flow(-1, "mass flow")


def test_validate_cp_rejects_negative_value() -> None:
    """Verify validate_cp rejects negative specific heat values."""
    # Fails if negative specific heat values are not rejected by validate_cp.
    with pytest.raises(ValueError):
        validate_cp(-1, "cp")


def test_sensible_heat_regression() -> None:
    """Regression test for sensible_heat."""
    assert sensible_heat(2.0, 4.2, 20.0, 80.0) == 504.0


def test_sensible_heat_rejects_negative_mass_flow() -> None:
    """Regression test for sensible_heat invalid mass flow."""
    with pytest.raises(ValueError):
        sensible_heat(-1.0, 4.2, 20.0, 80.0)


def test_sensible_heat_rejects_non_numeric_inputs() -> None:
    """Regression test for sensible_heat invalid input type."""
    with pytest.raises(TypeError):
        sensible_heat("2", 4.2, 20.0, 80.0)


def test_latent_heat_regression() -> None:
    """Regression test for latent_heat."""
    assert latent_heat(3.0, 2257.0) == 6771.0


def test_latent_heat_rejects_negative_mass_flow() -> None:
    """Regression test for latent_heat invalid mass flow."""
    with pytest.raises(ValueError):
        latent_heat(-1.0, 2257.0)


def test_latent_heat_rejects_non_numeric_inputs() -> None:
    """Regression test for latent_heat invalid latent heat input type."""
    with pytest.raises(TypeError):
        latent_heat(3.0, "2257")


def test_reaction_enthalpy_regression() -> None:
    """Regression test for reaction_enthalpy."""
    assert reaction_enthalpy(2.0, 50.0) == 100.0


def test_reaction_enthalpy_rejects_negative_moles() -> None:
    """Regression test for reaction_enthalpy invalid moles."""
    with pytest.raises(ValueError):
        reaction_enthalpy(-1.0, 50.0)


def test_reaction_enthalpy_rejects_non_numeric_inputs() -> None:
    """Regression test for reaction_enthalpy invalid input type."""
    with pytest.raises(TypeError):
        reaction_enthalpy(2.0, "50")


def test_cp_constant_regression() -> None:
    """Regression test for cp_constant."""
    assert cp_constant(3.5) == 3.5


def test_cp_constant_rejects_non_numeric_inputs() -> None:
    """Regression test for cp_constant invalid input type."""
    with pytest.raises(TypeError):
        cp_constant("3.5")


def test_heat_exchanger_energy_balance_regression() -> None:
    """Regression test for heat_exchanger_energy_balance."""
    assert heat_exchanger_energy_balance(2.0, 4.2, 20.0, 80.0) == 504.0


def test_heat_exchanger_energy_balance_rejects_negative_mass_flow() -> None:
    """Regression test for heat_exchanger_energy_balance invalid mass flow."""
    with pytest.raises(ValueError):
        heat_exchanger_energy_balance(-1.0, 4.2, 20.0, 80.0)


def test_heat_exchanger_energy_balance_rejects_non_numeric_inputs() -> None:
    """Regression test for heat_exchanger_energy_balance invalid input type."""
    with pytest.raises(TypeError):
        heat_exchanger_energy_balance(2.0, "4.2", 20.0, 80.0)


def test_two_stream_heat_exchanger_balance_regression() -> None:
    """Regression test for two_stream_heat_exchanger_balance."""
    q_hot, q_cold, imbalance = two_stream_heat_exchanger_balance(
        2.0, 4.2, 80.0, 60.0, 1.5, 3.0, 20.0, 50.0
    )
    assert q_hot == -168.0
    assert q_cold == 135.0
    assert imbalance == -33.0


def test_two_stream_heat_exchanger_balance_rejects_invalid_temperature_direction() -> (
    None
):
    """Regression test for two_stream_heat_exchanger_balance invalid temperature direction."""
    with pytest.raises(ValueError):
        two_stream_heat_exchanger_balance(2.0, 4.2, 80.0, 90.0, 1.5, 3.0, 20.0, 50.0)


def test_two_stream_heat_exchanger_balance_rejects_non_numeric_inputs() -> None:
    """Regression test for two_stream_heat_exchanger_balance invalid input type."""
    with pytest.raises(TypeError):
        two_stream_heat_exchanger_balance(2.0, 4.2, 80.0, 60.0, 1.5, 3.0, 20.0, "50")
