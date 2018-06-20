# Reloading Modules
## in iPython
Always set 
```python
%load_ext autoreload
%autoreload 2
```
so modules get always autoreloaded.
Otherwise, after your edits, iPython will still use the old code.
## Manually reloading
Manually reload your module, after importing the module for reimport:
```python
import importlib
# if the module you loaded before was etl.helper
importlib.reload(etl.helper)
```