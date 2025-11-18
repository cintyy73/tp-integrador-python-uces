from datetime import datetime
from data.students import save_students, students
from utils.functions import pause, print_separator, print_success



def cases_menu(student_data, course_id):
    """Menú de gestión de casos para estudiantes."""
    while True:
        print(f"""
    === Menú de Casos - Curso {course_id} ===
    Alumno/a: {student_data.get('name')} {student_data.get('surname')}
    
    1. Ver mis casos
    2. Crear nuevo caso
    3. Ver detalle de un caso
    0. Cerrar sesión
        """)
        
        option = input("Ingrese una opción: ")
        
        match option:
            case "1":
                show_cases(student_data, course_id)
            case "2":
                create_case(student_data, course_id)
            case "3":
                view_case_detail(student_data)
            case "0":
                print("\n¡Hasta pronto!")
                return
            case _:
                print("\nOpción no válida. Intente nuevamente.")

#TODO agregar opción de volver al menu anterior o al menu principal o salir en ver casos y detalles de un caso


def show_cases(student_data, course_id):
    """Muestra todos los casos del estudiante ordenados por fecha."""
    # Obtener la lista de casos del diccionario student_data
    # .get("cases", []) retorna [] si la clave no existe (valor por defecto)
    student_cases = student_data.get("cases", [])
    
    if not student_cases:
        print("\nNo tienes casos registrados.")
        return
    #TODO ver de agregar opciones de ordenar en asc y desc REVISAR SORT!
    # Ordenar lista de diccionarios usando sorted()
    # key=lambda x: x['created_at'] indica que ordene por la fecha
    # lambda es una función anónima que recibe x (cada caso) y retorna x['created_at']
    # reverse=True ordena de mayor a menor (más reciente primero)
    sorted_cases = sorted(student_cases, key=lambda x: x['created_at'], reverse=True)
    
    print(f"\n{'='*50}")
    print("Tus Casos (ordenados por fecha)")
    print(f"{'='*50}")
    
    # Iterar sobre cada diccionario en la lista sorted_cases
    for case in sorted_cases:
        # case es un diccionario, accedemos a sus claves con []
        print(f"ID: {case['id']}")
        print(f"Motivo: {case['reason']}")
        print(f"Estado: {case['status']}")
        print(f"Fecha: {case['created_at']}")
        print_separator()


def create_case(student_data, course_id):
    """Crea un nuevo caso para el estudiante."""
    print("\n=== Crear Nuevo Caso ===")
    
    reason = input("Motivo del caso: ")
    description = input("Descripción detallada: ")
    
    if not reason.strip() or not description.strip():
        print("\nEl motivo y la descripción son obligatorios.")
        pause()
        return
    
    # Generar ID único basado en los casos del estudiante
    student_cases = student_data.get("cases", [])
    # len() cuenta cuántos elementos tiene la lista (acumulador)
    case_number = len(student_cases) + 1
    # f-string para formatear: {case_number:03d} → número con 3 dígitos (001, 002, etc.)
    case_id = f"CASO-{student_data['id']}-{case_number:03d}"
    
    # Crear un nuevo diccionario para el caso
    new_case = {
        "id": case_id,
        "reason": reason,
        "description": description,
        "response": "",
        "status": "pending",
        "created_at": datetime.now().strftime("%Y-%m-%d")
    }
    
    # Agregar el diccionario new_case a la lista de casos
    # .append() agrega un elemento al final de la lista
    student_data["cases"].append(new_case)
    
    # Buscar y actualizar el estudiante en la lista global
    # Recorrer todos los diccionarios en la lista students
    for student in students:
        # Comparar el id de cada estudiante con el id actual
        if student["id"] == student_data["id"]:
            student["cases"].append(new_case)
            break  # Salir del for cuando encontramos el estudiante
    
    # Guardar los cambios en el archivo JSON
    save_students(students)
    
    print_success("¡Caso creado exitosamente!")
    print(f"ID del caso: {case_id}")
    print("Estado: pending")
    print_success("El caso ha sido guardado permanentemente.")
    input("\nPresione Enter para continuar...")


def view_case_detail(student_data):
    """Muestra el detalle completo de un caso específico."""
    # Obtener la lista de casos del diccionario student_data
    student_cases = student_data.get("cases", [])
    
    if not student_cases:
        print(f"\nNo tienes casos registrados.")
        return
    
    case_id = input("\nIngrese el ID del caso: ")
    
    # Buscar un caso específico en la lista
    # next() + generator expression para encontrar el primer match
    # c["id"] accede a la clave "id" de cada diccionario caso
    # Si no encuentra ninguno, retorna None
    case = next((c for c in student_cases if c["id"] == case_id), None) 
    
    if not case:
        print(f"\nNo se encontró el caso con ID: {case_id}")
        return
    
    # Mostrar todos los datos del diccionario case
    print(f"\n{'='*50}")
    print(f"Detalle del Caso {case['id']}")
    print(f"{'='*50}")
    print(f"\nMotivo: {case['reason']}")
    print(f"Estado: {case['status']}")
    print(f"Fecha de creación: {case['created_at']}")
    print(f"\nDescripción:")
    print(f"{case['description']}")
    
    # .get('response') es más seguro que ['response']
    # Si la clave no existe, retorna None en vez de error
    if case.get('response'):
        print(f"\n--- Respuesta del Docente ---")
        print(f"{case['response']}")
    else:
        print(f"\nEste caso aún no tiene respuesta.")
    
    print(f"{'='*50}")
