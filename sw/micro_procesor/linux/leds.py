# LEDs toggle every 1 second

import time


def ledRGBon():
        red = open("/sys/class/leds/led_r/brightness", "w")
        green = open("/sys/class/leds/led_g/brightness", "w")
        blue = open("/sys/class/leds/led_b/brightness", "w")

        red.write(str(1))
        green.write(str(1))
        blue.write(str(1))

        red.close()
        green.close()
        blue.close()


def ledRGBoff():
        red = open("/sys/class/leds/led_r/brightness", "w")
        green = open("/sys/class/leds/led_g/brightness", "w")
        blue = open("/sys/class/leds/led_b/brightness", "w")

        red.write(str(0))
        green.write(str(0))
        blue.write(str(0))

        red.close()
        green.close()
        blue.close()


while(1):
    ledRGBoff()
    time.sleep(1)
    ledRGBon()
    time.sleep(1)
