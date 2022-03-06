import machine, rp2, time
from machine import Pin
#GPIO 27
Red    = Pin(13, Pin.OUT, value=1, drive=Pin.HIGH_POWER)
#GPIO 23
Green  = Pin(16, Pin.OUT, value=1, drive=Pin.HIGH_POWER)
#GPIO 24
Blue   = Pin(18, Pin.OUT, value=1, drive=Pin.HIGH_POWER)
#GPIO 22 & Pin 17 (3V3)
Button = Pin(15, Pin.IN, pull=Pin.PULL_DOWN)

modes = [0,1,2,3,4,5,6,7]
mode = modes[0]

#forever loop
while True:
    # Button press
    if Button.value = 1:
        #Off
        if mode == 7:
            mode = modes[0]
            Red.value(1)
            Red.drive(Pin.HIGH_POWER)
            Blue.value(1)
            Blue.drive(Pin.HIGH_POWER)
            Green.value(1)
            Green.drive(Pin.HIGH_POWER)
        #Next Mode
        else:
            mode = modes[mode+1]
            #Red
            if mode == 1:
                Red.value(0)
                Red.drive(Pin.LOW_POWER)
                Blue.value(1)
                Blue.drive(Pin.HIGH_POWER)
                Green.value(1)
                Green.drive(Pin.HIGH_POWER)
            #Blue
            if mode == 2:
                Red.value(1)
                Red.drive(Pin.HIGH_POWER)
                Blue.value(0)
                Blue.drive(Pin.LOW_POWER)
                Green.value(1)
                Green.drive(Pin.HIGH_POWER)
            #Green
            if mode == 3:
                Red.value(1)
                Red.drive(Pin.HIGH_POWER)
                Blue.value(1)
                Blue.drive(Pin.HIGH_POWER)
                Green.value(0)
                Green.drive(Pin.LOW_POWER)
            #Cyan
            if mode == 4:
                Red.value(1)
                Red.drive(Pin.HIGH_POWER)
                Blue.value(0)
                Blue.drive(Pin.LOW_POWER)
                Green.value(0)
                Green.drive(Pin.LOW_POWER)
            #Magenta
            if mode == 5:
                Red.value(0)
                Red.drive(Pin.LOW_POWER)
                Blue.value(0)
                Blue.drive(Pin.LOW_POWER)
                Green.value(1)
                Green.drive(Pin.HIGH_POWER)
            #Yellow
            if mode == 6:
                Red.value(0)
                Red.drive(Pin.LOW_POWER)
                Blue.value(1)
                Blue.drive(Pin.HIGH_POWER)
                Green.value(0)
                Green.drive(Pin.LOW_POWER)
            #Orange // a test
            if mode == 7:
                Red.value(0)
                Red.drive(Pin.LOW_POWER)
                Blue.value(1)
                Blue.drive(Pin.HIGH_POWER)
                Green.value(0)
                Green.drive(Pin.MED_POWER)
        # A 1 second pause in the loop so it doesn't jump 100 times
        time.sleep(1)