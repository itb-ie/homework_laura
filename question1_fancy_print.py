from question1 import first_wave, second_wave

import matplotlib.pyplot as plt
# here I just use the two numbers to display them as a fancy pie chart
# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'First Wave', 'Second Wave'
sizes = [first_wave, second_wave]
explode = (0, 0.1)  # only "explode" the 2nd slice

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()
