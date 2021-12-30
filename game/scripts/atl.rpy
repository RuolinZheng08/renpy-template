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

    transform truecenter_transform:
        xanchor 0.5 yanchor 0.5 xalign 0.5 yalign 0.5