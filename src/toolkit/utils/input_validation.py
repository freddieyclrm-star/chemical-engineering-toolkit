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


def check_non_negative(value: float, name: str) -> bool:
    """Return True if value is non-negative; otherwise print an error and return False.

    Args:
        value: Numeric value to validate.
        name: A descriptor for the value used in error messages.

    Returns:
        True if value is zero or positive; False otherwise.
    """
    if value >= 0:
        return True
    print(f"{name.capitalize()} must be non-negative.")
    return False
