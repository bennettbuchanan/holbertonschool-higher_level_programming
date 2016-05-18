def fibonacci(n):
    """Returns the fibonacci number of x.

    Keyword arguments:
    x -- The int to calculate the fibonacci number from.
    """
    i = 2
    tmp1 = 0
    tmp2 = 1
    fib = 1

    if type(n) is not int:
        print "Please enter an integer."
        return
    if n == 0:
        return 0
    if n > 0:
        while i < n:
            tmp1 = tmp2
            tmp2 = fib
            fib = tmp1 + tmp2
            i += 1
    if n < 0:
        n *= -1
        while i < n:
            tmp1 = tmp2
            tmp2 = fib
            fib = tmp1 + tmp2
            i += 1
        if n % 2 != True:
            fib *= -1
    return fib
