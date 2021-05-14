from bokeh.plotting import figure, show
from bokeh.models import NumeralTickFormatter

# prepare some data
x = [1, 2, 3, 4, 5]
y = [4, 5, 5, 7, 2]

# create a new plot with responsive width
p = figure(
    title="Plot responsive sizing example",
    y_range = (0, 25),
    sizing_mode="stretch_width",
    plot_height=250,
    x_axis_label="x",
    y_axis_label="y",
)

# add circle renderer
circle = p.circle(x, y, fill_color="red", size=15)


# change some things about the x-axis
p.xaxis.axis_label = "Temp"
p.xaxis.axis_line_width = 3
p.xaxis.axis_line_color = "red"

# change things on all axes
p.axis.minor_tick_in = -3
p.axis.minor_tick_out = 6

# change just some things about the x-grid
p.xgrid.grid_line_color = "red"

# change just some things about the y-grid
p.ygrid.grid_line_alpha = 0.8
p.ygrid.grid_line_dash = [6, 4]

# change the fill colors
p.background_fill_color = 'blue'
p.border_fill_color = 'red'
p.outline_line_color = 'yellow'

# format y axis
p.yaxis[0].formatter = NumeralTickFormatter(format='$0.00')

show(p)
