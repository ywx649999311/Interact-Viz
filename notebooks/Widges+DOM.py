# %% [markdown]
# ## Widges and DOM Elements

# %%
# add path


from bokeh.io import show, output_notebook

output_notebook()

# %%
# from bokeh.io import show
from bokeh.models import CustomJS, DatetimeRangePicker

datetime_range_picker = DatetimeRangePicker(
    title="Select date and time range",
    value=("2019-09-20T12:37:51", "2019-10-15T17:59:18"),
    min_date="2019-08-01T09:00:00",
    max_date="2019-10-30T18:00:00",
    width=400,
)
datetime_range_picker.js_on_change(
    "value",
    CustomJS(
        code="""
    console.log("datetime_range_picker: value=" + this.value, this.toString())
"""
    ),
)

show(datetime_range_picker)

# %%
from bokeh.io import show
from bokeh.models import CustomJS, DatetimePicker

datetime_picker = DatetimePicker(
    title="Select date and time",
    value="2019-09-20T12:37:51",
    min_date="2019-08-01T09:00:00",
    max_date="2019-10-30T18:00:00",
)
datetime_picker.js_on_change(
    "value",
    CustomJS(
        code="""
    console.log("datetime_picker: value=" + this.value, this.toString())
"""
    ),
)

show(datetime_picker)

# %%
from datetime import date

from bokeh.io import show
from bokeh.models import CustomJS, DateSlider

date_slider = DateSlider(
    value=date(2016, 1, 1), start=date(2015, 1, 1), end=date(2017, 12, 31)
)
date_slider.js_on_change(
    "value",
    CustomJS(
        code="""
    console.log('date_slider: value=' + this.value, this.toString())
"""
    ),
)

show(date_slider)

# %%
from bokeh.io import show
from bokeh.models import Button, CustomJS

button = Button(label="Foo", button_type="success")
button.js_on_event(
    "button_click", CustomJS(code="console.log('button: click!', this.toString())")
)

show(button)

# %%
from bokeh.io import show
from bokeh.models import CustomJS, RangeSlider

range_slider = RangeSlider(start=0, end=10, value=(1,9), step=.1, title="Stuff")
range_slider.js_on_change("value", CustomJS(code="""
    console.log('range_slider: value=' + this.value, this.toString())
"""))

show(range_slider)

# %%
