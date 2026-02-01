label scene9:

    """
    Me encuentro corriendo, como nunca he corrido en mi vida. 
    
    Pareciera un animal salvaje, moviéndose entre la selva con agilidad, mientras sigo sin perder de vista a mi fuel sabuesa, Izel.

    No pasa mucho tiempo, antes de que me encuentre ya al centro del pueblo. Pero por alguna razón no veo a nadie.

    Es como si el aire fuera diferente. Una ligera neblina cubre todo el pueblo.
    """

    show i_izel neutral at right
    z "GRRRRR ... ¡¡WRAFF WRAFF!!"

    show i_player wary at left
    p "¿Qué pasa, amiga?"

    """
    Levanto la mirada, y allí lo veo. 
    
    El hombre de Negro… solo que ya no es un hombre. 
    
    Al menos no completamente. 
    
    Sigue con un cuerpo como el de cualquier hombre.. 
    
    Pero su rostro. 
    
    Su rostro ya no es humano. 
    
    Es un monstruo, una bestia antinatural. 
    
    Con tatuajes brillando rojo vivo como brasas y una piel negra cual carbón, se presenta ante mí finalmente, sin máscaras.
    """

    d """
    ¡¡USTED ES UN TONTO COMPADRE!! 
    
    TODO LO QUE TENÍA QUE HACER ERA DEJARME ENCONTRAR AL NIÑO.
    
    PERO {i}NOOOOOOO{/i}, TENÍA QUE METERSE DONDE NO LE IMPORTABA, ¿CIERTO?
    
    ¿ACASO NO VINO A QUITARSE DE LOS PROBLEMAS DE LA VIDA?
    """

    """
    Su voz retumbaba y carraspeaba con una rabia que no había conocido, y tal vez nunca conoceré de nuevo. 
    
    El demonio aquél vociferaba mientras gritaba y lanzaba saliva con cada palabra rabiosa.
    """

    p """
    Los problemas no parecen alejarse nunca. 
    
    Así que solo debo seguir danzando con la vida, no cree, “compadre”?
    """

    d """
    JA JA JA JA JA!! 
    
    AH! 
    
    SE CREE MUY LISTO Y SE BURLA, ¿NO? 
    
    PERO YO SOY MUCHO MÁS LISTO QUE USTED.

    MIENTRAS ESTÉ BAJO MI NEBLINA, NADIE DEL PUEBLO PODRÁ AYUDARLO.

    ¡¡ESTÁ SOLO EN ESTO, COMPADRE!!
    """
    
    p """
    Tal vez, pero aún así no tendrá al niño. 
    Lo juro por mi vida.
    """

    d "¡ENTONCES POR SU VIDA SERÁ!"

    """
    El demonio se lanzó con una velocidad de rayo hacia mi.
    
    Pero justo antes de que sus garras me alcanzaran, se escuchó un {b}estruendo{/b}.
    
    El demonio retachó y cayó de espaldas a la tierra, y de una voltereta se levantó, un poco aturdido.

    Quedé estupefacto y aliviado. 
    
    Frente a mi se encontraban los tres ermitaños que en ese momento llegaron acudiendo a mi ayuda.
    """
    
    x2 "¡Ji, ji ,ji ,ji! lamentamos el retraso."

    "Me dice el tamborilero mientras brincotea alegremente."

    x2 "Nos tomó un poco atravesar esa barrera de neblina."

    x1 "¡Eh je, je! ¡Parece que tendremos un segundo round!"

    "El anciano se endereza y estira mientras le truena un poco la espalda."

    x3 """
    Hagamos que cuente entonces. [player_name] ya no somos lo que éramos. 
    
    El tiempo a pasado, y ya no podemos vencer.
    
    Es muy probable, que esta sea nuestra última batalla. 
    
    Toda nuestra fe está contigo.
    
    Encuentra al niño y llévatelo; corran hasta que el sol salga y sus rayos toquen al pueblo.

    Solo necesitan resistir.
    """

    """
    No hubo mucho tiempo para decir más.
    
    El demonio se lanzó contra los ermitaños y ellos se lanzaron contra él. 
    
    El cazador se movia como una bestia salvaje, rápido y feroz. 
    
    El tamborilero, brincando y danzando tocaba el tambor con singular alegría. 
    Cada retumbo del instrumento atontaba al demonio y lo hacía retroceder. 

    El anciano no se movía mucho, pero lanzaba ataques cual rayo con su coa cuando veía alguna abertura o distracción del demonio.

    De no haber tenido ya una misión, estaría viendo más de aquella batalla.
    """

    p "¡Izel, llevame al niño ya! ¡No tardes o podemos perderlo!"

    z "Wrrr raff!"

    "Corrimos rápido entre los árboles del jardín central y llegamos a un arbol muy viejo y con muchas ramas, justo al centro del jardín."

    z "Wraff Wraff!!"

    p "No puedo ver nada, pero debe estar aquí."

    """
    Después de pensarlo un poco, dejé de pensar y comencé a sentir.
    
    Cerré los ojos y comencé a escuchar a la tierra.
    """
    
    p "¡Oh Madre Tierra, guía mis sentidos. Permíteme ver lo oculto."

    """
    Un viento cálido sopló.
    
    Y como si un polvo fino se levantara al cielo, entre destellos comienzo a ver la figura de un niño jugando con unos muñecos de madera.
    
    Me inclino y le hablo.
    """

    p "Hola pequeño ¿a qué juegas?"

    n "Estoy jugando a vencer al hombre malo."

    p "Ah ese es un juego muy divertido. ¿Cómo llegaste aquí?"

    n """
    Los hombres de las máscaras blancas me ayudaron a escapar del hombre malo. 
    
    Después me dijeron que me escondiera, así que vine a mi árbol favorito. 
    
    Siempre juego a las escondidas aquí. 
    
    Pero me cansé de esperar y me puse a jugar.
    """

    p "¿Cómo te llamas?"

    $ kid_name = "Chuy"

    n "Me dicen Chuy."

    p "Escucha Chuy, el poder que te mantiene oculto del hombre malo ya casi se acaba, puedo verlo. Debemos seguir corriendo hasta que amanezca."

    d "{b}¡MUY TARDE PARA ESO!{/b}"

    n "Aaaaah!!"
    
    p "Oh no!"

    """
    Podía ver que el demonio estaba bastante lastimado...
    
    Pero los ermitaños ya yacían en el suelo inmóviles.

    Sus cuerpos comenzaron a disiparse como polvo al aire. 
    """

    d """
    JA JA JA! 
    
    PARECE QUE HAS PERDIDO COMPADRE. 
    
    ME HA COSTADO MUCHO TRABAJO, ¡PERO ESE NIÑO VA A SER MÍO! 
    
    Y EL SIGUIENTE AÑO VOLVERÉ MAS FUERTE Y YA NO HABRÁ NADIE QUE ME DETENGA.
    """

    """
    El demonio se lanzo en un ataque final hacia mí. De forma instintiva me volteé hacia el niño y lo cubrí.

    {b}¡¡¡KABOOOM!!!{/b}

    Lo escuché. 
    
    El tambor que antes tenía el ermitaño enorme ahora estaba conmigo. 
    
    Y no solo eso. 
    
    Yo había cambiado por completo. 
    
    Tenía una máscara como la de los ermitaños cubriendo mi rostro.
    
    Mi vestimenta era de Ixtle.
    
    En mi mano tenía la Coa.
    
    Y una corona adornaba mi cabeza.
    """

    d """
    No...
    
    ¡¡¡NOOOOOOOOO!!!
    
    ¡YA HABÍA ACABADO CON USTEDES!
    """

    p "Esto acaba ahora."

    """
    Hice sonar mi tambor, y el sonido fue tal que casi noquea al demonio. 
    
    Con un movimiento ágil de mi coa, partí el rostro del demonio por la mitad. 
    
    El demonio en su último intento sostuvo las mitades con desesperación y apretó con fuerza para que su rostro no se separara.

    Extendí mi brazo.
    """

    p "¡Ahora, Izel!"

    """
    La sabuesa brincó sobre mi brazo extendido, agarró vuelo, dió una voltereta y lanzó su larga cola como látigo, azotando con un certero golpe purificador al demonio.
    """

    d "s - s... s..omos muchos... nunca... acabarás... con nosotros -aggh!!- ..."

    "Y así el demonio empezó a desintegrarse."

    p "No importa. Estaré aquí siempre, como lo he estado por mucho tiempo..."

    p """
    Lo logramos.
    
    Granjero Anciano.

    Tamborilero.

    Cazador.

    Gracias.
    """

    """
    El sol comienza a brillar sobre Ixtlahuacán y la neblina se ha disipado por completo. 
    
    Escucho los gritos de alegría de los pobladores.
    """

    m "¡Hijito!! ¡Ay Gracias, Gracias a Dios estás bien!"

    n "¡Mami! ¡Mami! El Señor de la Máscara me salvó del hombre malo que me quería llevar."

    m "¡Gracias Señor!... ¿C-Cuál es su nombre? ¿Quién es usted?"
    
    """
    ¿Quien soy yo?
    
    Tomé un tiempo, y escuché el canto de la tierra para saberlo.
    
    Y respondí:
    """

    p """
    Mi máscara soy yo.
    
    Y yo soy mi máscara.

    Soy un Chayacate.
    """

    "FIN"

    jump story_end
