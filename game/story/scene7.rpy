label scene7:

    """
    Sigo el sendero que se hace más y más espeso. 
    
    Según mis cálculos, estoy seguro que tendría que haber cruzado por el pueblo, y aún así sigo en esta zona densa de árboles tan variados que a veces no sé si estoy en un bosque o en una selva. 
    
    Tal vez me he perdido, pues ya no alcanzo a distinguir la vereda.

    Pero justo cuando empiezo a dudar, veo aparecer frente a mi un grupo de tejones.
    
    De cuerpo, cola y hocico largo, con un pelaje de color café oscuro pero con unas manchas blancas adornando el rostro y las orejas; 
    no puedo evitar pensar que se ven algo lindos.

    La manada de tejones se detiene y me miran fijamente. Después avanza rápidamente alejándose de mi, pero se detienen casi de inmediato y vuelven a mirarme fijamente. 
    
    Casi pareciera que quieren que los siga. Y precisamente eso hago. 

    Y así durante un tiempo, los tejones avanzan en grupo, deteniéndose cuando ven que me estoy quedando atrás. Lo que me reafirma que debo seguirlos. 

    Finalmente, veo a los tejones atravesar un matorral. 
    
    Con dificultad, me muevo a través de la vegetación y me encuentro en un pequeño claro. 
    
    Puedo ver las estrellas arriba de mi, hermosas y brillantes.

    Pero mi temporal asombro queda en el suelo cuando de las sombras uno de los matorrales se mueve, y de él se levanta el ermitaño cazador. 
    
    De no ser que se hubiera mostrado voluntariamente, jamás habría sabido que estaba ahí.

    Sentí un poco de estremecimiento a su figura. 
    
    No era muy grande, pero se veía agilidad en su cuerpo y una fuerza que ha resistido los elementos a los que pocos nos enfrentamos en estos tiempos.
    
    Realmente estaba frente a un cazador experimentado.
    """
    
    show i_player wary at left
    show i_cha_hunt neutral at right

    p "Buenas noches, disculpe… he venido por guía de sus hermanos, el {i}granjero anciano{/i} y el {i}alegre tamborilero{/i}. Supongo que sabrá que se robaron a un niño."

    x3 "Efectivamente."

    p "¿Sabe usted quién se lo robó? {i}¿Sabe dónde está el niño?{/i}"

    x3 "Yo lo sé, y a la vez no."

    show i_player angry

    p "¿A qué se refiere? ¿Qué clase de juego enfermo está jugando?"

    x3 "Yo y mis hermanos nos robamos al niño. Y lo escondimos en un sitio en el pueblo. Nadie podrá encontrarlo. Ni siquiera nosotros mismos."

    show i_player jumpy
    p "¡¿Qué?!"
    
    show i_player wary
    p "¿Así que siempre fueron ustedes?"

    """
    Sentí un vacío en mi corazón, ese vacío que surge cuando una verdad que escondía una traición sale a la luz. 
    
    Pero aún no era tiempo de derrumbarse.
    """
    
    p """
    Pero ¿por qué?... ¿Por qué dice que no lo pueden encontrar ustedes?
    
    ¿Cómo es que no saben dónde está ahora si ustedes mismos se lo llevaron?
    """

    x3 "Mi sabuesa, mi perra fiel… fue herida. Justo cuando escondimos al niño. La vida casi ha dejado su cuerpo."

    """
    Entonces vi a su sabuesa acostada de lado. Se notaba que respiraba con dificultad, parecía tener un gran arañazo en el cuello. 
    
    Muy probablemente iba a morir pronto.
    """

    x3 """
    Sin mi sabuesa, no puedo encontrar al niño nuevamente.
    
    ...

    Sin embargo... ahora que estás aquí...
    
    Sí... Sí.
    
    Puedo hacer un sacrificio... y un acto de fe.
    
    ¿Estarías dispuesto a ayudarme?
    """

    menu:
        "Obtener ayuda del Hombre de Negro":
            jump no_help_hunter
        "Ayudar al Cazador":
            jump help_hunter



