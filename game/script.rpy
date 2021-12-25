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

    "You can configure more expressions by mixing and matching eyes, brows, and mouth on the expression showcase screen."

    call screen expression_showcase_screen()

    show sprite vivian smile blush
    vivian "See you next time!"

    return
