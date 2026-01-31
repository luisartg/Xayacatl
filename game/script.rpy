# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:

#-----specific options----------------

# Set default transition for show/hide
define _scene_show_hide_transition = Dissolve(0.5)

#---------images-----------------------------------------
image i_player serious = At('lemuel serious', sprite_highlight('player'))
image i_player wary = At('lemuel wary', sprite_highlight('player'))
image i_player relax = At('lemuel relax', sprite_highlight('player'))
image i_player happy = At('lemuel happy', sprite_highlight('player'))
image i_player jumpy = At('lemuel jumpy', sprite_highlight('player'))
image i_player angry = At('lemuel angry', sprite_highlight('player'))
image i_player think = At('lemuel think', sprite_highlight('player'))

image i_camp worry = At('camp worry', sprite_highlight('campesino'))
image i_camp neutral = At('camp neutral', sprite_highlight('campesino'))
image i_camp help = At('camp help', sprite_highlight('campesino'))

image i_maria happy = At('maria happy', sprite_highlight('maria'))

image i_kid happy = At('kid happy', sprite_highlight('kid'))
image i_kid scared = At('kid scared', sprite_highlight('kid'))

image i_cha_old neutral = At('cha1 neutral', sprite_highlight('cha_old'))

image i_cha_tam neutral = At('cha2 neutral', sprite_highlight('cha_tam'))

image i_cha_hunt neutral = At('cha3 neutral', sprite_highlight('cha_hunt'))

image i_dev neutral = At('dem neutral', sprite_highlight('devil'))
image i_dev mad = At('dem mad', sprite_highlight('devil'))




#--------------- characters----------------------
define player_name = "Viajero"
define campesino_name = "Campesino"
define kid_name = "Niño"
define devil_name = "Voz"

define p = Character("[player_name]", image='i_player', callback=name_callback, cb_name='player')
define c = Character("[campesino_name]", image='i_camp', callback=name_callback, cb_name='campesino')
define m = Character("Doña María", image='i_maria', callback=name_callback, cb_name='maria')
define n = Character("[kid_name]", image='i_kid', callback=name_callback, cb_name='kid')
define x1 = Character("Granjero Anciano", image='i_cha_old', callback=name_callback, cb_name='cha_old')
define x2 = Character("Tamborilero", image='i_cha_tam', callback=name_callback, cb_name='cha_tam')
define x3 = Character("Cazador", image='i_cha_hunt', callback=name_callback, cb_name='cha_hunt')
define z = Character("Izel", image='i_izel', callback=name_callback, cb_name='izel')
define d = Character("[devil_name]", image='i_dev', callback=name_callback, cb_name='devil')

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
    jump scene5

label story_end:

    return
