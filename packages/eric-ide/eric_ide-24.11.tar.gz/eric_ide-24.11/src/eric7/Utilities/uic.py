# -*- coding: utf-8 -*-

# Copyright (c) 2009 - 2024 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing a function to compile all user interface files of a
directory or directory tree.
"""

from PyQt6.uic import compileUiDir


def __pyName(py_dir, py_file):
    """
    Local function to create the Python source file name for the compiled
    .ui file.

    @param py_dir suggested name of the directory
    @type str
    @param py_file suggested name for the compiled source file
    @type str
    @return tuple of directory name and source file name
    @rtype tuple of (str, str)
    """
    return py_dir, "Ui_{0}".format(py_file)


def compileUiFiles(directory, recurse=False):
    """
    Module function to compile the .ui files of a directory tree to Python
    sources.

    @param directory name of a directory to scan for .ui files
    @type str
    @param recurse flag indicating to recurse into subdirectories
    @type boolean)
    """
    compileUiDir(directory, recurse, __pyName)
