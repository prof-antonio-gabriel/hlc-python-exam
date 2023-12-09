from json import JSONDecodeError, load, dump
from pathlib import Path
from assetments.ejercicio3.usuario import Usuario


class GestorUsuarios:
    def __init__(self, archivo):
        """
        Inicializa una instancia del gestor de usuarios, estableciendo la ruta al archivo JSON.

        Este constructor acepta una ruta a un archivo JSON y la convierte en un objeto Path, que se utiliza posteriormente para
        cargar los datos de los usuarios.

        Parámetros:
        archivo (str): Una cadena de texto que representa la ruta al archivo JSON que contiene la información de los usuarios.
                       Esta ruta puede ser absoluta o relativa.

        Atributos de la Clase Creados:
        archivo (Path): Un objeto Path que representa la ruta al archivo JSON. Utilizar Path (del módulo pathlib) facilita
                        la manipulación de rutas de archivos en diferentes sistemas operativos y proporciona una serie de
                        métodos y atributos útiles para interactuar con el sistema de archivos.

        Ejemplo:
        >>> gestor = GestorUsuarios("data/usuarios.json")
        """
        self.archivo = Path(archivo)
        self.usuarios = []

    def cargar_usuarios(self):
        """
        Carga la información de usuarios desde un archivo JSON especificado en el atributo `archivo` de esta clase (self)

        Este método se encarga de leer y decodificar la información de usuarios desde un archivo JSON.
        Si el archivo existe y su contenido está en el formato correcto, el método lo lee y convierte los datos
        a objetos de la clase Usuario (a través de la implementación de Usuario.from_dict).
        Si el archivo no existe, se lanza una excepción.

        Durante el proceso de carga, el método maneja varios tipos de excepciones para asegurar que el programa no falle
        inesperadamente y proporcione retroalimentación útil sobre cualquier problema que ocurra. Estos incluyen problemas
        al abrir el archivo (OSError), errores en la decodificación del JSON (JSONDecodeError), y otras excepciones
        inesperadas. En cada caso, se lanza un ValueError con un mensaje descriptivo y se devuelve una lista vacía.

        Devuelve:
        list: Una lista de objetos Usuario, donde cada objeto representa a un usuario cargado desde el archivo JSON.
              Si ocurre cualquier error o el archivo no existe, se lanza una excepción.

        Excepciones:
        ValueError: Se lanza si ocurre un error al leer el archivo JSON, un error al abrir el archivo,
                    o cualquier otro error inesperado durante la carga de los usuarios.
        JSONDecodeError: Se lanza si el archivo JSON no tiene el formato adecuado.
        Exception: Se lanza cuando ocurre una excepción genérica.

        Ejemplo:
        # Ejemplo correcto
        >>> gestor = GestorUsuarios("data/usuarios.json")
        >>> gestor.cargar_usuarios()
        # Devuelve una lista de objetos Usuario cargados desde 'usuarios.json', o una lista vacía en caso de error

        # Ejemplo cuando el archivo JSON no existe
        >>> gestor = GestorUsuarios("archivo_inexistente.json")
        >>> gestor.cargar_usuarios()
        Error al cargar usuarios: Error al abrir el archivo


        # Ejemplo cuando hay un error en el formato JSON
        >>> gestor = GestorUsuarios("data/archivo_malformado.json")
        >>> gestor.cargar_usuarios()
        Error al cargar usuarios: Error al leer el archivo JSON

        # Ejemplo cuando ocurre un error inesperado
        >>> gestor = GestorUsuarios("data/archivo_con_problemas.json")
        >>> gestor.cargar_usuarios()
        Error al cargar usuarios: Error inesperado al cargar usuarios

        """
        try:
            with open(self.archivo, 'r') as f:
                usuarios_data = load(f)["usuarios"]
                return [Usuario.from_dict(usuario) for usuario in usuarios_data]
        except JSONDecodeError:
            raise ValueError(f"Error al leer el archivo JSON")
        except OSError:
            raise ValueError(f"Error al abrir el archivo")
        except Exception:
            raise ValueError(f"Error inesperado al cargar usuarios")

    def guardar_usuarios(self):
        """
        Guarda la lista actual de usuarios en el archivo JSON.
        En caso de errores de IO o excepciones generales, se imprime un mensaje de error.

        :return: None. Los efectos son la escritura en el archivo JSON.
        """
        try:
            usuarios_data = {"usuarios": [usuario.to_dict() for usuario in self.usuarios]}
            with open(self.archivo, 'w') as f:
                dump(usuarios_data, f, indent=4)
        except IOError as err:
            print(f"Error al guardar usuarios en el archivo: {err}")
        except Exception as err:
            print(f"Error inesperado al guardar usuarios: {err}")

    def anadir_usuario(self, usuario):
        """
        Añade un nuevo usuario a la lista de usuarios y actualiza el archivo JSON de usuarios.

        Este método toma un objeto Usuario como parámetro y lo añade a la lista interna de usuarios de la clase.
        Tras añadir el nuevo usuario, el método también invoca a otro método (como `guardar_usuarios`) para actualizar
        el archivo JSON correspondiente, asegurando que los cambios se reflejen de manera persistente en el almacenamiento.

        Parámetros:
        usuario (Usuario): Un objeto Usuario que representa al nuevo usuario que se desea añadir a la lista.

        Devuelve:
        Este método no devuelve un valor, es un procedimiento.

        Ejemplo:
        >>> gestor = GestorUsuarios("data/usuarios.json")
        >>> nuevo_usuario = Usuario(nombre="Ana", edad=25, email="ana@example.com")
        >>> gestor.anadir_usuario(nuevo_usuario)
        # El usuario 'Ana' se añade a la lista de usuarios y se actualiza el archivo 'usuarios.json'.
        """
        self.usuarios.append(usuario)
        self.guardar_usuarios()

    def obtener_usuario(self, nombre_usuario):
        """
        Busca y devuelve un objeto Usuario basado en el nombre de usuario proporcionado.

        Este método recorre la lista interna de usuarios y compara el nombre de cada usuario
        con el nombre de usuario proporcionado como parámetro. Si encuentra un usuario con un
        nombre que coincide, devuelve ese objeto Usuario. Si no se encuentra ningún usuario
        con el nombre proporcionado, el método devuelve None.

        Este enfoque de búsqueda es sensible a mayúsculas y minúsculas, lo que significa que
        la búsqueda de "usuario" y "Usuario" dará resultados diferentes.

        Parámetros:
        nombre_usuario (str): El nombre del usuario que se desea buscar en la lista de usuarios.

        Retorna:
        Usuario: El objeto Usuario que coincide con el nombre proporcionado. Si no se encuentra
                 un usuario con ese nombre, se devuelve None.

        Ejemplo:
        >>> gestor = GestorUsuarios("data/usuarios.json")
        >>> gestor.obtener_usuario("Ana")
        # Devuelve el objeto Usuario para 'Ana' si existe, de lo contrario None.

        Consideraciones:
        - La búsqueda es sensible a mayúsculas y minúsculas, lo que debe tenerse en cuenta al
          proporcionar el parámetro de nombre de usuario.
        - Este método no modifica el estado de la lista de usuarios ni interactúa con el archivo JSON.
        """
        for usuario in self.usuarios:
            if usuario.nombre == nombre_usuario:
                return usuario
        return None

    def eliminar_usuario(self, nombre_usuario):
        """
        Elimina un usuario de la lista de usuarios basado en el nombre y actualiza el archivo JSON.

        Este método busca en la lista interna de usuarios y elimina cualquier usuario cuyo nombre coincida
        con el nombre de usuario proporcionado. Utiliza la comprensión de listas para crear una nueva lista
        que solo contiene aquellos usuarios cuyos nombres no coinciden con el nombre dado. Después de actualizar
        la lista de usuarios, invoca al método `guardar_usuarios` para asegurar que los cambios se reflejen
        en el archivo JSON de almacenamiento permanente.

        Es importante tener en cuenta que este método elimina todos los usuarios que coincidan con el nombre
        proporcionado. Si hay múltiples usuarios con el mismo nombre, todos serán eliminados.

        Parámetros:
        nombre_usuario (str): El nombre del usuario a eliminar de la lista de usuarios.

        Efectos Secundarios:
        - Modifica la lista interna de usuarios, eliminando los que coinciden con el nombre proporcionado.
        - Actualiza el archivo JSON de usuarios para reflejar la eliminación.

        Ejemplo:
        >>> gestor = GestorUsuarios("data/usuarios.json")
        >>> gestor.eliminar_usuario("Ana")
        # Esto eliminará a 'Ana' de la lista de usuarios y actualizará 'usuarios.json'.

        Consideraciones:
        - Si no hay ningún usuario con el nombre proporcionado, la lista de usuarios permanecerá sin cambios.
        - Este método no retorna un valor. Su propósito es modificar el estado interno y el archivo de almacenamiento.
        - La búsqueda y eliminación son sensibles a mayúsculas y minúsculas.
        """
        self.usuarios = [usuario for usuario in self.usuarios if usuario.nombre != nombre_usuario]
        self.guardar_usuarios()
