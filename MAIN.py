
"""
A simple program to calculate the area of a rectangle.
"""
def calculate_rectangle_area(length, width):
    """
    Calculates the area of a rectangle.

    Args:
        length (float or int): The length of the rectangle.
        width (float or int): The width of the rectangle.

    Returns:
        float or int: The calculated area of the rectangle.
    """
    return length * width

def main():
    """
    Main function to get user input, perform calculations, and print results.
    """
    print("Welcome to the Rectangle Area Calculator!")
    try:
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))

        if length <= 0 or width <= 0:
            print("Error: Length and width must be positive numbers.")
            return

        area = calculate_rectangle_area(length, width)

        print("\n--- Calculation Results ---")
        print(f"Length: {length}")
        print(f"Width: {width}")
        print(f"Area of the rectangle: {area}")

    except ValueError:
        print("Error: Invalid input. Please enter a number.")


if __name__ == "__main__":
    main()

