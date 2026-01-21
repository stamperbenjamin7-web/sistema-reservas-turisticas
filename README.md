# Sistema de Reservas Turísticas

Este repositorio contiene una aplicación de ejemplo para gestionar reservas turísticas en una isla (Aruba).  
Se divide en **dos partes**:  

---

## Parte 1: Aplicación Web con Django

- Framework: **Django**
- Funcionalidad:
  - Modelo `Reserva` para registrar las reservas.
  - Modelo `ActividadTuristica` para manejar las actividades.
  - Panel de administración de Django (`/admin`) para gestionar reservas y actividades.
  - Templates y vistas básicas para mostrar la información.
- Base de datos: SQLite (por defecto en Django)
- Cómo ejecutar:
  1. Instalar dependencias:
     ```bash
     pip install django
     ```
  2. Entrar a la carpeta del proyecto:
     ```bash
     cd primer_parte/proyecto
     ```
  3. Ejecutar migraciones:
     ```bash
     python manage.py makemigrations
     python manage.py migrate
     ```
  4. Crear superusuario para acceder al admin:
     ```bash
     python manage.py createsuperuser
     ```
  5. Iniciar servidor de desarrollo:
     ```bash
     python manage.py runserver
     ```
  6. Acceder a la aplicación en: [http://127.0.0.1:8000](http://127.0.0.1:8000)  
     Acceder al panel admin en: [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

---

## Parte 2: Interfaz de Administración con PyQt6

- Librería: **PyQt6**
- Funcionalidad:
  - Interfaz gráfica para gestionar reservas.
  - Incluye ventanas, botones, y eventos para agregar/modificar/eliminar reservas.
  - Conexión con la estructura de datos de la Parte 1 (simulada).
- Cómo ejecutar:
  1. Instalar PyQt6:
     ```bash
     pip install PyQt6
     ```
  2. Ejecutar la aplicación:
     ```bash
     python segunda_parte/app.py
     ```
  3. Se abrirá la ventana principal con las opciones para administrar reservas y actividades.

---

## Estructura del repositorio

