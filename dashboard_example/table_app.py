import numpy as np
from bokeh.plotting import figure, curdoc
from bokeh.models import ColumnDataSource, CDSView, BooleanFilter
from bokeh.models.widgets import Button, DataTable, TableColumn
from bokeh.layouts import layout

def periodic_callback():
    """Update view."""

    mask = np.random.randint(0, 2, (10,), dtype=bool)
    view = CDSView(source=data_scr, filters=[BooleanFilter(mask)])
    filtered_table.view = view

def get_layout():
    """Create layout and app elements."""

    data_scr = ColumnDataSource({"x":np.random.normal(size=(10,)),
                                 "y":np.random.normal(size=(10,))})
    columns = [TableColumn(field="x", title="First"),
               TableColumn(field="y", title="Second")]

    full_table = DataTable(columns=columns, source=data_scr)

    mask = [True for el in data_scr.data["y"]]
    data_view = CDSView(source=data_scr, filters=[BooleanFilter(mask)])
    filtered_table = DataTable(columns=columns, source=data_scr, view=data_view)

    lt = layout([[full_table], [filtered_table]])
    return data_scr, filtered_table, lt

bokeh_doc = curdoc()

# Creating data source
data_scr, filtered_table, lt = get_layout()

bokeh_doc.add_root(lt)
bokeh_doc.add_periodic_callback(periodic_callback, 1000)
bokeh_doc.title = "Bokeh App tables."
