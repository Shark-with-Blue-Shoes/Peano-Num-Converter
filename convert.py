import sys

def to_peano(n: int) -> str:
    """
    Converts a non-negative integer to its Peano numeral representation.

    Args:
        n: The non-negative integer to convert.

    Returns:
        A string representing the Peano numeral.

    Raises:
        ValueError: If the input is a negative integer.
    """
    if n < 0:
        raise ValueError("Peano numerals are defined for non-negative integers only.")
    elif n == 0:
        return "O"
    else:
        # Recursively call for n-1 and wrap it with 'S(...)'
        return f"S({to_peano(n - 1)})"

def from_peano(peano_str: str) -> int:
    """
    Converts a Peano numeral string to its corresponding non-negative integer.

    Args:
        peano_str: A string representing a Peano numeral (e.g., "O", "S(O)", "S(S(O))").

    Returns:
        The non-negative integer represented by the Peano numeral.

    Raises:
        ValueError: If the input string is not a valid Peano numeral.
    """
    peano_str = peano_str.strip() # Remove leading/trailing whitespace

    if peano_str == "O":
        return 0
    elif peano_str.startswith("S(") and peano_str.endswith(")"):
        # Extract the content inside S(...)
        inner_str = peano_str[2:-1] # Remove "S(" from start and ")" from end

        # Check for empty inner string or invalid characters within
        if not inner_str:
            raise ValueError(f"Invalid Peano numeral: Empty successor argument in '{peano_str}'")

        # Recursively call from_peano for the inner part
        try:
            return 1 + from_peano(inner_str)
        except ValueError as e:
            # Re-raise with more context
            raise ValueError(f"Invalid Peano numeral: Malformed successor argument in '{peano_str}' -> {e}")
    else:
        raise ValueError(f"Invalid Peano numeral format: '{peano_str}'. Expected 'O' or 'S(...)'")


if __name__ == "__main__":
    # Check if a command-line argument was provided
    if len(sys.argv) < 2:
        print("Usage: python your_script_name.py <input_value>")
        print("  <input_value> can be a non-negative integer (e.g., '5')")
        print("  OR a Peano numeral string (e.g., 'S(S(O))')")
        sys.exit(1) # Exit with an error code

    input_value = sys.argv[1]

    # Attempt to convert from Peano first, as it has a more distinct format
    if input_value == "O" or (input_value.startswith("S(") and input_value.endswith(")")):
        try:
            result_int = from_peano(input_value)
            print(f"Peano: '{input_value}' -> Integer: {result_int}")
        except ValueError as e:
            print(f"Error converting from Peano: {e}")
            sys.exit(1)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            sys.exit(1)
    else:
        # If it's not a Peano string, assume it's an integer
        try:
            num_int = int(input_value)
            result_peano = to_peano(num_int)
            print(f"Integer: {num_int} -> Peano: {result_peano}")
        except ValueError:
            print(f"Error: '{input_value}' is not a valid non-negative integer or Peano numeral.")
            sys.exit(1)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            sys.exit(1)
