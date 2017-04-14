from matplotlib import pyplot as plt
import numpy as np
import csv
from matplotlib import animation




f = open('SATYAJEETmeditation2.csv','r')
reader = csv.reader(f)
freq = []
for i in range(30):
    freq.append(i)
freq = np.array(freq)
fig = plt.figure()
ax = plt.axes(xlim=(0,30),ylim=(0,10))
line, = ax.plot([],[],lw=2)
plt.ylabel('Amplitude ---->')
plt.xlabel('Frequency ---->')

def init():
    line.set_data([],[])
    return line,
def animate(i):
    amp = list(map(float,np.array(next(reader))))
    line.set_data(freq,amp)
    return line,

anim = animation.FuncAnimation(fig, animate, init_func=init,frames=3000,interval=20,blit=True)
anim.save('real_video11.mp4',fps=30,extra_args=['-vcodec','libx264'])


plt.show()
    

