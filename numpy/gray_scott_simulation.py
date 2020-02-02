#Gray Scott equations model diffusion reaction between chemical species.
#The set up of the initial state and parameters given in this paper- http://www.staff.science.uu.nl/~frank011/Classes/complexity/Literature/Pearson.pdf
# -----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


# Parameters from http://www.aliensaint.com/uo/java/rd/
# -----------------------------------------------------
n = 256
#Du, Dv, F, k = 0.16, 0.08, 0.035, 0.065  # Bacteria 1
#Du, Dv, F, k = 0.14, 0.06, 0.035, 0.065  # Bacteria 2
#Du, Dv, F, k = 0.16, 0.08, 0.060, 0.062  # Coral
#Du, Dv, F, k = 0.19, 0.05, 0.060, 0.062  # Fingerprint
# Du, Dv, F, k = 0.10, 0.10, 0.018, 0.050  # Spirals
# Du, Dv, F, k = 0.12, 0.08, 0.020, 0.050  # Spirals Dense
# Du, Dv, F, k = 0.10, 0.16, 0.020, 0.050  # Spirals Fast
# Du, Dv, F, k = 0.16, 0.08, 0.020, 0.055  # Unstable
# Du, Dv, F, k = 0.16, 0.08, 0.050, 0.065  # Worms 1
Du, Dv, F, k = 0.16, 0.08, 0.054, 0.063  # Worms 2
#Du, Dv, F, k = 0.16, 0.08, 0.035, 0.060  # Zebrafish


U = np.zeros((n+2, n+2), dtype = np.double)
V = np.zeros((n+2, n+2), dtype = np.double)

# U, V = Z['U'], Z['V']
u, v = U[1:-1, 1:-1], V[1:-1, 1:-1]

r = 100
u[...] = 1.0
U[n//2-r:n//2+r, n//2-r:n//2+r] = 0.50
V[n//2-r:n//2+r, n//2-r:n//2+r] = 0.25
u += 0.05*np.random.uniform(-1, +1, (n, n))
v += 0.05*np.random.uniform(-1, +1, (n, n))


def update(frame):
    global U, V, u, v, im
    for i in range(1000):
        Lu = laplacian(U)
        Lv = laplacian(V)
        uvv = u*v*v
        u += (Du*Lu - uvv + F*(1-u))
        v += (Dv*Lv + uvv - (F+k)*v)

    im.set_data(V)
    im.set_clim(vmin=V.min(), vmax=V.max())

fig = plt.figure(figsize=(4, 4))
fig.add_axes([0.0, 0.0, 1.0, 1.0], frameon=False)
im_v = plt.imshow(V, interpolation='bicubic', cmap=plt.cm.viridis)

plt.xticks([]), plt.yticks([])
animation = FuncAnimation(fig, update, interval=10, frames=2000)
# animation.save('gray-scott-1.mp4', fps=40, dpi=80, bitrate=-1, codec="libx264",
#                extra_args=['-pix_fmt', 'yuv420p'],
#                metadata={'artist':'Nicolas P. Rougier'})
plt.show()
