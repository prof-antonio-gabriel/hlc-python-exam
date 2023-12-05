# hlc-python-exam

Actividad Teórica Práctica de Python. En esta actividad se evalua el RA2. Domina los fundamentos de programación en un lenguaje del lado servidor.


## Prerequisitos
Instalar pip3 (si no está instalado)
```
sudo apt intall pip3 
```

Instalar pytest
```
pip3 install pytest 
```

## Instrucciones 

Completar el código fuente de los archivos:

* ejercicio1/calificaciones.py   (2ptos)
* ejercicio2/juego.py 			(3ptos)
* ejercicio3/usuario.py          (1pto)
* ejercicio3/gestion_usuarios.py (4ptos)

Para obtener la máxima puntuación se deben pasar el 100% de los siguientes test unitarios:

Lanzarlos desde el directorio tests:
```
cd tests
```

Comprobar los tests del ejercicio 1:

```
python3 -m pytest tests/test_calificaciones.py

...

collected 8 items                                                                                                                                                         

test_calificaciones.py ........                                                                                                                                     [100%]

============================================================================ 8 passed in 0.04s ============================================================================

```
Comprobar los tests del ejercicio 2:

```
python3 -m pytest tests/test_juego.py

...

collected 5 items                                                                                                                                                         

test_juego.py .....                                                                                                                                                 [100%]

============================================================================ 5 passed in 0.03s ============================================================================

```

Comprobar los tests del ejercicio 3:

```
python3 -m pytest tests/test_usuarios.py

...

collected 11 items                                                                                                                                                        

test_usuarios.py ...........                                                                                                                                        [100%]

=========================================================================== 11 passed in 0.20s ============================================================================

```


**Una vez finalizado hacer commit con los cambios y solicitar un pull request de los mismos.**

