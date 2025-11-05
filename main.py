def check():
    global fail, pass2, state
    if state != 0:
        return
    if obs1 == 0:
        if obs1_status == 0:
            if motion == 0 or motion == 1:
                fail = 1
            else:
                pass2 = 1
        else:
            if motion == 1:
                pass2 = 1
            else:
                fail = 1
    elif obs2 == 0:
        if obs2_status == 0:
            if motion == 0 or motion == 1:
                fail = 1
            else:
                pass2 = 1
        else:
            if motion == 1:
                pass2 = 1
            else:
                fail = 1
    if fail == 1:
        state = 1
        basic.clear_screen()
        basic.show_string("GAME OVER")
        basic.show_string("SCORE")
        basic.show_number(score)
        state = -1

def on_set_enter_handler():
    global state
    state = -1
states.set_enter_handler("Mario", on_set_enter_handler)

def on_set_enter_handler2():
    global fish_state
    fish_state = 0
states.set_enter_handler("Fis", on_set_enter_handler2)

def on_add_loop_handler():
    music.play(music.builtin_playable_sound_effect(soundExpression.giggle),
        music.PlaybackMode.LOOPING_IN_BACKGROUND)
    basic.show_string("STALLING!")
states.add_loop_handler("Stall", on_add_loop_handler)

def on_add_loop_handler2():
    if input.button_is_pressed(Button.B):
        basic.clear_screen()
        music.stop_all_sounds()
        states.set_state("FlEr")
states.add_loop_handler("Flash", on_add_loop_handler2)

def on_set_enter_handler3():
    global appSD
    appSD = 0
states.set_enter_handler("On", on_set_enter_handler3)

def on_add_loop_handler3():
    basic.clear_screen()
    if ebld == 1:
        led.plot(randint(0, 4), randint(0, 4))
    elif ebld == 2:
        led.plot(randint(0, 4), randint(0, 4))
        music.play(music.tone_playable(523, music.beat(BeatFraction.SIXTEENTH)),
            music.PlaybackMode.UNTIL_DONE)
        basic.pause(10)
states.add_loop_handler("UIIAIOUIIIAI", on_add_loop_handler3)

def on_add_loop_handler4():
    global ebld
    if input.pin_is_pressed(TouchPin.P0):
        ebld = 0
    elif input.pin_is_pressed(TouchPin.P1):
        ebld = 1
    elif input.pin_is_pressed(TouchPin.P2):
        ebld = 2
states.add_loop_handler("UIIAIOUIIIAI", on_add_loop_handler4)

def ShowFish():
    global fishX, fish_miss, fish_state
    led.unplot(fishX, fishY)
    fishX += -1
    if fishX == 1:
        fish_miss += 1
        if fish_miss >= 5:
            fish_state = 2
            basic.clear_screen()
            basic.show_string("GAME OVER")
            basic.show_string("SCORE")
            basic.show_number(fish_score)
            fish_state = 0
            return
    led.plot_brightness(fishX, fishY, 50)

def on_set_enter_handler4():
    while states.match_current("Flash"):
        basic.show_string("Flash!")
        music.play(music.tone_playable(392, music.beat(BeatFraction.DOUBLE)),
            music.PlaybackMode.IN_BACKGROUND)
        basic.pause(3000)
        music.play(music.tone_playable(392, music.beat(BeatFraction.DOUBLE)),
            music.PlaybackMode.IN_BACKGROUND)
        basic.show_leds("""
            # . . . .
            # . . . .
            # . . . .
            # . . . .
            # . . . .
            """)
        basic.pause(3000)
        music.play(music.tone_playable(392, music.beat(BeatFraction.DOUBLE)),
            music.PlaybackMode.IN_BACKGROUND)
        basic.show_leds("""
            # # . . .
            # # . . .
            # # . . .
            # # . . .
            # # . . .
            """)
        basic.pause(3000)
        music.play(music.tone_playable(392, music.beat(BeatFraction.DOUBLE)),
            music.PlaybackMode.IN_BACKGROUND)
        basic.show_leds("""
            # # # . .
            # # # . .
            # # # . .
            # # # . .
            # # # . .
            """)
        basic.pause(3000)
        music.play(music.tone_playable(392, music.beat(BeatFraction.DOUBLE)),
            music.PlaybackMode.IN_BACKGROUND)
        basic.show_leds("""
            # # # # .
            # # # # .
            # # # # .
            # # # # .
            # # # # .
            """)
        basic.pause(3000)
        music.play(music.tone_playable(392, music.beat(BeatFraction.DOUBLE)),
            music.PlaybackMode.IN_BACKGROUND)
        basic.show_leds("""
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            """)
        basic.pause(3000)
        music.play(music.tone_playable(392, music.beat(BeatFraction.DOUBLE)),
            music.PlaybackMode.IN_BACKGROUND)
        basic.show_string("Flashing compleeted!")
        control.reset()
