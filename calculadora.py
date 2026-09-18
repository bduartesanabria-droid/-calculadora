"""Operaciones básicas de una calculadora."""


def sumar(a: float, b: float) -> float:
    """Devuelve la suma de dos números."""
    return a + b


def restar(a: float, b: float) -> float:
    """Devuelve la diferencia entre dos números."""
    return a - b


def multiplicar(a: float, b: float) -> float:
    """Devuelve el producto de dos números."""
    return a * b


def dividir(a: float, b: float) -> float:
    """Devuelve la división de dos números.

    Raises:
        ZeroDivisionError: si el divisor es cero.
    """
    if b == 0:
        raise ZeroDivisionError("No se puede dividir entre cero")
    return a / b
