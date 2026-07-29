from toolkit.balances.core_energy import sensible_heat

def test_sensible_heat():
    result = sensible_heat(mass_flow=10, cp=4184, t_in=10, t_out=30)
    assert result == 836800

def test_zero_temperature_change():
    assert sensible_heat(10, 4184, 10, 10) == 0