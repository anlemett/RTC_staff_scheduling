import numpy as np
import matplotlib.pyplot as plt


category_names = ['5 controllers', '6 controllers', '7 controllers', '8 cotrollers']
results_07_29 = {
    '0.2': [30, 70, 0, 0],
    '0.3': [30, 70, 0, 0],
    '0.4': [30, 70, 0, 0],
    '0.5': [90, 10, 0, 0],
    '0.6': [90, 10, 0, 0],
    '0.7': [100, 0, 0, 0]
}

results_02_16 = {
    '0.2': [0, 0, 0, 100],
    '0.3': [0, 0, 0, 100],
    '0.4': [0, 0, 0, 100],
    '0.5': [0, 0, 30, 70],
    '0.6': [0, 100, 0, 0],
    '0.7': [100, 0, 0, 0]
}

def stacked_barplot(results, category_names):
 
    labels = list(results.keys())
    data = np.array(list(results.values()))
    data_cum = data.cumsum(axis=1)

    temp = [0.1, 0.4, 0.7, 0.9]
    category_colors = plt.get_cmap('RdYlGn_r')(temp)
    
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.invert_yaxis()
    ax.set_ylabel('Cutoff')
    ax.xaxis.set_visible(False)
    ax.set_xlim(0, np.sum(data, axis=1).max())

    for i, (colname, color) in enumerate(zip(category_names, category_colors)):
        widths = data[:, i]
        starts = data_cum[:, i] - widths
        ax.barh(labels, widths, left=starts, height=0.5,
                label=colname, color=color)
        xcenters = starts + widths / 2

        r, g, b, _ = color
        text_color = 'black' if r * g * b < 0.5 else 'darkgrey'
        for y, (x, c) in enumerate(zip(xcenters, widths)):
            if c!=0:
                ax.text(x, y, str(int(c)) + " %", ha='center', va='center', color=text_color)
    ax.legend(ncol=len(category_names), bbox_to_anchor=(0, 1),
              loc='lower left', fontsize='small')

    return fig, ax


#stacked_barplot(results_07_29, category_names)
stacked_barplot(results_02_16, category_names)
plt.show()