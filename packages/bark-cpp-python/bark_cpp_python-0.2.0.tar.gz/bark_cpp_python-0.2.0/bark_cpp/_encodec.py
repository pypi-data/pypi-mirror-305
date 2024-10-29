"""Internal module use at your own risk
"""
import os
import pathlib

import bark_cpp._ctypes_extensions as ctypes_ext

libencodec_base_path = pathlib.Path(os.path.abspath(os.path.dirname(__file__))) / "lib"
libencodec = ctypes_ext.load_shared_library("encodec", libencodec_base_path)