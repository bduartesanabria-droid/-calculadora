import pytest

from calculadora import dividir, multiplicar, restar, sumar


@pytest.mark.parametrize(
    ("operacion", "a", "b", "resultado"),
    [
        (sumar, 2, 3, 5),
        (restar, 8, 3, 5),
        (multiplicar, 4, 3, 12),
        (dividir, 10, 2, 5),
    ],
)
def test_operaciones_basicas(operacion, a, b, resultado):
    assert operacion(a, b) == resultado


def test_dividir_entre_cero():
    with pytest.raises(ZeroDivisionError, match="No se puede dividir entre cero"):
        dividir(10, 0)
