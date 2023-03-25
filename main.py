music.start_melody(music.built_in_melody(Melodies.BIRTHDAY),
    MelodyOptions.FOREVER)

def on_forever():
    basic.show_icon(IconNames.CHESSBOARD)
    basic.pause(1000)
    basic.show_icon(IconNames.SILLY)
    basic.pause(1000)
basic.forever(on_forever)
