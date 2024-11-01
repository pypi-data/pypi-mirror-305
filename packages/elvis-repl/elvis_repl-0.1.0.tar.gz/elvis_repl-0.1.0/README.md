# Elvis Has Left the Building
Some say it's pointless. Some say it's brilliant. Elvis doesn't care either way - Elvis has already left the building.

A REPL template engine that remembers your variables and helps you generate code in both Jupyter and CLI environments.

## Installation

```bash
pip install elvis-repl
```

## Usage

```python
from elvis_repl import elvis

# Create a template with variables
elvis("cube_{id} = cube(\"{name}\")", 
      id=1, 
      name="first_cube")

# Variables are remembered
elvis.vars()

# Render without showing
elvis.render()

# Show last rendered template
elvis.show()

# Execute when ready
elvis.run()

# Clear state
elvis.clear()
```

## Features

- Works in both Jupyter and regular Python REPL
- Remembers variables between template generations
- Separate render/show/run steps for control
- Chainable API
- Simple and intuitive interface