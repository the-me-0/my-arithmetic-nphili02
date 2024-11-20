# tests/test_pgcd.py
from src.my_arithmetic_nphili02.functions import pgcd

def test_pgcd():
    assert pgcd(56, 98) == 14
    assert pgcd(101, 10) == 1
    assert pgcd(15, 5) == 5
    assert pgcd(25, 25) == 25
    assert pgcd(17, 31) == 1
