# -*- coding: utf-8 -*-
# @Author: Simon Walser
# @Date:   2023-09-12 13:20:57
# @Last Modified by:   Simon Walser
# @Last Modified time: 2024-11-01 14:55:14


import os
import sys
from typing import List
from pathlib import Path

################################################################################
#
# Class / Function definitions
#
################################################################################


def py_auto_append(
    path_caller: str,
    levels_up: int=0,
    rm_elems: List[str]=['__pycache__', '.', 'config', 'web'],
    verbose: bool=False,
    ):
    """
    Appends all folders and subfolders of the root directory to the Python path.

    Args:
        path_caller (str): Path of the calling module, typically `__file__`.
        levels_up (int): Levels to go up from the caller path to find the root directory. Defaults to 0.
        rm_elems (List[str]): Substrings of folder names to ignore. Defaults to ['__pycache__', '.', 'config', 'web'].
        verbose (bool): If True, lists all appended paths. Defaults to False.
    """

    path_abs_caller = os.path.abspath(path_caller)

    max_level_up = len(Path(path_abs_caller).parents)
    levels_up = levels_up if max_level_up > levels_up else (max_level_up - 1)

    directory = os.path.abspath(Path(path_abs_caller).parents[levels_up])
    paths_all = os.walk(directory)

    for path in paths_all:
        if (not any([rme in path[0] for rme in rm_elems])) and \
           (not any([ppath == path[0] for ppath in sys.path])):
            sys.path.append(path[0])
            if verbose: print(f'Appending {path[0]}')