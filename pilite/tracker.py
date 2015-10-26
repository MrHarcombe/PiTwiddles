import sys, serial

try:
    s = serial.Serial("/dev/ttyAMA0", 9600, timeout=1)
    s.open()
    s.write("$$$ALL,OFF\r")
    x, y = 0, 1
    down = True
    while True:
        print("Now at (%d,%d)\n" % (x, y))
        s.write("$$$P%d,%d,OFF\r" % (x, y))
        if down:
            if y % 2 == 1:
                if x == 14:
                    y += 1
                    # print("x rightmost, inc y")
                else:
                    x += 1
                    # print("inc x")
            else:
                if x == 1:
                    y += 1
                    # print("x leftmost, inc y")
                else:
                    x -= 1
                    # print("dec x")
        else:
            if y % 2 == 1:
                if x == 14:
                    y -= 1
                else:
                    x += 1
            else:
                if x == 1:
                    y -= 1
                else:
                    x -= 1

        if x == 1 and y == 1:
            down = True
        elif x == 14 and y == 9:
            down = False

        s.write("$$$P%d,%d,ON\r" % (x, y))
        
except serial.SerialException, se:
    sys.stderr.write("error drawing tracker: %s\n" % (se))
    sys.exit(1)