states.set_enter_handler("Flash", on_set_enter_handler4)

def on_add_loop_handler5():
    music.play(music.create_sound_expression(WaveShape.SINE,
            1,
            1002,
            255,
            255,
            500,
            SoundExpressionEffect.TREMOLO,
            InterpolationCurve.LINEAR),
        music.PlaybackMode.UNTIL_DONE)
    basic.show_leds("""
        # . # . #
        # . # . #
        # . # . #
        # . . . #
        # . # . #
        """)
    basic.pause(100)
    basic.show_leds("""
        . . . . .
        . # . # .
        . # . # .
        . # . # .
        . . . . .
        """)
states.add_loop_handler("Error", on_add_loop_handler5)

def on_add_loop_handler6():
    basic.clear_screen()
    if appDMod == 0:
        states.set_state("Sleep")
    elif appDMod == 1:
        states.set_state("Stall")
    elif appDMod == 2:
        states.set_state("Flash")
    elif appDMod == 3:
        states.set_state("V")
states.add_loop_handler("OnSDM", on_add_loop_handler6)

def on_add_loop_handler7():
    basic.pause(500)
    music.play(music.builtin_playable_sound_effect(soundExpression.yawn),
        music.PlaybackMode.UNTIL_DONE)
    basic.show_string("ZZZ")
    if input.button_is_pressed(Button.B):
        states.set_state("Debug")
states.add_loop_handler("Sleep", on_add_loop_handler7)

def on_add_loop_handler8():
    global ModeCloc
    basic.pause(1000)
    if input.button_is_pressed(Button.A):
        states.set_state("ClocS")
    elif input.button_is_pressed(Button.B):
        ModeCloc += 1
states.add_loop_handler("Cloc", on_add_loop_handler8)

def on_add_loop_handler9():
    if ModeCloc == 0:
        basic.show_leds("""
            . . # . .
            . . # . .
            . . # # .
            . . . . .
            . . . . .
            """)
    elif ModeCloc == 1:
        basic.show_leds("""
            # . # . #
            # . . . #
            # # # # #
            # . . . #
            # # # # #
            """)
states.add_loop_handler("Cloc", on_add_loop_handler9)

def on_add_loop_handler10():
    global ModeCloc
    if ModeCloc == 2:
        ModeCloc = 0
states.add_loop_handler("Cloc", on_add_loop_handler10)

def on_set_enter_handler5():
    global ebld
    ebld = 1
states.set_enter_handler("UIIAIOUIIIAI", on_set_enter_handler5)

def on_set_enter_handler6():
    basic.show_string(timeanddate.date(timeanddate.DateFormat.YYYY_MM_DD))
    states.set_state("Cloc")
states.set_enter_handler("Dit", on_set_enter_handler6)

def on_set_enter_handler7():
    basic.show_string(timeanddate.time(timeanddate.TimeFormat.HHMM2_4HR))
    states.set_state("Cloc")
states.set_enter_handler("Tim", on_set_enter_handler7)

def on_add_loop_handler11():
    global appSD
    if appSD == 4:
        appSD = 0
states.add_loop_handler("On", on_add_loop_handler11)

def on_add_loop_handler12():
    global appSD
    basic.pause(3000)
    if input.button_is_pressed(Button.A):
        states.set_state("OnLDD")
    elif input.button_is_pressed(Button.B):
        appSD += 1
states.add_loop_handler("On", on_add_loop_handler12)

def on_add_loop_handler13():
    led.set_brightness(255)
    if appSD == 0:
        basic.show_leds("""
            . # # . .
            # # # . .
            . # # # #
            . # # # .
            . . . . .
            """)
    elif appSD == 1:
        basic.show_leds("""
            # # . # #
            # . # . #
            # . . . #
            # . . . #
            # . . . #
            """)
    elif appSD == 2:
        basic.show_leds("""
            . . . . .
            . # # . #
            # . . # #
            . # # . #
            . . . . .
            """)
    elif appSD == 3:
        basic.show_leds("""
            # # # # #
            # . # . #
            # . # # #
            # . . . #
            # # # # #
            """)
states.add_loop_handler("On", on_add_loop_handler13)

def on_set_enter_handler8():
    global ModeCloc
    ModeCloc = 0
states.set_enter_handler("Cloc", on_set_enter_handler8)

