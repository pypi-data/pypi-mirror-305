# src/elvis_repl/core.py
from typing import Dict, Any, Optional

class elvis:
    """
    Elvis: Template engine that remembers, when leaving the building
    
    render(): Generate code from template
    show(): Display what would be generated
    run(): Execute the last rendered template
    """
    def __init__(self):
        self._vars: Dict[str, Any] = {}
        self._last_rendered: Optional[str] = None
        self._template: Optional[str] = None
        self.ipython = self._get_ipython()
        
    def _get_ipython(self):
        """Safely detect IPython/Jupyter environment"""
        try:
            from IPython import get_ipython
            return get_ipython()
        except (ImportError, NameError):
            return None
    
    def render(self) -> str:
        """
        Render template with variables but don't display
        Variables are stored for reuse
        """
        # Store variables and template result
        self._vars.update()
        self._last_rendered = self._template.format(**self._vars)
        return self._last_rendered
    
    def show(self):
        """
        Display rendered template
        In Jupyter: Creates editable cell
        In CLI: Shows the code
        """
        if not self._last_rendered:
            content = self.render()
        else:
            content = self._last_rendered
            
        if not content:
            print("Nothing to show! Render a template first.")
            return
            
        if self.ipython:
            self.ipython.set_next_input(content, replace=True)
        else:
            print(content)
    
    def run(self):
        """Execute last rendered template"""
        if not self._last_rendered:
            raise ValueError("Nothing to run! Render a template first.")
        exec(self._last_rendered)
    
    def vars(self):
        """Show current template variables"""
        for key, value in self._vars.items():
            print(f"{key} = {repr(value)}")
    
    def clear(self):
        """Clear stored variables and last render"""
        self._vars.clear()
        self._last_rendered = None
        
    def __call__(self, template: str, **kwargs):
        """Shortcut to render and show in one step"""
        self._template = template
        # Update variable
        self._vars.update(kwargs)

        # Update template and show result
        self.render()
        self.show()
        return self

# Create singleton instance
elvis = elvis()