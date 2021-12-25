init python:
    # define italics and bold fonts
    # the arguments are: font file, boldness, italics
    config.font_replacement_map["fonts/Mali/Mali-Regular.ttf", True, False] = ("fonts/Mali/Mali-Bold.ttf", False, False)
    config.font_replacement_map["fonts/Mali/Mali-Regular.ttf", False, True] = ("fonts/Mali/Mali-Italic.ttf", False, False)
    config.font_replacement_map["fonts/Mali/Mali-Regular.ttf", True, True] = ("fonts/Mali/Mali-BoldItalic.ttf", False, False)


init:
    define vivian = Character("Vivian")
