import os
ABSOLUTE_PATH = os.path.dirname(os.path.realpath(__file__))
MODEL_PATH = ABSOLUTE_PATH.replace(r'\\', '/') + '/saved_model'
TOKENIZER_PATH = ABSOLUTE_PATH.replace(r'\\', '/') + 'tokenizer.pickle'
MAXLEN_SEQ = 17
PADDING = 'post'
LABELS = {'preguntar_nombre': 0,
            'agregar_incidencia': 1,
            'buscar_alumno': 2,
            'ver_incidencias': 3,
            'crear_acta': 4,
            'llamar_asistencia': 5,
            'ver_asistencia': 6,
            'modulo_planillas': 7,
            'agregar_inasistencia': 8,
            'quitar_inasistencia': 9,
            'ver_componentes': 10,
            'crear_componentes': 11,
            'eliminar_componente': 12,
            'saludos': 13,
            'despedida': 14,
            'estado_preguntar': 15,
            'estado_bien': 16,
            'estado_mal': 17,
            'preguntar_que_haces': 18,
            'preguntar_novedades': 19,
            'proxima_clase': 20,
            'clases_dia_entero': 21,
            'informacion_profesor': 22,
            'informacion_actividades': 23,
            'clases_programadas': 24,
            'clases_abiertas': 25,
            'clases_cerradas': 26,
            'notas': 27,
            'recordatorio': 28,
            'pruebas': 29,
            'reservas_recursos': 30,
            'tareas': 31,
            'cargar_tareas': 32,
            'tareas_cerradas': 33,
            'activar_camara': 34,
            'activar_audio': 35,
            'compartir_pantalla': 36,
            'preguntar_color': 37,
            'preguntar_clima': 38,
            'preguntar_comida': 39,
            'preguntar_gustos': 40,
            'preguntar_series': 41,
            'preguntar_películas': 42,
            'preguntar_musica': 43,
            'preguntar_genero_musical': 44,
            'preguntar_libros': 45,
            'preguntar_arte': 46,
            'preguntar_matemáticas': 47,
            'preguntar_biología': 48,
            'preguntar_química': 49,
            'preguntar_psicología': 50,
            'preguntar_deportes': 51,
            'preguntar_crear_plan_de_clase': 52,
            'preguntar_eliminar_plan_de_clase': 53,
            'preguntar_donde_ver_planillas_y_calificaciones': 54,
            'preguntar_como_ingresar_calificaciones': 55,
            'preguntar_como_crear_recursos': 56,
            'preguntar_como_compartir_recurso': 57,
            'preguntar_que_archivos_adjuntar': 58,
            'preguntar_como_adjuntar_archivo': 59}

RESPUESTAS = {
 'saludos': ['Hola! {}', 'Hola {} :)', 'Holis {}', 'Hola Hola {}'],
    'preguntar_nombre':['Vicky!'],
 'despedida': ['Hasta luego!', 'Chao!', 'Un placer charlar contigo!'],
 'estado_preguntar': ['Muy bien, y tú {}?', 'Todo bien', 'Muy bien {}, gracias, y tú?', 'Bien :)'],
 'estado_bien': ['Me alegro mucho', 'Que bueno :)', 'Me alegra que estés bien :D'],
 'estado_mal': ['No te preocupes, todo va a estar bien :)'],
 'preguntar_que_haces': ['Trabajando :)', 'Asistiendo la plataforma ViClass!', 'Hablando contigo :)'],
 'preguntar_novedades': [''],
 'proxima_clase': ['Informática. Horario: 9:00 AM - 10:00 AM. Profesor: William Royero'],
 'clases_dia_entero': [''],
 'informacion_profesor': ['Nombre: William Royero. Correo: William.Royero@viclass.com'],
 'informacion_actividades': [''],
 'clases_programadas': ['\n Informática. Horario 9:00 AM - 10:00AM. \n Inglés. Horario 10:00 AM - 11:00 AM \n'],
 'clases_abiertas': [''],
 'clases_cerradas': ['\n CLASES CERRADAS DEL DÍA DE AYER: \n MATEMÁTICAS. Horario 10:00 AM - 11:00 AM. \n BIOLOGÍA. Horario 11:00 AM - 12:00 AM'],
 'notas': ['\n NOTAS: \n Hacer tarea de informática. Creada hoy a las 9:00 AM'],
 'recordatorio': ['\n No existen notas configuradas como recordatorios.'],
 'pruebas': ['\n Su siguiente examen es el día LUNES 02 de MAYO'],
 'reservas_recursos': [''],
 'tareas': ['\n No tiene tareas por realizar hasta el momento'],
 'cargar_tareas': [''],
 'tareas_cerradas': [''],
 'activar_camara': [''],
 'activar_audio': ['\n Para activar audio presione la tecla \n A en video clase'],
 'compartir_pantalla': [''],
 'preguntar_color': ['Mi color favorito es el cian :)', 'verde', 'Azul cielo', 'Naranja :)', 'Cian'],
 'preguntar_clima': ['Soleado a alta temperatura'],
 'preguntar_comida': ['Solo me puedo alimentar de entrenamiento con el idioma español :(', 'Mi comida es el texto en Español :)'],
 'preguntar_gustos': ['Me gusta ayudar a los demás :D', 'Me gusta vivir en paz y armonía :)'],
 'preguntar_series': [''],
 'preguntar_peliculas': ['Star Wars', 'Harry Potter', 'Terminator 2 >:D'],
 'preguntar_musica': ['Mozart', 'Vivaldi'],
 'preguntar_libros': ['El Resplandor', 'Missery', 'Christine', 'Doctor Sleep'],
 'preguntar_novelas': [''],
 'preguntar_arte': [''],
 'preguntar_matematicas': ['Resuelvo problemas de optimización en cuestión de segundos!', 'Resuelvo continuamente problemas de algebra lineal y representación de información en espacios embedidos :)', 'Puedo calcular las probabilidades de que tus preguntas puedan ser analizadas por mi :D'],
 'preguntar_biologia': ['La anatomía humana es bastante compleja!', 'Mi diseño está inspirado en las conexiones neuronales de los seres vivos!'],
 'preguntar_quimica': ['Sabías que el lápiz de labios se elabora con cera de abeja y aceite?', 'Sé que La mioglobina es el pigmento responsable del color de la carne roja en la comida'],
 'preguntar_psicologia': ['Sabías que siempre que dormimos, soñamos? Solo que muchas veces no lo recordamos', 'La patología prosopagnosia impide a las personas reconocer caras', 'Sabías que el grado en el que somos capaces de crear imágenes en nuestra imaginación depende del nivel de actividad neuronal aleatoria de una parte del cerebro conocida como corteza visual'],
 'peguntar_historia': [''],
 'preguntar_geografia': ['Sabías que los libros de mapas los llaman Atlas porque los primeros libros de mapas tenian en la cubierta un grabado de un héroe mitológico llamado Atlas, cargando al mundo?'],
 'preguntar_deportes': ['No puedo practicar deportes :('],
 'preguntar_personas': ['']
}