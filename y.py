import time
want = open("dream.txt","r")
def outhink(want):
    space = " " * 4
    for i in range(2):
        print
        time.sleep(.8)
        for everything in want:
            print space + everything,
            time.sleep(.05)
            # same
        print "\n\n\t\t",
        print i+1,
        print " sheep"
        want.seek(0)
ou = "secondary person"
