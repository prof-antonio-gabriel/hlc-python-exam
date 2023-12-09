class Usuario:
    def __init__(self, nombre, edad):
        """
        Inicializa los atributos de un nuevo usuario: nombre y edad (son los atributos)

        :param nombre: El nombre del usuario.
        :param edad: La edad del usuario.
        """
        self.nombre = nombre
        self.edad = edad

    def to_dict(self):
        """
        Convierte el objeto Usuario a un diccionario para su serialización.

        :return: Diccionario representando al usuario.
        """
        return {
            "nombre": self.nombre,
            "edad": self.edad
        }

    @staticmethod
    def from_dict(data):
        """
        Crea un objeto Usuario a partir de un diccionario.

        :param data: Diccionario con los datos del usuario.
        :return: Objeto Usuario.
        """
        return Usuario(data['nombre'], data['edad'])