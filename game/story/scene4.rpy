label scene4:
    #test
    #$ x1_help = True

    "Avanzando por el camino, observo a lo lejos al Hombre de Negro."

    show i_dev neutral at right
    show i_player serious at left

    if x1_help:
        d """
        Veo que conoció al anciano. 
        
        ¿Creé que es prudente perder el tiempo así en momentos como estos?

        No creo que sea el momento de estar afilando cuchillitos.
        """
        menu:
            "Hice lo que creí correcto":
                d """
                Lo correcto, ¿eh? 
                
                Siga mi consejo compadre. 
                
                No ayude a la gente culpable. 
                
                ¿Acaso no vio el maíz en el costal? 
                
                ¿Usted recuerda que había maiz tirado en la calle donde se robaron al niño?
                
                {i}{b}Es obvio que ese viejo sabe algo.{/b}{/i}
                """
            "Supongo que tendré que ser más directo con el siguiente ermitaño.":
                d "Eso sería prudente, compadre."

        d "Bueno, lo hecho, hecho está."
    else:
        d "Muy bien hecho, compadre."
    
    d """
    No habrá olvidado nuestro buen trato, ¿cierto?
    
    ¿Le dijo algo el anciano?
    """

    menu:
        "Hay que ir al oeste donde encontraremos a otro ermitaño.":
            jump escene4_help_devil
        "No dijo nada útil." if x1_help:
            jump escene4_no_help_devil



label escene4_help_devil:
    d "¡Muy bien! ¡Así se hace, compadre! Y como es prometido: Diez Monedas de Plata."

    $ silver_count += 1

    show i_player happy
    p """
    {b}¡Es increíble, realmente es plata!{/b} 
    
    Voy a poder comprar una buena tierra con esto. 
    
    Podré vivir sin problemas en este lugar."""
    
    d "Por supuesto. Tu me cuidas, y yo te cuido."

    jump escene4_closure
    


label escene4_no_help_devil:

    d """
    Nada, eh? Bueno… 
    
    Supongo que guardaré mis riquezas para cuando pueda conseguir algo. 
    """
    jump escene4_closure



label escene4_closure:
    d """
    En fin.
    
    Debo retirarme, pero el trato sigue en pie.
    
    Si consigue cualquier información y me la da
    
    {b}10 monedas de plata serán suyas.{/b} 
    
    Me retiro, {i}¡suerte en la búsqueda!{/i}
    """

    hide i_dev
    hide i_player

    jump scene5