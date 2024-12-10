import functools

import matplotlib.pyplot as plt
import numpy as np

import matplotlib.animation as animation
from scipy.stats import expon

def generate(N):
    Us = np.zeros(N)
    lambda_exp = 5
    for i in range(1, N+1):
        X = expon.rvs(scale = 1./lambda_exp, size=i)
        Us[i-1] = (np.sum(X)/i - 1./lambda_exp) * np.sqrt(i) * lambda_exp
    return Us;

def animate(frame_number, bar_container):
    data = generate(1000)
    n, _ = np.histogram(data, HIST_BINS)
    for count, rect in zip(n, bar_container.patches):
        rect.set_height(count)

    return bar_container.patches

HIST_BINS = np.linspace(-4, 4, 100)
fig, ax = plt.subplots()
_, _, bar_container = ax.hist(np.zeros(1000), HIST_BINS, lw=1,
                              ec="yellow", fc="green", alpha=0.5)
ax.set_ylim(top=55)

anim = functools.partial(animate, bar_container=bar_container)
ani = animation.FuncAnimation(fig, anim, 50, repeat=False, blit=True)
plt.close()
ani.save('CLT.gif',writer='pillow')

