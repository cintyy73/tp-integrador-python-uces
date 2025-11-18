from auth.login import login
from auth.register import register
import os
import sys
from utils.functions import print_header, clear_screen, pause

# Agregar el directorio raíz al path si se ejecuta directamente (consultar aRolando)
if __name__ == "__main__":
    sys.path.insert(
        0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
    )


def main_menu():
    """
    Muestra el menú principal y gestiona la navegación inicial.
    Retorna True para continuar en el bucle principal (de init),
    o False para salir de la aplicación.
    """
    while True:
        clear_screen()

        print_header("¡Bienvenido/a a UCES!")

        print(
            """
            Desde nuestra Mesa de Ayuda podrás gestionar las solicitudes que necesites.

            Por favor, seleccione una opción:
            1. Iniciar Sesión   
            2. Registrarme  
            0. Salir
            """
        )

        option = input("\nIngrese su opción: ").strip()

        match option:
            case "1":
                login()
            case "2":
                register()
            case "0":
                print("\nGracias por utilizar la Mesa de Ayuda. ¡Hasta luego!")
                return False
            case _:
                print("\nOpción no válida. Por favor, intente nuevamente.")
                pause()
#TODO agregar rol docente para gestionar casos 