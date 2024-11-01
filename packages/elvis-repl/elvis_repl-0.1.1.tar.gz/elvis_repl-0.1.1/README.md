# Elvis Has Left the Building

Generate Python code strings to recreate objects with their current state. Perfect for:
- Saving exact object recreation code
- Working in terminals where copy-paste is painful
- Quick templating of repetitive code
  
Some say it's pointless. Some say it's brilliant. Elvis doesn't care either way - Elvis has already left the building.

## Install
```bash
pip install elvis-repl
```

## Usage
```python
from elvis_repl import elvis

# Generate object creation code
elvis("df = pd.read_csv(\"{file}\", skiprows={skip})", 
      file="data.csv", skip=2)
# Output: df = pd.read_csv("data.csv", skiprows=2)

# Reuse with changed variables
elvis._vars['skip'] = 3
elvis("df = pd.read_csv(\"{file}\", skiprows={skip})")

# Generate multiple similar objects
for i in range(2):
    elvis("obj_{id} = MyClass(\"{name}\")", id=i, name=f"instance_{i}")
```

## Features
- Remember variables between templates
- Preview code before execution with .show()
- Execute when ready with .run()
- Works in both Jupyter and CLI

Remember: When your session crashes, Elvis makes sure you know how to rebuild everything exactly as it was.