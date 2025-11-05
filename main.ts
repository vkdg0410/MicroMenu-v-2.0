function check () {
    if (state != 0) {
        return
    }
    if (obs1 == 0) {
        if (obs1_status == 0) {
            if (motion == 0 || motion == 1) {
                fail = 1
            } else {
                pass = 1
            }
        } else {
            if (motion == 1) {
                pass = 1
            } else {
                fail = 1
            }
        }
    } else if (obs2 == 0) {
        if (obs2_status == 0) {
            if (motion == 0 || motion == 1) {
                fail = 1
            } else {
                pass = 1
            }
        } else {
            if (motion == 1) {
                pass = 1
            } else {
                fail = 1
            }
        }
    }
    if (fail == 1) {
        state = 1
        basic.clearScreen()
        basic.showString("GAME OVER")
        basic.showString("SCORE")
        basic.showNumber(score)
        state = -1
    }
}
states.setEnterHandler("Mario", function () {
    state = -1
})
states.setEnterHandler("Fis", function () {
    fish_state = 0
})
states.addLoopHandler("Stall", function () {
    music.play(music.builtinPlayableSoundEffect(soundExpression.giggle), music.PlaybackMode.LoopingInBackground)
    basic.showString("STALLING!")
})
states.setEnterHandler("On", function () {
    appSD = 0
})
states.addLoopHandler("UIIAIOUIIIAI", function () {
    basic.clearScreen()
    if (ebld == 1) {
        led.plot(randint(0, 4), randint(0, 4))
    } else if (ebld == 2) {
        led.plot(randint(0, 4), randint(0, 4))
        music.play(music.tonePlayable(523, music.beat(BeatFraction.Sixteenth)), music.PlaybackMode.UntilDone)
        basic.pause(10)
    }
})
states.addLoopHandler("UIIAIOUIIIAI", function () {
    if (input.pinIsPressed(TouchPin.P0)) {
        ebld = 0
    } else if (input.pinIsPressed(TouchPin.P1)) {
        ebld = 1
    } else if (input.pinIsPressed(TouchPin.P2)) {
        ebld = 2
    }
})
function ShowFish () {
    led.unplot(fishX, fishY)
    fishX += -1
    if (fishX == 1) {
        fish_miss += 1
        if (fish_miss >= 5) {
            fish_state = 2
            basic.clearScreen()
            basic.showString("GAME OVER")
            basic.showString("SCORE")
            basic.showNumber(fish_score)
            fish_state = 0
            return
        }
    }
    led.plotBrightness(fishX, fishY, 50)
}
states.setEnterHandler("Flash", function () {
    while (states.matchCurrent("Flash")) {
        basic.showString("Flash!")
        music.play(music.tonePlayable(392, music.beat(BeatFraction.Double)), music.PlaybackMode.InBackground)
        basic.pause(3000)
        music.play(music.tonePlayable(392, music.beat(BeatFraction.Double)), music.PlaybackMode.InBackground)
        basic.showLeds(`
            # . . . .
            # . . . .
            # . . . .
            # . . . .
            # . . . .
            `)
        if (input.buttonIsPressed(Button.B)) {
            states.setState("FlEr")
        }
        basic.pause(3000)
        music.play(music.tonePlayable(392, music.beat(BeatFraction.Double)), music.PlaybackMode.InBackground)
        basic.showLeds(`
            # # . . .
            # # . . .
            # # . . .
            # # . . .
            # # . . .
            `)
        if (input.buttonIsPressed(Button.B)) {
            states.setState("FlEr")
        }
        basic.pause(3000)
        music.play(music.tonePlayable(392, music.beat(BeatFraction.Double)), music.PlaybackMode.InBackground)
        basic.showLeds(`
            # # # . .
            # # # . .
            # # # . .
            # # # . .
            # # # . .
            `)
        if (input.buttonIsPressed(Button.B)) {
            states.setState("FlEr")
        }
        basic.pause(3000)
        music.play(music.tonePlayable(392, music.beat(BeatFraction.Double)), music.PlaybackMode.InBackground)
        basic.showLeds(`
            # # # # .
            # # # # .
            # # # # .
            # # # # .
            # # # # .
            `)
        if (input.buttonIsPressed(Button.B)) {
            states.setState("FlEr")
        }
        basic.pause(3000)
        music.play(music.tonePlayable(392, music.beat(BeatFraction.Double)), music.PlaybackMode.InBackground)
        basic.showLeds(`
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            `)
        basic.pause(3000)
        music.play(music.tonePlayable(392, music.beat(BeatFraction.Double)), music.PlaybackMode.InBackground)
        if (input.buttonIsPressed(Button.B)) {
            states.setState("FlEr")
        }
        basic.showString("Flashing compleeted!")
        states.setState("AUpd")
    }
})
states.addLoopHandler("Error", function () {
    music.play(music.createSoundExpression(WaveShape.Sine, 1, 1002, 255, 255, 500, SoundExpressionEffect.Tremolo, InterpolationCurve.Linear), music.PlaybackMode.UntilDone)
    basic.showLeds(`
        # . # . #
        # . # . #
        # . # . #
        # . . . #
        # . # . #
        `)
    basic.pause(100)
    basic.showLeds(`
        . . . . .
        . # . # .
        . # . # .
        . # . # .
        . . . . .
        `)
})
states.addLoopHandler("OnSDM", function () {
    basic.clearScreen()
    if (appDMod == 0) {
        states.setState("Sleep")
    } else if (appDMod == 1) {
        states.setState("Stall")
    } else if (appDMod == 2) {
        states.setState("Flash")
    } else if (appDMod == 3) {
        states.setState("V")
    }
})
states.addLoopHandler("Sleep", function () {
    basic.pause(500)
    music.play(music.builtinPlayableSoundEffect(soundExpression.yawn), music.PlaybackMode.UntilDone)
    basic.showString("ZZZ")
    if (input.buttonIsPressed(Button.B)) {
        states.setState(states.previousState())
    }
})
states.addLoopHandler("Cloc", function () {
    basic.pause(1000)
    if (input.buttonIsPressed(Button.A)) {
        states.setState("ClocS")
    } else if (input.buttonIsPressed(Button.B)) {
        ModeCloc += 1
    }
})
states.addLoopHandler("Cloc", function () {
    if (ModeCloc == 0) {
        basic.showLeds(`
            . . # . .
            . . # . .
            . . # # .
            . . . . .
            . . . . .
            `)
    } else if (ModeCloc == 1) {
        basic.showLeds(`
            # . # . #
            # . . . #
            # # # # #
            # . . . #
            # # # # #
            `)
    }
})
states.addLoopHandler("Cloc", function () {
    if (ModeCloc == 2) {
        ModeCloc = 0
    }
})
states.setEnterHandler("UIIAIOUIIIAI", function () {
    ebld = 1
})
states.setEnterHandler("Dit", function () {
    basic.showString(timeanddate.date(timeanddate.DateFormat.YYYY_MM_DD))
    states.setState("Cloc")
})
states.setEnterHandler("Tim", function () {
    basic.showString(timeanddate.time(timeanddate.TimeFormat.HHMM24hr))
    states.setState("Cloc")
})
states.addLoopHandler("On", function () {
    if (appSD == 4) {
        appSD = 0
    }
})
states.addLoopHandler("On", function () {
    if (input.buttonIsPressed(Button.A)) {
        states.setState("OnLDD")
    } else if (input.buttonIsPressed(Button.B)) {
        appSD += 1
        basic.pause(1500)
    }
})
states.addLoopHandler("On", function () {
    led.setBrightness(255)
    if (appSD == 0) {
        basic.showLeds(`
            . # # . .
            # # # . .
            . # # # #
            . # # # .
            . . . . .
            `)
    } else if (appSD == 1) {
        basic.showLeds(`
            # # . # #
            # . # . #
            # . . . #
            # . . . #
            # . . . #
            `)
    } else if (appSD == 2) {
        basic.showLeds(`
            . . . . .
            . # # . #
            # . . # #
            . # # . #
            . . . . .
            `)
    } else if (appSD == 3) {
        basic.showLeds(`
            # # # # #
            # . # . #
            # . # # #
            # . . . #
            # # # # #
            `)
    }
})
states.setEnterHandler("Cloc", function () {
    ModeCloc = 0
})
states.setEnterHandler("FlEr", function () {
    basic.showLeds(`
        # . # . #
        # . # . #
        # . # . #
        # . . . #
        # . # . #
        `)
    basic.pause(1000)
    basic.showString("Resume update? [A]Yes [B]No")
    if (input.buttonIsPressed(Button.A)) {
        states.setState("Flash")
    } else if (input.buttonIsPressed(Button.B)) {
        if (randint(0, 2) == 1) {
            states.setState("Error")
        } else {
            states.setState("On")
        }
    }
})
states.setEnterHandler("V", function () {
    basic.showString("V 1.0")
    if (input.buttonIsPressed(Button.A) || input.buttonIsPressed(Button.B)) {
        states.setState("Debug")
    }
})
function ShowFishingLine () {
    if (show_fishingline == 2) {
        fishline_max = 4
        if (fishX == 2) {
            fishline_max = fishY
            fishX = -1
            fishY = -1
            fish_score += 10
        }
        for (let index = 0; index <= fishline_max - 1; index++) {
            led.plotBrightness(2, 1 + index, 100)
        }
    } else if (show_fishingline == 1) {
        for (let index2 = 0; index2 <= 3; index2++) {
            led.unplot(2, 4 - index2)
        }
    }
}
states.addLoopHandler("Debug", function () {
    if (appDMod == 4) {
        appDMod = 0
    }
})
states.addLoopHandler("Debug", function () {
    if (input.buttonIsPressed(Button.A)) {
        states.setState("OnSDM")
    } else if (input.buttonIsPressed(Button.B)) {
        appDMod += 1
        basic.pause(1500)
    }
})
states.addLoopHandler("Debug", function () {
    led.setBrightness(255)
    if (appDMod == 0) {
        basic.showLeds(`
            . . . # .
            . . # # .
            . # # # .
            . . # # .
            . . . # .
            `)
    } else if (appDMod == 1) {
        basic.showLeds(`
            # . . . #
            . # . # .
            . . # . .
            . # . # .
            # . . . #
            `)
    } else if (appDMod == 2) {
        basic.showLeds(`
            . . . . .
            . # . # .
            # . . . #
            . # . # .
            . . . . .
            `)
    } else if (appDMod == 3) {
        basic.showLeds(`
            . . . # #
            . . . . #
            # . # # .
            # . # . .
            . # . # .
            `)
    }
})
states.addLoopHandler("ClocS", function () {
    basic.clearScreen()
    if (ModeCloc == 0) {
        states.setState("Tim")
    } else if (ModeCloc == 1) {
        states.setState("Dit")
    }
})
states.addLoopHandler("OnLDD", function () {
    basic.clearScreen()
    if (appSD == 0) {
        states.setState("UIIAIOUIIIAI")
    } else if (appSD == 1) {
        states.setState("Mario")
    } else if (appSD == 2) {
        states.setState("Fis")
    } else if (appSD == 3) {
        states.setState("Cloc")
    }
})
states.setEnterHandler("Debug", function () {
    appDMod = 0
    music.play(music.builtinPlayableSoundEffect(soundExpression.twinkle), music.PlaybackMode.UntilDone)
    basic.showString("DM")
    basic.showLeds(`
        . # # # .
        . # # # #
        . . # . .
        . . # . .
        . . # . .
        `)
    basic.pause(250)
})
function show_obs () {
    if (state != 0) {
        return
    }
    if (obs1 != -1) {
        if (obs1_status == 0) {
            led.unplot(obs1, 3)
            led.unplot(obs1, 4)
            obs1 += -1
            led.plot(obs1, 3)
            led.plot(obs1, 4)
        } else {
            led.unplot(obs1, 1)
            led.unplot(obs1, 2)
            led.unplot(obs1, 3)
            obs1 += -1
            led.plot(obs1, 1)
            led.plot(obs1, 2)
            led.plot(obs1, 3)
        }
    }
    if (obs2 != -1) {
        if (obs2_status == 0) {
            led.unplot(obs2, 3)
            led.unplot(obs2, 4)
            obs2 += -1
            led.plot(obs2, 3)
            led.plot(obs2, 4)
        } else {
            led.unplot(obs2, 1)
            led.unplot(obs2, 2)
            led.unplot(obs2, 3)
            obs2 += -1
            led.plot(obs2, 1)
            led.plot(obs2, 2)
            led.plot(obs2, 3)
        }
    }
}
states.setEnterHandler("AUpd", function () {
    basic.showString("Restart? [A] Yes [B] No")
    basic.showLeds(`
        . # # # .
        # . . . #
        # . . . #
        # . . . #
        . # # # .
        `)
    while (true) {
        if (input.buttonIsPressed(Button.A)) {
            control.reset()
        } else if (input.buttonIsPressed(Button.B)) {
            states.setState("On")
        }
    }
})
states.addLoopHandler("Mario", function () {
    if (state == -1) {
        basic.showLeds(`
            # # . # #
            # # # # #
            # . # . #
            # . . . #
            # . . . #
            `)
        motion = 0
        motion_lock = 0
        obs1 = -1
        obs1_status = -1
        obs2 = -1
        obs2_status = -1
        score = 0
        fail = 0
    } else if (state == 0) {
        basic.clearScreen()
        if (obs1 == -1) {
            if (obs2 == -1 || (0 as any) <= (1 as any)) {
                obs1_status = randint(0, 1)
                obs1 = 5
            }
        }
        if (obs2 == -1) {
            if (obs1 == -1 || obs1 <= 1) {
                obs2_status = randint(0, 1)
                obs2 = 5
            }
        }
        pass = 0
        show_mario()
        check()
        show_obs()
        check()
        if (pass == 1) {
            score += 5
        }
    } else {
    	
    }
    basic.pause(500)
})
states.addLoopHandler("Mario", function () {
    if (input.buttonIsPressed(Button.A)) {
        if (state == -1) {
            basic.clearScreen()
            state = 0
        } else if (state == 0) {
            if (motion == 0) {
                motion = 2
                motion_lock = 1
            }
        }
    }
})
states.addLoopHandler("Mario", function () {
    if (input.buttonIsPressed(Button.B)) {
        if (state == 0) {
            if (motion == 0) {
                motion = 1
                motion_lock = 2
            }
        }
    }
})
function show_mario () {
    if (state != 0) {
        return
    }
    if (motion == 0) {
        led.plot(0, 3)
        led.plot(0, 4)
    } else if (motion == 1) {
        if (motion_lock >= 1) {
            if (motion_lock == 2) {
                led.unplot(0, 3)
            }
            led.plot(0, 4)
            basic.pause(200)
            motion_lock += -1
        } else {
            led.plot(0, 3)
            led.plot(0, 4)
            motion = 0
        }
    } else if (motion == 2) {
        if (motion_lock == 1) {
            led.unplot(0, 4)
            led.plot(0, 2)
            led.plot(0, 3)
            basic.pause(200)
            led.unplot(0, 3)
            led.plot(0, 1)
            basic.pause(200)
            led.unplot(0, 2)
            led.plot(0, 0)
            basic.pause(200)
            motion_lock = 0
        } else {
            led.plot(0, 0)
            led.plot(0, 1)
            basic.pause(200)
            motion = 3
        }
    } else if (motion == 3) {
        led.unplot(0, 0)
        led.plot(0, 1)
        led.plot(0, 2)
        basic.pause(200)
        led.unplot(0, 1)
        led.plot(0, 3)
        basic.pause(200)
        led.unplot(0, 2)
        led.plot(0, 4)
        motion = 0
    }
}
states.addLoopHandler("Fis", function () {
    if (fish_state == 1 && input.buttonIsPressed(Button.A)) {
        show_fishingline = 2
    }
})
states.addLoopHandler("Fis", function () {
    if (fish_state == 0 && input.buttonIsPressed(Button.A)) {
        fish_state = 1
        basic.clearScreen()
        led.plot(2, 0)
    }
})
states.addLoopHandler("Fis", function () {
    if (fish_state == 0) {
        basic.showLeds(`
            . # # . .
            # . # . #
            # . # # #
            # . # . #
            . # # . .
            `)
        show_fishingline = 0
        fishX = -1
        fishY = -1
        speed = 10
        fish_miss = 0
        fish_score = 0
    } else if (fish_state == 1) {
        if (show_fishingline == 2) {
            ShowFishingLine()
            show_fishingline = 1
        } else if (show_fishingline == 1) {
            ShowFishingLine()
            show_fishingline = 0
        }
        if (fishX == -1) {
            fishX = 5
            fishY = randint(2, 4)
        } else {
            if (speed <= 0) {
                if (fish_score >= 200) {
                    speed = 1
                } else if (fish_score >= 100) {
                    speed = 3
                } else if (fish_score >= 50) {
                    speed = 5
                } else {
                    speed = 10
                }
                ShowFish()
            } else {
                speed += -1
            }
        }
    } else {
    	
    }
    basic.pause(100)
})
let speed = 0
let motion_lock = 0
let fishline_max = 0
let show_fishingline = 0
let ModeCloc = 0
let appDMod = 0
let fish_score = 0
let fish_miss = 0
let fishY = 0
let fishX = 0
let ebld = 0
let appSD = 0
let fish_state = 0
let score = 0
let obs2_status = 0
let pass = 0
let fail = 0
let motion = 0
let obs1_status = 0
let obs2 = 0
let obs1 = 0
let state = 0
music.play(music.builtinPlayableSoundEffect(soundExpression.hello), music.PlaybackMode.UntilDone)
basic.showString("Dev")
basic.pause(100)
basic.showLeds(`
    # . # . .
    # # # . #
    # . # # #
    # . # . #
    . . # . #
    `)
basic.pause(1000)
if (input.buttonIsPressed(Button.A)) {
    states.setState("Debug")
} else if (input.buttonIsPressed(Button.B)) {
    states.setState("Error")
} else {
    states.setState("On")
}
basic.forever(function () {
    if (input.logoIsPressed() && input.buttonIsPressed(Button.B)) {
        if (states.matchPrevious("On")) {
            states.setState("On")
        } else if (states.matchPrevious("OnSDM")) {
            states.setState("OnSDM")
        }
    }
})
