#!/usr/bin/python3
import doctest
import importlib.util

# Load the module from the file path
spec = importlib.util.spec_from_file_location("add_integer", "./0-add_integer.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

# Run doctests from the module
doctest.testmod(module, verbose=True)
