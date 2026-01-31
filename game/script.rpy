# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:

image i_player serious = At('lemuel serious', sprite_highlight('player'))

image i_camp worry = At('camp worry', sprite_highlight('campesino'))
image i_camp neutral = At('camp neutral', sprite_highlight('campesino'))
image i_camp help = At('camp help', sprite_highlight('campesino'))

define player_name = "Viajero"
define campesino_name = "Campesino"
define kid_name = "Niño"
define devil_name = "Voz"

define p = Character("[player_name]", image='i_player', callback=name_callback, cb_name='player')
define c = Character("[campesino_name]", image='i_camp', callback=name_callback, cb_name='campesino')
define m = Character("Doña María")
define n = Character("[kid_name]")
define x1 = Character("Granjero Anciano")
define x2 = Character("Tamborilero")
define x3 = Character("Cazador")
define z = Character("Izel")
define d = Character("[devil_name]")

#----------------flags------------------------
default x1_help = False
default x2_help = False
default x3_help = False
default xoco_count = 0
default silver_count = 0

#----------------bright-----------------------
# default u_diag = matrixcolor BrightnessMatrix(-0.5) 
# default a_diag = matrixcolor BrightnessMatrix(0) 


# El juego comienza aquí.

label start:

    # Muestra una imagen de fondo: Aquí se usa un marcador de posición por
    # defecto. Es posible añadir un archivo en el directorio 'images' con el
    # nombre "bg room.png" or "bg room.jpg" para que se muestre aquí.

    scene bg black

    # Muestra un personaje: Se usa un marcador de posición. Es posible
    # reemplazarlo añadiendo un archivo llamado "eileen happy.png" al directorio
    # 'images'.

    #show eileen happy

    # Presenta las líneas del diálogo.

    #e "Has creado un nuevo juego Ren'Py."

    #e "Añade una historia, imágenes y música, ¡y puedes presentarlo al mundo!"

    # Finaliza el juego:
    jump scene1

label story_end:

    return
