# pgcd_project/pgcd.py
def pgcd(a: int, b: int) -> int:
    """
    Calcul du plus grand commun diviseur (PGCD) de deux nombres.
    Utilise l'algorithme d'Euclide.
    """
    while b != 0:
        a, b = b, a % b
    return a
