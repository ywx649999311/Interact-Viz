# %% [markdown]
# ## Linking + Brushing

# %%
# add path

import holoviews as hv

from holoviews.operation import gridmatrix
from holoviews import opts

hv.extension("bokeh", width=100)

# %% [markdown]
# ### 1. holoview + Bokeh:gridmatrix

# %%
from bokeh.sampledata.autompg import autompg

autompg

# %%
autompg_ds = hv.Dataset(autompg, ["yr", "name", "origin"])

mopts = opts.Points(
    size=2, tools=["box_select", "lasso_select"], active_tools=["box_select"]
)

gridmatrix(autompg_ds, chart_type=hv.Points).opts(mopts)

# %% [markdown]
# ### 2. Bokeh: Linked Brushing

# %%
from bokeh.layouts import gridplot
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure, show
from bokeh.sampledata.penguins import data
from bokeh.transform import factor_cmap

SPECIES = sorted(data.species.unique())

TOOLS = "box_select,lasso_select,help,reset"

source = ColumnDataSource(data)

left = figure(
    width=300, height=400, title=None, tools=TOOLS, background_fill_color="#fafafa"
)
left.scatter(
    "bill_length_mm",
    "body_mass_g",
    source=source,
    color=factor_cmap("species", "Category10_3", SPECIES),
)

right = figure(
    width=300,
    height=400,
    title=None,
    tools=TOOLS,
    background_fill_color="#fafafa",
    y_axis_location="right",
)
right.scatter(
    "bill_depth_mm",
    "flipper_length_mm",
    source=source,
    color=factor_cmap("species", "Category10_3", SPECIES),
)

show(gridplot([[left, right]]))

# %% [markdown]
# ### 3. Bokeh: Plot + Table

# %%
from bokeh.layouts import column
from bokeh.models import (
    ColumnDataSource,
    DataTable,
    HoverTool,
    IntEditor,
    NumberEditor,
    NumberFormatter,
    SelectEditor,
    StringEditor,
    StringFormatter,
    TableColumn,
)
from bokeh.plotting import figure, show
from bokeh.sampledata.autompg2 import autompg2 as mpg

source = ColumnDataSource(mpg)

manufacturers = sorted(mpg["manufacturer"].unique())
models = sorted(mpg["model"].unique())
transmissions = sorted(mpg["trans"].unique())
drives = sorted(mpg["drv"].unique())
classes = sorted(mpg["class"].unique())

columns = [
    TableColumn(
        field="manufacturer",
        title="Manufacturer",
        editor=SelectEditor(options=manufacturers),
        formatter=StringFormatter(font_style="bold"),
    ),
    TableColumn(field="model", title="Model", editor=StringEditor(completions=models)),
    TableColumn(
        field="displ",
        title="Displacement",
        editor=NumberEditor(step=0.1),
        formatter=NumberFormatter(format="0.0"),
    ),
    TableColumn(field="year", title="Year", editor=IntEditor()),
    TableColumn(field="cyl", title="Cylinders", editor=IntEditor()),
    TableColumn(
        field="trans", title="Transmission", editor=SelectEditor(options=transmissions)
    ),
    TableColumn(field="drv", title="Drive", editor=SelectEditor(options=drives)),
    TableColumn(field="class", title="Class", editor=SelectEditor(options=classes)),
    TableColumn(field="cty", title="City MPG", editor=IntEditor()),
    TableColumn(field="hwy", title="Highway MPG", editor=IntEditor()),
]
data_table = DataTable(
    source=source,
    columns=columns,
    editable=True,
    width=800,
    index_position=-1,
    index_header="row index",
    index_width=60,
)

p = figure(
    width=800,
    height=300,
    tools="pan,wheel_zoom,xbox_select,reset, lasso_select",
    active_drag="xbox_select",
)

cty = p.scatter(
    x="index", y="cty", fill_color="#396285", size=8, alpha=0.5, source=source
)
hwy = p.scatter(
    x="index", y="hwy", fill_color="#CE603D", size=8, alpha=0.5, source=source
)

tooltips = [
    ("Manufacturer", "@manufacturer"),
    ("Model", "@model"),
    ("Displacement", "@displ"),
    ("Year", "@year"),
    ("Cylinders", "@cyl"),
    ("Transmission", "@trans"),
    ("Drive", "@drv"),
    ("Class", "@class"),
]
cty_hover_tool = HoverTool(renderers=[cty], tooltips=[*tooltips, ("City MPG", "@cty")])
hwy_hover_tool = HoverTool(
    renderers=[hwy], tooltips=[*tooltips, ("Highway MPG", "@hwy")]
)

p.add_tools(cty_hover_tool, hwy_hover_tool)

show(column(p, data_table))

# %% [markdown]
# ### 4. Bokeh: Linked Properties

# %%
from bokeh.layouts import column
from bokeh.models import Slider
from bokeh.plotting import figure, show

plot = figure(width=400, height=400)
r = plot.circle([1, 2, 3, 4, 5], [3, 2, 5, 6, 4], radius=0.2, alpha=0.5)

slider = Slider(start=0.1, end=2, step=0.01, value=0.2)
slider.js_link("value", r.glyph, "radius")

show(column(plot, slider))

# %%