label no_help_hunter: 
    
    show i_player think
    p "No..."

    show i_player angry
    p """
    ¡NO!
    
    No sé qué están haciendo. 
    
    Pero cometieron un error y robaron un niño.
    
    Yo sé quien sí puede ayudarme a encontrar al niño.
    
    Ahora entiendo por qué él les tenía tanto miedo.
    """
    hide i_player
    x3 "¿Que … nos tenía miedo? No me digas que.. ¡NO! ¡NO, ESPERA…!"

    hide i_cha_hunt
    "Pero yo ya no lo escuchaba. Comencé a correr hacia el pueblo."

    jump scene8


label help_hunter:

    $ x3_help = True

    show i_player think
    "Dejo mi mente en blanco por un momento."
    
    show i_player wary
    p "Si les ayudo… ¿Van a devolver al niño con sus padres?"

    x3 "Así será."
    
    p "Está bien, cómo puedo ayudarte."

    x3 "Primero... el sacrificio..."

    hide i_player
    "El cazador se voltea dándome la espalda."

    show i_cha_hunt neutral at center
    x3 """
    {b}¡OH, MADRE TIERRA!{/b}

    Imploro tu guía y ayuda. 
    
    {i}¡Envíame a la más valiente de tus bestias!{/i}
    """
    
    """
    El cazador se quedó esperando haciendo cánticos en un lenguaje que desconozco. 
    
    Y después de un rato, un pequeño animalito apareció de entre la maleza y entró al claro.
    
    Se trataba de un pequeño tejón.

    El pobrecillo avanzaba poco a poco hacia el cazador. 
    
    Podía notar como todo su cuerpo temblaba. 
    
    Pero aún así avanzó sin dar un solo paso atrás hasta llegar justo enfrente del cazador.
    """

    x3 """
    Ah! Noble {i}pezotli{/i}. 
    
    La batalla se acerca.
    
    Y no son los más fuertes los que ganan. 
    
    Sino los que enfrentan las dificultades de frente y con valor.

    MADRE TIERRA, NOBLE PEZOTLI. Permítanme tomar su fuerza. ¡Les estoy eternamente agradecido!
    """

    """
    Entonces vi la cosa más sorprendente que haya presenciado jamás. 
    
    El cazador alzó las manos y puso una sobre la cabeza del tejón y la otra sobre la herida de su sabuesa. 
    
    Una luz cegadora llenó el claro, y cuando me ajusté de nuevo a la oscuridad, ahí estaba la querida perra del cazador. 
    """

    hide i_cha_hunt
    pause 1.0
    show i_izel neutral at center

    """
    Pero ya no era una perra común y corriente: con un cuerpo canino, pero con facciones de tejón, la nueva sabuesa se erguía imponente al lado de su amo.
    
    Y lo que más resaltaba era su larguísima cola, bien podría estar presenciando a un ser mitológico.
    """

    x3 "Yo te nombro {i}Izel{/i}, mi querida sabuesa."

    hide i_izel
    """
    Izel lamió con entusiasmo la máscara del Cazador.

    Podía notar en el cazador su alegría, pero también su tristeza.
    """

    show i_cha_hunt neutral at right
    show i_player wary at left

    x3 """
    Y ahora, el acto de fe:
    
    Lleva a Izel contigo, buen hombre.
    
    Déjala que te guíe, y encontrarás al niño.
    
    Protéjelo de todo mal hasta que salga el sol.
    
    Solo entonces estará a salvo por siempre.
    
    Te entrego este fruto de Xocohuitxtle.
    
    La bendición de la Madre Tierra te acompaña.
    
    Pero recuerda mantenerte en el buen camino.
    """
    
    $ xoco_count += 1

    """
    Asiento con la cabeza, aun un poco anonadado por todo lo que ha pasado. 
    
    Pero rápidamente me volteo y comienzo a correr hacia el pueblo siguiendo a la sabuesa Izel.
    """

    hide i_cha_hunt
    hide i_player

    jump scene8