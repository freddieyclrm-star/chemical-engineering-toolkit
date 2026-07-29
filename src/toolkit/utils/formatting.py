def format_result(title, value, unit):
    title = title + ":"
    print(f"{title:<20}{value:.3f} {unit}")
    print()

def format_label(title, value, unit):
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

def format_section(header):
    print(f"--- {header} ---")
    print()

def success_message():
    print("Calculation completed successfully.")

def error_message():
    print("Error: Invalid input detected.")