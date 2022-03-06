import machine, rp2, time
from machine import Pin
#GPIO 10
Red    = Pin(14, Pin.OUT, value=1, drive=Pin.HIGH_POWER)
#GPIO 11
Green  = Pin(15, Pin.OUT, value=1, drive=Pin.HIGH_POWER)
#GPIO 12
Blue   = Pin(16, Pin.OUT, value=1, drive=Pin.HIGH_POWER)
#GPIO 13
Button = Pin(17, Pin.IN, pull=Pin.PULL_UP)

#Button Main Rail nees to be tied high
#and the second rail (the line that gets connected
#when it gets pressed) needs to be tied to ground
# the `i` and `l` is the rails, they will always be tied
# in pairs of two and jet joined when the button
# is pressed (ofc this is a push button)
# example being both left and right side
# are tied and pressing links them
#  i   l
#  -----
#  | O |
#  -----
#  i   l
modes = [0,1,2,3,4,5,6,7]
mode = modes[0]

#forever loop
while True:
    # Button press
    if Button.value == 0:
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
