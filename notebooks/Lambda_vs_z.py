# %% [markdown]
# ## Rest-frame to Observed-fram Lambda vs Redshift

# %%
import numpy as np

# %%
from bokeh.io import output_notebook
from bokeh.plotting import figure, show
from bokeh.palettes import BuRd9
from bokeh.models import CrosshairTool

output_notebook()


# %% [markdown]
# ### 1. Function for converting lambda from rest to observed


# %%
def rest2obs(wlen, z):
    """Compute the observed wavelength given the rest-frame wavelength and redshift.

    Args:
        wlen(float): Rest-frame wavelength.
        z(float): Redshift of the source.
    """

    return wlen * (1 + z)


# %% [markdown]
# #### Pre-compute observed-frame $\lambda$ for a few fixed rest-frame $\lambda$

# %%
zs = np.linspace(0, 6, 200)
rest_wlens = [912, 1216, 1549, 1909, 2800, 5007, 6563]
obs_wlens = []
for rest_wlen in rest_wlens:
    obs_wlens.append(rest2obs(rest_wlen, zs))

# %% [markdown]
# ### 2. Observed-Lambda vs Z

# %%
p = figure(
    title="Lambda vs Redshift",
    x_range=(0, 6),
    y_range=(3000, 11000),
    height=500,
)
p.xaxis.axis_label = "Redshift"
p.yaxis.axis_label = "Rest-frame Wavelength"
crosshair = CrosshairTool()
p.add_tools(crosshair)

# line_clrs = viridis(len(obs_wlens))
line_clrs = BuRd9

for i in range(len(obs_wlens)):
    p.line(
        zs,
        obs_wlens[i],
        line_color=line_clrs[i],
        line_width=2.5,
        legend_label=f"{rest_wlens[i]} AA",
    )


show(p)

# %%
