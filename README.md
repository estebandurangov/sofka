# Tutorial 

## Instalación

- Abra una Terminal de comandos y clone el proyecto usando git clone https://github.com/estebandurangov/sofka.git
- usamos cd sofka para abrir la carpeta de nuestro proyecto
- instalamos las dependencias usando: pip install -r requirements.txt
- ejecutamos nuestro proyecto usando: python manage.py runserver
- en la consola nos muestra en que puerto se ejecuto nuestra app, generalmente es (http://127.0.0.1:8000/)
- abrimos el proyecto en nuestro navegador.

## Instrucciones de Uso

### Jugar
- En la pagina de inicio aparecerá un Formulario donde el usuario ingresa su nombre y al dar clic en iniciar puede jugar

### Configurar Juego
para administrar nuestro juego es necesario seguir la ruta http://localhost:8000/juego/configurar/

en la pagina de configuración tenemos 3 secciones:
- Administrar las preguntas existente, desde aquí podemos ver nuestras preguntas y se agregaron botones para eliminar o editar las preguntas y sus respectivas opciones.
- agregar nuevas preguntas.
- ver un listado de los jugadores que han participado de la competencia, estos estarán ordenados de acuerdo a su puntaje.

## Descripción de la App
