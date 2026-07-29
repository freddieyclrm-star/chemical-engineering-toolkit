import pytest
from toolkit.units.conversion import Converter

def test_cm_to_m():
    conv = Converter()
    assert conv.convert(100, "cm", "m") == 1

def test_bar_to_pa():
    conv = Converter()
    assert conv.convert(1, "bar", "Pa") == 100000

def test_pa_to_bar():
    conv = Converter()
    assert conv.convert(100000, "Pa", "bar") == 1

def test_celsius_to_kelvin():
    conv = Converter()
    assert conv.convert(25, "C", "K") == 298.15

def test_kelvin_to_celsius():
    conv = Converter()
    assert round(conv.convert(300, "K", "C"), 2) == 26.85

def test_kg_to_g():
    conv = Converter()
    assert conv.convert(1, "kg", "g") == 1000