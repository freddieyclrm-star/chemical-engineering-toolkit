import pytest

from toolkit.units.conversion import Converter, UNITS
from toolkit.utils.input_validation import validate_unit_supported


def test_cm_to_m() -> None:
    """Convert 100 centimeters to meters and verify the result is 1."""
    conv = Converter()
    # Fails if centimeters-to-meters conversion is incorrect or the converter uses the wrong factor.
    assert conv.convert(100, "cm", "m") == 1


def test_bar_to_pa() -> None:
    """Convert 1 bar to pascals and verify the result is 100000."""
    conv = Converter()
    # Fails if the bar-to-pascal conversion factor is wrong.
    assert conv.convert(1, "bar", "Pa") == 100000


def test_pa_to_bar() -> None:
    """Convert 100000 pascals to bar and verify the result is 1."""
    conv = Converter()
    # Fails if pascal-to-bar conversion is incorrect or the reverse conversion is not applied properly.
    assert conv.convert(100000, "Pa", "bar") == 1


def test_celsius_to_kelvin() -> None:
    """Convert 25 degrees Celsius to Kelvin and verify the result is 298.15."""
    conv = Converter()
    # Fails if the Celsius-to-Kelvin offset or scaling is incorrect.
    assert conv.convert(25, "C", "K") == 298.15


def test_kelvin_to_celsius() -> None:
    """Convert 300 Kelvin to degrees Celsius and verify the rounded result is 26.85."""
    conv = Converter()
    # Fails if Kelvin-to-Celsius conversion is wrong or rounding is not handled as expected.
    assert round(conv.convert(300, "K", "C"), 2) == 26.85


def test_kg_to_g() -> None:
    """Convert 1 kilogram to grams and verify the result is 1000."""
    conv = Converter()
    # Fails if kilograms-to-grams conversion uses the wrong multiplier.
    assert conv.convert(1, "kg", "g") == 1000


def test_m_to_cm() -> None:
    """Convert 2 meters to centimeters and verify the result is 200."""
    conv = Converter()
    # Fails if meters-to-centimeters conversion is incorrect.
    assert conv.convert(2, "m", "cm") == 200


def test_g_to_kg() -> None:
    """Convert 500 grams to kilograms and verify the result is 0.5."""
    conv = Converter()
    # Fails if grams-to-kilograms conversion is incorrect or decimal handling is wrong.
    assert conv.convert(500, "g", "kg") == 0.5


def test_kelvin_to_celsius_round() -> None:
    """Convert 310 Kelvin to degrees Celsius and verify the rounded result is 36.85."""
    conv = Converter()
    # Fails if the conversion result is not rounded to the expected precision.
    assert round(conv.convert(310, "K", "C"), 2) == 36.85


def test_validate_unit_supported_raises_for_unsupported_unit() -> None:
    """Validate that an unsupported unit raises ValueError."""
    # Fails if unsupported units are not rejected or if the error message does not match the expected text.
    with pytest.raises(ValueError, match="unit 'km' is not supported"):
        validate_unit_supported("km", ["m", "cm", "kg"], "unit")


def converter() -> Converter:
    return Converter()


def test_init_uses_unit_definitions() -> None:
    conv = Converter()
    assert conv.units == UNITS


def test_temperature_conversions() -> None:
    conv = Converter()
    assert conv.convert(0, "C", "K") == pytest.approx(273.15)
    assert conv.convert(32, "F", "C") == pytest.approx(0.0)
    assert conv.convert(273.15, "K", "F") == pytest.approx(32.0)


def test_linear_unit_conversion() -> None:
    conv = Converter()
    non_temperature_categories = [
        category
        for category, units in UNITS.items()
        if category != "temperature" and len(units) >= 2
    ]
    if not non_temperature_categories:
        pytest.skip("No non-temperature category available for conversion testing")

    category = non_temperature_categories[0]
    units = UNITS[category]
    from_unit, to_unit = list(units.keys())[:2]
    value = 10.0
    expected = value * units[from_unit] / units[to_unit]
    assert conv.convert(value, from_unit, to_unit) == pytest.approx(expected)


def test_invalid_units_raise_value_error() -> None:
    conv = Converter()
    with pytest.raises(ValueError):
        conv.convert(1.0, "not_a_unit", "C")
    with pytest.raises(ValueError):
        conv.convert(1.0, "C", "not_a_unit")


def test_incompatible_units_raise_value_error() -> None:
    conv = Converter()
    with pytest.raises(ValueError):
        conv.convert(1.0, "C", "m")


def test_unsupported_temperature_conversion_raises_value_error() -> None:
    conv = Converter()
    with pytest.raises(ValueError):
        conv.convert(1.0, "C", "C")
