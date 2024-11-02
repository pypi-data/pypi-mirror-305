# pypathadd

`pypathadd` is a simple Python utility that appends all folders and subfolders of a specified root directory to the Python path. This functionality can simplify package imports, especially in larger projects with nested directories.

## Features

- Automatically adds all folders and subfolders in a specified root directory to the Python path.
- Allows exclusion of specific folders (e.g., `__pycache__`) to keep the path clean.
- Simple, flexible, and lightweight, making it easy to integrate into any project.

## Installation

You can install `pypathadd` from PyPI:

```bash
pip install pypathadd
```

## Usage

Here’s a quick example of how to use pypathadd to simplify your import paths.

### Basic Example

```python
from pypathadd import py_auto_append

# Automatically append folders from the root directory two levels up
py_auto_append(__file__, levels_up=2, verbose=True)

# You can now import modules from parent directories without adjusting sys.path manually
import your_module_in_parent_dir
```

### Arguments

- `path_caller` (str): Path of the calling module, typically __file__.
- `levels_up` (int, optional): Number of levels to go up from the caller path to set the root directory. Defaults to 0.
- `rm_elems` (List[str], optional): List of folder names (or substrings) to exclude from being added to the path. Defaults to ['__pycache__', '.', 'config', 'web'].
- `verbose` (bool, optional): If True, prints each path added to the system path. Defaults to False.

### Example with Custom Arguments

```python
from pypathadd import py_auto_append

# Specify folders to exclude from path
py_auto_append(__file__, levels_up=1, rm_elems=['__pycache__', 'tests'], verbose=True)
```

## Why use `pypathadd`?
In projects with deep folder structures, importing modules from different parts of the hierarchy can be cumbersome. `pypathadd` dynamically appends paths to `sys.path`, allowing for clean and organized imports across directories.

## License
This project is licensed under the MIT License. See the LICENSE file for details.