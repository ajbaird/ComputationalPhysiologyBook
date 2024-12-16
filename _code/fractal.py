import numpy as np

import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm


def mandelbrot(c, max_iter):
    z = c
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return max_iter

def create_fractal(xmin, xmax, ymin, ymax, width, height, max_iter):
    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)
    n3 = np.empty((width, height))
    for i in range(width):
        for j in range(height):
            n3[i, j] = mandelbrot(r1[i] + 1j*r2[j], max_iter)
    return (r1, r2, n3)

def plot_fractal(xmin, xmax, ymin, ymax, width=10, height=10, max_iter=256):
    dpi = 400
    img_width = dpi * width
    img_height = dpi * height

    x, y, fractal = create_fractal(xmin, xmax, ymin, ymax, img_width, img_height, max_iter)

    fig, ax = plt.subplots(figsize=(width, height), dpi=dpi)
    extent = [xmin, xmax, ymin, ymax]
    ax.imshow(fractal.T, extent=extent, cmap='viridis', norm=LogNorm())
    #ax.set_title('Mandelbrot Fractal')
    plt.savefig('mandelbrot.png')
    plt.show()

if __name__ == "__main__":
    plot_fractal(-2.0, 1.0, -1.5, 1.5)