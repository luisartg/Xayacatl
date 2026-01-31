label scene5:
    

    """
    La oscuridad ya cae sobre los montes y la llanura de Ixtlahuacán. 
    
    Mis ojos ya casi no pueden ver más que pequeños detalles alumbrados a la cercanía de mi lámpara de aceite, y al fondo solo observo muchas figuras oscuras y sombras creadas por la abundante vegetación a lo largo del camino. 
    
    Aparte de algunos troncos caídos en medio de esta vía selvática, la senda no es tan difícil de transitar.
    
    Sin embargo, no puedo evitar sentirme un poco cohibido; 
    Como si una sombra fría yaciera siempre en mi espalda. 
    Como si una neblina muy espesa estuviera siempre detrás de mí. 
    
    Pero cada vez que volteo, solo hay oscuridad profunda.

    Sigo avanzando cada vez más rápido, con una creciente duda de si habré desviado en algún momento de letargo el camino señalado.
    
    Pero pronto mis dudas internas comienzan a disiparse cuando escucho un sonido ajeno a la floresta.

    \"Pum\"

    \"Pum Pum\"

    \"Pum ... Pum\"

    Es inconfundible. 
    
    Es el sonido de un tambor. 
    
    Olvidando todos las dudas que me aquejaban, como si una esperanza sonora me envolviera, sigo el camino con firmeza y comienzo a divisar una luz al fondo. 

    Se trata de otra pequeña cabaña y una fogata encendida.
    
    La fogata truena y cruje, y su calor me llena de paz y tranquilidad que juraba me habían abandonado en el trayecto a este lugar...
    
    Y cuando mis ojos se ajustan a la luz de la fogata, que al principio me deslumbraba por el cambio de iluminación, alcanzo a ver detrás de ella a un hombre grande, muy grande.
    
    Ancho y risueño, con un tambor apoyado en su gran barriga.

    \"Pum...\"

    Nos quedamos en silencio por solo unos instantes.
    
    Me armo de valor para pronunciar mis palabras.
    """

    show i_player wary at left
    p "¡Buenas tardes!"

    show i_cha_tam neutral at right
    x2 """
    ¡Noches ya! 
    Ji, ji, ji. 
    Es la mejor hora para las fiestas. 
    
    Aunque a decir verdad, cualquier hora para mi es hora de fiesta. Ji, ji, ji.
    
    {i}¡Y justamente ha llegado en el momento de festejar en grande!{/i}
    
    Nuestra Madre Tierra merece siempre una celebración {i}¿no cree?{/i}
    """

    "Miro alrededor y observo que no hay nada preparado para alguna celebración."

    show i_player serious
    p "Disculpe mi atrevimiento, pero no veo mucha decoración, ni los ritos acostumbrados de las fiestas."

    x2 "¡Oh!"

    "Puedo notar tristeza en su quejido."

    x2 """
    ¡Es por mi tambor!

    ¡No está afinado! 
    
    Y por más que he intentado, no logro ajustarlo bien.
    
    Cuando quiero que haga {i}\"Rat\"{/i} suena {i}\"Blof\"{/i} y luego lo toco para que haga {i}\"Pam\"{/i} y solo sale {i}\"Pum\"{/i}. 
    
    No me hallo. 

    Tal vez si alguien pudiera ayudarme, terminaría más rápido para comenzar el jolgorio...
    """
    show i_player wary
    p "Ya veo… Ehm.. Escuche, se han robado un niño en Ixtlahuacán."

    x2 "..."
    
    p """
    Acabo de recordar que me dijeron que cuando vieron a alguien llevarse al niño, se escuchaban sonidos como de tambor. 
    
    ¿{i}Usted{/i} no habrá estado ahí cerca cuando se lo llevaron? 
    
    Tal vez vió algo.
    """

    x2 "Tal vez… Pero es tan difícil recordar, ¡y siempre me siento mal si mi tambor no suena bien!"

    menu:
        "Ayudar al Músico":
            jump help_music_man
        "Seguir la búsqueda":
            jump no_help_music_man



label help_music_man:
    $ x2_help = True

    show i_player think
    p """
    {i}*Suspiro*{/i} 
    
    Está bien, le ayudo entonces.
    """
    show i_player relax

    x2 "Ji, ji, ji! Muchas gracias, buen amigo! Mire, usted sostenga firme esta parte y así…"

    hide i_player
    hide i_cha_tam
    #ruidos de herramientas
    """
    Durante un rato, ayudé a ese enorme tamborilero. 
    
    Ajustamos su tambor y probamos el sonido hasta que los tronidos y retumbos comenzaron a ser fuertes, claros, y profundos. 
    
    Entonces ese gran ermitaño se levantó, como si su vasto tamaño fuera una mentira, y comenzó a brincar y danzar tocando su tambor con alegría. 
    
    Los sonidos me envolvían y un deseo profundo me llenó el alma; 
    comencé también a danzar. 
    
    Danzamos alrededor de la fogata y los tronidos del tambor pronto me parecieron tan fuertes como el resonar de un trueno. 
    
    Me sentía ágil y ligero, y los dolores del viaje y de la larga caminata eran cosa del pasado. 
    
    En ese momento me encontraba celebrando con {i}algo más grande que el tamborilero y yo{/i}.

    No se cuanto tiempo pasó, pero cuando terminamos sentía el calor interno de mi cuerpo, y mi corazón resonando y respondiendo al canto de la tierra.

    Entonces abrí los ojos y ví que el tamborilero extendía su mano hacia mí para entregarme algo.
    """

    show i_player relax at left
    show i_cha_tam neutral at right
    x2 "Tome esto, buen hombre."

    $ xoco_count += 1

    "Abro la palma de mi mano y recibo un fruto de Xocohuiztle."

    x2 """
    Has celebrado con la Madre Tierra y su bendición cae sobre tí, como la lluvia cae sobre las plantas sedientas. 
    
    {i}Pero recuerda mantenerte en el buen camino.{/i}

    El niño no está aquí, pero mi hermano del Este, {i}el Cazador{/i}, seguramente podrá decirte dónde está. Toma esta vereda, y pronto llegarás con él.
    """

    hide i_cha_tam

    "Comencé entonces a dirigirle hacia el nuevo camino, cuando escucho la voz del tamborilero atrás de mi."

    show i_player serious
    x2 """
    Recuerda [player_name]... 
    
    Los problemas siempre existirán,
    
    pero solo debes recordar danzar al ritmo de la vida.
    """

    show i_player think
    p " ...Entiendo. Debo irme entonces. Adiós."

    hide i_player
    jump scene6



label no_help_music_man:

    show i_player angry
    p """
    ¡Escuche, hay un niño robado y perdemos el tiempo!
    
    ¡Es obvio que usted oculta algo!
    
    Si no me dice donde está, iré por el pueblo y los traeré aquí mismo
    
    ¡y verá la fiesta que se va a armar entonces!
    """
    
    "El tamborilero suspira tristemente."
    
    x2 """
    Hay gran fuerza dentro de tí, como la del sonido de mi tambor. 
    
    Pero me temo que la fuerza sin ritmo solo es ruido.

    ...

    Toma la vereda al este. Si la sigues, pronto encontrarás a mi hermano {i}el Cazador{/i}. El podrá guiarte para encontrar al niño.
    """
    
    show i_player think
    p "Ya veo. Le agradezco entonces. Me retiro ya."

    hide i_player
    hide i_cha_tam
    jump scene6
