def isOdd(number):
    """
    input: integer 'number'
    returns true if 'number' is odd, otherwise false.
    """

    # precondition
    assert isinstance(number, int), "'number' must been an int"
    assert isinstance(number % 2 != 0, bool), "compare bust been from type bool"

    return number % 2 != 0