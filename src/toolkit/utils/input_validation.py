def get_float(prompt: str) -> float:
    """Prompt a user until a valid float is entered.

    Args:
        prompt: The input prompt displayed to the user.

    Returns:
        The validated float entered by the user.
    """
    while True:
        try:
            user_input = float(input(prompt))
            return user_input
        except ValueError:
            print("Invalid number. Please try again.")


def check_positive(value: float, name: str) -> bool:
    """Return True if value is positive; otherwise print an error and return False.

    Args:
        value: Numeric value to validate.
        name: A descriptor for the value used in error messages.

    Returns:
        True if value is greater than zero; False otherwise.
    """
    if value > 0:
        return True
    print(f"{name.capitalize()} must be positive.")
    return False


def check_temperature_direction(t_in: float, t_out: float, stream_type: str) -> bool:
    """Validate that temperature change matches the expected direction for hot or cold streams.

    Args:
        t_in: Inlet temperature.
        t_out: Outlet temperature.
        stream_type: The stream type, expected "hot" or "cold".

    Returns:
        True if the temperatures follow the correct direction for the stream type; False otherwise.
    """
    stream_type_clean = stream_type.lower().strip()
    if stream_type_clean == "hot":
        if t_in > t_out:
            return True
        print("Hot stream outlet temperature must be lower than inlet temperature.")
        return False
    if stream_type_clean == "cold":
        if t_in < t_out:
            return True
        print("Cold stream outlet temperature must be higher than inlet temperature.")
        return False

    print("Unknown stream type")
    return False


def check_non_negative(value, name: str) -> bool:
    """Return True if value is non-negative; otherwise print an error and return False.

    Args:
        value: Numeric value to validate.
        name: A descriptor for the value used in error messages.

    Returns:
        True if value is zero or positive; False otherwise.
    """
    if isinstance(value, (int, float)):
        if value >= 0:
            return True
        print(f"{name.capitalize()} must be non-negative.")
        return False

    if isinstance(value, (list, tuple)):
        for item in value:
            if not isinstance(item, (int, float)):
                print(f"{name.capitalize()} must be numeric.")
                return False
            if item < 0:
                print(f"{name.capitalize()} must be non-negative.")
                return False
        return True

    return False


def validate_numeric(value: float, name: str) -> None:
    """Validate that a value is numeric (int or float).

    Args:
        value: The value to validate.
        name: A descriptor used in error messages.

    Raises:
        TypeError: If the value is not a numeric type.
    """
    if isinstance(value, (int, float)):
        return
    elif isinstance(value, (list, tuple)):
        for item in value:
            if not isinstance(item, (int, float)):
                raise TypeError(
                    f"{name} must be a numeric value or a list/tuple of numeric values."
                )
    else:
        raise TypeError(
            f"{name} must be a numeric value or a list/tuple of numeric values."
        )


def validate_positive(value: float, name: str) -> None:
    """Validate that a numeric value is positive (> 0).

    Args:
        value: The value to validate.
        name: A descriptor used in error messages.

    Raises:
        TypeError: If the value is not a numeric type.
        ValueError: If the value is not greater than zero.
    """
    validate_numeric(value, name)
    if value <= 0:
        raise ValueError(f"{name} must be positive.")


def validate_non_negative(value, name: str) -> None:
    """Validate that a numeric value is non-negative (>= 0).

    Args:
        value: The value to validate.
        name: A descriptor used in error messages.

    Raises:
        TypeError: If the value is not a numeric type.
        ValueError: If the value is negative.
    """
    if isinstance(value, (int, float)):
        validate_numeric(value, name)
        if value < 0:
            raise ValueError(f"{name} must be non-negative.")
    elif isinstance(value, (list, tuple)):
        for item in value:
            validate_numeric(item, name)
            if item < 0:
                raise ValueError(f"{name} must be non-negative.")
    else:
        raise TypeError(
            f"{name} must be a numeric value or a list/tuple of numeric values."
        )


