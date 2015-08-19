image bg forest = "images/Forest.jpg"
image bg bedroom = "images/bedroom.jpg"
image bg woods = "images/woods.jpg"
image bg woods = "images/woods.jpg"
image bg nuke = "images/nuclearExplotion.jpg"
image Ishiene = "images/Ishiene.png"
image madpika = "images/madPikachu.png"
image madCharacter = "images/angryCharacter.png"
image pikachu animated:
    "images/pikachu!.png"
    pause.1
    "images/pikachu!2.png"
    pause.1
    repeat
image Alex animated:
    "images/Character.png"
    pause .2
    "images/Character1.png"
    pause .2
    "images/Character.png"
    pause .9
    repeat
image fartAlex = "images/Character2.png"
image wonderAlex = "images/wonderCharacter.png"
image pikachu = "images/pikachu.png"
image engaño = "images/A_mi_no_me_engañas_meme.png"
image goomba = "images/goomba.png"
image motivated ="images/motivatedCharacter.png"
image excited = "images/Character3.png"
image sad animated:
    "images/Character4.png"
    pause .1
    "images/Character5.png"
    pause .1
    repeat
image derp animated:
    "images/Derp.png"
    pause .1
    "images/Derp2.png"
    pause .1
    repeat

define Alex = Character('Alex', color="#660033")
define Pikachu = Character('Pikachu', color="#FFFF00")
define ishiene = Character('Ishiene', color="#0066FF")

# - El juego comienza aquí.
label start:
    scene bg bedroom with dissolve
    show Alex animated with dissolve
    "Alex es un tipo normal, con una vida normal, que vive en una casa normal y en una sociedad muy normal..."
    show fartAlex
    play sound "Silly_Farts-Joe-1473367952.mp3"
    "A quien engaño.. el es el ser mas extraño que habita en la tierra."
    "Alex a pesar de ser muy extraño, tiene al amigo mas fiel del mundo."
    hide Alex
    show fartAlex at left
    with move
    play sound "Bleat-SoundBible.com-893851569.mp3"
    show pikachu at right with dissolve 
    "Su querido Pikachu...."
    "Si.... pikachu tambien es muy raro, por eso son tal para cual."
    show wonderAlex at left
    hide fartAlex with dissolve
    show pikachu with dissolve:
        size(400,462.5)
    Alex "Pikachu me gustaria ir al bosque para divertirnos, que opinas?"
    Alex "Talvez hagamos nuevos amigos, y nunca nos separaremos de ellos, y seremos felices por siempre."
    menu:
        "Pika, pikachu!!(Ir al bosque)":
            Pikachu "Pikaaa, pikachuuu"
            Alex "Lo que tu digas pikachu, vamos al bosque."
            jump theForest
        "Pika, pikachu!!(Ni hablar mejor quedemos en casa)":
            Pikachu "Pikaaa, pikachuuu"
            Alex "Lo que tu digas pikachu, nos quedamos aqui."
            jump choice1

label theForest:
    scene forest with fade
    play music "Crickets-SoundBible.com-1506135086.mp3" fadeout 1
    show Alex animated with dissolve
    Alex "No veo a nadie por aqui"
    hide Alex animated
    show engaño at right
    with dissolve
    Alex "Ya dejen de jugar a las escondidas"
    "De pronto un goomba salvaje aparecio"
    show goomba at left with dissolve:
        size(234,279)
    with move
    hide engaño
    show excited at right
    hide excited
    show motivated at right
    Alex "Es hora de esclavizar a un amigo!!"
    hide motivated
    show excited at right
    Alex "Digo... hora de conseguir un amigo!!"
    hide goomba with dissolve
    hide excited
    show sad animated at right with dissolve
    "Lastimosamente el Goomba huyo porque Alex era tan raro como de costumbre."
    
    menu:
        "Deseas regresar a casa?":
            show sad animated at left with dissolve
            with move
            Alex "Mejor nos vamos, nadie me quiere, todos me odian, mejor me como un gusanito"
            show pikachu at right
            Pikachu "Piiiika pikaaaaa, pikachuuu"
            jump choice1
        "Naaaa, sigamos caminando":
            stop music fadeout 1
            jump woods
            
    jump choicedone
    
label stayHome:
    jump choicedone
label woods:
    scene bg woods with fade
    show derp animated at left
    with move
    with dissolve
    "Alex es tan despistado que se perdio en un bosque oscuro como era de esperarse, se sentia abrumado por la oscuridad del bosque, pero su fiel pikachu estaba dispuesto a protegerlo"
    "De la nada, una sirena aparecio"
    show Ishiene at right with dissolve
    ishiene "Sera mejor que abandonen estas tierras, o estaran condenados al eterno castigo de poseidon"
    hide derp animated 
    show madpika at left:
        size(400,462.5)
    with dissolve
    play sound "Pokemon anime Pikachu thunderbolt sound effect.mp3"
    Pikachu"HHMmmmm Pika!!"
    hide madpika
    show madCharacter at left
    Alex "Pikachuuu!!! Use Thuuuuuunderboooooooolt!!!"
    with dissolve
    hide madCharacter
    show pikachu animated at left:
        size(400,462.5)
    with move
    play sound "Pikachu's First Thunderbolt.mp3"
    Pikachu "Piiiiiiiiiikaaaaaaaachuuuuuuuu!!!"
    jump choicedone
label choicedone:
    scene bg nuke with fade
    play sound "nuclear explosion   sound effect[1].mp3"
    
label choice1:
    "Y asi termina la historia de nuestro extraño personaje"