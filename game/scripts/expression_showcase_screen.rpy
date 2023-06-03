screen expression_showcase_screen():
    default brows = "vivian_brows_neutral"
    default eyes = "vivian_eyes_center_blink"
    default mouth = "vivian_mouth_neutral"
    default blush = False
    default tears = False

    frame:
        xalign 0.5
        yalign 0.5
        padding (50, 50, 50, 50)

        hbox:
            spacing 100
            # left
            viewport:
                scrollbars "vertical"
                xsize 300
                ymaximum config.screen_height
                child_size (None, 4000)

                has vbox
                spacing 20

                vbox:
                    label "Brows"
                    for exp in ['neutral', 'angry', 'raised', 'worried']:
                        textbutton exp:
                            action SetScreenVariable(
                                name='brows', 
                                value='vivian_brows_%s' % exp
                                )

                vbox:
                    label "Eyes"
                    for exp in ['center_blink', 'down_blink', 'away_blink', 'closed', 'laugh']:
                        textbutton exp:
                            action SetScreenVariable(
                                name='eyes', 
                                value='vivian_eyes_%s' % exp
                                )

                vbox:
                    label "Mouth"
                    for exp in ['neutral', 'smile', 'laugh', 'pout', 'oh']:
                        textbutton exp:
                            action SetScreenVariable(
                                name='mouth', 
                                value='vivian_mouth_%s' % exp
                                )

                vbox:
                    label "Others"
                    style_prefix "check"
                    textbutton "blush":
                        action ToggleScreenVariable(name='blush', true_value=True, false_value=False)
                    textbutton "tears":
                        action ToggleScreenVariable(name='tears', true_value=True, false_value=False)

            # middle
            python:
                args = [
                (0, 0), "vivian_base",
                (0, 0), brows,
                (0, 0), eyes,
                (0, 0), mouth
                ]
                if blush:
                    args.extend([(0, 0), "vivian_blush"])
                if tears:
                    args.extend([(0, 0), "vivian_tears"])
            $ sprite = LiveComposite(
                (532,1080),
                *args
                )
            add sprite

            # right
            textbutton 'Exit' action Return()