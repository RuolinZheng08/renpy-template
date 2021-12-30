init python:
    # first-person blink
    def eyewarp(x):
        return x ** 1.33

    # ATL transition
    eyeopen = ImageDissolve("wipes/eye.png", 2, ramplen=128, reverse=False, time_warp=eyewarp)
    eyeclose = ImageDissolve("wipes/eye.png", 2, ramplen=128, reverse=True, time_warp=eyewarp)

init:
    transform additive_blend:
        additive 1.0

    transform floating:
        yoffset 0
        ease 1. yoffset -5
        ease 1. yoffset 0
        repeat