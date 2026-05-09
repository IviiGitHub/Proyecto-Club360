# 🏟️ Club 360 - Sistema de Gestión de Turnos

## ¡Bienvenidos al repositorio oficial de Club 360! Este proyecto está desarrollado por el equipo de Otomano Aiti utilizando Django. Nuestra meta es ofrecer una experiencia fluida para que los socios reserven sus actividades deportivas.
## 🚀 Guía de Inicio Rápido (Para el Equipo)

 Para que todos trabajemos en sintonía y evitemos conflictos de código, sigan estos pasos al unirse al proyecto:
## 1. Clonar el repositorio
```Bash
git clone https://github.com/tu-usuario/Club360.git
cd Club360
```

## 2. Configurar el entorno virtual
```Bash

python -m venv env
```
### En Windows:
```Bash
.\env\Scripts\activate
```
### En Mac/Linux:
```Bash
source env/bin/activate
```
## 3. Instalar dependencias
```Bash

pip install django qrcode pillow
```
## 4. Flujo de Trabajo (Git Flow)

Para mantener la estabilidad, usaremos tres niveles de ramas:
- main: Versión estable (Solo el encargado de la entrega mergea aquí).
  
- dev: Rama de integración. Aquí subimos nuestros avances para probarlos juntos.
    
- feature/tu-tarea: Tu rama personal. Creala desde dev con git checkout -b feature/nombre.

Antes de subir algo a dev:

- Hacé git pull origin dev en tu PC.

- Mergeá dev en tu rama (git merge dev) y resolvé conflictos si los hay.

- Subí tu rama y abrí un Pull Request en GitHub.

## 🧠 ¿Cómo funciona Django? El Modelo MVT

Si venís de otros lenguajes, quizás conozcas el MVC. Django usa MVT (Model-Template-View). Es como una cocina de un restaurante:
## 1. Model (El Depósito/Ingredientes) - models.py

Aquí definimos la estructura de nuestros datos. Es el único lugar donde hablamos con la base de datos SQLite.

    Ejemplo: El modelo Socio dice que cada persona tiene un nombre, un DNI y un estado (Activo/Suspendido).

## 2. View (El Chef) - views.py

Es el cerebro. La vista recibe el pedido del usuario, va al "Depósito" (Modelo) a buscar los ingredientes y decide cómo prepararlos.

    Ejemplo: La vista de reservas filtra los turnos de la disciplina elegida y chequea que no pasen los 30 días.

## 3. Template (El Plato Servido) - templates/*.html

Es lo que el usuario ve. Es HTML puro con algunas etiquetas especiales de Django ({% %}) que nos permiten mostrar los datos que el Chef (View) preparó.

    Ejemplo: La lista de cuadraditos con los horarios de Padel.

## 4. URL (El Menú/Mozo) - urls.py

Es el mapa que conecta lo que el usuario escribe en el navegador con la View correcta.

    Ejemplo: Si entran a /reservas/, el mozo sabe que debe llamar al Chef de la "Vista de Reservas".

⚠️ Reglas de Oro

- No suban la base de datos (db.sqlite3): Cada uno tiene la suya local para pruebas.

- Migraciones: Si tocan el models.py, avisen al grupo antes de subir los archivos de migrations/.
