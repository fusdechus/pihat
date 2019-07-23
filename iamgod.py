#! /usr/bin/python
for i in range (10, 20): 
    for i in range (2, 20):
        if 3%i == 0:
            j=3/i
            from sense_hat import SenseHat
            import time
            sense = SenseHat()

            blue = (0, 0, 255)
            red = (255, 0, 0)
            yellow = (255, 255, 0)

            sense.set_pixel(0, 0, blue)
            sense.set_pixel(0, 1, blue)
            sense.set_pixel(1, 0, blue)
            sense.set_pixel(2, 0, blue)
            sense.set_pixel(0, 2, blue)
            sense.set_pixel(1, 1, blue)
            sense.set_pixel(1, 2, blue)
            sense.set_pixel(2, 1, blue)
            sense.set_pixel(2, 2, blue)
            sense.set_pixel(7, 0, blue)
            sense.set_pixel(6, 0, blue)
            sense.set_pixel(5, 0, blue)
            sense.set_pixel(7, 1, blue)
            sense.set_pixel(6, 1, blue)
            sense.set_pixel(5, 1, blue)
            sense.set_pixel(7, 2, blue)
            sense.set_pixel(6, 2, blue)
            sense.set_pixel(5, 2, blue)
            sense.set_pixel(3, 7, yellow)
            sense.set_pixel(2, 6, yellow)
            sense.set_pixel(2, 5, yellow)
            sense.set_pixel(2, 4, yellow)
            sense.set_pixel(2, 3, yellow)
            sense.set_pixel(3, 6, yellow)
            sense.set_pixel(3, 5, yellow)
            sense.set_pixel(3, 4, yellow)
            sense.set_pixel(3, 3, yellow)
            sense.set_pixel(4, 7, yellow)
            sense.set_pixel(4, 6, yellow)
            sense.set_pixel(4, 5, yellow)
            sense.set_pixel(4, 4, yellow)
            sense.set_pixel(4, 3, yellow)
            sense.set_pixel(5, 6, yellow)
            sense.set_pixel(5, 5, yellow)
            sense.set_pixel(5, 4, yellow)
            sense.set_pixel(5, 3, yellow)
            time.sleep(.3)
            sense.clear()

            break
    else:
        from sense_hat import SenseHat
        sense = SenseHat()


        sense.clear()
