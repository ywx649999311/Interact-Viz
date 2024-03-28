## Setup Instructions

### Poetry
1. Install `poetry`:

> see: https://python-poetry.org/docs/#installing-with-the-official-installer

2. Config `poetry`:
```
poetry config virtualenvs.in-project true
```
3. Create the virtual environment for the project:
```
poetry install
```
One can activate the virtual env with (when needed to):
```
source .venv/bin/activate
```
4. Create and add ipykernel for the poetry environment:
```
poetry run python3 -m ipykernel install --user --name proj --display-name "proj (poetry)"
```

### Jupytext
5. Install & enable `jupytext` (for version control notebooks):

    a. Install `jupytext` under the env runing your Jupyter server:

    > see: https://jupytext.readthedocs.io/en/latest/install.html#installation

    b. Restart Jupyter server

### Pre-commit
6. Run the following:
```
poetry run pre-commit install
```
