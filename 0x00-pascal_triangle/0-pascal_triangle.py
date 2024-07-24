#!/usr/bin/python3
"""
0-main
"""
import importlib.util
import sys

# Load the module
module_name = '0-pascal_triangle'
file_path = './0-pascal_triangle.py'
spec = importlib.util.spec_from_file_location(module_name, file_path)
module = importlib.util.module_from_spec(spec)
sys.modules[module_name] = module
spec.loader.exec_module(module)

pascal_triangle = module.pascal_triangle

def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print_triangle(pascal_triangle(5))
