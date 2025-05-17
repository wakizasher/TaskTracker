def calculate_color_sequence(target):
    """
    Find the sequence of colors that transforms the initial value of 1
    into the target number.
    """
    sequence = []

    # Work backwards from the target to the initial value of 1
    current = target
    while current > 1:  # Stop when we reach the initial value
        digit = current % 4
        sequence.insert(0, digit)
        current = (current - digit) // 4

    return sequence


def verify_sequence(sequence, target):
    """Verify that applying the sequence to the initial value of 1 gives the target."""
    value = 1
    for digit in sequence:
        value = value * 4 + digit
    return value == target


def display_color_sequence(sequence):
    """Display the color sequence in a simple way that works in any terminal."""
    color_names = {
        0: "Green (G)",
        1: "Blue (B)",
        2: "Red (R)",
        3: "Yellow (Y)"
    }

    color_letters = {
        0: "G",
        1: "B",
        2: "R",
        3: "Y"
    }

    # Display the sequence as symbols
    print("\nColor Sequence:")
    for digit in sequence:
        symbol = {
            0: "[G]",  # Green
            1: "[B]",  # Blue
            2: "[R]",  # Red
            3: "[Y]"  # Yellow
        }[digit]
        print(symbol, end="")
    print()  # New line

    # Display the sequence as letters only
    print("\nColor Sequence as Letters:")
    print("".join(color_letters[digit] for digit in sequence))

    # Display with names
    print("\nColor Sequence with Names:")
    for i, digit in enumerate(sequence):
        print(f"Step {i + 1}: {color_names[digit]}")

    # Create flag string
    flag_text = "".join(color_letters[digit] for digit in sequence)
    print(f"\nFlag: tctf{{{flag_text}}}")


# Target number from the image
target = 414363270630243

# Find the sequence
sequence = calculate_color_sequence(target)

# Display the sequence
display_color_sequence(sequence)

# Verify the solution
print("\nVerification:")
value = 1
for i, digit in enumerate(sequence):
    old_value = value
    value = value * 4 + digit
    print(f"Step {i + 1}: {old_value} * 4 + {digit} = {value}")

print(f"\nFinal value: {value}")
print(f"Target value: {target}")
print(f"Match: {verify_sequence(sequence, target)}")