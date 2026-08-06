def rectangle_area(length, breadth):
    """Calculate and return the area of a rectangle."""
    return length * breadth
def circle_area(radius):
    """Calculate and return the area of a circle."""
    return 3.14 * radius * radius


if __name__ == '__main__':
    # Test cases
    test_length = 10
    test_breadth = 5
    
    # Function call
    result = rectangle_area(test_length, test_breadth)
    print(f"Area: {result}")
