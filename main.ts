music.startMelody(music.builtInMelody(Melodies.Birthday), MelodyOptions.Forever)
basic.forever(function on_forever() {
    basic.showIcon(IconNames.Chessboard)
    basic.pause(1000)
    basic.showIcon(IconNames.Silly)
    basic.pause(1000)
})
