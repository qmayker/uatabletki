from random import choice
from config import VIEWPORTS

def get_size(d_type:str, os:str):
    TYPE_VIEWS = VIEWPORTS.get(d_type)
    print(os)
    if not TYPE_VIEWS:
        return {"width": 1366, "height": 768}
    print(OS_VIEWS.keys())