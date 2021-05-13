from bokeh.plotting import figure, show
from bokeh.models import BoxAnnotation


x = [1, 2, 3, 4, 5]
y1 = [6, 7, 2, 4, 5]
y2 = [2, 3, 4, 5, 6]
y3 = [4, 5, 5, 7, 2]

p = figure(title='Multiple glyphs example', x_axis_label='x', y_axis_label='y')

p.line(x, y1, legend_label='Temp.', line_color='blue', line_width=2)
p.vbar(x=x, top=y2, legend_label='Rate', color='red', width=0.5, bottom=0)
p.circle(x, y3, legend_label='Objects', line_color='yellow', size=12)

# add legend customisation
p.legend.location = 'top_left'
p.legend.title = 'Obervations'
p.legend.label_text_font = 'times'
p.legend.label_text_color = 'navy'
p.legend.border_line_width = 3


# add box annotation
low_box = BoxAnnotation(top=3, fill_alpha=0.1, fill_color='red')
mid_box = BoxAnnotation(bottom=3, top=6, fill_alpha=0.1, fill_color='green')
high_box = BoxAnnotation(bottom=6, fill_alpha=0.1, fill_color='blue')

p.add_layout(low_box)
p.add_layout(mid_box)
p.add_layout(high_box)

show(p)
