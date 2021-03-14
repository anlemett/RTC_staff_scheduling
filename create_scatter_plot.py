import matplotlib.pyplot as plt

'''
February_16_x = [0.2, 0.3, 0.4, 0.5, 0.5, 0.6, 0.7]
February_16_y = [8, 8, 8, 8, 7, 6, 5]

ax = plt.gca()

# ['o', '.', ',', 'x', '+', 'v', '^', '<', '>', 's', 'd']:
plt.plot(February_16_x, February_16_y , 's', markersize=7, label="Fabruary 16", color='blue')

n = ["30 %", "70 %"]
#for i, txt in enumerate(n):
ax.annotate("70 %", xy=( February_16_x[3], February_16_y[3] ), xytext=( 0.5, 8.13 ))
ax.annotate("30 %", xy=( February_16_x[4], February_16_y[4] ), xytext=( 0.5, 7.13 ))

plt.xlabel('Cutoff')
plt.ylabel('Number of controllers')

plt.legend(numpoints=1, loc="lower left")

ax.set_xlim(0.15,0.75)
ax.set_ylim(4,9)
'''

July_29_x = [0.2, 0.2, 0.3, 0.3, 0.4, 0.4, 0.5, 0.5, 0.6, 0.6, 0.7]
July_29_y = [5, 6, 5, 6, 5, 6, 5, 6, 5, 6, 5]

ax = plt.gca()

plt.plot(July_29_x, July_29_y , 'o', markersize=7, label="July 29", color='red')

n = ["30 %", "70 %"]
#for i, txt in enumerate(n):
ax.annotate("70 %", xy=( July_29_x[0], July_29_y[0] ), xytext=( 0.2, 6.13 ))
ax.annotate("30 %", xy=( July_29_x[1], July_29_y[1] ), xytext=( 0.2, 5.13 ))

ax.annotate("70 %", xy=( July_29_x[2], July_29_y[2] ), xytext=( 0.3, 6.13 ))
ax.annotate("30 %", xy=( July_29_x[3], July_29_y[3] ), xytext=( 0.3, 5.13 ))

ax.annotate("70 %", xy=( July_29_x[4], July_29_y[4] ), xytext=( 0.4, 6.13 ))
ax.annotate("30 %", xy=( July_29_x[5], July_29_y[5] ), xytext=( 0.4, 5.13 ))

ax.annotate("10 %", xy=( July_29_x[6], July_29_y[6] ), xytext=( 0.5, 6.13 ))
ax.annotate("90 %", xy=( July_29_x[7], July_29_y[7] ), xytext=( 0.5, 5.13 ))

ax.annotate("10 %", xy=( July_29_x[8], July_29_y[8] ), xytext=( 0.6, 6.13 ))
ax.annotate("90 %", xy=( July_29_x[9], July_29_y[9] ), xytext=( 0.6, 5.13 ))

plt.xlabel('Cutoff')
plt.ylabel('Number of controllers')

plt.legend(numpoints=1)

ax.set_xlim(0.15,0.75)
ax.set_ylim(4,9)
