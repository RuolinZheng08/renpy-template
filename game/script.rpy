label start:
    scene bg hallway

    show sprite vivian
    vivian "Hello!"

    show sprite vivian laugh
    vivian "You are funny."

    show sprite vivian neutralAway blush
    vivian "I can't believe I'm saying this but..."

    show sprite vivian neutralDown -blush
    vivian "I don't know how to say this really..."

    call screen expression_showcase_screen()

    return
