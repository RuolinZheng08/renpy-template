label start:
    scene bg hallway

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

    $ time_of_day = SEPIA
    $ sprite_effect = None
    show sprite vivian sadDown tears
    "Now we are in flashback mode."
    vivian "... You promised me to come back, didn't you?"

    $ time_of_day = NIGHT
    $ sprite_effect = DIM
    show sprite vivian smile -tears
    "Now back to the present timeline."
    vivian "Hey. You are spacing out. Did I say something strange?"

    "This concludes our effect showcase. More effects on the way!"

    return
