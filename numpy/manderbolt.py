# x refers to real part , y refers to imaginary part

def mandelbrot(iterations,xmin, xmax, ymin, ymax,xn,yn, horizon = 2.0):

    real = np.linspace(xmin,xmax,xn, dtype = np.float32)
    imaginary = np.linspace(ymin,ymax,yn, dtype = np.float32)

    C= real +imaginary[:,None] * 1j

    N = np.zeros(C.shape,np.int64)
    Z = np.zeros(C.shape, np.complex64)

    for n in range(iterations):
        I = np.less(abs(Z),horizon)
        N[I] = n
        Z[I] = Z[I]**2 + C[I]
    N[N == maxiter-1] = 0



    return Z.shape, N.shape
