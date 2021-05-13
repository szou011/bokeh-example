from bokeh.plotting import figure, show

x = [1, 2, 3, 4, 5]
y1 = [6, 7, 2, 4, 5]
y2 = [2, 3, 4, 5, 6]
y3 = [4, 5, 5, 7, 2]

p = figure(title='Multiple glyphs example', x_axis_label='x', y_axis_label='y')

p.line(x, y1, legend_label='Temp.', line_color='blue', line_width=2)
p.vbar(x=x, top=y2, legend_label='Rate', color='red', width=0.5, bottom=0)
p.circle(x, y3, legend_label='Objects', line_color='yellow', size=12)

show(p)
