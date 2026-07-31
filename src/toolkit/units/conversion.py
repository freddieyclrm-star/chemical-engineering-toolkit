from toolkit.units.unit_definitions import UNITS


class Converter:
    def __init__(self):
        self.units = UNITS

    def convert(self, value: float, from_unit: str, to_unit: str) -> float:
        """Convert a numeric value from one unit to another within the same category.

        Parameters
        ----------
        value : float
            The numerical value to convert.
        from_unit : str
            The unit symbol/name of the input value (must exist in UNITS).
        to_unit : str
            The unit symbol/name to convert to (must exist in UNITS and be
            in the same category as from_unit).

        Returns
        -------
        float
            The converted value in the target unit.

        Raises
        ------
        ValueError
            If either unit is invalid, if units are from different categories,
            or if a requested temperature conversion is unsupported.

        Examples
        --------
        >>> conv = Converter()
        >>> conv.convert(100, 'C', 'K')
        373.15
        """

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
            raise ValueError("Incompatible units")

        if from_unit_cat == "temperature":
            if from_unit == "C" and to_unit == "F":
                result = value * 9 / 5 + 32
            elif from_unit == "F" and to_unit == "C":
                result = (value - 32) * 5 / 9
            elif from_unit == "C" and to_unit == "K":
                result = value + 273.15
            elif from_unit == "K" and to_unit == "C":
                result = value - 273.15
            elif from_unit == "F" and to_unit == "K":
                result = (value - 32) * 5 / 9 + 273.15
            elif from_unit == "K" and to_unit == "F":
                result = (value - 273.15) * 9 / 5 + 32
            else:
                raise ValueError("Unsupported temperature conversion")

            return result

        category_dict = UNITS[from_unit_cat]
        base_value = value * category_dict[from_unit]
        result = base_value / category_dict[to_unit]

        return result
