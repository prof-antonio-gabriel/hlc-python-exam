# Ejercicio 2: juego.py
# Puntuación: 3 ptos.


def es_jugada_valida(jugada):
    """
    Verifica si la jugada es válida, es decir, que jugada está dentro de estos tres posibles valores:
    piedra, papel o tijera

    :param jugada: La jugada del jugador.
    :return: True si la jugada es válida, False en caso contrario.
    """
    return jugada in ["piedra", "papel", "tijera"]


def determinar_ganador(jugada1, jugada2):
    """
    Determina el ganador entre dos jugadas, para ello hay que implementar todos los ifs necesarios para controlar
    todas las posibles combinaciones del juego piedra papel o tijera.

    :param jugada1: La jugada del jugador 1 (piedra, papel o tijera)
    :param jugada2: La jugada del jugador 2 (piedra, papel o tijera)
    :return: Una cadena que indica el resultado: "Jugador 1 gana" o "Jugador 2 gana" o "Empate"
    """
    if jugada1 == jugada2:
        return "Empate"
    elif (jugada1 == "piedra" and jugada2 == "tijera") or \
         (jugada1 == "tijera" and jugada2 == "papel") or \
         (jugada1 == "papel" and jugada2 == "piedra"):
        return "Jugador 1 gana"
    else:
        return "Jugador 2 gana"


def jugar(jugada1, jugada2):
    """
    Ejecuta una ronda del juego con las jugadas proporcionadas y maneja excepciones.
    :param jugada1: La jugada del jugador 1.
    :param jugada2: La jugada del jugador 2.
    :return: El resultado de la ronda o una cadena de texto con el siguiente mensaje de error:
        f"Jugada Inválida: {jugada1}" si la jugada no es válida para la jugada1
        f"Jugada Inválida: {jugada1}" si la jugada no es válida para la jugada2
    """
    try:
        if not es_jugada_valida(jugada1):
            raise ValueError(f"Jugada inválida: {jugada1}")
        if not es_jugada_valida(jugada2):
            raise ValueError(f"Jugada inválida: {jugada2}")
        return determinar_ganador(jugada1, jugada2)
    except ValueError as e:
        return str(e)
