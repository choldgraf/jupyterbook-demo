# ---
# jupyter:
#   jupytext:
#     formats: ipynb,md,Rmd,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.2'
#       jupytext_version: 1.2.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Jupytext with Jupyter Book
#
# It's also possible to build Jupyter Books using [Jupytext](https://jupytext.readthedocs.io), a tool for
# two-way conversion between Jupyter Notebooks an text-based versions of a Jupyter Notebook (e.g., `.md` or `.py`).
#
# Using Jupytext allows you to store your Jupyter Notebooks as **text files**, which makes them much better for
# collaboration and "diffing" using a tool like Git. The drawbacks are that you no longer keep the outputs with
# your files, which means building your book with outputs requires running each file at build-time.
#
# ## This notebook is stored in Jupytext format!
#
# For example, the notebook for this page is stored in a Jupytext format. In this case, we've used
# a markdown file. [You can find the original (text-based) format here](https://github.com/jupyter/jupyter-book/blob/master/jupyter_book/book_template/content/features/jupytext.md).
#
# Below we'll show some Python code, which Jupyter Book can execute at build time.

# %%
# Import some data
import numpy as np
import matplotlib.pyplot as plt
plt.ion()

# %%
# We'll make a simple plot!
data = np.random.randn(2, 100)

fig, ax = plt.subplots()
ax.scatter(*data, c=data[0], s=500)
ax.text(0, 0, "Jupytext is great!", fontdict={'size': 40, 'horizontalalignment': 'center'})

# %% [markdown]
# ## Jupytext works with cell tags
#
# You can still use cell tags in your Jupytext files by using the format that Jupytext expects.
# For example, the Python code below will have its code cell hidden:

# %% {"tags": ["hide_input"]}
# We'll make a simple plot!
data = np.random.randn(2, 100)

fig, ax = plt.subplots()
ax.scatter(*data, c=data[1], s=500, cmap='coolwarm')
ax.text(0, 0, "Jupytext is great!", fontdict={'size': 40, 'horizontalalignment': 'center'})

# %% [markdown]
# ## A recommended workflow with Jupytext and notebooks
#
# Even if you're storing your content in a text-based file, it's useful to **write your content in notebooks**
# and convert them to text format before committing them in Git. This allows you to add **tags** to your notebooks
# that propagate to your Jupytext format. This allows you to use the editing capabilities of a Jupyter interface, but
# the version-control benefits of a text-based file.
