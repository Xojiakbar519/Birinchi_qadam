import pyautogui
import time

code = '''

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.axis('off')

lines = []
n_lines = 120

# boshlang'ich chiziqlar
for i in range(n_lines):
    line, = ax.plot([], [], lw=1)
    lines.append(line)

def update(frame):
    t = frame * 0.05
    
    for i, line in enumerate(lines):
        angle = i * (2 * np.pi / n_lines)
        
        # radius va deformatsiya
        r = 1 + 0.3 * np.sin(4 * angle + t)
        
        x = r * np.cos(angle + t)
        y = r * np.sin(angle + t)
        
        # chiziq segmenti
        x_vals = [0, x]
        y_vals = [0, y]
        
        line.set_data(x_vals, y_vals)
        
        # rang gradatsiyasi (oq-sariq)
        color = (1, 0.9 * abs(np.sin(angle + t)), 0.2)
        line.set_color(color)
    
    return lines

ani = FuncAnimation(fig, update, frames=200, interval=30, blit=True)

plt.show()

'''

time.sleep(3)  # recording boshlashga vaqt

for char in code:
    pyautogui.write(char)
    time.sleep(0.000000005)


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.axis('off')

lines = []
n_lines = 120

# boshlang'ich chiziqlar
for i in range(n_lines):
    line, = ax.plot([], [], lw=1)
    lines.append(line)

def update(frame):
    t = frame * 0.05
    
    for i, line in enumerate(lines):
        angle = i * (2 * np.pi / n_lines)
        
        # radius va deformatsiya
        r = 1 + 0.3 * np.sin(4 * angle + t)
        
        x = r * np.cos(angle + t)
        y = r * np.sin(angle + t)
        
        # chiziq segmenti
        x_vals = [0, x]
        y_vals = [0, y]
        
        line.set_data(x_vals, y_vals)
        
        # rang gradatsiyasi (oq-sariq)
        color = (1, 0.9 * abs(np.sin(angle + t)), 0.2)
        line.set_color(color)
    
    return lines

ani = FuncAnimation(fig, update, frames=200, interval=30, blit=True)

plt.show()



