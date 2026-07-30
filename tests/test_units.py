from toolkit.units.conversion import Converter


def test_cm_to_m() -> None:
    """Convert 100 centimeters to meters and verify the result is 1."""
    conv = Converter()
    assert conv.convert(100, "cm", "m") == 1


def test_bar_to_pa() -> None:
    """Convert 1 bar to pascals and verify the result is 100000."""
    conv = Converter()
    assert conv.convert(1, "bar", "Pa") == 100000


def test_pa_to_bar() -> None:
    """Convert 100000 pascals to bar and verify the result is 1."""
    conv = Converter()
    assert conv.convert(100000, "Pa", "bar") == 1


def test_celsius_to_kelvin() -> None:
    """Convert 25 degrees Celsius to Kelvin and verify the result is 298.15."""
    conv = Converter()
    assert conv.convert(25, "C", "K") == 298.15


def test_kelvin_to_celsius() -> None:
    """Convert 300 Kelvin to degrees Celsius and verify the rounded result is 26.85."""
    conv = Converter()
    assert round(conv.convert(300, "K", "C"), 2) == 26.85


def test_kg_to_g() -> None:
    """Convert 1 kilogram to grams and verify the result is 1000."""
    conv = Converter()
    assert conv.convert(1, "kg", "g") == 1000
