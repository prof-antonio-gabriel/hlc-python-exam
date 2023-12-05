# test_juego.py

from assetments.ejercicio2.juego import determinar_ganador, es_jugada_valida, jugar


def test_determinar_ganador():
    assert determinar_ganador("piedra", "tijera") == "Jugador 1 gana"
    assert determinar_ganador("tijera", "papel") == "Jugador 1 gana"
    assert determinar_ganador("papel", "piedra") == "Jugador 1 gana"
    assert determinar_ganador("piedra", "piedra") == "Empate"
    assert determinar_ganador("papel", "tijera") == "Jugador 2 gana"
    assert determinar_ganador("tijera", "piedra") == "Jugador 2 gana"


def test_es_jugada_valida():
    assert es_jugada_valida("piedra") is True
    assert es_jugada_valida("papel") is True
    assert es_jugada_valida("tijera") is True
    assert es_jugada_valida("lagarto") is False


def test_jugar_ganador():
    assert jugar("piedra", "tijera") == "Jugador 1 gana"
    assert jugar("papel", "piedra") == "Jugador 1 gana"
    assert jugar("tijera", "papel") == "Jugador 1 gana"


def test_jugar_empate():
    assert jugar("piedra", "piedra") == "Empate"
    assert jugar("papel", "papel") == "Empate"
    assert jugar("tijera", "tijera") == "Empate"


def test_jugar_jugada_invalida():
    # La función jugar ya no lanza una excepción, en cambio retorna un mensaje de error.
    # Por lo tanto, el test debe verificar el mensaje de error en lugar de capturar una excepción.
    assert jugar("piedra", "avión") == "Jugada inválida: avión"

