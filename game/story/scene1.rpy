label scene1:
    """
    El incesante sube y baja de la carreta se detiene.

    Poco a poco abro los ojos, un poco empapado de sudor por el calor húmedo característico de Colima.

    Me levanto, un poco dolorido y entumecido por el viaje. Pero al fin he llegado a Ixtlahuacán.

    El sol ya está a punto de meterse detrás de las montañas del valle, pero aún se pueden ver algunos detalles de mi alrededor.
    
    Le pago sus respectivas monedas al conductor, y procedo a dirigirme a la entrada del pueblo.

    Aunque me he divertido mucho en las ciudades grandes, la verdad es que añoro la vida campesina.
    
    La tranquilidad y la hermosa vegetación de los alrededores le traerá paz a mi corazón.
    
    Espero poder comenzar mi nueva vida aquí lejos de los problemas.

    Sigo el camino de tierra a través de un gran arco de piedra, con la inscripción “Bienvenido a Ixtlahuacán”.

    Ahora solo queda...
    """

    show i_camp worry at right 

    c "Señor! Perdone que lo aborde tan de repente, pero le imploro su ayuda, si Dios lo permite en su ser."

    show i_player serious at left  

    p "Eh… Claro, dígame, en qué puedo servirle."

    c "Se han robado al niño de Doña María!"

    p """
    {i}Ahí va mi vida libre de problemas.{/i}

    ¿Se lo robaron? 
    
    ¿Sería posible que solo está jugando por ahí y se le hizo tarde para volver a su casa?
    """

    show i_camp help 

    c """
    No señor, le digo que es verdad, porque Don Bartolo vió al que se lo llevó. 
    
    Bueno, más bien solo lo vió a lo lejos. 
    
    Y fue muy extraño, solo vió a alguien, moviéndose rápido y desapareciendo en las sombras. 
    
    El dice que iba vestido con ropas claras, pero eso no ayuda porque pos' aquí todos vestimos manta, señor! 
    
    Aunque también Don Bartolo jura que escuchó sonidos como de unos {b}tambores{/b} 
    
    y que iba correteando junto a ellos un animal, tal vez un {b}perro o tejón{/b}. 
    
    Cuando se acercó a donde los vió desaparecer, solo había algunos granos de {b}maíz{/b} en el suelo.
    """
    menu:
        "Está bien, lo ayudo.":
            jump do_help
        "Sabe, vengo muy cansado del viaje, no sería de mucha ayuda.":
            jump no_help
    
label no_help:

    hide i_camp 

    "El campesino se aleja, un poco triste pero acelera su paso a la búsqueda."

    p """
    Esto no es algo que sea de mi incumbencia. 

    Vine acá a {b}dejar los problemas atrás.{/b}
    """

    hide i_player 

    """
    Y así, el viajero toma su camino a través de la entrada de Ixtlahuacán. 
    
    Pero algo extraño comienza a suceder. 
    
    Mientras más camina por la senda, una neblina, al inicio ligera, comienza a tomar un gran espesor. 
    
    Camina y camina pensando que pronto llegará al cúmulo de casitas que se veían en el pueblo. 
    
    Pero nunca llega. 
    
    Se ha perdido. 
    
    Sigue en el camino, y sin embargo ya no hay nada alrededor. 
    
    Solo niebla, y el arrepentimiento, de que tal vez si hubiera deseado ayudar, su situación habría cambiado. 
    
    Sin saber que hacer, vaga eternamente y no se vuelve a escuchar de él jamás.

    Excepto tal vez, 
    
    en un pueblo lejano al norte de ahí, llamado Villa de Álvarez, 
    
    donde un carretero cuenta como en Ixtlahuacán,
    
    vió al hombre que llevó hasta allá, desaparecer entre sombras, al ocultarse el sol tras la montaña. 
    
    Lo tildan de borracho y loco. 
    
    Pero en verdad fue la última persona que vió a aquel viajero partir a lugares más allá de nuestra comprensión terrenal.
    """

    jump story_end

label do_help:

    show i_camp neutral 

    c """
    ¡Dios se lo pague y lo proteja siempre! 
    """

    show i_camp help 
    c """
    Por favor señor, ayúdenos yendo al sur de aquí. 
    
    Tome ese pequeño camino que ve allá, y lo llevará a una cabaña. 
    
    Allí sabemos que vive un ermitaño. 
    
    La verdad no hemos hablado con él, y es un poco extraño.
    
    Lo vemos bailar entre los caminos de la selva cuando vamos a cazar. 
    
    Pero nos mantenemos en nuestros territorios y hemos estado en paz así. 
    
    Le pido que vaya y discretamente revise, digo, solo pa' estar seguros.
    """

    p "Entiendo, entonces voy y vuelvo. Supongo que puedo encontrarlos en el centro del pueblo."

    show i_camp neutral 
    c "¡Ándele, usted si es requete listo! ¡Dios lo acompañe! Le diré a los demás que usted acaba de llegar, Don.."

    $ player_name = renpy.input("Disculpe, ¿Cómo se llama usted?", default="Lemuel", length=20)
    $ player_name = player_name.strip() or "Lemuel"

    p "[player_name], a su servicio."

    $ campesino_name = "Juan"
    c "¡Don [campesino_name], pa' servir a usté' y Dios¡ Con su permiso, Don [player_name]."

    hide i_camp 
    hide i_player 

    jump scene2

