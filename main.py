left_sensor = 0
right_sensor = 0
distance = 0
bitbot.select_model(BBModel.XL)



def in_ten_cm():
    pass
def red_light():
    bitbot.goms(BBDirection.REVERSE, 60, 400)
    bitbot.drive_turn_milliseconds(BBRobotDirection.LEFT, 487, 500)

def on_forever():
    serial.write_line("" + str(bitbot.sonar(BBPingUnit.CENTIMETERS)))
    bitbot.go(BBDirection.FORWARD, 60)
    global distance, right_sensor, left_sensor
    distance = bitbot.sonar(BBPingUnit.CENTIMETERS)
    right_sensor = bitbot.read_light(BBLightSensor.RIGHT)
    left_sensor = bitbot.read_light(BBLightSensor.LEFT)
    bitbot.motor(BBMotor.RIGHT, left_sensor)
    bitbot.motor(BBMotor.LEFT, right_sensor)

    if bitbot.read_light(BBLightSensor.LEFT) > 10:
        bitbot.set_led_color(0x80FF80)
        bitbot.led_brightness(60)
        bitbot.go(BBDirection.FORWARD, 60)
        basic.show_leds("""
            . . . # .
            # # # . #
            # . # . #
            # # # # #
            . . # . #
            """)
    else:
        bitbot.set_led_color(0xFF0000)
        bitbot.led_brightness(60)
        red_light()
        basic.show_leds("""
            # . # . #
            . # . # .
            # . # . #
            . # . # .
            # . # . #
            """)
basic.forever(on_forever)
