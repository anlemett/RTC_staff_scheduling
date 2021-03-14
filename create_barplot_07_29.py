import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

import numpy as np
import pandas as pd

color1 = '#fddbc7' #light orange
color2 = '#ef8a62' #dark orange
color3 = '#d1e5f0' #light blue
color4 = '#67a9cf' #blue
color5 = '#2166ac' #dark blue

line_color = 'red'
point_color = 'red'

label1 = '10 %'
label2 = '30 %'
label3 = '70 %'
label4 = '90 %'
label5 = '100 %'


part1 = [6, 6, 6, 6, 6, 5]
part2 = [5, 5, 5, 5, 5, 0]
labels = ['0.2', '0.3', '0.4', '0.5', '0.6', '0.7']

x = np.array([0, 1, 2, 3, 4, 5])
width = 0.35  # the width of the bars

fig, ax = plt.subplots()

ax.set_ylabel('Number of controllers', fontsize=16)
plt.ylim((0,9))
axes = plt.gca()
axes.yaxis.grid(color='lightgrey', linestyle='--', linewidth=0.5, zorder= 0)

x_shift = np.array([0, 1, 2, 3, 4, 4.8])
#ax.set_xticks(x)
ax.set_xticks(x_shift)
ax.set_xticklabels(labels)
ax.set_xlabel('Cutoff', fontsize=16)

rects1 = ax.bar(x - width/2, part1, width, label='', zorder= 3)
rects2 = ax.bar(x + width/2, part2, width, label='', zorder= 3)

rects1[0].set_color(color3)
rects1[1].set_color(color3)
rects1[2].set_color(color3)
rects1[3].set_color(color1)
rects1[4].set_color(color1)
rects1[5].set_color(color5)

rects2[0].set_color(color2)
rects2[1].set_color(color2)
rects2[2].set_color(color2)
rects2[3].set_color(color4)
rects2[4].set_color(color4)
rects2[5].set_color(color5)


patch1 = mpatches.Patch(color=color1, label=label1)
patch2 = mpatches.Patch(color=color2, label=label2)
patch3 = mpatches.Patch(color=color3, label=label3)
patch4 = mpatches.Patch(color=color4, label=label4)
patch5 = mpatches.Patch(color=color5, label=label5)
plt.legend(handles=[patch1, patch2, patch3, patch4, patch5])


y = np.array([5.7, 5.7, 5.7, 5.1, 5.1, 5])

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

ax.annotate('70 %', xy=(rects1[0].get_x() + rects1[0].get_width() / 2, rects1[0].get_height()),
                    xytext=(3, 3),
                    textcoords="offset points",
                    ha='center', va='bottom')
ax.annotate('30 %', xy=(rects2[0].get_x() + rects2[0].get_width() / 2, rects2[0].get_height()),
                    xytext=(3, 3),
                    textcoords="offset points",
                    ha='center', va='bottom')

ax.annotate('70 %', xy=(rects1[1].get_x() + rects1[1].get_width() / 2, rects1[1].get_height()),
                    xytext=(3, 3),
                    textcoords="offset points",
                    ha='center', va='bottom')
ax.annotate('30 %', xy=(rects2[1].get_x() + rects2[1].get_width() / 2, rects2[1].get_height()),
                    xytext=(3, 3),
                    textcoords="offset points",
                    ha='center', va='bottom')

ax.annotate('70 %', xy=(rects1[2].get_x() + rects1[2].get_width() / 2, rects1[2].get_height()),
                    xytext=(3, 3),
                    textcoords="offset points",
                    ha='center', va='bottom')
ax.annotate('30 %', xy=(rects2[2].get_x() + rects2[2].get_width() / 2, rects2[2].get_height()),
                    xytext=(3, 3),
                    textcoords="offset points",
                    ha='center', va='bottom')

ax.annotate('10 %', xy=(rects1[3].get_x() + rects1[3].get_width() / 2, rects1[3].get_height()),
                    xytext=(3, 3),
                    textcoords="offset points",
                    ha='center', va='bottom')
ax.annotate('90 %', xy=(rects2[3].get_x() + rects2[3].get_width() / 2, rects2[3].get_height()),
                    xytext=(3, 3),
                    textcoords="offset points",
                    ha='center', va='bottom')

ax.annotate('10 %', xy=(rects1[4].get_x() + rects1[4].get_width() / 2, rects1[4].get_height()),
                    xytext=(3, 3),
                    textcoords="offset points",
                    ha='center', va='bottom')
ax.annotate('90 %', xy=(rects2[4].get_x() + rects2[4].get_width() / 2, rects2[4].get_height()),
                    xytext=(3, 3),
                    textcoords="offset points",
                    ha='center', va='bottom')

ax.annotate('100 %', xy=(rects1[5].get_x() + rects1[5].get_width() / 2, rects1[5].get_height()),
                    xytext=(3, 3),
                    textcoords="offset points",
                    ha='center', va='bottom')

'''
fig.tight_layout()

#plt.savefig('barplot_2020_07_29.eps', format='eps', dpi=1200, bbox_inches = 'tight', pad_inches = 0.02)
plt.savefig('barplot_2020_07_29.png', format='png', dpi=1200, bbox_inches = 'tight', pad_inches = 0.02)


plt.show()