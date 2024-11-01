import pytest
import sys
from elvis_repl import elvis

# Basic functionality tests
def test_template_creation():
    elvis.clear()  # Start fresh
    result = elvis("test_{x}", x=42)
    assert elvis._vars.get('x') == 42

def test_render_output():
    elvis.clear()
    elvis._template = "print({x})"
    elvis._vars['x'] = 42
    result = elvis.render()
    assert result == "print(42)"

def test_clear_state():
    elvis.clear()
    elvis("test_{x}", x=42)
    elvis.clear()
    assert not elvis._vars
    assert elvis._last_rendered is None

# Test variable management
def test_variable_updates():
    elvis.clear()
    elvis("test_{x}", x=1)
    assert elvis._vars.get('x') == 1
    elvis("test_{x}", x=2)
    assert elvis._vars.get('x') == 2

# Test error cases
def test_run_without_render():
    elvis.clear()
    with pytest.raises(ValueError):
        elvis.run()

# Test environment detection
def test_ipython_detection():
    assert hasattr(elvis, 'ipython')