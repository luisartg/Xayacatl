label scene6:
    #test
    #$ x2_help = True
    
    "Caminando ya mas deprisa por la vereda alcanzo a detectar en medio del camino al hombre vestido de negro."
    
    show i_player relax at left
    show i_dev neutral at right

    if x2_help:
        d """ 
        Se ve muy contento compadre.
        
        ¿No le parece exagerado estar haciendo tanto ruido y bailando a estas horas de la noche?
        
        ¿y con la situación de un niño en peligro?
        """

        show i_player wary

        menu:
            "Estoy haciendo lo mejor que puedo hacer… me adapto al ritmo de esta búsqueda.":                
                d """
                Pff!! {i}El “Ritmo” {/i}
                
                {i}{b}JA, JA, JA, JA, JA. {/b}{/i} 
                
                ¡Buena esa, compadre!

                ¡Ah! Me hacía falta reir... 
                
                Realmente estoy muy... {b}estresado{/b}, ¿sabe?
                
                Yo sé que ese {i}tamborilerucho{/i} estuvo ahí cuando robaron al niño. 
                
                Y usted lo dejó como si nada... 
                
                Pero bueno, a lo importante.
                """

            "No pasará de nuevo, creo que ya estamos cerca de encontrar al niño.":
                d """
                Si bueno... yo también puedo sentir que estamos cerca. 
                
                Como sea.
                """
    else:
        d "Magistral trabajo, compadre."

    d """
    No habrá olvidado nuestro buen trato, ¿cierto?
    
    ¿Le dijo algo el gordinflón?
    """

    menu:
        "Hay que ir al {b}Este{/b}, donde encontraremos al cazador ermitaño.":
            jump escene6_help_devil
        "Tampoco dijo nada útil." if x2_help:
            jump escene6_no_help_devil



label escene6_help_devil:

    d """
    Ah... 
    
    AJA JA JA, Si..., claro, claro.
    
    Excelente. 
    
    Bueno, como es prometido: Diez Monedas de Plata.
    """
    
    $ silver_count += 1

    show i_player happy

    """
    Recibo con manos temblorosas las 10 monedas. 
    
    Brillan con una luz extrañamente bella, incluso entre tanta oscuridad.
    
    No puedo creer que me esté haciendo rico con tanta facilidad.
    
    Debo seguir rápido para continuar creciendo de esta manera.
    """

    d """
    Lo veo en sus ojos, compadre.
    
    Entiende perfectamente este mundo.
    
    La vida tiene problemas ¡SÍ!
    
    Pero la riqueza... La riqueza siempre lo soluciona todo, ¿no es así?
    """
    show i_player relax
    jump escene6_closure



label escene6_no_help_devil:

    d """
    {b}{i}¡¿Nada de nuevo?!{/i}{/b} 
    
    Usted no se está tomando esto en serio... {i}\"Compadre\"{/i}.
    """
    
    "El hombre refunfuñó y resopló."

    show i_dev mad
    """
    Y juro que por un momento vi como sus resoplidos soltaban pequeñas brasas que brillaban como rojas luciérnagas,
    revoloteando en la oscuridad. 
    
    El hombre se recompuso y tomó su actitud usual.
    """
    
    show i_dev neutral
    d """
    Disculpe.
    
    Me alteré un poco. Ha sido una noche larga. 
    """
    show i_player wary
    jump escene6_closure

label escene6_closure:
    d """
    Presiento que la siguiente será nuestra última parada.
    
    El trato sigue entonces. ¡Leo veo luego, compadre!
    """
    hide i_dev

    """
    Y así como llegó se fue. 
    
    A veces me pregunto cómo se va así como así, casi desapareciendo pero presente de algún modo. 
    
    Fugaz y etéreo. Hasta que simplemente no lo puedo ver más.
    """

    hide i_player
    jump scene7