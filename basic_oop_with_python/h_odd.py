def odd(n):
    """Returns 1 if argument int is odd, and 0 otherwise.

    Keyword arguments:
    n -- The variable to test for evenness.
    """
    if type(n) is not int:
        return 0
    if n % 2 != 0:
        return 1
    else:
        return 0
