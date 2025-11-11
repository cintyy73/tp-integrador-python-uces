"""
Módulo de gestión de datos de estudiantes
==========================================

Este módulo maneja la persistencia de datos de estudiantes en formato JSON.
Proporciona funciones para cargar y guardar la lista de estudiantes,
permitiendo que los datos persistan entre ejecuciones del programa.

Estructuras de datos:
- Lista de diccionarios, donde cada diccionario representa un estudiante
- Cada estudiante tiene: id, name, surname, email, password, course_id, cases
"""

import json
import os

# Ruta al archivo JSON donde se almacenan los estudiantes
# __file__ es la ruta de este archivo, dirname obtiene su directorio
STUDENTS_FILE = os.path.join(os.path.dirname(__file__), 'students.json')


def load_students():
    """
    Carga la lista de estudiantes desde el archivo JSON.
    
    Si el archivo existe, lo lee y retorna la lista de estudiantes.
    Si no existe, retorna una lista vacía.
    
    Retorna:
        list: Lista de diccionarios con datos de estudiantes
    """
    # Verificar si el archivo existe
    if os.path.exists(STUDENTS_FILE):
        # Abrir el archivo en modo lectura con codificación UTF-8
        with open(STUDENTS_FILE, 'r', encoding='utf-8') as f:
            # json.load() convierte el contenido JSON a estructuras Python
            return json.load(f)
    # Si no existe el archivo, retornar lista vacía
    return []


def save_students(students_list):
    """
    Guarda la lista de estudiantes en el archivo JSON.
    
    Parámetros:
        students_list (list): Lista de diccionarios con datos de estudiantes
    
    Retorna:
        None
    
    Nota:
        - indent=4: formatea el JSON con sangría de 4 espacios
        - ensure_ascii=False: permite caracteres especiales (tildes, ñ, etc.)
    """
    # Abrir archivo en modo escritura, si no existe lo crea
    with open(STUDENTS_FILE, 'w', encoding='utf-8') as f:
        # json.dump() convierte estructuras Python a formato JSON
        json.dump(students_list, f, indent=4, ensure_ascii=False)


# Variable global: lista de estudiantes cargada al iniciar el módulo
# Esta lista es compartida por todos los módulos que importen students
students = load_students()
