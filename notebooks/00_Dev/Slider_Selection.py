# %% [markdown]
# ## Link A Range Slider to A Plot
# Use the slider to make cuts on data and reflect the cut in the plots

# %%
from bokeh.io import show, output_notebook

output_notebook()

# %%
from bokeh.sampledata.penguins import data

data

# %%
from bokeh.layouts import gridplot
from bokeh.models import ColumnDataSource, RangeSlider, CustomJS
from bokeh.plotting import figure
from bokeh.transform import factor_cmap

SPECIES = sorted(data.species.unique())

TOOLS = "box_select,lasso_select,help,reset"

s1 = ColumnDataSource(data)
s2 = ColumnDataSource(data)

left = figure(
    width=400, height=400, title=None, tools=TOOLS, background_fill_color="#fafafa"
)
left.scatter(
    "bill_length_mm",
    "body_mass_g",
    source=s2,
    color=factor_cmap("species", "Category10_3", SPECIES),
)

right = figure(
    width=400,
    height=400,
    title=None,
    tools=TOOLS,
    background_fill_color="#fafafa",
    y_axis_location="right",
)
right.scatter(
    "bill_length_mm",
    "flipper_length_mm",
    source=s2,
    color=factor_cmap("species", "Category10_3", SPECIES),
)

slider_min, slider_max = data.bill_depth_mm.min(), data.bill_depth_mm.max()
range_slider = RangeSlider(
    start=slider_min,
    end=slider_max,
    value=(slider_min, slider_max),
    step=0.1,
    title="bill_depth_mm:",
)
range_slider.js_on_change(
    "value",
    CustomJS(
        args=dict(s1=s1, s2=s2),
        code="""
    var start = this.value[0];
    var end = this.value[1];
    let s1_data = s1.data;

    let indicesInRange = [];
    for (let i = 0; i < s1_data.index.length; i++) {
        if (s1_data.bill_depth_mm[i] >= start && s1_data.bill_depth_mm[i] <= end) {
            indicesInRange.push(i); // If it does, push the index to the array
        }
    }

    const new_data = {};
    Object.keys(s1_data).forEach(key=> {
        new_data[key] = Array.from(indicesInRange, (i) => s1.data[key][i])
    }
    )
    s2.data = new_data;
""",
    ),
)

show(gridplot([[range_slider], [left, right]]))

# %%
