"""
Sistema de Mesa de Ayuda - UCES
================================
Trabajo Integrador - Programación I
Tecnicatura en Programación de Sistemas

Autor: Cintia Paez
Fecha: Noviembre 2025

Descripción:
Sistema completo de gestión de casos para estudiantes que permite:
- Registro e inicio de sesión de usuarios
- Creación y seguimiento de casos de ayuda
- Visualización de casos ordenados por fecha
- Persistencia de datos en formato JSON

Este es el archivo principal que ejecuta el programa.
"""

import sys
import os

# Agregar el directorio src al path para que funcionen los imports absolutos
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from menues.main_menu import main_menu


def init():
    """
    Función de inicialización del programa.
    Mantiene el programa ejecutándose hasta que el usuario decida salir.
    
    Retorna:
        None
    """
    # Bucle principal del programa
    while True:
        # Si main_menu retorna False, significa que el usuario quiere salir
        if not main_menu():
            break  # Salir del bucle y terminar el programa


# Punto de entrada del programa
# __name__ == "__main__" se ejecuta solo cuando se corre este archivo directamente
if __name__ == "__main__":
    init()
