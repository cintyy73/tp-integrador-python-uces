from data.students import students, save_students
from utils.functions import print_header, clear_screen, pause, print_success, print_error


def register():
    """Registra un nuevo estudiante en el sistema."""
    clear_screen()
    print_header("Registro de Estudiante")
    
    name = input("Nombre y apellido: ").strip()
    email = input("Email de usuario: ").strip()
    password = input("Contraseña: ").strip()

    # Validar que los campos no estén vacíos
    if not name or not email or not password:
        print_error("Todos los campos son obligatorios. Registro cancelado.")
        pause()
        return False

    # Verificar si el email ya existe
    # any() recorre la lista students
    # s["email"] accede a la clave "email" de cada diccionario
    # Retorna True si encuentra alguna coincidencia
    if any(s["email"] == email for s in students):
        print_error(f"El email '{email}' ya está registrado en el sistema.")
        pause()
        return False

    course_raw = input("ID del curso al que perteneces: ").strip()
    
    # Validar que course_raw contenga solo dígitos (números)
    # .isdigit() retorna True si todos los caracteres son 0-9
    if not course_raw.isdigit():
        print_error("ID de curso inválido. Debe ser un número.")
        pause()
        return False
    
    course_id = int(course_raw)

    new_student = {
        # Generar ID automático: toma el ID más alto y suma 1
        # s["id"] accede al id de cada estudiante en la lista
        # max() encuentra el valor más grande
        "id": max([s["id"] for s in students]) + 1 if students else 1,
        
        # name.split() divide el string por espacios en una lista
        # [0] toma el primer elemento (nombre)
        "name": name.split()[0] if name else "",
        
        # [1:] toma desde el segundo elemento en adelante (apellidos)
        # " ".join() une la lista con espacios
        "surname": " ".join(name.split()[1:]) if len(name.split()) > 1 else "",
        
        "email": email,
        "phone": "",
        "age": None,
        "password": password,
        
        # course_id se guarda como lista para permitir múltiples cursos
        "course_id": [course_id],
        
        # cases es una lista vacía que almacenará diccionarios de casos
        "cases": []
    }
    
    students.append(new_student)
    
    # Guardar los nuevso students en el archivo JSON
    save_students(students)
    
    # Verificación: mostrar que el estudiante fue agregado
    clear_screen()
    print_header("Registro Exitoso")
    print(f"\n¡Bienvenido/a, {name}!")
    print(f"Email: {email}")
    print(f"Curso: {course_id}")
    print(f"ID asignado: {new_student['id']}")
    print_success("Los datos han sido guardados permanentemente.")
    pause()
    return True
