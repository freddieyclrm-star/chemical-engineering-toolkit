from toolkit.units.unit_definitions import UNITS

class Converter:
    def __init__(self):
        self.units = UNITS

    def convert(self, value, from_unit, to_unit):
        from_unit_cat = None
        to_unit_cat = None
        for category, unitname in self.units.items():
            if from_unit in unitname:
                from_unit_cat = category
            if to_unit in unitname:
                to_unit_cat = category

        if from_unit_cat is None:
            raise ValueError(f"Invalid from_unit: {from_unit}")
        if to_unit_cat is None:
            raise ValueError(f"Invalid to_unit: {to_unit}")
        if from_unit_cat != to_unit_cat:
            raise ValueError(f"Incompatible units")

        if from_unit_cat == "temperature":
            if from_unit == "C" and to_unit == "F":
                result = value *9/5 +32
            elif from_unit == "F" and to_unit == "C":
                result = (value -32) *5/9
            elif from_unit == "C" and to_unit == "K":
                result = value +273.15
            elif from_unit == "K" and to_unit == "C":
                result = value - 273.15
            elif from_unit == "F" and to_unit == "K":
                result = (value-32) *5/9+273.15
            elif from_unit == "K" and to_unit == "F":
                result = (value-273.15) *9/5+32
            else:
                raise ValueError("Unsupported temperature conversion")

            return result
    
        category_dict = UNITS[from_unit_cat]
        base_value = value * category_dict[from_unit]
        result = base_value / category_dict[to_unit]

        return result


