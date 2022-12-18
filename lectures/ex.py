"""this is our first python"""
from operator import mod, floordiv
def divide_exact(n,d):
    """ return quotient and reminder of divide n by d
    >>> p , r = divide_exact(2013, 10)
    >>> p
    201
    >>> r
    3
    """

    return floordiv(n,d), mod(n,d)


#print('quotient',p)
#print('reminder',r)