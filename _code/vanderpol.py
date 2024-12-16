import numpy as np
from scipy.integrate import solve_ivp
import imageio
import os

import matplotlib.pyplot as plt

# Van der Pol oscillator differential equations
def vanderpol(t, y, mu):
    return [y[1], mu * (1 - y[0]**2) * y[1] - y[0]]

# Parameters
mu = 1.0
t_span = (0, 20)
y0 = [2, 0]
t_eval = np.linspace(t_span[0], t_span[1], 1000)

# Solve the differential equations
sol = solve_ivp(vanderpol, t_span, y0, args=(mu,), t_eval=t_eval)

# Create a phase portrait
fig, ax = plt.subplots()
ax.plot(sol.y[0], sol.y[1])
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Van der Pol Oscillator Phase Portrait')

# Save the phase portrait as a series of images
filenames = []
for i in range(len(sol.t)):
    fig, ax = plt.subplots()
    ax.plot(sol.y[0][:i], sol.y[1][:i])
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Van der Pol Oscillator Phase Portrait')
    filename = f'frame_{i:03d}.png'
    filenames.append(filename)
    plt.savefig(filename)
    plt.close()

# Create a GIF from the images
with imageio.get_writer('vanderpol.gif', mode='I') as writer:
    for filename in filenames:
        image = imageio.imread(filename)
        writer.append_data(image)

# Clean up the image files
for filename in filenames:
    os.remove(filename)

print("GIF saved as vanderpol.gif")