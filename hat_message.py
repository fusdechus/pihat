#! /usr/bin/python
from sense_hat import SenseHat
sense = SenseHat ()
import time
for i in range (10, 20): 
    for i in range (2, 20):
        if 3%i == 0:
            j=3/i
            from sense_hat import SenseHat
            import random
            sense = SenseHat()
            e = random.randint(0,255)
            print("the random number is"), r, ("this time")
            r = (e, e+100, e)

            pixels = [
        r, r, r, r, r, r, r, r,
        r, r, r, r, r, r, r, r,
        r, r, r, r, r, r, r, r,
        r, r, r, r, r, r, r, r,
        r, r, r, r, r, r, r, r, 
        r, r, r, r, r, r, r, r,
        r, r, r, r, r, r, r, r,
        r, r, r, r, r, r, r, r, 
]           
        
        time.sleep(.3)
        sense.clear()
        print("no")
        break
    else:
        from sense_hat import SenseHat
        sense = SenseHat()
        print ("2")

        sense.clear()
