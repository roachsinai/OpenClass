def divide_exact(n, d):
    """Return the quotient and remander of dividing N by D.
    
    >>> q, r = divide_exact(2015, 10)
    >>> q
    201
    >>> r
    5
    """
    return n // d, n % d