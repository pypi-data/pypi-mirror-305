# -*- coding: utf-8 -*-
# @Author: Simon Walser
# @Date:   2023-09-13 15:52:34
# @Last Modified by:   Simon Walser
# @Last Modified time: 2024-11-01 15:36:48


import sys
import unittest
from pathlib import Path

# Add the root project directory to sys.path
project_root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(project_root / "src"))
from pypathadd.pypathadd import py_auto_append

################################################################################
#
# Class / Function definitions
#
################################################################################

class TestPyPathAdd(unittest.TestCase):

    def setUp(self):
        # Store the original sys.path to restore it after each test
        self.original_sys_path = sys.path.copy()

    def tearDown(self):
        # Restore sys.path to its original state after each test
        sys.path = self.original_sys_path

    def test_py_auto_append_basic(self):
        """Test that py_auto_append adds directories up to the specified level."""
        py_auto_append(__file__, levels_up=1)

        # Define the expected directory to be added to sys.path
        expected_directory = str(Path(__file__).resolve().parent.parent)

        # Check if the expected directory is in sys.path
        self.assertIn(expected_directory, sys.path)

    def test_py_auto_append_exclude(self):
        """Test that py_auto_append excludes specified folders."""
        py_auto_append(__file__, levels_up=1, rm_elems=['tests'])

        # Define the directory that would be ignored
        ignored_directory = str(Path(__file__).resolve().parent)

        # Check if the ignored directory is not in sys.path
        self.assertNotIn(ignored_directory, sys.path)

    def test_py_auto_append_verbose(self):
        """Test the verbose output by capturing printed output (optional)."""
        import io
        import contextlib

        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            py_auto_append(__file__, levels_up=1, verbose=True)

        # Check if the verbose output includes the expected directory
        expected_output = str(Path(__file__).resolve().parent.parent)
        self.assertIn(expected_output, output.getvalue())


################################################################################
#
# Main functions
#
################################################################################

if __name__ == "__main__":
    unittest.main()
