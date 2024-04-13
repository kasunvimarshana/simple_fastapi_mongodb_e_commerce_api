"""
# import sys
# import os

# # Append the current directory to the Python module search path
# sys.path.append(os.path.abspath('.'))
# sys.path.insert(0, ".")

# # Now you can import modules or packages from the current directory
# '''
# # from . import *
# '''
# '''
# # from . import module_01 as module_01
# # from . import module_02 as module_02

# # __all__ = list(
# #     set(
# #         module_01.__all__ 
# #         + module_02.__all__
# #         )
# #     )
# '''
"""

from . import health_routes as health_routes

__all__ = list(
    "health_routes"
)
