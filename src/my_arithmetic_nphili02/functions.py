# pgcd_project/pgcd.py
def pgcd(a: int, b: int) -> int:
    """
    Calcule le plus grand commun diviseur (PGCD) de deux nombres en utilisant l'algorithme d'Euclide.

    Parameters
    ----------
    a : int
        Le premier nombre.
    b : int
        Le deuxième nombre.

    Returns
    -------
    int
        Le PGCD des deux nombres.

    Examples
    --------
    >>> pgcd(56, 98)
    14

    >>> pgcd(101, 10)
    1
    """
    while b != 0:
        a, b = b, a % b
    return a
