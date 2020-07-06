import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')

x_vals = []
y_vals = []

index = count()

def animate(i):
	data = pd.read_csv('Example7.csv')
	x = data['xvalue']
	y1 = data['Building1Flame']
	y2 = data['Building2Flame']
	y3 = data['Building3Flame']
	y4 = data['Building4Flame']
	y5 = data['Building5Flame']
	plt.cla()
	plt.plot(x, y1, label='Building 1')
	plt.plot(x, y2, label='Building 2')
	plt.plot(x, y3, label='Building 3')
	plt.plot(x, y4, label='Building 4')	
	plt.plot(x, y5, label='Building 5')
	plt.legend(loc='upper right')
	plt.tight_layout()

ani = FuncAnimation(plt.gcf(), animate, interval=1000)
plt.tight_layout()
plt.show()
