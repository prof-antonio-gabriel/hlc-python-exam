# test_gestion_usuarios.py

import pytest
from unittest.mock import MagicMock
from assetments.ejercicio3.gestion_usuarios import Usuario, GestorUsuarios


# Test para la clase Usuario
def test_usuario_to_dict():
    usuario = Usuario("Carlos", 40)
    assert usuario.to_dict() == {"nombre": "Carlos", "edad": 40}


def test_usuario_from_dict():
    usuario_dict = {"nombre": "Carlos", "edad": 40}
    usuario = Usuario.from_dict(usuario_dict)
    assert usuario.nombre == "Carlos"
    assert usuario.edad == 40


# Test para cargar_usuarios
def test_cargar_usuarios_con_archivo_valido():
    gestor = GestorUsuarios("../data/usuarios.json")
    usuarios = gestor.cargar_usuarios()
    assert isinstance(usuarios, list)
    assert all(isinstance(usuario, Usuario) for usuario in usuarios)


def test_cargar_usuarios_con_archivo_malformado():
    gestor = GestorUsuarios("../data/archivo_malformado.json")
    with pytest.raises(ValueError) as excinfo:
        gestor.cargar_usuarios()
    assert "Error al leer el archivo JSON" in str(excinfo.value)


def test_cargar_usuarios_con_error_lectura():
    gestor = GestorUsuarios("archivo_inexistente.json")
    with pytest.raises(ValueError) as excinfo:
        gestor.cargar_usuarios()
    assert "Error al abrir el archivo" in str(excinfo.value)


def test_anadir_usuario():
    gestor = GestorUsuarios("../data/usuarios2.json")
    usuario_original = Usuario(nombre="Ana", edad=25)
    gestor.anadir_usuario(usuario_original)

    assert usuario_original in gestor.usuarios


def test_obtener_usuario_existente():
    gestor = GestorUsuarios("../data/usuarios2.json")
    usuario_existente = Usuario(nombre="Ana", edad=25)
    gestor.usuarios.append(usuario_existente)

    resultado = gestor.obtener_usuario("Ana")
    assert resultado == usuario_existente


def test_obtener_usuario_inexistente():
    gestor = GestorUsuarios("../data/usuarios2.json")
    gestor.usuarios = [Usuario(nombre="Juan", edad=30)]

    resultado = gestor.obtener_usuario("Ana")
    assert resultado is None


def test_eliminar_usuario_existente():
    gestor = GestorUsuarios("../data/usuarios2.json")
    usuario_existente = Usuario(nombre="Ana", edad=25)
    gestor.usuarios.append(usuario_existente)

    gestor.eliminar_usuario("Ana")
    assert usuario_existente not in gestor.usuarios


def test_eliminar_usuario_inexistente():
    gestor = GestorUsuarios("../data/usuarios2.json")
    usuario_original = Usuario(nombre="Juan", edad=30)
    gestor.usuarios.append(usuario_original)

    gestor.eliminar_usuario("Ana")
    assert usuario_original in gestor.usuarios  # El usuario original sigue en la lista
    assert len(gestor.usuarios) == 1  # La lista no cambia de tamaño


def test_eliminar_usuario_actualiza_archivo_json():
    gestor = GestorUsuarios("../data/usuarios2.json")
    gestor.guardar_usuarios = MagicMock()

    gestor.eliminar_usuario("Ana")
    gestor.guardar_usuarios.assert_called_once()






