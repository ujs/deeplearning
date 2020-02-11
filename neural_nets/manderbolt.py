# x refers to real part , y refers to imaginary part

def mandelbrot(z, iterations, horizon = 2.0, xmin, xmax, ymin, ymax,xn,yn):

    real = np.linspace(xmin,xmax,xn, dtype = np.float32)
    imaginary = np.linspace(ymin,ymax,yn, dtype = np.float32)

    C= real +imaginary[:,None] * 1j

    Z = np.zeros(C.shape, dtype = complex)
