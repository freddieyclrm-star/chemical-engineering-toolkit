import os


class Colour:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"


def format_result(title: str, value: float, unit: str) -> None:
    """Print a formatted result with title, value (3 decimal places), and unit.

    Args:
        title: The title label for the result.
        value: The numerical value to format.
        unit: The unit of measurement.
    """
    title = title + ":"
    print(f"{Colour.OKGREEN}{title:<20}{value:.3f} {unit}{Colour.ENDC}")
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

    print(f"{Colour.BOLD}{title:<20}{Colour.ENDC}{value_str} {unit}")


def format_section(header: str) -> None:
    """Print a section header with dashes.

    Args:
        header: The section header text to display.
    """
    spacer(1)
    print(f"{Colour.BOLD}{Colour.OKBLUE}--- {header} ---{Colour.ENDC}")
    spacer(1)


def success_message() -> None:
    """Print a success message indicating calculation completion."""
    print(f"{Colour.OKGREEN}✔ Calculation completed successfully. {Colour.ENDC}")


def error_message() -> None:
    """Print an error message for invalid input."""
    print(f"{Colour.FAIL}✖ Error: Invalid input detected.{Colour.ENDC}")


def clear_screen():
    """Clear the terminal screen."""
    os.system("cls" if os.name == "nt" else "clear")


def invalid_choice():
    """Print a warning message for an invalid user menu choice."""
    print(f"{Colour.WARNING}Invalid choice. Please try again.{Colour.ENDC}")


def spacer(lines: int = 1):
    """Print blank lines to add vertical spacing.

    Args:
        lines: The number of blank lines to print.
    """
    print("\n" * lines)
