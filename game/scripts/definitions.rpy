init python:
    # define italics and bold fonts
    # the arguments are: font file, boldness, italics
    config.font_replacement_map["fonts/Mali/Mali-Regular.ttf", True, False] = ("fonts/Mali/Mali-Bold.ttf", False, False)
    config.font_replacement_map["fonts/Mali/Mali-Regular.ttf", False, True] = ("fonts/Mali/Mali-Italic.ttf", False, False)
    config.font_replacement_map["fonts/Mali/Mali-Regular.ttf", True, True] = ("fonts/Mali/Mali-BoldItalic.ttf", False, False)

    ## for character sprites
    class Picker(object):
        def __init__(self, options):
            self.options =  [ i.split() for i in options ]

        def __call__(self, attributes):
            rv = set(attributes)

            for i in self.options:
                if i[0] in attributes:
                    rv.update(i[1:])

            return rv

init:
    define vivian = Character("Vivian")
    # use this instead if we want side image
    # define vivian = Character("Vivian", image='vivian')

    ## character sprites

    define expressions = [
    "neutral eyes_center_blink brows_neutral mouth_neutral",
    "smile eyes_center_blink brows_neutral mouth_smile",
    "neutralAway eyes_away_blink brows_neutral mouth_neutral",
    "neutralDown eyes_down_blink brows_neutral mouth_neutral",
    "laugh eyes_laugh brows_raised mouth_laugh",
    ]

    # blink
    image sprite_vivian_eyes_center_blink = DynamicBlink(
        "images/chara/vivian/sprite_vivian_eyes_center.png",
        "images/chara/vivian/sprite_vivian_eyes_closed.png"
        )

    image sprite_vivian_eyes_down_blink = DynamicBlink(
        "images/chara/vivian/sprite_vivian_eyes_down.png",
        "images/chara/vivian/sprite_vivian_eyes_closed.png"
        )

    image sprite_vivian_eyes_away_blink = DynamicBlink(
        "images/chara/vivian/sprite_vivian_eyes_away.png",
        "images/chara/vivian/sprite_vivian_eyes_closed.png"
        )

    layeredimage sprite vivian:
        always "sprite_vivian_base"

        attribute blush
        attribute tears

        group eyes auto prefix "eyes"
        group brows auto prefix "brows"
        group mouth auto prefix "mouth"

        group expressions:
            attribute neutral default null
            attribute smile null
            attribute neutralAway null
            attribute neutralDown null
            attribute laugh null

        attribute_function Picker(expressions)

    # uncomment this to use vivian on the side
    # image side vivian = LayeredImageProxy("vivian")