def on_set_enter_handler9():
    basic.show_leds("""
        # . # . #
        # . # . #
        # . # . #
        # . . . #
        # . # . #
        """)
    basic.pause(1000)
    basic.show_string("Resume update? [A]Yes [B]No")
    if input.button_is_pressed(Button.A):
        states.set_state("Flash")
    elif input.button_is_pressed(Button.B):
        if randint(0, 2) == 1:
            states.set_state("Error")
        else:
            states.set_state("On")
states.set_enter_handler("FlEr", on_set_enter_handler9)

def on_set_enter_handler10():
    basic.show_string("V 1.0")
    states.set_state("OnSDM")
states.set_enter_handler("V", on_set_enter_handler10)

def ShowFishingLine():
    global fishline_max, fishX, fishY, fish_score
    if show_fishingline == 2:
        fishline_max = 4
        if fishX == 2:
            fishline_max = fishY
            fishX = -1
            fishY = -1
            fish_score += 10
        index = 0
        while index <= fishline_max - 1:
            led.plot_brightness(2, 1 + index, 100)
            index += 1
    elif show_fishingline == 1:
        for index2 in range(4):
            led.unplot(2, 4 - index2)

def on_add_loop_handler14():
    global appDMod
    if appDMod == 4:
        appDMod = 0
states.add_loop_handler("Debug", on_add_loop_handler14)

def on_add_loop_handler15():
    global appDMod
    basic.pause(3000)
    if input.button_is_pressed(Button.A):
        states.set_state("OnSDM")
    elif input.button_is_pressed(Button.B):
        appDMod += 1
states.add_loop_handler("Debug", on_add_loop_handler15)

def on_add_loop_handler16():
    led.set_brightness(255)
    if appDMod == 0:
        basic.show_leds("""
            . . . # .
            . . # # .
            . # # # .
            . . # # .
            . . . # .
            """)
    elif appDMod == 1:
        basic.show_leds("""
            # . . . #
            . # . # .
            . . # . .
            . # . # .
            # . . . #
            """)
    elif appDMod == 2:
        basic.show_leds("""
            . . . . .
            . # . # .
            # . . . #
            . # . # .
            . . . . .
            """)
    elif appDMod == 3:
        basic.show_leds("""
            . . . # #
            . . . . #
            # . # # .
            # . # . .
            . # . # .
            """)
states.add_loop_handler("Debug", on_add_loop_handler16)

def on_add_loop_handler17():
    basic.clear_screen()
    if ModeCloc == 0:
        states.set_state("Tim")
    elif ModeCloc == 1:
        states.set_state("Dit")
states.add_loop_handler("ClocS", on_add_loop_handler17)

def on_add_loop_handler18():
    basic.clear_screen()
    if appSD == 0:
        states.set_state("UIIAIOUIIIAI")
    elif appSD == 1:
        states.set_state("Mario")
    elif appSD == 2:
        states.set_state("Fis")
    elif appSD == 3:
        states.set_state("Cloc")
states.add_loop_handler("OnLDD", on_add_loop_handler18)

def on_set_enter_handler11():
    global appDMod
    appDMod = 0
    music.play(music.builtin_playable_sound_effect(soundExpression.twinkle),
        music.PlaybackMode.UNTIL_DONE)
    basic.show_string("DEBUG MODE!")
states.set_enter_handler("Debug", on_set_enter_handler11)

def show_obs():
    global obs1, obs2
    if state != 0:
        return
    if obs1 != -1:
        if obs1_status == 0:
            led.unplot(obs1, 3)
            led.unplot(obs1, 4)
            obs1 += -1
            led.plot(obs1, 3)
            led.plot(obs1, 4)
        else:
            led.unplot(obs1, 1)
            led.unplot(obs1, 2)
            led.unplot(obs1, 3)
            obs1 += -1
            led.plot(obs1, 1)
            led.plot(obs1, 2)
            led.plot(obs1, 3)
    if obs2 != -1:
        if obs2_status == 0:
            led.unplot(obs2, 3)
            led.unplot(obs2, 4)
            obs2 += -1
            led.plot(obs2, 3)
            led.plot(obs2, 4)
        else:
            led.unplot(obs2, 1)
            led.unplot(obs2, 2)
            led.unplot(obs2, 3)
            obs2 += -1
            led.plot(obs2, 1)
            led.plot(obs2, 2)
            led.plot(obs2, 3)

