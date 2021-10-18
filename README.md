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
haciendo uso de Django se crea una aplicación que se encarga de la gestion del Juego, para ver la logica del programa ingrese en la carpeta https://github.com/estebandurangov/sofka/tree/main/juego

### Lenguaje utilizado
Para el desarrollo del proyecto se realizó una aplicación web usando el Framework Django para el lenguaje de programación python.

### Persistencia de datos o guardado de históricos.
Se hace uso de la base de datos Sqllite3 que Django implementa por defecto, está base de datos se usa para guardar las preguntas de la aplicación y los puntajes obtenidos por los jugadores.

Para guardar la información temporal de la partida de los jugadores se utiliza las sessiones de Django, con estas lo que hacemos es incrementar el puntaje acumulado de los jugadores de forma local y solo se enviará esta información a la base de datos cuando se termine el juego.

### Manejos de listas o colecciones y ciclos de control adecuados
se usan en diferentes partes del programa, tanto en las plantillas como en la logica del backend.

### Modelo del programa
Para la construcción del modelo simplemente se utilizó la logica una categoria tiene varias preguntas y una pregunta tiene varias respuestas,
con esto y las facilidades que nos brinda Django se construyó el modelo. esto se puede ver plasmado en la Carpeta: juego/models.py (https://github.com/estebandurangov/sofka/blob/main/juego/models.py)
