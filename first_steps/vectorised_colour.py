import random

from bokeh.plotting import figure, show

x = list(range(0, 26))

y = random.sample(range(0, 100), 26)

colours = ["#%02x%02x%02x" % (255, int(round(value * 255 / 100)), 255) for value in y]

p = figure(
        title='Vectorised colour scheme'
        , max_width=500
        , plot_height=250)

p.line(x, y, line_color='blue', line_width=1)
p.circle(x, y, fill_color=colours, line_color='blue', size=15)

show(p)
