import math

def calculate_square_root(number):
    """
    Calculate the square root of a given number.

    Parameters:
    - number (float): The number for which the square root needs to be calculated.

    Returns:
    - float: The square root of the given number.
    """
    if number < 0:
        raise ValueError("Cannot calculate the square root of a negative number.")
    
    return math.sqrt(number)

# Example usage:
try:
    input_number = float(input("Enter a number to calculate its square root: "))
    result = calculate_square_root(input_number)
    print(f"The square root of {input_number} is {result}")
except ValueError as ve:
    print(f"Error: {ve}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

