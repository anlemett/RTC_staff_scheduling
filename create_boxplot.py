import pandas as pd
import seaborn as sns

data = {'Cutoff':['0.2', '0.2', '0.3', '0.3', '0.4', '0.4', '0.5', '0.5', '0.6', '0.6', '0.7', '0.7'], 
        'Number':[8, 8, 8, 8, 8, 8, 7, 8, 6, 6, 5, 5]}

df = pd.DataFrame(data)

df["Number"] = pd.to_numeric(df["Number"])

print(df.head())

#df.boxplot(by ='Cutoff', column =['Number'], grid = False) 

sns.set_style("whitegrid") 
  
#sns.boxplot(x = 'Cutoff', y = 'Number', data = df, fliersize=55, linewidth=None, whis=5, 
#            flierprops = dict(markerfacecolor = '0.50', markersize = 2))

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon
plt.rcParams["axes.grid"] = False

axes = plt.axes()
ax = plt.gca()

shift = 0.05

pts = np.array([[0,8-shift], [0,8+shift],[10,8+shift], [10, 8-shift]])
p = Polygon(pts, closed=False)
ax.add_patch(p)

pts = np.array([[10,8-shift], [10,8+shift],[20,8+shift], [20, 8-shift]])
p = Polygon(pts, closed=False)
ax.add_patch(p)

pts = np.array([[20,8-shift], [20,8+shift],[30,8+shift], [30, 8-shift]])
p = Polygon(pts, closed=False)
ax.add_patch(p)

pts = np.array([[30,7], [30,8],[40,8], [40, 7]])
p = Polygon(pts, closed=False)
ax.add_patch(p)

pts = np.array([[40,6-shift], [40,6+shift],[50,6+shift], [50, 6-shift]])
p = Polygon(pts, closed=False)
ax.add_patch(p)

pts = np.array([[50,5-shift], [50,5+shift],[60,5+shift], [60, 5-shift]])
p = Polygon(pts, closed=False)
ax.add_patch(p)

plt.xlabel('Cutoff')
plt.ylabel('Number of controllers')

positions = (5, 15, 25, 35, 45, 55, 65)
labels = ("0.2", "0.3", "0.4", "0.5", "0.6", "0.7")
plt.xticks(positions, labels)

ax.set_xlim(0,60)
ax.set_ylim(4,9)


plt.show()
