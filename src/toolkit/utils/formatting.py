def format_result(title: str, value: float, unit: str) -> None:
    """Print a formatted result with title, value (3 decimal places), and unit.

    Args:
        title: The title label for the result.
        value: The numerical value to format.
        unit: The unit of measurement.
    """
    title = title + ":"
    print(f"{title:<20}{value:.3f} {unit}")
    print()


def format_label(title: str, value, unit: str) -> None:
    """Print a formatted label with title, value (handles lists/numbers), and unit.

    Args:
        title: The title label for the output.
        value: The value to format (int, float, list, or str).
        unit: The unit of measurement.
    """
    title = title + ":"

    # Handle lists → join into a readable string
    if isinstance(value, list):
        value = ", ".join(str(v) for v in value)

    # Handle numbers → apply 3dp formatting
    if isinstance(value, (int, float)):
        value_str = f"{value:.3f}"
    else:
        value_str = str(value)

    print(f"{title:<20}{value_str} {unit}")


def format_section(header: str) -> None:
    """Print a section header with dashes.

    Args:
        header: The section header text to display.
    """
    print(f"--- {header} ---")
    print()


def success_message() -> None:
    """Print a success message indicating calculation completion."""
    print("Calculation completed successfully.")


def error_message() -> None:
    """Print an error message for invalid input."""
    print("Error: Invalid input detected.")
