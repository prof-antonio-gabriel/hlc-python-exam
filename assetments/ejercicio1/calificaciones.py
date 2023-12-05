# Ejercicio 1: calificaciones.py
# Puntuación: 2 ptos.

def calcular_promedio(calificaciones):
    """
    Calcula el promedio de una lista de calificaciones numéricas.

    Esta función intenta calcular el promedio de las calificaciones proporcionadas.
    Si la lista de calificaciones está vacía, la función captura un ZeroDivisionError
    y en su lugar lanza un ValueError con el mensaje: "La lista de calificaciones está vacía, no se puede calcular el promedio.".

    Parámetros:
    calificaciones (list): Una lista de calificaciones numéricas. Las calificaciones
                           deben ser valores numéricos y la lista no debe estar vacía.

    Devuelve:
    float: El promedio de las calificaciones en la lista.

    Excepciones:
    ValueError: Se lanza si la lista de calificaciones está vacía.

    Ejemplo:
    >>> calcular_promedio([20, 30, 40])
    30.0

    >>> calcular_promedio([])
    ValueError: La lista de calificaciones está vacía, no se puede calcular el promedio.
    """
    return None # Eliminar esta línea e implementar el código de esta función


def calificacion_maxima(calificaciones):
    """
    Encuentra y devuelve la calificación máxima en una lista de calificaciones numéricas.

    Esta función busca la calificación más alta en una lista de calificaciones numéricas.
    Se valida que la lista no esté vacía y que todos sus elementos sean de tipo numérico
    (enteros o flotantes). Si la lista está vacía, se lanza una ValueError. Si la lista
    contiene elementos no numéricos, se lanza una TypeError.

    Parámetros:
    calificaciones (list): Una lista de calificaciones numéricas. La lista no debe estar vacía
                           y todos sus elementos deben ser enteros o flotantes.

    Devuelve:
    int o float: La calificación máxima encontrada en la lista. El tipo de retorno dependerá
                 del tipo de elementos en la lista de calificaciones.

    Excepciones:
    ValueError: Se lanza si la lista de calificaciones está vacía.
    TypeError: Se lanza si alguno de los elementos de la lista no es numérico.

    Ejemplo:
    >>> calificacion_maxima([20, 30, 40])
    40

    >>> calificacion_maxima([])
    ValueError: No se puede encontrar una calificación máxima en una lista vacía.

    >>> calificacion_maxima([20, "30", 40])
    TypeError: Todos los elementos de la lista deben ser numéricos.
    """
    return None # Eliminar esta línea e implementar el código de esta función


def calificacion_minima(calificaciones):
    """
    Encuentra y devuelve la calificación mínima en una lista de calificaciones numéricas.

    Esta función busca la calificación más alta en una lista de calificaciones numéricas.
    Se valida que la lista no esté vacía y que todos sus elementos sean de tipo numérico
    (enteros o flotantes). Si la lista está vacía, se lanza una ValueError. Si la lista
    contiene elementos no numéricos, se lanza una TypeError.

    Parámetros:
    calificaciones (list): Una lista de calificaciones numéricas. La lista no debe estar vacía
                           y todos sus elementos deben ser enteros o flotantes.

    Devuelve:
    int o float: La calificación mínima encontrada en la lista. El tipo de retorno dependerá
                 del tipo de elementos en la lista de calificaciones.

    Excepciones:
    ValueError: Se lanza si la lista de calificaciones está vacía.
    TypeError: Se lanza si alguno de los elementos de la lista no es numérico.

    Ejemplo:
    >>> calificacion_maxima([20, 30, 40])
    20

    >>> calificacion_maxima([])
    ValueError: No se puede encontrar una calificación mínima en una lista vacía.

    >>> calificacion_maxima([20, "30", 40])
    TypeError: Todos los elementos de la lista deben ser numéricos.
    """
    return None # Eliminar esta línea e implementar el código de esta función

