def get_float(prompt):
    """Prompt a user until a valid float is entered."""
    while True:
        try:
            user_input = float(input(prompt))
            return user_input
        except ValueError:
            print("Invalid number. Please try again.")

def check_positive(value, name):
    """Return True if value is positive; otherwise print an error and return False."""
    if value > 0:
        return True
    print(f"{name.capitalize()} must be positive.")
    return False

def check_temperature_direction(t_in, t_out, stream_type):
    """Validate that temperature change matches the expected direction for hot/cold streams."""
    if stream_type.lower().strip() == "hot":
        if t_in > t_out:
            return True
        print("Hot stream outlet temperature must be lower than inlet temperature.")
        return False
    if stream_type.lower().strip() == "cold":
        if t_in < t_out:
            return True
        print("Cold stream outlet temperature must be higher than inlet temperature.")
        return False

    print("Unknown stream type")
    return False

def check_non_negative(value, name):
    """Return True if value is non-negative; otherwise print an error and return False."""
    if value >= 0:
        return True
    print(f"{name.capitalize()} must be non-negative.")
    return False
