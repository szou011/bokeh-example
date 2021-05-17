from bokeh.models import Div, RangeSlider, Spinner
from bokeh.plotting import figure, show
from bokeh.layouts import layout


x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [4, 5, 5, 7, 2, 6, 4, 9, 1, 3]

p = figure(x_range=(1,9), plot_width=500, plot_height=250)
points = p.circle(x=x, y=y, size=30, fill_color="#21a7df")

div = Div(
    text="""
        <p>Select the circle's size using this control element:</p>
        """,
    width=200,
    height=30,
)

spinner = Spinner(
    title="Circle size",  # a string to display above the widget
    low=0,  # the lowest possible number to pick
    high=60,  # the highest possible number to pick
    step=5,  # the increments by which the number can be adjusted
    value=points.glyph.size,  # the initial value to display in the widget
    width=200
    )

spinner.js_link("value", points.glyph, "size")

range_slider = RangeSlider(
    title="Adjust x-axis range", # a title to display above the slider
    start=0,  # set the minimum value for the slider
    end=10,  # set the maximum value for the slider
    step=1,  # increments for the slider
    value=(p.x_range.start, p.x_range.end),  # initial values for slider
    )

range_slider.js_link("value", p.x_range, "start", attr_selector=0)
range_slider.js_link("value", p.x_range, "end", attr_selector=1)

plots = layout([
    [div, spinner],
    [range_slider],
    [p],
])

show(plots)
