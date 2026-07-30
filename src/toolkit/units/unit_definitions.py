"""Unit definitions for conversion factors.

Reference:
- Conversion values are based on standard international definitions and trusted sources such as NIST unit conversions and engineering reference tables.
"""

UNITS = {
    "length": {
        "mm": 0.001,
        "cm": 0.01,
        "m": 1.0,
        "km": 1000.0,
        "in": 0.0254,
        "ft": 0.3048,
        "yard": 0.9144,
        "mile": 1609.34,
    },
    "temperature": ["C", "F", "K"],
    "mass": {
        "mg": 0.000001,
        "g": 0.001,
        "kg": 1.0,
        "oz": 0.0283495,
        "lb": 0.453592,
        "tonnes": 1000,
    },
    "speed": {"m/s": 1.0, "km/h": 0.277778, "mph": 0.44704},
    "volume": {
        "ml": 0.001,
        "l": 1.0,
        "m3": 1000.0,
        "gallon": 3.78541,
        "quart": 0.946353,
        "pint": 0.473176,
        "cup": 0.236588,
    },
    "time": {
        "s": 1.0,
        "min": 60.0,
        "h": 3600.0,
        "day": 86400.0,
        "week": 604800.0,
        "month": 2628000.0,
        "year": 31536000.0,
    },
    "area": {
        "mm2": 0.000001,
        "cm2": 0.0001,
        "m2": 1.0,
        "km2": 1000000.0,
        "ft2": 0.092903,
        "in2": 0.00064516,
        "ha": 10000.0,
        "acre": 4046.86,
        "mi2": 2589988.11,
    },
    "pressure": {
        "Pa": 1.0,
        "kPa": 1000.0,
        "MPa": 1000000.0,
        "bar": 100000.0,
        "psi": 6894.76,
        "atm": 101325.0,
        "torr": 133.322,
    },
    "energy": {
        "J": 1.0,
        "kJ": 1000.0,
        "cal": 4.184,
        "kcal": 4184.0,
        "Wh": 3600.0,
        "kWh": 3600000.0,
    },
}
