function in_ten_cm () {
	
}
function red_light () {
    bitbot.goms(BBDirection.Reverse, 60, 400)
    bitbot.driveTurnMilliseconds(BBRobotDirection.Left, 487, 500)
}
let left_sensor = 0
let right_sensor = 0
bitbot.select_model(BBModel.XL)
basic.forever(function () {
    serial.writeLine("" + bitbot.sonar(BBPingUnit.Centimeters))
    bitbot.go(BBDirection.Forward, 60)
    right_sensor = bitbot.readLight(BBLightSensor.Right)
    left_sensor = bitbot.readLight(BBLightSensor.Left)
    bitbot.motor(BBMotor.Right, left_sensor)
    bitbot.motor(BBMotor.Left, right_sensor)
    if (bitbot.readLight(BBLightSensor.Left) > 10) {
        bitbot.setLedColor(0x80FF80)
        bitbot.ledRainbow()
        bitbot.ledBrightness(60)
        bitbot.go(BBDirection.Forward, 60)
        basic.showLeds(`
            . . . # .
            # # # . #
            # . # . #
            # # # # #
            . . # . #
            `)
    } else if (bitbot.readLight(BBLightSensor.Right) < 10) {
        bitbot.setLedColor(0xFF0000)
        bitbot.ledBrightness(60)
        bitbot.stop(BBStopMode.Brake)
        basic.showLeds(`
            # . # . #
            . # . # .
            # . # . #
            . # . # .
            # . # . #
            `)
    }
})
