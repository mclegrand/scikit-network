"""utils module"""
from sknetwork.utils.check import is_symmetric
from sknetwork.utils.format import *
from sknetwork.utils.membership import get_membership, from_membership
from sknetwork.utils.neighbors import get_neighbors, get_degrees, get_weights
from sknetwork.utils.simplex import projection_simplex, projection_simplex_array, projection_simplex_csr
from sknetwork.utils.tfidf import get_tfidf


class Bunch(dict):
    """Container object for datasets.
    Dictionary-like object that exposes its keys as attributes.

    This code is taken from scikit-learn.
    >>> bunch = Bunch(a=1, b=2)
    >>> bunch['a']
    1
    >>> bunch.a
    1
    >>> bunch.b = 3
    >>> bunch['b']
    3
    >>> bunch.c = 4
    >>> bunch['c']
    4
    """
    def __init__(self, **kwargs):
        super().__init__(kwargs)

    def __setattr__(self, key, value):
        self[key] = value

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(key)
