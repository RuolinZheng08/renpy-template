label start:
    # play music 'audio/ambience/birds.wav'
    scene bg hallway
    "This is a showcase of the Ren'Py features that I frequently find myself using."

    show sprite vivian
    vivian "Hello!"

    show sprite vivian laugh
    vivian "You are funny."

    show sprite vivian neutralAway blush
    vivian "I can't believe I'm saying this but..."

    show sprite vivian neutralDown -blush
    vivian "Uhhh... I don't know how to tell you this but..."

    "You can configure more expressions by mixing and matching eyes, brows, and mouth on the expression showcase screen."

    call screen expression_showcase_screen()

    show sprite vivian smile blush
    vivian "Time sure flies when I'm with you."

    $ time_of_day = DUSK
    vivian "I can't believe it's already getting dark. Let's go somewhere else before it gets dark."

    $ time_of_day = NIGHT
    scene bg house with dissolve
    vivian "Now it's dark and we are in the woods. Spooky!"

    $ sprite_effect = DIM
    vivian "Would it be better if I turn on the flashlight on my phone?"
    vivian "... This place is giving me déjà vu..."
    hide sprite vivian
    scene bg black with eyeclose

    $ time_of_day = SEPIA
    $ sprite_effect = None
    scene bg house
    show sprite vivian sadDown tears
    "Now we are in flashback mode."
    vivian "... You promised me to come back, didn't you?"
    hide sprite vivian

    $ time_of_day = NIGHT
    $ sprite_effect = DIM
    scene bg black
    scene bg house with eyeopen
    "Now back to the present timeline."
    show sprite vivian smile -tears
    vivian "Hey. You are spacing out. Did I say something strange?"

    vivian "Hey... are you okay? You look sleepy."
    hide sprite vivian
    scene bg black with eyeclose

label paperplane:
    scene bg paperplane with dissolve
    "I remember this girl..."
    show sprite paperplane with dissolve

    "And paper airplanes..."
    "Was it summer?"

    hide sprite paperplane
    scene bg black with eyeclose

label pool:
    scene bg pool at Pan((100, 100), (100, 1097), 40, repeat=True)
        # truecenter        
    # with dissolve
    show sprite pool at truecenter with dissolve
    show effects pool:
        parallel:
            truecenter
            additive_blend

    "I remember this girl..."
    "We went swimming together..."
    "It was on a sunny day in August..."

    hide sprite pool
    hide effects pool
    scene bg black with eyeclose
    "This concludes our effect showcase. More effects on the way!"
    return
