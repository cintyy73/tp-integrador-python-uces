# Sistema de Mesa de Ayuda - UCES

Sistema de gestión de casos para estudiantes. Este repositorio contiene un prototipo de Mesa de Ayuda donde los estudiantes pueden registrarse, iniciar sesión, crear casos y consultar el estado de sus solicitudes.

## 📋 Descripción

El programa ofrece:
- Registro e inicio de sesión de estudiantes
- Creación y seguimiento de casos por alumno y por curso
- Persistencia simple usando archivos JSON (en `src/data/`)

## 🚀 Características principales

- Registro de estudiantes
- Login con reintentos y validación
- Menú de gestión de casos: ver, crear y ver detalle
- Guardado de datos en JSON

## 📁 Estructura del proyecto (real)

```
paez-cintia-tp-integrador-uces/
├── src/
│   ├── auth/
│   │   ├── login.py          # Lógica de inicio de sesión
│   │   └── register.py       # Lógica de registro
│   │
│   ├── data/
│   │   ├── cases.json        # Datos de ejemplo de casos (JSON)
│   │   ├── students.json     # Datos de ejemplo de estudiantes (JSON)
│   │   └── students.py       # Carga/guardado de estudiantes
│   │
│   ├── menues/
│   │   ├── main_menu.py      # Menú principal
│   │   └── cases_menu.py     # Menú para gestión de casos
│   │
│   ├── utils/
│   │   └── functions.py      # Utilidades (clear_screen, print_header, pause)
│   │
│   └── main.py               # Punto de entrada del programa
│
└── README.md
```

## 🔧 Requisitos

- Python 3.10 o superior

## 💻 Cómo ejecutar

Desde la raíz del proyecto (recomendado):

```bash
python src/main.py
```

O desde dentro de la carpeta `src`:

```bash
cd src
python main.py
```

## 📖 Resumen de uso

- Al ejecutar verás el menú principal con opciones para iniciar sesión, registrarte o salir.
- Después del login, accederás al menú de casos para ver, crear o examinar casos.

## 🧪 Usuarios de prueba (opcionales)

- Puedes crear usuarios con el comando de registro dentro de la aplicación. No hay cuentas preconfiguradas obligatorias en el repo.

## 🔐 Seguridad y validaciones

- Validación de campos obligatorios en el registro
- Evita emails duplicados
- Reintentos limitados para login

## 🛠️ Tecnologías

- Python 3.10+ (uso de match-case en menús)
- Módulo datetime para fechas

## 🙏 Agradecimientos

Agradecimiento especial al **Profesor Rolando Gareca** por su guía, enseñanza y apoyo durante el transcurso de esat cursada fundamental para el desarrollo de este trabajo integrador en la materia Programación I de la Tecnicatura en Programación de Sistemas.

## 👥 Autor

**Cintia Paez** — Trabajo Integrador - UCES

---
