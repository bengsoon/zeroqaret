# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/00_helper.ipynb.

# %% auto 0
__all__ = ['view_df', 'get_now', 'get_today', 'create_header', 'write_file']

# %% ../nbs/00_helper.ipynb 4
from loguru import logger
import os
from pathlib import Path
from fastcore.basics import patch_to, patch

import pandas as pd

from typing import Union, List

from datetime import datetime

# %% ../nbs/00_helper.ipynb 6
def view_df(df: "pd.DataFrame", # Pandas DataFrame to be viewed
            min_rows: int = 60, # minimum row 
            max_colswidth: int = 500, # maximum width of the column
            max_cols: int = None # maximum columns
           ):
    "View dataframe in full columns in Jupyter! If `max_cols==None`, it will show the full column."
    
    with pd.option_context('display.max_columns', max_cols, 'display.min_rows', min_rows, 'display.max_colwidth', max_colswidth):
        display(df)

# %% ../nbs/00_helper.ipynb 8
def get_now():
    " Returns the time now in 'yyyy-mm-dd_HHMMSS"
    return datetime.now().strftime("%Y%m%d_%H%M%S")

# %% ../nbs/00_helper.ipynb 10
def get_today(fmt="%Y-%m-%d"):
    " Returns today's date (default format: 'yyyy-mm-dd')"
    return datetime.today().strftime(fmt)

# %% ../nbs/00_helper.ipynb 11
def create_header(msg: str, # message on the header
                 ) -> str:
    """ Creates a simple ASCII header """
    header = "\n"
    header += "   \n" + "".center(100, "*")
    header += "   \n" + "                                                                                        ".center(100, "*")
    header += "   \n" + f"                                    {msg}                                    ".center(100, "*")
    header += "   \n" + "                                                                                        ".center(100, "*")
    header += "   \n" + "".center(100, "*")
    header += "\n"
    
    return header

# %% ../nbs/00_helper.ipynb 12
def write_file(file_path, text, mode=""):
    with open(file_path, "a") as f:
        f.write(text)