def on_add_loop_handler19():
    global motion, motion_lock, obs1, obs1_status, obs2, obs2_status, score, fail, pass2
    if state == -1:
        basic.show_leds("""
            # # . # #
            # # # # #
            # . # . #
            # . . . #
            # . . . #
            """)
        motion = 0
        motion_lock = 0
        obs1 = -1
        obs1_status = -1
        obs2 = -1
        obs2_status = -1
        score = 0
        fail = 0
    elif state == 0:
        basic.clear_screen()
        if obs1 == -1:
            if obs2 == -1 or (0) <= (1):
                obs1_status = randint(0, 1)
                obs1 = 5
        if obs2 == -1:
            if obs1 == -1 or obs1 <= 1:
                obs2_status = randint(0, 1)
                obs2 = 5
        pass2 = 0
        show_mario()
        check()
        show_obs()
        check()
        if pass2 == 1:
            score += 5
    else:
        pass
    basic.pause(500)
states.add_loop_handler("Mario", on_add_loop_handler19)

def on_add_loop_handler20():
    global state, motion, motion_lock
    if input.button_is_pressed(Button.A):
        if state == -1:
            basic.clear_screen()
            state = 0
        elif state == 0:
            if motion == 0:
                motion = 2
                motion_lock = 1
states.add_loop_handler("Mario", on_add_loop_handler20)

def on_add_loop_handler21():
    global motion, motion_lock
    if input.button_is_pressed(Button.B):
        if state == 0:
            if motion == 0:
                motion = 1
                motion_lock = 2
states.add_loop_handler("Mario", on_add_loop_handler21)

def show_mario():
    global motion_lock, motion
    if state != 0:
        return
    if motion == 0:
        led.plot(0, 3)
        led.plot(0, 4)
    elif motion == 1:
        if motion_lock >= 1:
            if motion_lock == 2:
                led.unplot(0, 3)
            led.plot(0, 4)
            basic.pause(200)
            motion_lock += -1
        else:
            led.plot(0, 3)
            led.plot(0, 4)
            motion = 0
    elif motion == 2:
        if motion_lock == 1:
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
        else:
            led.plot(0, 0)
            led.plot(0, 1)
            basic.pause(200)
            motion = 3
    elif motion == 3:
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

def on_add_loop_handler22():
    global show_fishingline
    if fish_state == 1 and input.button_is_pressed(Button.A):
        show_fishingline = 2
states.add_loop_handler("Fis", on_add_loop_handler22)

def on_add_loop_handler23():
    global fish_state
    if fish_state == 0 and input.button_is_pressed(Button.A):
        fish_state = 1
        basic.clear_screen()
        led.plot(2, 0)
states.add_loop_handler("Fis", on_add_loop_handler23)

def on_add_loop_handler24():
    global show_fishingline, fishX, fishY, speed, fish_miss, fish_score
    if fish_state == 0:
        basic.show_leds("""
            . # # . .
            # . # . #
            # . # # #
            # . # . #
            . # # . .
            """)
        show_fishingline = 0
        fishX = -1
        fishY = -1
        speed = 10
        fish_miss = 0
        fish_score = 0
    elif fish_state == 1:
        if show_fishingline == 2:
            ShowFishingLine()
            show_fishingline = 1
        elif show_fishingline == 1:
            ShowFishingLine()
            show_fishingline = 0
        if fishX == -1:
            fishX = 5
            fishY = randint(2, 4)
        else:
            if speed <= 0:
                if fish_score >= 200:
                    speed = 1
                elif fish_score >= 100:
                    speed = 3
                elif fish_score >= 50:
                    speed = 5
                else:
                    speed = 10
                ShowFish()
            else:
                speed += -1
    else:
        pass
    basic.pause(100)
states.add_loop_handler("Fis", on_add_loop_handler24)

speed = 0
motion_lock = 0
fishline_max = 0
show_fishingline = 0
ModeCloc = 0
appDMod = 0
fish_score = 0
fish_miss = 0
fishY = 0
fishX = 0
ebld = 0
appSD = 0
fish_state = 0
score = 0
obs2_status = 0
pass2 = 0
fail = 0
motion = 0
obs1_status = 0
obs2 = 0
obs1 = 0
state = 0
music.play(music.builtin_playable_sound_effect(soundExpression.hello),
    music.PlaybackMode.UNTIL_DONE)
basic.show_icon(IconNames.HAPPY)
basic.pause(1000)
basic.clear_screen()
if input.button_is_pressed(Button.A):
    states.set_state("Debug")
elif input.button_is_pressed(Button.B):
    states.set_state("Error")
else:
    states.set_state("On")

def on_forever():
    if input.logo_is_pressed() and input.button_is_pressed(Button.B):
        states.set_state("On")
basic.forever(on_forever)
