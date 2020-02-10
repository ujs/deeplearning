# x refers to real part , y refers to imaginary part

def mandelbrot(z, iterations, horizon = 2.0):
    c = z
    for n in range(iterations):
        if abs(z) > horizon:
            return n
        else:
            z = z*z + c


def mandelbrot_set(xmin, xmax, ymin, ymax):
    real = 
    imaginary =
