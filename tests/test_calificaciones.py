import pytest
from assetments.ejercicio1.calificaciones import calcular_promedio, calificacion_maxima, calificacion_minima


# Tests para calcular_promedio
def test_calcular_promedio_valores_normales():
    assert calcular_promedio([10, 20, 30]) == 20
    assert calcular_promedio([5, 15, 25, 35]) == 20


def test_calcular_promedio_zero_division():
    with pytest.raises(ValueError) as excinfo:
        calcular_promedio([])
    assert str(excinfo.value) == "La lista de calificaciones está vacía, no se puede calcular el promedio."


# Test para calificacion_maxima
def test_calificacion_maxima_valores_normales():
    assert calificacion_maxima([10, 20, 30]) == 30
    assert calificacion_maxima([5, 15, 25, 35]) == 35


def test_calificacion_maxima_zero_division():
    with pytest.raises(ValueError) as excinfo:
        calificacion_maxima([])
    assert str(excinfo.value) == "No se puede encontrar una calificación máxima en una lista vacía."


def test_calificacion_maxima_type_error():
    # Verificar que se lanza TypeError para una lista con elementos no numéricos
    with pytest.raises(TypeError):
        calificacion_maxima([10, '20', 30])
    with pytest.raises(TypeError):
        calificacion_maxima([10, None, 30])
    with pytest.raises(TypeError):
        calificacion_maxima(['a', 'b', 'c'])



# Test para calificacion_minima
def test_calificacion_minima_valores_normales():
    assert calificacion_minima([10, 20, 30]) == 10
    assert calificacion_minima([5, 15, 25, 35]) == 5


def test_calificacion_minima_zero_division():
    with pytest.raises(ValueError) as excinfo:
        calificacion_minima([])
    assert str(excinfo.value) == "No se puede encontrar una calificación mínima en una lista vacía."


def test_calificacion_minima_type_error():
    # Verificar que se lanza TypeError para una lista con elementos no numéricos
    with pytest.raises(TypeError):
        calificacion_minima([10, '20', 30])
    with pytest.raises(TypeError):
        calificacion_minima([10, None, 30])
    with pytest.raises(TypeError):
        calificacion_minima(['a', 'b', 'c'])
