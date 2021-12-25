screen expression_showcase_screen():
    default sprite_brows = "sprite_vivian_brows_neutral"
    default sprite_eyes = "sprite_vivian_eyes_center_blink"
    default sprite_mouth = "sprite_vivian_mouth_neutral"
    default sprite_blush = False
    default sprite_tears = False

    frame:
        xalign 0.5
        yalign 0.5
        padding (50, 50, 50, 50)

        hbox:
            spacing 100
            # left
            vbox:
                label "Brows"

                label "Eyes"

                label "Mouth"

                vbox:
                    label "Others"
                    style_prefix "check"
                    textbutton "Blush":
                        action ToggleScreenVariable(name='sprite_blush', true_value=True, false_value=False)
                    textbutton "Tears":
                        action ToggleScreenVariable(name='sprite_tears', true_value=True, false_value=False)

            # middle
            python:
                sprite_args = [
                (0, 0), "sprite_vivian_base",
                (0, 0), sprite_brows,
                (0, 0), sprite_eyes,
                (0, 0), sprite_mouth
                ]
                if sprite_blush:
                    sprite_args.extend([(0, 0), "sprite_vivian_blush"])
                if sprite_tears:
                    sprite_args.extend([(0, 0), "sprite_vivian_tears"])
            $ sprite = LiveComposite(
                (532,1080),
                *sprite_args
                )
            add sprite

            # right
            textbutton 'Exit' action Return()