def validate_temperature_direction(t_in: float, t_out: float, stream_type: str) -> None:
    """Validate that temperature change matches the expected direction for hot or cold streams.

    Args:
        t_in: Inlet temperature.
        t_out: Outlet temperature.
        stream_type: The stream type, expected "hot" or "cold".

    Raises:
        ValueError: If the temperatures do not follow the correct direction for the stream type.
    """
    validate_numeric(t_in, "Inlet temperature")
    validate_numeric(t_out, "Outlet temperature")
    stream_type_clean = stream_type.lower().strip()
    if stream_type_clean == "hot":
        if t_in <= t_out:
            raise ValueError(
                "Hot stream inlet temperature must be greater than outlet temperature."
            )
    elif stream_type_clean == "cold":
        if t_in >= t_out:
            raise ValueError(
                "Cold stream inlet temperature must be less than outlet temperature."
            )
    else:
        raise ValueError("Unknown stream type")


def assert_temperature_range(value: float, name: str) -> None:
    """Validate that a temperature value is not below absolute zero.

    Args:
        value: The temperature value to validate.
        name: A descriptor used in error messages.

    Raises:
        TypeError: If the value is not a numeric type.
        ValueError: If the value is below absolute zero (-273.15).
    """
    validate_numeric(value, name)
    if value < -273.15:
        raise AssertionError(f"{name} cannot be below absolute zero (-273.15).")


def validate_mass_flow(value: float, name: str) -> None:
    """Validate mass flow: numeric and non-negative.

    Args:
        value: Mass flow value to validate.
        name: Descriptor used in error messages.

    Raises:
        TypeError: If value is not numeric.
        ValueError: If value is negative.
    """
    validate_numeric(value, name)
    validate_non_negative(value, name)


def validate_density(value: float, name: str) -> None:
    """Validate density: numeric and non-negative.

    Args:
        value: Density value to validate.
        name: Descriptor used in error messages.

    Raises:
        TypeError: If value is not numeric.
        ValueError: If value is negative.
    """
    validate_numeric(value, name)
    validate_non_negative(value, name)


def validate_volumetric_flow(value: float, name: str) -> None:
    """Validate volumetric flow: numeric and non-negative.

    Args:
        value: Volumetric flow value to validate.
        name: Descriptor used in error messages.

    Raises:
        TypeError: If value is not numeric.
        ValueError: If value is negative.
    """
    validate_numeric(value, name)
    validate_non_negative(value, name)


def validate_cp(value: float, name: str) -> None:
    """Validate specific heat capacity: numeric and non-negative.

    Args:
        value: Specific heat capacity value to validate.
        name: Descriptor used in error messages.

    Raises:
        TypeError: If value is not numeric.
        ValueError: If value is negative.
    """
    validate_numeric(value, name)
    validate_non_negative(value, name)


def validate_unit_supported(unit: str, supported_units, name: str) -> None:
    """Validate that a unit string is supported.

    Args:
        unit: Unit string to validate.
        supported_units: Iterable of supported unit strings.
        name: Descriptor used in error messages.

    Raises:
        TypeError: If unit is not a string or supported_units is not iterable.
        ValueError: If unit is not in supported_units.
    """
    if not isinstance(unit, str):
        raise TypeError(f"{name} must be a string.")
    try:
        contains = unit in supported_units
    except TypeError:
        raise TypeError("Supported_units must be an iterable of strings.")
    if not contains:
        raise ValueError(
            f"{name} '{unit}' is not supported. Supported: {supported_units}"
        )


def validate_pressure(value: float, name: str) -> None:
    """Validate pressure: numeric and non-negative.

    Args:
        value: Pressure value to validate.
        name: Descriptor used in error messages.

    Raises:
        TypeError: If value is not numeric.
        ValueError: If value is negative.
    """
    validate_numeric(value, name)
    validate_non_negative(value, name)


def validate_stoich_coeff(value: dict, name: str) -> None:
    """Validate stoichiometric coefficients.

    Args:
        value: Stoichiometric coefficient value or mapping of values.
        name: Descriptor used in error messages.

    Raises:
        TypeError: If value contains non-numeric entries.
    """
    if isinstance(value, dict):
        for item in value.values():
            if not isinstance(item, (int, float)):
                raise TypeError(
                    f"{name} must be a numeric value, list/tuple, or dict of numeric values."
                )


def validate_mass_fraction(value: dict, name: str) -> None:
    if isinstance(value, dict):
        for item in value.values():
            if not isinstance(item, (int, float)):
                raise TypeError(
                    f"{name} must be a numeric value, list/tuple, or dict of numeric values."
                )

    if sum(value.values()) == 0:
        raise ValueError("Total mass must be non-zero to compute mass fractions")
