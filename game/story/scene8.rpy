label scene8:
    #test
    #$ x3_help = True
    #$ silver_count = 0

    """
    Corriendo por la senda, puedo ver a lo lejos las luces de los pobladores al centro del pueblo. 
    """

    if x3_help:

        show i_dev neutral at right
        d """
        ¡COMPADRE!

        Ya veo que tiene una nueva acompañante, y ya ha descubierto la verdad. ¿Cierto?
        """

        show i_izel neutral at left
        z "¡¡Grrrr!!"

        hide i_izel
        pause 0.5
        show i_player wary at left
        p """
        Si, los ermitaños se robaron al niño, pero el cazador me ha permitido recuperarlo. 
        
        Solo debo seguir el rastro de su sabuesa.
        """

        d """
        ¡Excelente, compadre! No habrá olvidado nuestro buen trato, ¿cierto?

        Deme a esa sabuesa, compadre. Y yo le daré mis últimas 10 monedas de plata. 
        
        Usted se va a dormir, que ya es muy noche y ha estado recorriendo muchos caminos. 
        
        Y yo me encargaré del resto. 
        
        ¿Qué le parece?
        """

        menu:
            "¡Acepto!":
                show i_player happy
                jump accept_option
            "No... no lo sé" if silver_count>0:
                show i_player think
                d "No se ande con jueguitos conmigo, compadre. Un trato es un trato, ¿acaso no es un hombre de palabra?"

                show i_player wary
                "El tiene razón. Después de todo, he aceptado las monedas antes. Asiento, aunque con duda al incio."
                
                jump escene8_help_devil

            "No." if silver_count==0:
                show i_player wary
                d """
                Ja Ja.. Ja. A ver compadre. 
                
                Creo que no me entendió. 
                
                Usted se ve cansado.
                
                Deme a la sabuesa ¡y yo le diré a todo el pueblo que usted es el héroe!
                """

                menu: 
                    "...Sí... Suena bien.":
                        show i_player wary
                        jump accept_option

                    "Dije que no.":
                        show i_player angry
                        show i_dev mad
                        d """
                        ¡A USTED QUE LE IMPORTA ESE NIÑO!

                        No es más que un forastero en esta tierra. Ni que fuera suyo.

                        Por última vez... ¡DEME A ESE ANIMAL!
                        """

                        menu:
                            "... Sí.. sí claro, no se en que estaba pensando.":
                                show i_player think
                                jump accept_option

                            "¡NUNCA!":
                                show i_player angry
                                jump escene8_no_help_devil

    else:
        show i_player wary
        ## El jugador no ayudó al cazador: El jugador continua, pero se ha quedado sin guía.
        """
        Pero pronto me encuentro con un problema. Llega un momento en que me detengo para tomarme un respiro.

        No se cuando comenzó, pero una neblina antinatural, cual presencia maligna, comienza caer sobre mi.
        
        Es tan densa que apenas puedo ver mis manos frente a mi.

        Me he perdido.
        """
        show i_player tired
        """
        Vago y vago, gritando auxilio. Esperando que mi amigo, el Hombre Vestido de negro aparezca.

        Pero no lo encuentro.

        No se cuanto tiempo pasa, pero cada vez me siento más cansado y sediento.

        ...
        Me tomaré un descanso...
        """
        hide i_player
        
        imp_nar """
        \"Nada más se supo entonces de [player_name]. {i}Quedó varado en la nada{/i}.
        
        Quizá algún {b}guía{/b} pudiera haberle llevado através de tan espesa neblina. Pero eso será en otra vida... tal vez.\"
        """
        centered "FIN"
        jump story_end

label accept_option:
    show i_dev mad
    d "JA JA JA JA JA! AAAHHH! ¡ES UN TRATO ENTONCES!"
    show i_dev neutral
    jump escene8_help_devil


label escene8_help_devil:

    show i_player happy
    """
    El hombre de negro lanza una bolsa con 10 monedas de plata hacia mí. 
    
    Mientras el bolso va cayendo a mis manos extendidas, el tiempo parece detenerse. 
    
    Escucho el hermoso repicar de las monedas de plata golpeándose las unas contra las otras en el bolso. 
    
    No me doy cuenta hasta que es tarde y siento un ardor en el cuello. 

    """
    show i_player tired
    "Mi cuerpo deja de sentirse. "
    hide i_player
    """
    Mi cabeza cae a la maleza del suelo, y mis ojos se cierran en un sueño imposible de vencer...
    
    Mientras el resto de mi cuerpo se desploma hacia otro lado.
    """
    
    d """
    Tenga muy buenas noches, {i}\"compadre\"{/i}...
    
    Hum...
    
    JE, JE...
    
    JE JE JE JE...
    """
    show i_dev mad
    d "AAAAAHHH JA JA JA JA JA JAAA!!!"
    hide i_dev 

    centered "FIN"

    jump story_end

label escene8_no_help_devil:
    show i_dev mad
    d "¡¡¡GRAAAWWWRRR!!! ¡ENTONCES QUE ASÍ SEA!"
    hide i_dev
    """
    Una llamarada rápida se prende frente a mi y en un santiamén el hombre de negro desaparece.
    """
    hide i_player
    jump scene9
