from data.students import students
from menues.cases_menu import cases_menu
from utils.functions import print_header, clear_screen, pause, confirm_action, print_error

#TODO  limpiar course_id
def login():
    clear_screen()
    print_header("Inicio de Sesión")

    while True:
        email = input("Usuario (email): ").strip()

        # Buscar estudiante por email en la lista
        # u.get("email") accede al valor de la clave "email" de cada diccionario
        # next() retorna el primer elemento que cumple la condición, o None si no encuentra
        matched = next((u for u in students if u.get("email") == email), None)

        if not matched:
            print_error(f"El usuario '{email}' no existe en el sistema.")
            if not confirm_action("¿Desea intentar nuevamente? (s/n): "):
                print("\nLogin cancelado. Volviendo al menú principal...")
                pause()
                return False  # Vuelve al menú principal
        else:
            break  # Usuario encontrado, salir del bucle de email

    intentos_maximos = 3
    password_correcta = False  

    for i in range(intentos_maximos):
        # Mostramos el número de intentos
        print(f"\n--- (Intento {i + 1} de {intentos_maximos}) ---")

        password = input("Contraseña: ")

        # matched.get("password") obtiene el valor de la clave "password" del diccionario
        if matched.get("password") == password:
            password_correcta = True
            break
        else:
            print("Contraseña incorrecta.")
            # Acumulador: calcula cuántos intentos quedan
            intentos_restantes = intentos_maximos - (i + 1)
            if intentos_restantes > 0:
                print(f"Le quedan {intentos_restantes} intento(s).")

    if not password_correcta:
        clear_screen()
        print_header("ACCESO DENEGADO")
        print("\nHa superado el número máximo de intentos.")
        print("Volviendo al menú principal...")
        pause()
        return False  # Vuelve al menú principal

    # Verificar si el estudiante tiene cursos asignados
    # "course_id" in matched chequea si existe la clave en el diccionario
    if "course_id" in matched:
        while True:
            course_raw = input("\nID del curso (obligatorio): ").strip()

            if not course_raw:
                print_error("Debe ingresar un ID de curso para continuar.")
                if not confirm_action("¿Desea intentar nuevamente? (s/n): "):
                    return False
                continue

            if not course_raw.isdigit():
                print_error("ID de curso inválido. Debe ser un número.")
                if not confirm_action("¿Desea intentar nuevamente? (s/n): "):
                    return False
                continue

            course_id = int(course_raw)

            # matched.get("course_id", []) obtiene la lista de cursos
            # Si no existe la clave, retorna [] (lista vacía) como valor por defecto
            # course_id not in [...] verifica si el id NO está en la lista
            if course_id not in matched.get("course_id", []):
                print_error(f"El usuario no está registrado en el curso {course_id}.")
                print(f"Cursos disponibles: {matched.get('course_id', [])}")
                if not confirm_action("¿Desea intentar nuevamente? (s/n): "):
                    return False
                continue

            break
        clear_screen()
        print_header("Bienvenido/a")
        # Acceder a múltiples claves del diccionario matched
        print(f"\n¡Hola, {matched.get('name')} {matched.get('surname')}!")
        print(f"Curso seleccionado: {course_id}")
        input("\nPresione Enter para acceder al menú de casos...")

        cases_menu(matched, course_id)

    return True
