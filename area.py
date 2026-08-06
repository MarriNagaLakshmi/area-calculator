def rectangle_area(length, breadth):
    """Calculate and return the area of a rectangle."""
    return length * breadth

if __name__ == '__main__':
    # Test cases
    test_length = 10
    test_breadth = 5
    
    # Function call
    result = rectangle_area(test_length, test_breadth)
    print(f"Area: {result}")
