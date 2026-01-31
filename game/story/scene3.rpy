label scene3:
    """
    Luego de caminar un rato, subiendo y subiendo, alcanzo a divisar una cabañita. 
    
    Afuera de la cabaña veo unas parcelas. 
    
    Y sentado en una banca de madera cerca de la ventana de la cabaña, está un hombre viejo.
    """
    p "¡B-Buenas Tardes!"

    x1 "..."

    p """
    Disculpe que lo moleste a estas horas. 
    
    Fijese que se robaron a un niño y pues venía a preguntar si no había visto a alguien pasar por aquí
    
    o si usted ha visto al niño.
    """

    x1 "..."

    p """
    No puedo evitar observar que usted tiene un costal de grano de maíz, ahí a su lado.
    
    Fíjese que me dijeron que en el lugar donde vieron al niño por última vez, encontraron regados unos granos de maíz.
    """

    x1 """
    El {i}\"Tlaolli\"{/i} es un regalo de la {b}Madre Tierra{/b}. 
    
    Por ella somos, vivimos, y luego regresamos a ella.
    
    Es necesario comenzar a bendecirla para que nuestra Madre nos brinde buena cosecha para el siguiente ciclo. 
    
    Pero ya mis años me pesan, y no he podido afilar mi {b}coa{/b} como es debido. 
    
    {i}Buen hombre{i}, ¿me ayudaría a terminar de afilar mi Coa?
    """

    p "Escuche, la verdad es que no hay tiempo para eso en este momento. Se robaron a un niño y no puedo perder un minuto más aquí."

    x1 """
    Se lo pido de nuevo buen hombre.

    Ya solo queda un poco más de afilado que hacerle. 
    
    Con su fuerza estoy seguro que lo hará muy rápido.
    
    Además, cuando se trata de bendiciones, el tiempo no es importante, solo lo que hacemos es importante.
    
    Estos rituales son la base de nuestra existencia.
    """

    menu:
        "Ayudar al Granjero Anciano":
            jump help_old_man
        "Seguir con la búsqueda":
            jump no_help_old_man



label help_old_man:

    $ x1_help = True

    """
    A pesar de las circunstancias, accedí a ayudar al anciano. 
    
    Tal vez sea un poco extraño, pero pudiera decirme algo si yo lo ayudo primero.
    """ 

##*Sonidos de afilado*

    x1 """
    Ha hecho algo muy bueno. 
    
    Ahora podré continuar con mis rituales hacia nuestra querida Madre Tierra.
    """

    """
    Y como si hubiera sido revitalizado, 
    
    el anciano comienza a brincar y danzar. 
    
    Una vez terminada su danza, voltea hacia mí. 
    
    Extiende su mano y me entrega un pequeño fruto."""

    $ xoco_count += 1

    x1 """
    El xocohuiztle es vida.
    
    {b}{i}La fuerza de la madre tierra lo bendice a usted.{/i}{/b}
    
    {b}Pero recuerde mantenerse en el buen camino.{/b}

    El niño se encuentra aún por aquí, pero yo no sé donde se encuentra.
    
    Sin embargo, el peligro aún lo acecha. 
    
    Le recomiendo visitar a mi hermano, el ermitaño del oeste. 
    
    Siga este camino de aquí y llegará muy rápido.
    """

    p "Entiendo. Bueno, debo retirarme. Adiós."

    jump scene4



label no_help_old_man:

    p "Lo siento viejo, no puedo quedarme aquí."

    x1 """
    Ah… entiendo. 
    
    En ese caso, deberías dirigirte al oeste. 
    
    Allá vive un ermitaño, mi hermano. 
    
    Puede que él sepa algo."""

    p "Ya veo. Bueno. Adiós."

    jump scene4
