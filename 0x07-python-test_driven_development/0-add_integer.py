def add_integer(a, b=98):
    """
    Function to add two integers.

    Args:
        a (int or float): The first argument.
        b (int or float, optional): The second argument. Default is 98.

    Returns:
        int: The sum of a and b as an integer.

    Raises:
        TypeError: If either a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or float")
    a = int(a)
    b = int(b)
    return int(a + b)
