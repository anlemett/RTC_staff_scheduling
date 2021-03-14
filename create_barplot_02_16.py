import matplotlib.pyplot as plt
import numpy as np

import pandas as pd

color1 = '#ef8a62'
color2 = '#fddbc7'
color3 = '#d1e5f0'
color4 = '#67a9cf'
color5 = '#2166ac'

color1 = '#fddbc7' #light orange
color2 = '#ef8a62' #dark orange
color3 = '#d1e5f0' #light blue
color4 = '#67a9cf' #blue
color5 = '#2166ac' #dark blue

line_color = 'red'
point_color = 'red'

labels = ['0.2', '0.3', '0.4', '0.5', '0.6', '0.7']
part1 = [8, 8, 8, 8, 6, 5]
part2 = [0, 0, 0, 7, 0, 0]

x = np.array([0, 1, 2, 3, 4, 5])
width = 0.35  # the width of the bars

fig, ax = plt.subplots()

ax.set_ylabel('Number of controllers', fontsize=16)
plt.ylim((0,9))
axes = plt.gca()
axes.yaxis.grid(color='lightgrey', linestyle='--', linewidth=0.5, zorder= 0)

x_shift = np.array([-0.2, 0.8, 1.8, 3, 3.8, 4.8])
#ax.set_xticks(x)
ax.set_xticks(x_shift)
ax.set_xticklabels(labels)
ax.set_xlabel('Cutoff', fontsize=16)

rects1 = ax.bar(x - width/2, part1, width, label='', zorder= 3)
rects2 = ax.bar(x + width/2, part2, width, label='', zorder= 3)

rects1[0].set_color(color5)
rects1[1].set_color(color5)
rects1[2].set_color(color5)
rects1[3].set_color(color3)
rects1[4].set_color(color5)
rects1[5].set_color(color5)

rects2[3].set_color(color2)

y = np.array([8, 8, 8, 7.7, 6, 5])

for i in range(len(x)):
    ax.scatter(x_shift[i], y[i], color=point_color, zorder=4)

ax.plot(x_shift, y, color = line_color, zorder=4);

'''
def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


#autolabel(rects1)
#autolabel(rects2)

ax.annotate('100 %', xy=(rects1[0].get_x() + rects1[0].get_width() / 2, rects1[0].get_height()),
                    xytext=(3, 3),
                    textcoords="offset points",
                    ha='center', va='bottom')

ax.annotate('100 %', xy=(rects1[1].get_x() + rects1[1].get_width() / 2, rects1[1].get_height()),
                    xytext=(3, 3),
                    textcoords="offset points",
                    ha='center', va='bottom')

ax.annotate('100 %', xy=(rects1[2].get_x() + rects1[2].get_width() / 2, rects1[2].get_height()),
                    xytext=(3, 3),
                    textcoords="offset points",
                    ha='center', va='bottom')


ax.annotate('70 %', xy=(rects1[3].get_x() + rects1[3].get_width() / 2, rects1[3].get_height()),
                    xytext=(3, 3),
                    textcoords="offset points",
                    ha='center', va='bottom')

ax.annotate('30 %', xy=(rects2[3].get_x() + rects2[3].get_width() / 2, rects2[3].get_height()),
                    xytext=(3, 3), 
                    textcoords="offset points",
                    ha='center', va='bottom')

ax.annotate('100 %', xy=(rects1[4].get_x() + rects1[4].get_width() / 2, rects1[4].get_height()),
                    xytext=(3, 3),
                    textcoords="offset points",
                    ha='center', va='bottom')

ax.annotate('100 %', xy=(rects1[5].get_x() + rects1[5].get_width() / 2, rects1[5].get_height()),
                    xytext=(3, 3),
                    textcoords="offset points",
                    ha='center', va='bottom')

'''
fig.tight_layout()

#plt.savefig('barplot_2020_02_16.eps', format='eps', dpi=1200, bbox_inches = 'tight', pad_inches = 0.02)
plt.savefig('barplot_2020_02_16.png', format='png', dpi=1200, bbox_inches = 'tight', pad_inches = 0.02)

plt.show()